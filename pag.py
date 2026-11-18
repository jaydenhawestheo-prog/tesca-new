STYLE = """
:root{--bg:#ffffff;--card:#f8fafc;--text:#1e293b;--sub:#64748b;--acc:#0044cc;--cyan:#00b4ff;--bdr:#e2e8f0;--pill:#ffffff;--sh:0 4px 20px rgba(0,68,204,.08)}
body.dark{--bg:#070d1f;--card:#111a33;--text:#f1f5f9;--sub:#94a3b8;--acc:#38bdf8;--cyan:#00b4ff;--bdr:#1e293b;--pill:#16203c;--sh:0 4px 24px rgba(0,0,0,.4)}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"Segoe UI",Roboto,Arial,sans-serif;background:var(--bg);color:var(--text);min-height:100vh;display:flex;flex-direction:column;transition:background .2s,color .2s}
.corner-logo{position:fixed;top:14px;right:18px;width:44px;height:44px;object-fit:contain;border-radius:10px;background:#ffffff;padding:3px;box-shadow:0 2px 8px rgba(0,0,0,.15);z-index:1400}
body.dark .corner-logo{background:#000000;border:1px solid #1e293b}
.top-actions{display:flex;align-items:center;gap:10px;position:relative}
.icon-pill{background:var(--card);border:1px solid var(--bdr);color:var(--text);padding:8px 14px;border-radius:20px;font-size:.88rem;font-weight:600;cursor:pointer;display:flex;align-items:center;gap:6px}
.icon-pill:hover{border-color:var(--cyan);color:var(--acc)}
.set-menu{position:absolute;top:115%;right:0;width:210px;background:var(--pill);border:1px solid var(--bdr);border-radius:12px;padding:12px;box-shadow:var(--sh);display:none;z-index:1200;font-size:.86rem}
.set-menu div{padding:6px 4px;border-bottom:1px solid var(--bdr);color:var(--sub)}
.set-menu div:last-child{border:none}
.hero{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:24px 20px 32px;text-align:center}
.search-wrap{position:relative;width:100%;max-width:580px}
.search-pill{display:flex;align-items:center;background:var(--pill);border:1px solid var(--bdr);border-radius:30px;padding:6px 16px;box-shadow:var(--sh);transition:border-color .2s,box-shadow .2s}
.search-pill:focus-within{border-color:var(--cyan);box-shadow:0 6px 24px rgba(0,180,255,.18)}
.s-icon{color:var(--sub);font-size:1.1rem;margin-right:10px}
.search-box{flex:1;border:none;outline:none;background:transparent;color:var(--text);font-size:1.05rem;padding:8px 0}
.mic-btn{background:none;border:none;cursor:pointer;font-size:1.15rem;padding:4px 6px}
.suggestions{position:absolute;top:110%;left:0;right:0;background:var(--pill);border:1px solid var(--bdr);border-radius:16px;box-shadow:var(--sh);z-index:1200;display:none;text-align:left;overflow:hidden}
.suggestions div{padding:11px 18px;cursor:pointer;border-bottom:1px solid var(--bdr)}
.suggestions div:hover{background:var(--card);color:var(--acc)}
.btn-row{display:flex;gap:12px;justify-content:center;margin-top:22px;flex-wrap:wrap}
.btn{background:#0044cc;color:#fff;border:none;border-radius:22px;padding:10px 22px;font-size:.94rem;font-weight:600;cursor:pointer}
.btn:hover{background:#003399}
.btn-sec{background:var(--card);color:var(--text);border:1px solid var(--bdr)}
.btn-sec:hover{border-color:var(--cyan);color:var(--acc)}
.trend-head{font-size:.82rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--sub);margin-bottom:10px}
.chips{display:flex;gap:8px;flex-wrap:wrap}
.chip{background:var(--pill);border:1px solid var(--bdr);padding:6px 14px;border-radius:18px;font-size:.88rem;color:var(--text);text-decoration:none}
.chip:hover{border-color:var(--cyan);color:var(--acc)}
.navbar{position:sticky;top:0;z-index:1000;background:var(--pill);border-bottom:2px solid var(--cyan);padding:12px 24px;display:flex;align-items:center;justify-content:space-between}
.brand{font-size:1.4rem;font-weight:800;color:var(--acc);text-decoration:none;letter-spacing:1px}
.nav-links{display:flex;align-items:center;gap:12px}
.nav-links a{text-decoration:none;color:var(--text);font-size:.9rem;font-weight:600}
.game-btn{background:linear-gradient(135deg,#0044cc,#00b4ff);color:#fff!important;padding:7px 14px;border-radius:18px}
.theme-btn{background:var(--card);border:1px solid var(--bdr);color:var(--text);padding:7px 14px;border-radius:18px;font-size:.88rem;font-weight:600;cursor:pointer}
.hero-search{display:flex;gap:10px;align-items:center}
.hero-search .search-wrap{display:flex;align-items:center;background:var(--pill);border:1px solid var(--bdr);border-radius:30px;padding:4px 14px}
.wrap{max-width:900px;margin:28px auto;padding:0 20px;width:100%}
.card{background:var(--pill);border:1px solid var(--bdr);border-radius:16px;padding:28px 32px;box-shadow:var(--sh)}
h1{font-size:1.6rem;color:var(--text);margin:18px 0 16px;padding-bottom:8px;border-bottom:1px solid var(--bdr)}
.item{display:flex;gap:18px;margin-bottom:20px;padding-bottom:18px;border-bottom:1px solid var(--bdr);align-items:flex-start}
.thumb{width:92px;height:92px;object-fit:cover;border-radius:10px;border:1px solid var(--bdr);flex-shrink:0}
.r-title{font-size:1.25rem;font-weight:700;color:var(--acc);text-decoration:none}
.r-title:hover{text-decoration:underline}
.r-desc{font-size:.85rem;color:var(--sub);margin:3px 0 8px}
.speak-btn{background:var(--card);border:1px solid var(--bdr);color:var(--text);padding:5px 12px;border-radius:14px;font-size:.8rem;cursor:pointer;margin-top:8px}
"""

JS = """
<script>
const WIKI = "https://en.wikipedia.org";
function esc(s){const d=document.createElement("div");d.textContent=s==null?"":String(s);return d.innerHTML;}
if(localStorage.getItem("tesca-dark")==="1")document.body.classList.add("dark");
function toggleTheme(){document.body.classList.toggle("dark");localStorage.setItem("tesca-dark",document.body.classList.contains("dark")?"1":"0");}
function toggleSet(){const m=document.getElementById("setMenu");if(m)m.style.display=m.style.display==="block"?"none":"block";}
const inp=document.getElementById("qInput"),box=document.getElementById("sugBox");
if(inp&&box){let t;inp.addEventListener("input",()=>{clearTimeout(t);const v=inp.value.trim();if(!v){box.style.display="none";return;}
t=setTimeout(async()=>{try{
const r=await fetch(WIKI+"/w/api.php?action=opensearch&format=json&origin=*&limit=5&search="+encodeURIComponent(v));
const d=await r.json(),items=Array.isArray(d)?d.at(1)||[]:[];
if(!items.length){box.style.display="none";return;}
box.innerHTML="";items.forEach(x=>{const div=document.createElement("div");div.textContent=x;div.onclick=()=>location.href="/search?q="+encodeURIComponent(x);box.appendChild(div);});
box.style.display="block";}catch(e){box.style.display="none";}},200);});
document.addEventListener("click",e=>{if(!e.target.closest(".search-wrap"))box.style.display="none";const m=document.getElementById("setMenu");if(m&&!e.target.closest(".top-actions"))m.style.display="none";});
document.addEventListener("keydown",e=>{if(e.key==="/"&&document.activeElement!==inp){e.preventDefault();inp.focus();}});}
function startVoice(){const SR=window.SpeechRecognition||window.webkitSpeechRecognition;if(!SR){alert("Voice search works in Chrome or Edge.");return;}const rec=new SR();rec.onresult=e=>{const res=e.results.item(0);if(res)inp.value=res.item(0).transcript;inp.form.submit();};rec.start();}
function speakText(b){window.speechSynthesis.cancel();window.speechSynthesis.speak(new SpeechSynthesisUtterance(b.getAttribute("data-text")));}
async function loadResults(q,lucky){
const out=document.getElementById("resOut");if(!out||!q)return;
try{
const r=await fetch(WIKI+"/w/api.php?action=opensearch&format=json&origin=*&limit=6&search="+encodeURIComponent(q));
const d=await r.json(),titles=Array.isArray(d)?d.at(1)||[]:[],urls=Array.isArray(d)?d.at(3)||[]:[];
if(!titles.length){out.innerHTML="<p>No articles found for <strong>"+esc(q)+"</strong>.</p>";return;}
if(lucky&&urls.at(0)){location.href=urls.at(0);return;}
out.innerHTML="";
for(const t of titles){
const sr=await fetch(WIKI+"/api/rest_v1/page/summary/"+encodeURIComponent(t.replace(/ /g,"_")));
if(!sr.ok)continue;
const info=await sr.json(),el=document.createElement("div");el.className="item";
const img=info.thumbnail&&info.thumbnail.source?`<img src="${esc(info.thumbnail.source)}" class="thumb" alt="">`:"";
const pageUrl=(info.content_urls&&info.content_urls.desktop&&info.content_urls.desktop.page)||WIKI+"/wiki/"+encodeURIComponent(t);
el.innerHTML=`${img}<div><a href="${esc(pageUrl)}" target="_blank" rel="noopener" class="r-title">${esc(info.title||t)}</a><div class="r-desc">${esc(info.description||"General Topic")}</div><p>${esc(info.extract)}</p><button type="button" class="speak-btn" onclick="speakText(this)">Listen to Summary</button></div>`;
el.querySelector("button").setAttribute("data-text",info.extract||"");
out.appendChild(el);}
}catch(e){out.innerHTML="<p>Search failed. Check your internet connection.</p>";}}
</script>
"""

HOME_HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Tesca</title><style>__STYLE__h1.tesca-title{font-size:4.2rem!important;font-family:"Bauhaus 93","Arial Rounded MT Bold","Trebuchet MS",sans-serif!important;font-weight:900!important;letter-spacing:6px!important;line-height:1.05!important;background:linear-gradient(90deg,#001f7a 0%,#0055cc 45%,#14b8a6 100%)!important;-webkit-background-clip:text!important;background-clip:text!important;-webkit-text-fill-color:transparent!important;-webkit-text-stroke:1px #000000!important;paint-order:stroke fill!important;border:none!important;margin:10px auto 24px!important;padding:0!important;display:inline-block!important}.fab-game{position:fixed!important;bottom:24px!important;right:24px!important;left:auto!important;background:linear-gradient(135deg,#0044cc,#00b4ff)!important;color:#fff!important;padding:12px 20px!important;border-radius:30px!important;display:inline-flex!important;align-items:center!important;gap:8px!important;font-size:1rem!important;font-weight:700!important;text-decoration:none!important;box-shadow:0 8px 24px rgba(0,119,255,.4)!important}.top-bar,.hero{position:relative;z-index:1}@media(max-width:820px){.bg-rings{display:none!important}}.mobile-aurora{display:none}@media(max-width:820px){.bg-rings{display:none!important}.mobile-aurora{display:block;position:fixed;top:-90px;left:50%;transform:translateX(-50%);width:130vw;height:280px;border-radius:50%;background:radial-gradient(ellipse at 50% 35%,rgba(0,119,255,.32) 0%,rgba(20,184,166,.22) 45%,transparent 75%);filter:blur(22px);pointer-events:none;z-index:0}}</style></head><body>
<header class="top-bar"><div></div><div class="top-actions"><button type="button" class="icon-pill" onclick="toggleTheme()">Theme</button><button type="button" class="icon-pill" onclick="toggleSet()">Settings</button><div id="setMenu" class="set-menu"><div>Press <strong>/</strong> to focus search</div><div>Voice search via Mic icon</div></div><a href="/"><img src="/dod.png" alt="Tesca Logo" class="corner-logo"></a></div></header>
<main class="hero"><h1 id="tescaLogoTitle" class="tesca-title">TESCA</h1><form action="/search" method="GET" class="search-wrap"><div class="search-pill"><span class="s-icon">&#128269;</span><input id="qInput" name="q" class="search-box" placeholder="Search Tesca..." autocomplete="off" required><button type="button" class="mic-btn" onclick="startVoice()" title="Voice Search">&#127908;</button></div><div id="sugBox" class="suggestions"></div><div class="btn-row"><button type="submit" class="btn">Tesca Search</button><button type="submit" name="lucky" value="1" class="btn btn-sec">I'm Feeling Lucky</button></div></form><div class="trend-card"><div class="trend-head">Trending Topics</div><div class="chips"><a href="/search?q=Python+(programming+language)" class="chip">Python</a><a href="/search?q=Space+exploration" class="chip">Space Exploration</a><a href="/search?q=Artificial+intelligence" class="chip">Artificial Intelligence</a><a href="/search?q=Bengaluru" class="chip">Bengaluru</a></div></div></main>
<a href="/game" class="fab-game" style="z-index:9999!important;pointer-events:auto!important" title="Play Tesca Space"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="20" height="12" rx="6"/><path d="M6 12h4M8 10v4"/><circle cx="15" cy="11" r="1" fill="currentColor"/><circle cx="17" cy="13" r="1" fill="currentColor"/></svg><span>Game</span></a>
__JS__<div class="bg-rings" style="position:fixed;inset:0;pointer-events:none;overflow:hidden;z-index:0"><div style="position:absolute;width:420px;height:420px;border-radius:50%;top:15%;left:-140px;background:radial-gradient(circle,rgba(0,68,204,.22),transparent 70%)"></div><div style="position:absolute;width:440px;height:440px;border-radius:50%;bottom:10%;right:-140px;background:radial-gradient(circle,rgba(20,184,166,.22),transparent 70%)"></div><div style="position:absolute;width:240px;height:240px;border-radius:50%;top:34%;left:-95px;border:3px solid rgba(0,119,255,.22);box-shadow:0 0 0 34px rgba(20,184,166,.08)"></div><div style="position:absolute;width:280px;height:280px;border-radius:50%;top:22%;right:-115px;border:3px solid rgba(20,184,166,.24);box-shadow:0 0 0 38px rgba(0,68,204,.08)"></div></div><div class="mobile-aurora"></div><style>.side-panel{display:none;position:fixed;top:50%;transform:translateY(-50%);width:215px;background:var(--pill);border:1px solid var(--bdr);border-radius:18px;padding:16px;box-shadow:var(--sh);z-index:1100;font-size:.85rem;text-align:left;transition:transform .2s,border-color .2s}.side-panel:hover{border-color:var(--cyan)}.side-left{left:22px}.side-right{right:22px}.sp-title{font-size:.75rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--acc);margin-bottom:10px;display:flex;align-items:center;justify-content:space-between}.sp-clock{font-size:1.35rem;font-weight:800;color:var(--text);margin-bottom:2px}.sp-date{font-size:.78rem;color:var(--sub);margin-bottom:12px}.sp-btn{display:block;width:100%;text-align:left;background:var(--card);border:1px solid var(--bdr);color:var(--text);padding:8px 11px;border-radius:12px;font-size:.82rem;font-weight:600;cursor:pointer;margin-bottom:8px;text-decoration:none}.sp-btn:hover{border-color:var(--cyan);color:var(--acc)}.sp-fact{font-size:.78rem;color:var(--sub);line-height:1.4;background:var(--card);padding:8px 10px;border-radius:10px;min-height:48px}.sp-score{font-size:1.4rem;font-weight:800;color:var(--acc);margin:4px 0 10px}.sp-rec a{display:block;padding:5px 8px;border-radius:8px;color:var(--text);text-decoration:none;font-size:.8rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.sp-rec a:hover{background:var(--card);color:var(--acc)}@media(max-width:820px){.bg-rings{display:none!important}}.mobile-aurora{display:none}@media(max-width:820px){.bg-rings{display:none!important}.mobile-aurora{display:block;position:fixed;top:-90px;left:50%;transform:translateX(-50%);width:130vw;height:280px;border-radius:50%;background:radial-gradient(ellipse at 50% 35%,rgba(0,119,255,.32) 0%,rgba(20,184,166,.22) 45%,transparent 75%);filter:blur(22px);pointer-events:none;z-index:0}}</style>
<button type="button" onclick="toggleSide('leftPanel')" style="position:fixed;left:0;top:50%;transform:translateY(-50%);z-index:1250;background:linear-gradient(135deg,#0044cc,#00b4ff);color:#fff;border:none;border-radius:0 14px 14px 0;padding:12px 10px;cursor:pointer;font-weight:700;font-size:.82rem;box-shadow:0 4px 14px rgba(0,119,255,.35);font-size:1rem" title="Toggle Live Pulse">&#9654;</button><aside id="leftPanel" class="side-panel side-left" style="left:44px"><div class="sp-title"><span>Live Pulse</span><span>&#9201;</span></div><div id="spClk" class="sp-clock">--:--</div><div id="spDt" class="sp-date">Loading...</div><button type="button" class="sp-btn" onclick="randWiki()">&#127922; Random Article</button><button type="button" class="sp-btn" onclick="loadFact()">&#128161; Quick Fact</button><div id="spFact" class="sp-fact">Click "Quick Fact" for a bite-sized discovery!</div></aside>
<button type="button" onclick="toggleSide('rightPanel')" style="position:fixed;right:0;top:50%;transform:translateY(-50%);z-index:1250;background:linear-gradient(135deg,#0044cc,#14b8a6);color:#fff;border:none;border-radius:14px 0 0 14px;padding:12px 10px;cursor:pointer;font-weight:700;font-size:.82rem;box-shadow:0 4px 14px rgba(20,184,166,.35);font-size:1rem" title="Toggle Tesca Space">&#9664;</button><aside id="rightPanel" class="side-panel side-right" style="right:44px"><div class="sp-title"><span>Tesca Space</span><span>&#128640;</span></div><div style="font-size:.78rem;color:var(--sub)">Your High Score</div><div id="spHi" class="sp-score">0 pts</div><a href="/game" class="sp-btn" style="text-align:center;background:linear-gradient(135deg,#0044cc,#00b4ff);color:#fff;border:none">Play Now</a><div class="sp-title" style="margin-top:12px"><span>Recent</span><span>&#128337;</span></div><div id="spRec" class="sp-rec"><span style="font-size:.78rem;color:var(--sub)">No searches yet</span></div></aside>
<script>function toggleSide(id){const el=document.getElementById(id);if(!el)return;const open=el.style.display!=="block";el.style.display=open?"block":"none";const btn=el.previousElementSibling;if(btn)btn.textContent=(id==="leftPanel")?(open?"◀":"▶"):(open?"▶":"◀");}function tick(){const d=new Date(),c=document.getElementById("spClk"),dt=document.getElementById("spDt");if(c)c.textContent=d.toLocaleTimeString([],{hour:"2-digit",minute:"2-digit",second:"2-digit"});if(dt)dt.textContent=d.toLocaleDateString([],{weekday:"short",month:"short",day:"numeric"});}tick();setInterval(tick,1000);const hi=document.getElementById("spHi");if(hi)hi.textContent=(localStorage.getItem("tesca-hi")||0)+" pts";const recBox=document.getElementById("spRec"),hist=JSON.parse(localStorage.getItem("tesca-hist")||"[]");if(recBox&&hist.length){recBox.innerHTML=hist.slice(0,3).map(x=>`<a href="/search?q=${encodeURIComponent(x)}">&#128269; ${esc(x)}</a>`).join("");}const sf=document.querySelector("form[action='/search']");if(sf)sf.addEventListener("submit",()=>{const v=document.getElementById("qInput").value.trim();if(v){const h=[v,...hist.filter(i=>i!==v)].slice(0,5);localStorage.setItem("tesca-hist",JSON.stringify(h));}});async function randWiki(){try{const r=await fetch("/fact"),d=await r.json();if(d.title)location.href="/search?q="+encodeURIComponent(d.title);else alert("Could not fetch article.");}catch(e){alert("Error fetching article.");}}async function loadFact(){const box=document.getElementById("spFact");if(!box)return;box.textContent="Fetching...";try{const r=await fetch("/fact"),d=await r.json();box.textContent=d.extract||"Could not load fact.";}catch(e){box.textContent="Could not load fact.";}}</script></body></html>""".replace("__STYLE__", STYLE).replace("__JS__", JS)




