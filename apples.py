import json
import os
import random
import urllib.request

from flask import Flask, redirect, render_template_string, request, send_from_directory, url_for

from g import GAME_HTML
from pag import HOME_HTML
from res import RESULTS_HTML

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RANDOM_SUMMARY_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

BACKUP_FACTS = [
    {"title": "Venus", "extract": "A single day on Venus is longer than an entire year on Venus."},
    {"title": "Octopus", "extract": "Octopuses have three hearts, nine brains, and blue copper-based blood."},
    {"title": "Honey", "extract": "Natural honey never spoils; edible 3,000-year-old honey has been found in ancient Egyptian tombs."},
    {"title": "Space", "extract": "Because there is no atmosphere in space, sound waves cannot travel and space is completely silent."},
    {"title": "Bengaluru", "extract": "Bengaluru sits at an elevation of over 900 meters (3,000 ft) above sea level, giving it a mild climate year-round."},
]

app = Flask(__name__)


@app.route("/dod.png")
def logo():
    return send_from_directory(BASE_DIR, "dod.png")


@app.route("/")
def home():
    return render_template_string(HOME_HTML)


@app.route("/search")
def search():
    q = request.args.get("q", "").strip()
    if not q:
        return redirect(url_for("home"))
    lucky = bool(request.args.get("lucky"))
    return render_template_string(RESULTS_HTML, q=q, lucky=lucky)


@app.route("/game")
def play_game():
    return render_template_string(GAME_HTML)


@app.route("/fact")
def random_fact():
    try:
        req = urllib.request.Request(RANDOM_SUMMARY_URL, headers={"User-Agent": "TescaSearch/1.0"})
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = json.load(resp)
        return {"title": data.get("title", "Fact"), "extract": data.get("extract", "No fact found.")}
    except Exception as e:
        app.logger.warning("Fact API failed, using backup fact: %s", e)
        return random.choice(BACKUP_FACTS)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", 5001)))
