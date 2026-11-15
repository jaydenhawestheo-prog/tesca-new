from pag import JS, STYLE

RESULTS_HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{{q}} - Tesca Wiki</title><style>__STYLE__</style></head><body>
<a href="/"><img src="/dod.png" alt="Tesca Logo" class="corner-logo"></a>
<header class="navbar"><a href="/" class="brand">Tesca</a><nav class="nav-links"><a href="/">Main Page</a>
<a href="/game" class="game-btn">Play Tesca Space</a><button type="button" class="theme-btn" onclick="toggleTheme()">Dark Mode</button></nav></header>
<div class="wrap"><main class="card"><form action="/search" class="hero-search" style="margin-top:0"><div class="search-wrap">
<input id="qInput" name="q" value="{{q}}" class="search-box" placeholder="Search Tesca..." autocomplete="off" required>
<button type="button" class="mic-btn" onclick="startVoice()">&#127908;</button><div id="sugBox" class="suggestions"></div></div>
<button type="submit" class="btn">Search</button></form><h1>Results for "{{q}}"</h1>
<div id="resOut"><p>Searching Tesca...</p></div></main></div>__JS__
<script>loadResults({{q|tojson}}, {{lucky|tojson}});</script></body></html>""".replace("__STYLE__", STYLE).replace("__JS__", JS)
