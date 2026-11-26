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



FAMOUS_MEMES = {
    "67": ("6-7 Meme (LaMelo Ball / Skrilla)", "Viral trend inspired by Skrilla's song Doot Doot (6 7) and NBA star LaMelo Ball's 6ft 7in height - paired with the classic two-handed palm-up weighing gesture."),
    "6 7": ("6-7 Meme (LaMelo Ball / Skrilla)", "Viral trend inspired by Skrilla's song Doot Doot (6 7) and NBA star LaMelo Ball's 6ft 7in height - paired with the classic two-handed palm-up weighing gesture."),
    "scuba": ("Scuba Meme", "Viral reaction meme featuring a scuba diver underwater?used when someone dives way too deep into overthinking, drama, or a bizarre rabbit hole."),
    "fahhh": ("FAHHH Sound Effect Meme", "Dramatic echoing 'FAHHH!' vocal sound effect used in edits right when someone fails, gets caught, or faces instant regret."),
    "fahh": ("FAHHH Sound Effect Meme", "Dramatic echoing 'FAHHH!' vocal sound effect used in edits right when someone fails, gets caught, or faces instant regret."),
    "rickroll": ("Rickroll (Never Gonna Give You Up)", "Tricking someone into clicking a disguised link that plays Rick Astley's 1987 hit song."),
    "never gonna give you up": ("Rickroll", "You just got Rickrolled! Classic bait-and-switch internet prank since 2007."),
    "doge": ("Doge (Much Wow)", "A 2010 photo of Kabosu the Shiba Inu paired with colorful Comic Sans internal monologue like 'such code, very wow'."),
    "stonks": ("Stonks", "Meme Man standing in front of a rising stock chart?used ironically when making terrible financial or life decisions."),
    "this is fine": ("This Is Fine", "KC Green's cartoon dog sitting calmly in a burning room sipping coffee while everything falls apart."),
    "distracted boyfriend": ("Distracted Boyfriend", "Stock photo of a man checking out another woman while his girlfriend looks on in disbelief?used for shifting priorities."),
    "drake": ("Drakeposting", "Two-panel reaction from Drake's 'Hotline Bling' video: rejecting one option on top, approving the better one below."),
    "gigachad": ("GigaChad", "Ultra-muscular monochrome model Ernest Khalimov?used to praise bold, unbothered, or absurdly confident behavior."),
    "surprised pikachu": ("Surprised Pikachu", "Low-res Pikachu with an open-mouthed shocked expression when a completely predictable consequence happens."),
    "nyan cat": ("Nyan Cat", "A Pop-Tart cat flying through space leaving a rainbow trail to an endlessly looping J-pop melody."),
    "woman yelling at a cat": ("Woman Yelling at a Cat", "Taylor Armstrong pointing angrily on the left paired with Smudge the confused white cat sitting at a dinner table."),
    "shrek": ("Shrek", "DreamWorks' ogre turned into one of the internet's most enduring mashup and reaction icons."),
    "among us": ("Among Us (Sus)", "The 2020 social deduction hit that turned 'sus', 'impostor', and venting into everyday internet slang."),
    "gigachad": ("GigaChad", "Bold, unbothered energy?classic GigaChad approval.")
}

MEMES = [
    {"title": "Programming 101", "caption": "It works on my machine! ? Every developer right before deploying to production."},
    {"title": "Debugging Reality", "caption": "6 hours of debugging can save you 5 minutes of reading the documentation."},
    {"title": "CSS Struggles", "caption": "Trying to center a div: moves 2 pixels left, entire layout collapses."},
    {"title": "AI vs Human", "caption": "Me: 'Fix this tiny bug.' Code: *breaks 14 unrelated files*."},
    {"title": "Search Engine Life", "caption": "Users typing 'google.com' into Google?or typing 'tesca' into Tesca!"}
]

@app.route("/chat")
def casual_chat():
    q = request.args.get("q", "").strip().lower()
    for key, (title, desc) in FAMOUS_MEMES.items():
        if key in q:
            return {"type": "meme", "title": title, "text": desc}
    if any(w in q for w in ("meme", "memes", "funny")):
        try:
            req = urllib.request.Request("https://meme-api.com", headers={"User-Agent": "TescaSearch/1.0"})
            with urllib.request.urlopen(req, timeout=4) as resp:
                data = json.load(resp)
            if not data.get("nsfw") and data.get("url"):
                return {"type": "meme", "title": data.get("title", "Random Meme"), "text": f"From r/{data.get('subreddit', 'memes')}", "img": data["url"]}
        except Exception:
            pass
        m = random.choice(MEMES)
        return {"type": "meme", "title": m["title"], "text": m["caption"]}
    if any(w in q for w in ("joke", "laugh")):
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the web developer walk out of a restaurant? Because of the table layout.",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem."
        ]
        return {"type": "chat", "title": "Tesca Humor", "text": random.choice(jokes)}
    if any(w in q for w in ("how are you", "how r u", "whats up", "what's up")):
        return {"type": "chat", "title": "Doing great!", "text": "Running at full speed and ready to search anything or blast some meteors in Tesca Space!"}
    if any(w in q for w in ("who made you", "who created you", "your creator", "jayden")):
        return {"type": "chat", "title": "Built by Jayden", "text": "I was created by Jayden to make searching fast, fun, and interactive."}
    if any(w in q for w in ("bye", "goodbye", "see ya")):
        return {"type": "chat", "title": "Catch you later!", "text": "Come back anytime you need quick answers, memes, or a round of Tesca Space."}
    return {}

@app.route('/ping')
def ping():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", 5001)))

