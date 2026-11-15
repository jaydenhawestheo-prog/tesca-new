import json
import math
import os
import re
from flask import Flask, render_template_string, request

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "index.json"), "r", encoding="utf-8") as f:
    data = json.load(f)
    documents = data["documents"]
    inverted_index = data["inverted_index"]

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Tesca Search</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; max-width: 750px; margin: 40px auto; padding: 0 20px; background: #f9f9fb; color: #222; }
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
        h1 { color: #1a73e8; margin: 0; }
        #user-badge { font-size: 14px; color: #1a73e8; font-weight: bold; }
        .oneclick-btn { padding: 8px 14px; font-size: 14px; background: #fff; color: #1a73e8; border: 1px solid #1a73e8; border-radius: 20px; cursor: pointer; }
        form { display: flex; gap: 10px; margin-bottom: 25px; }
        input { flex: 1; padding: 12px; font-size: 16px; border: 1px solid #ccc; border-radius: 6px; }
        button[type="submit"] { padding: 12px 24px; font-size: 16px; background: #1a73e8; color: white; border: none; border-radius: 6px; cursor: pointer; }
        .fusion { background: #e8f0fe; padding: 15px; border-radius: 8px; margin-bottom: 25px; line-height: 1.5; }
        .result { background: white; padding: 15px; border-radius: 8px; margin-bottom: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
        .result a { color: #1a0dab; font-size: 18px; text-decoration: none; word-break: break-all; }
        .snippet { color: #4d5156; font-size: 14px; margin-top: 6px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Tesca Search</h1>
        <div>
            <span id="user-badge"></span>
            <button id="login-btn" class="oneclick-btn" onclick="oneClickSignIn()">1-Click Sign In (No Password)</button>
        </div>
    </div>

    <form method="get" action="/">
        <input type="text" name="q" value="{{ query }}" placeholder="Search the Tesca index..." required>
        <button type="submit">Search</button>
    </form>

    {% if query %}
        {% if results %}
            <div class="fusion"><strong>Knowledge Fusion:</strong><br>{{ fusion }}</div>
            {% for r in results %}
                <div class="result">
                    <a href="{{ r.url }}" target="_blank">{{ r.url }}</a>
                    <div class="snippet">{{ r.snippet }}...</div>
                </div>
            {% endfor %}
        {% else %}
            <p>No matching documents found.</p>
        {% endif %}
    {% endif %}

    <script>
        function oneClickSignIn() {
            const name = prompt("Enter your display name (saved automatically, no password needed):") || "Guest";
            localStorage.setItem("tesca_user", name);
            showUser(name);
        }

        function showUser(name) {
            document.getElementById("user-badge").textContent = "Signed in: " + name;
            document.getElementById("login-btn").style.display = "none";
        }

        window.onload = function () {
            const saved = localStorage.getItem("tesca_user");
            if (saved) showUser(saved);
        };
    </script>
</body>
</html>
"""

def search(query):
    query_words = re.findall(r"\w+", query.lower())
    scores = {}
    total_docs = len(documents)
    for word in query_words:
        if word not in inverted_index:
            continue
        doc_ids = inverted_index[word]
        idf = math.log((total_docs + 1) / (len(doc_ids) + 1))
        for doc_id in doc_ids:
            scores[doc_id] = scores.get(doc_id, 0) + idf
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)[:10]

@app.route("/")
def home():
    query = request.args.get("q", "").strip()
    results = []
    fusion = ""
    if query:
        ranked = search(query)
        for doc_id, score in ranked:
            doc = documents[str(doc_id)]
            results.append({"url": doc["url"], "snippet": doc["text"][:250]})
            if len(fusion) < 800:
                fusion += doc["text"][:250] + " "
    return render_template_string(HTML_PAGE, query=query, results=results, fusion=fusion)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
