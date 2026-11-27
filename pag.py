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
const ql=q.trim().toLowerCase();runZeroClick(q,out);
let greetHtml="";
if(["hi","hello","hey","hiya","how are you","who are you"].includes(ql)){
  greetHtml=`<div style="background:linear-gradient(135deg,rgba(0,68,204,.1),rgba(20,184,166,.12));border:1.5px solid var(--cyan);border-radius:16px;padding:20px 22px;margin-bottom:20px"><div style="font-size:.78rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--acc);margin-bottom:6px">Tesca Assistant</div><h3 style="margin-bottom:6px">Hi I'm Tesca</h3><p style="line-height:1.55">Ask me about any topic and feel free to play the built-in <a href="/game" style="color:var(--acc);font-weight:700">Tesca Space</a> game!</p></div>`;
}
try{
const [r,spR]=await Promise.all([
  fetch(WIKI+"/w/api.php?action=opensearch&format=json&origin=*&limit=6&profile=engine_autoselect&search="+encodeURIComponent(q)),
  fetch(WIKI+"/w/api.php?action=query&list=search&srinfo=suggestion&srlimit=1&format=json&origin=*&srsearch="+encodeURIComponent(q))
]);
let didYouMeanHtml="";
try{
  const spD=await spR.json();
  const sug=spD&&spD.query&&spD.query.searchinfo&&spD.query.searchinfo.suggestion;
  if(sug && sug.toLowerCase()!==q.trim().toLowerCase()){
    didYouMeanHtml=`<div style="margin-bottom:16px;font-size:.98rem;color:var(--sub)">Did you mean: <a href="/search?q=${encodeURIComponent(sug)}" style="color:var(--acc);font-weight:700;font-style:italic;text-decoration:none">${esc(sug)}</a>?</div>`;
  }
}catch(e){}
const d=await r.json(),titles=Array.isArray(d)?d.at(1)||[]:[],urls=Array.isArray(d)?d.at(3)||[]:[];
if(!titles.length){out.innerHTML=(didYouMeanHtml+greetHtml)||"<p>No articles found for <strong>"+esc(q)+"</strong>.</p>";return;}
if(lucky&&urls.at(0)){location.href=urls.at(0);return;}
const cKey="tesca-cache-v7-"+q.toLowerCase();
const cached=localStorage.getItem(cKey);
if(cached){out.innerHTML=cached;return;}
out.innerHTML=[1,2,3].map(()=>'<div class="item"><div class="skel" style="width:92px;height:92px;flex-shrink:0"></div><div style="flex:1"><div class="skel" style="height:20px;width:55%;margin-bottom:10px"></div><div class="skel" style="height:14px;width:90%;margin-bottom:8px"></div><div class="skel" style="height:14px;width:75%"></div></div></div>').join("");
const summaries=await Promise.all(titles.map(t=>fetch(WIKI+"/api/rest_v1/page/summary/"+encodeURIComponent(t.replace(/ /g,"_"))).then(res=>res.ok?res.json():null).catch(()=>null)));
try{
  const cr=await fetch("/chat?q="+encodeURIComponent(q));
  const cd=await cr.json();
  if(cd&&cd.title){
    const label=cd.type==="meme"?"Tesca Meme Drop":"Tesca Chat";
    
    greetHtml+=`<div style="background:linear-gradient(135deg,rgba(0,68,204,.1),rgba(20,184,166,.12));border:1.5px solid var(--cyan);border-radius:16px;padding:18px 20px;margin-bottom:20px"><div style="font-size:.75rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--acc);margin-bottom:4px">${label}</div><h3 style="margin-bottom:6px">${esc(cd.title)}</h3><p style="line-height:1.55">${esc(cd.text)}</p>${cd.img?`<img src="${esc(cd.img)}" alt="Meme" style="max-width:100%;max-height:340px;border-radius:12px;margin-top:10px;display:block">`:""}</div>`;
  }
}catch(e){}
out.innerHTML=didYouMeanHtml+greetHtml;
summaries.forEach((info,i)=>{
if(!info)return;
const t=titles[i],el=document.createElement("div");el.className="item";
const img=info.thumbnail&&info.thumbnail.source?`<img src="${esc(info.thumbnail.source)}" class="thumb" alt="">`:"";
const pageUrl=(info.content_urls&&info.content_urls.desktop&&info.content_urls.desktop.page)||WIKI+"/wiki/"+encodeURIComponent(t);
el.innerHTML=`${img}<div><a href="${esc(pageUrl)}" target="_blank" rel="noopener" class="r-title">${esc(info.title||t)}</a><div class="r-desc">${esc(info.description||"General Topic")}</div><p>${esc(info.extract)}</p><button type="button" class="speak-btn" onclick="speakText(this)">Listen to Summary</button></div>`;
el.querySelector("button").setAttribute("data-text",info.extract||"");
out.appendChild(el);
});
const valid=summaries.filter(x=>x&&x.extract);
const dateWords={"today":0,"what is today":0,"todays date":0,"today's date":0,"tomorrow":1,"what is tomorrow":1,"tomorrows date":1,"tomorrow's date":1,"yesterday":-1,"what was yesterday":-1};
const dOff=dateWords[q.trim().toLowerCase().replace(/[?]/g,"")];
let dateBullet="";
if(dOff!==undefined){
  const dt=new Date();dt.setDate(dt.getDate()+dOff);
  const label=dOff===0?"Today is":(dOff===1?"Tomorrow is":"Yesterday was");
  const fmt=dt.toLocaleDateString("en-US",{weekday:"long",year:"numeric",month:"long",day:"numeric"});
  dateBullet=`<li><strong>${label} ${fmt}.</strong></li>`;
}
if(valid.length || dateBullet){
  const points=valid.slice(0,3).map(x=>{
    const firstSent=x.extract.split(". ")[0].replace(/\.$/,"");
    return `<li><strong>${esc(x.title)}:</strong> ${esc(firstSent)}.</li>`;
  }).join("");
  const plainSummary=valid.slice(0,3).map(x=>x.extract.split(". ")[0]).join(". ");
  const aiBox=document.createElement("div");
  aiBox.style.cssText="margin-top:24px;padding:20px 22px;border-radius:16px;background:linear-gradient(135deg,rgba(0,68,204,.08),rgba(20,184,166,.12));border:1.5px solid var(--cyan);box-shadow:var(--sh);";
  aiBox.innerHTML=`<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px"><span style="font-size:.82rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--acc)">&#10024; Tesca AI Overview</span><span style="font-size:.75rem;color:var(--sub)">Synthesized from ${valid.slice(0,3).length} sources</span></div><ul style="padding-left:18px;line-height:1.6;margin-bottom:12px">${dateBullet}${points}</ul><button type="button" class="speak-btn" onclick="speakText(this)">&#128266; Listen to AI Overview</button>`;
  aiBox.querySelector("button").setAttribute("data-text",plainSummary);
  out.appendChild(aiBox);
}
localStorage.setItem(cKey,out.innerHTML);
}catch(e){out.innerHTML="<p>Search failed. Check your internet connection.</p>";}}
async function runZeroClick(q, out) {
  const ql = q.trim().toLowerCase();

  // 1. Live Weather (Open-Meteo - defaults to Bengaluru)
  if (ql === "weather" || ql.startsWith("weather ")) {
    const city = ql.replace(/^weather\s*/, "").trim() || "Bengaluru";
    const card = document.createElement("div");
    card.style.cssText = "background:linear-gradient(135deg,rgba(0,180,255,.12),rgba(20,184,166,.12));border:1.5px solid var(--cyan);border-radius:16px;padding:18px 22px;margin-bottom:20px";
    card.innerHTML = `<strong>Checking weather for ${esc(city)}...</strong>`;
    out.prepend(card);
    try {
      const geo = await fetch(`https://open-meteo.com{encodeURIComponent(city)}&count=1`).then(r => r.json());
      const loc = geo.results && geo.results;
      if (loc) {
        const w = await fetch(`https://open-meteo.com{loc.latitude}&longitude=${loc.longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m`).then(r => r.json());
        const c = w.current;
        card.innerHTML = `<div style="font-size:.75rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--acc)">Live Weather &bull; ${esc(loc.name)}, ${esc(loc.country || "")}</div><div style="font-size:2.1rem;font-weight:800;margin:4px 0">${c.temperature_2m}&deg;C</div><div style="font-size:.88rem;color:var(--sub)">Humidity: ${c.relative_humidity_2m}% &bull; Wind: ${c.wind_speed_10m} km/h</div>`;
      } else { card.remove(); }
    } catch (e) { card.remove(); }
    return;
  }

  // 2. Dictionary (DictionaryAPI.dev)
  if (ql.startsWith("define ")) {
    const word = ql.replace(/^define\s+/, "").trim();
    if (!word) return;
    const card = document.createElement("div");
    card.style.cssText = "background:var(--pill);border:1.5px solid var(--cyan);border-radius:16px;padding:18px 22px;margin-bottom:20px;box-shadow:var(--sh)";
    card.innerHTML = `<strong>Defining "${esc(word)}"...</strong>`;
    out.prepend(card);
    try {
      const res = await fetch(`https://dictionaryapi.dev{encodeURIComponent(word)}`).then(r => r.json());
      const entry = Array.isArray(res) ? res : null;
      if (entry && entry.meanings && entry.meanings) {
        const m = entry.meanings;
        const def = m.definitions.definition;
        card.innerHTML = `<div style="font-size:.75rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--acc)">Tesca Dictionary</div><h3 style="font-size:1.35rem;margin:4px 0">${esc(entry.word)} <span style="font-size:.92rem;color:var(--sub);font-weight:400">${esc(entry.phonetic || "")}</span></h3><div style="font-size:.82rem;font-style:italic;color:var(--acc);margin-bottom:6px">${esc(m.partOfSpeech)}</div><p style="line-height:1.55">${esc(def)}</p>`;
      } else { card.remove(); }
    } catch (e) { card.remove(); }
    return;
  }

  // 3. Unit & Currency Converter (km/miles, kg/lbs, c/f, usd/inr)
  const conv = ql.match(/^([\d.]+)\s*(km|miles|kg|lbs|c|f|usd|inr)\s+(?:to|in)\s+(km|miles|kg|lbs|c|f|usd|inr)$/);
  if (conv) {
    const val = parseFloat(conv), from = conv, to = conv;
    const fns = {
      "km_miles": v => v * 0.621371, "miles_km": v => v / 0.621371,
      "kg_lbs": v => v * 2.20462, "lbs_kg": v => v / 2.20462,
      "c_f": v => (v * 9/5) + 32, "f_c": v => (v - 32) * 5/9,
      "usd_inr": v => v * 84.5, "inr_usd": v => v / 84.5
    };
    if (fns[`${from}_${to}`]) {
      const ans = fns[`${from}_${to}`](val).toFixed(2);
      const card = document.createElement("div");
      card.style.cssText = "background:var(--pill);border:1.5px solid var(--cyan);border-radius:16px;padding:18px 22px;margin-bottom:20px;box-shadow:var(--sh)";
      card.innerHTML = `<div style="font-size:.75rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--acc)">Instant Converter</div><div style="font-size:1.65rem;font-weight:800;margin-top:4px">${val} ${from.toUpperCase()} = ${ans} ${to.toUpperCase()}</div>`;
      out.prepend(card);
      return;
    }
  }

  // 4. Math Calculator (e.g. 45 * 18)
  if (/^[0-9+\-*/().\s^%]+$/.test(ql) && /[+\-*/^%]/.test(ql)) {
    try {
      const ans = Function(`"use strict"; return (${ql.replace(/\^/g, "**")})`)();
      if (typeof ans === "number" && isFinite(ans)) {
        const card = document.createElement("div");
        card.style.cssText = "background:var(--pill);border:1.5px solid var(--cyan);border-radius:16px;padding:18px 22px;margin-bottom:20px;box-shadow:var(--sh)";
        card.innerHTML = `<div style="font-size:.75rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--acc)">Tesca Calculator</div><div style="font-size:.95rem;color:var(--sub)">${esc(q)} =</div><div style="font-size:1.85rem;font-weight:800">${ans}</div>`;
        out.prepend(card);
      }
    } catch (e) {}
  }
}

// 5. Search Bangs (!yt, !gh, !w, !g)
document.addEventListener("submit", e => {
  const form = e.target.closest("form[action='/search']");
  if (!form) return;
  const input = form.querySelector("input[name='q']");
  if (!input) return;
  const val = input.value.trim();
  const bangs = {
    "!yt ": "https://youtube.com",
    "!gh ": "https://github.com",
    "!w ":  "https://wikipedia.org",
    "!g ":  "https://google.com"
  };
  for (const [prefix, url] of Object.entries(bangs)) {
    if (val.toLowerCase().startsWith(prefix)) {
      e.preventDefault();
      location.href = url + encodeURIComponent(val.slice(prefix.length));
      return;
    }
  }
});
</script>
"""


HOME_HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Tesca</title><style>__STYLE__h1.tesca-title{font-size:4.2rem!important;font-family:"Bauhaus 93","Arial Rounded MT Bold","Trebuchet MS",sans-serif!important;font-weight:900!important;letter-spacing:6px!important;line-height:1.05!important;background:linear-gradient(90deg,#001f7a 0%,#0055cc 45%,#14b8a6 100%)!important;-webkit-background-clip:text!important;background-clip:text!important;-webkit-text-fill-color:transparent!important;-webkit-text-stroke:1px #000000!important;paint-order:stroke fill!important;border:none!important;margin:10px auto 24px!important;padding:0!important;display:inline-block!important}.fab-game{position:fixed!important;bottom:24px!important;right:24px!important;left:auto!important;background:linear-gradient(135deg,#0044cc,#00b4ff)!important;color:#fff!important;padding:12px 20px!important;border-radius:30px!important;display:inline-flex!important;align-items:center!important;gap:8px!important;font-size:1rem!important;font-weight:700!important;text-decoration:none!important;box-shadow:0 8px 24px rgba(0,119,255,.4)!important}.top-bar,.hero{position:relative;z-index:1}@media(max-width:932px),(pointer:coarse){.bg-rings{display:none!important}}.mobile-aurora{display:none}@media(max-width:932px),(pointer:coarse){.bg-rings{display:none!important}.mobile-aurora{display:block;position:fixed;top:-90px;left:50%;transform:translateX(-50%);width:130vw;height:280px;border-radius:50%;background:radial-gradient(ellipse at 50% 35%,rgba(0,119,255,.32) 0%,rgba(20,184,166,.22) 45%,transparent 75%);filter:blur(22px);pointer-events:none;z-index:0}}.mob-tab{display:none!important}.desk-tab{display:inline!important;writing-mode:vertical-rl;text-orientation:mixed}@media(max-width:950px),(pointer:coarse){.desk-tab{display:none!important}.mob-tab{display:inline!important;font-size:1.15rem;line-height:1}.bg-rings{display:none!important}}@media(orientation:landscape) and (max-height:520px){html,body{overflow-y:auto!important;height:auto!important;min-height:100vh!important}.hero{padding-top:54px!important;padding-bottom:20px!important}h1.tesca-title{font-size:2.4rem!important;margin:4px auto 10px!important}.trend-card{margin-top:10px!important}.fab-game{bottom:10px!important;right:10px!important;padding:8px 14px!important;font-size:.85rem!important}}</style></head><body>
<header class="top-bar"><div></div><div class="top-actions"><button type="button" class="icon-pill" onclick="toggleTheme()">Theme</button><button type="button" class="icon-pill" onclick="toggleSet()">Settings</button><div id="setMenu" class="set-menu"><div>Press <strong>/</strong> to focus search</div><div>Voice search via Mic icon</div></div><a href="/"><img src="/dod.png" alt="Tesca Logo" class="corner-logo"></a></div></header>
<main class="hero"><h1 id="tescaLogoTitle" class="tesca-title">TESCA</h1><form action="/search" method="GET" class="search-wrap"><div class="search-pill"><span class="s-icon">&#128269;</span><input id="qInput" name="q" class="search-box" placeholder="Search Tesca..." autocomplete="off" required><button type="button" class="mic-btn" onclick="startVoice()" title="Voice Search">&#127908;</button></div><div id="sugBox" class="suggestions"></div><div class="btn-row"><button type="submit" class="btn">Tesca Search</button><button type="submit" name="lucky" value="1" class="btn btn-sec">I'm Feeling Lucky</button></div></form><div class="trend-card"><div class="trend-head">Trending Topics</div><div class="chips"><a href="/search?q=Python+(programming+language)" class="chip">Python</a><a href="/search?q=Space+exploration" class="chip">Space Exploration</a><a href="/search?q=Artificial+intelligence" class="chip">Artificial Intelligence</a><a href="/search?q=Bengaluru" class="chip">Bengaluru</a></div></div></main>
<a href="/game" class="fab-game" style="z-index:9999!important;pointer-events:auto!important" title="Play Tesca Space"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="20" height="12" rx="6"/><path d="M6 12h4M8 10v4"/><circle cx="15" cy="11" r="1" fill="currentColor"/><circle cx="17" cy="13" r="1" fill="currentColor"/></svg><span>Game</span></a>
__JS__<div class="bg-rings" style="position:fixed;inset:0;pointer-events:none;overflow:hidden;z-index:0"><div style="position:absolute;width:420px;height:420px;border-radius:50%;top:15%;left:-140px;background:radial-gradient(circle,rgba(0,68,204,.22),transparent 70%)"></div><div style="position:absolute;width:440px;height:440px;border-radius:50%;bottom:10%;right:-140px;background:radial-gradient(circle,rgba(20,184,166,.22),transparent 70%)"></div><div style="position:absolute;width:240px;height:240px;border-radius:50%;top:34%;left:-95px;border:3px solid rgba(0,119,255,.22);box-shadow:0 0 0 34px rgba(20,184,166,.08)"></div><div style="position:absolute;width:280px;height:280px;border-radius:50%;top:22%;right:-115px;border:3px solid rgba(20,184,166,.24);box-shadow:0 0 0 38px rgba(0,68,204,.08)"></div></div><div class="mobile-aurora"></div><style>.side-panel{display:none;position:fixed;top:50%;transform:translateY(-50%);width:215px;background:var(--pill);border:1px solid var(--bdr);border-radius:18px;padding:16px;box-shadow:var(--sh);z-index:1100;font-size:.85rem;text-align:left;transition:transform .2s,border-color .2s}.side-panel:hover{border-color:var(--cyan)}.side-left{left:22px}.side-right{right:22px}.sp-title{font-size:.75rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--acc);margin-bottom:10px;display:flex;align-items:center;justify-content:space-between}.sp-clock{font-size:1.35rem;font-weight:800;color:var(--text);margin-bottom:2px}.sp-date{font-size:.78rem;color:var(--sub);margin-bottom:12px}.sp-btn{display:block;width:100%;text-align:left;background:var(--card);border:1px solid var(--bdr);color:var(--text);padding:8px 11px;border-radius:12px;font-size:.82rem;font-weight:600;cursor:pointer;margin-bottom:8px;text-decoration:none}.sp-btn:hover{border-color:var(--cyan);color:var(--acc)}.sp-fact{font-size:.78rem;color:var(--sub);line-height:1.4;background:var(--card);padding:8px 10px;border-radius:10px;min-height:48px}.sp-score{font-size:1.4rem;font-weight:800;color:var(--acc);margin:4px 0 10px}.sp-rec a{display:block;padding:5px 8px;border-radius:8px;color:var(--text);text-decoration:none;font-size:.8rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.sp-rec a:hover{background:var(--card);color:var(--acc)}@media(max-width:932px),(pointer:coarse){.bg-rings{display:none!important}}.mobile-aurora{display:none}@media(max-width:932px),(pointer:coarse){.bg-rings{display:none!important}.mobile-aurora{display:block;position:fixed;top:-90px;left:50%;transform:translateX(-50%);width:130vw;height:280px;border-radius:50%;background:radial-gradient(ellipse at 50% 35%,rgba(0,119,255,.32) 0%,rgba(20,184,166,.22) 45%,transparent 75%);filter:blur(22px);pointer-events:none;z-index:0}}</style>
<button type="button" onclick="toggleSide('leftPanel')" style="position:fixed;left:0;top:50%;transform:translateY(-50%);z-index:1250;background:linear-gradient(135deg,#0044cc,#00b4ff);color:#fff;border:none;border-radius:0 14px 14px 0;padding:12px 10px;cursor:pointer;font-weight:700;box-shadow:0 4px 14px rgba(0,119,255,.35)" title="Toggle Live Pulse"><span class="desk-tab">⏱ Pulse</span><span class="mob-tab" id="leftArrow">&#9654;</span></button><aside id="leftPanel" class="side-panel side-left" style="left:44px"><div class="sp-title"><span>Live Pulse</span><span>&#9201;</span></div><div id="spClk" class="sp-clock">--:--</div><div id="spDt" class="sp-date">Loading...</div><button type="button" class="sp-btn" onclick="randWiki()">&#127922; Random Article</button><button type="button" class="sp-btn" onclick="loadFact()">&#128161; Quick Fact</button><div id="spFact" class="sp-fact">Click "Quick Fact" for a bite-sized discovery!</div></aside>
<button type="button" onclick="toggleSide('rightPanel')" style="position:fixed;right:0;top:50%;transform:translateY(-50%);z-index:1250;background:linear-gradient(135deg,#0044cc,#14b8a6);color:#fff;border:none;border-radius:14px 0 0 14px;padding:12px 10px;cursor:pointer;font-weight:700;box-shadow:0 4px 14px rgba(20,184,166,.35)" title="Toggle Tesca Space"><span class="desk-tab">🚀 Space</span><span class="mob-tab" id="rightArrow">&#9664;</span></button><aside id="rightPanel" class="side-panel side-right" style="right:44px"><div class="sp-title"><span>Tesca Space</span><span>&#128640;</span></div><div style="font-size:.78rem;color:var(--sub)">Your High Score</div><div id="spHi" class="sp-score">0 pts</div><a href="/game" class="sp-btn" style="text-align:center;background:linear-gradient(135deg,#0044cc,#00b4ff);color:#fff;border:none">Play Now</a><div class="sp-title" style="margin-top:12px"><span>Recent</span><span>&#128337;</span></div><div id="spRec" class="sp-rec"><span style="font-size:.78rem;color:var(--sub)">No searches yet</span></div></aside>
<script>function toggleSide(id){const el=document.getElementById(id);if(!el)return;const open=el.style.display!=="block";el.style.display=open?"block":"none";const arr=document.getElementById(id==="leftPanel"?"leftArrow":"rightArrow");if(arr)arr.innerHTML=(id==="leftPanel")?(open?"&#9664;":"&#9654;"):(open?"&#9654;":"&#9664;");}function tick(){const d=new Date(),c=document.getElementById("spClk"),dt=document.getElementById("spDt");if(c)c.textContent=d.toLocaleTimeString([],{hour:"2-digit",minute:"2-digit",second:"2-digit"});if(dt)dt.textContent=d.toLocaleDateString([],{weekday:"short",month:"short",day:"numeric"});}tick();setInterval(tick,1000);const hi=document.getElementById("spHi");if(hi)hi.textContent=(localStorage.getItem("tesca-hi")||0)+" pts";const recBox=document.getElementById("spRec"),hist=JSON.parse(localStorage.getItem("tesca-hist")||"[]");if(recBox&&hist.length){recBox.innerHTML=hist.slice(0,3).map(x=>`<a href="/search?q=${encodeURIComponent(x)}">&#128269; ${esc(x)}</a>`).join("");}const sf=document.querySelector("form[action='/search']");if(sf)sf.addEventListener("submit",()=>{const v=document.getElementById("qInput").value.trim();if(v){const h=[v,...hist.filter(i=>i!==v)].slice(0,5);localStorage.setItem("tesca-hist",JSON.stringify(h));}});async function randWiki(){try{const r=await fetch("/fact"),d=await r.json();if(d.title)location.href="/search?q="+encodeURIComponent(d.title);else alert("Could not fetch article.");}catch(e){alert("Error fetching article.");}}async function loadFact(){const box=document.getElementById("spFact");if(!box)return;box.textContent="Fetching...";try{const r=await fetch("/fact"),d=await r.json();box.textContent=d.extract||"Could not load fact.";}catch(e){box.textContent="Could not load fact.";}}</script>
<!-- TESCA_WELCOME_START -->
<style>
.tw-backdrop{position:fixed;inset:0;background:rgba(4,7,17,.78);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);display:flex;align-items:center;justify-content:center;z-index:2500;padding:16px;perspective:1000px;transition:opacity .32s ease}
.tw-backdrop.tw-closing{opacity:0;pointer-events:none}
#twStars{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.tw-box{position:relative;width:100%;max-width:450px;background:rgba(13,22,48,.82);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);color:#f8fafc;border:2px solid #00b4ff;border-radius:22px;padding:38px 28px 58px;text-align:center;transform-style:preserve-3d;transition:transform .12s ease-out,box-shadow .3s ease,opacity .28s ease;animation:twPop .35s cubic-bezier(.16,1,.3,1),twNeon 3s ease-in-out infinite alternate;overflow:hidden}
.tw-box.tw-zoom-out{transform:scale(.9) translateY(8px)!important;opacity:0}
.tw-sheen{position:absolute;inset:0;pointer-events:none;background:radial-gradient(circle at var(--mx,50%) var(--my,50%),rgba(56,189,248,.22),transparent 60%);opacity:0;transition:opacity .25s}
.tw-box:hover .tw-sheen{opacity:1}
.tw-close{position:absolute;top:12px;right:14px;background:transparent;border:none;color:#e2e8f0;font-size:1.35rem;font-weight:700;cursor:pointer;line-height:1;padding:5px 9px;border-radius:10px;opacity:.85;z-index:2}
.tw-close:hover{opacity:1;background:rgba(56,189,248,.18)}
.tw-title{font-size:1.8rem;font-weight:800;letter-spacing:.5px;margin:6px 0;background:linear-gradient(90deg,#38bdf8,#2dd4bf,#60a5fa,#38bdf8);background-size:200% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;animation:twShimmer 3.5s linear infinite;min-height:2.4rem}
.tw-cursor{display:inline-block;width:3px;height:1.45rem;background:#38bdf8;margin-left:3px;vertical-align:middle;animation:twBlink .75s step-end infinite}
.tw-know{position:absolute;bottom:14px;right:16px;background:linear-gradient(135deg,#0044cc,#00b4ff);color:#fff;border:none;border-radius:999px;padding:8px 18px;font-size:.86rem;font-weight:700;cursor:pointer;box-shadow:0 4px 16px rgba(0,180,255,.4);opacity:0;transform:translateY(6px);transition:opacity .45s ease,transform .45s ease,box-shadow .2s;z-index:2}
.tw-know.tw-show{opacity:1;transform:translateY(0)}
.tw-know:hover{box-shadow:0 6px 22px rgba(45,212,191,.55)}
.tw-desc{font-size:.95rem;line-height:1.55;color:#cbd5e1;margin:12px 0 18px;text-align:left}
@keyframes twPop{from{opacity:0;transform:scale(.9)}to{opacity:1;transform:scale(1)}}
@keyframes twNeon{from{border-color:#00b4ff;box-shadow:0 0 22px rgba(0,180,255,.35),inset 0 0 14px rgba(0,180,255,.12)}to{border-color:#2dd4bf;box-shadow:0 0 34px rgba(45,212,191,.55),inset 0 0 20px rgba(45,212,191,.18)}}
@keyframes twShimmer{to{background-position:200% center}}
@keyframes twBlink{50%{opacity:0}}
</style>

<div id="tescaWelcomeOverlay" class="tw-backdrop">
  <canvas id="twStars"></canvas>

  <!-- Box 1: Welcome to Tesca -->
  <div id="tescaWelcomeBox" class="tw-box">
    <div class="tw-sheen"></div>
    <button type="button" class="tw-close" onclick="closeTescaWelcome()" title="Close">&#10005;</button>
    <div class="tw-title"><span id="twTypeText"></span><span id="twCursor" class="tw-cursor"></span></div>
    <button type="button" id="twKnowBtn" class="tw-know" onclick="openTescaKnowMore()">Know more</button>
  </div>

  <!-- Box 2: Description of Tesca -->
  <div id="tescaDescBox" class="tw-box" style="display:none;padding-bottom:26px">
    <div class="tw-sheen"></div>
    <button type="button" class="tw-close" onclick="closeTescaWelcome()" title="Close">&#10005;</button>
    <div class="tw-title" style="font-size:1.5rem">About Tesca</div>
    <p class="tw-desc">
      <strong>Tesca</strong> is a fast, modern search engine built by <strong>Jayden</strong>. Explore instant answers, discover live facts in <strong>Live Pulse</strong>, switch between light and dark themes, or launch your ship in the built-in <strong>Tesca Space</strong> arcade game.
    </p>
    <button type="button" class="btn" onclick="closeTescaWelcome()" style="width:100%;padding:11px;position:relative;z-index:2">Start Exploring</button>
  </div>
</div>

<script>
(function(){
  // 1. Typewriter Text Reveal
  const msg = "Welcome to Tesca";
  const target = document.getElementById("twTypeText");
  const knowBtn = document.getElementById("twKnowBtn");
  let idx = 0;
  function typeNext(){
    if(!target) return;
    if(idx < msg.length){
      target.textContent += msg.charAt(idx++);
      setTimeout(typeNext, 55);
    } else if(knowBtn) {
      knowBtn.classList.add("tw-show");
    }
  }
  setTimeout(typeNext, 180);

  // 2. Smooth 3D Hover Tilt & Light Sheen (Desktop)
  document.querySelectorAll(".tw-box").forEach(card => {
    card.addEventListener("mousemove", e => {
      const r = card.getBoundingClientRect();
      const x = e.clientX - r.left, y = e.clientY - r.top;
      const rx = ((y / r.height) - 0.5) * -10;
      const ry = ((x / r.width) - 0.5) * 10;
      card.style.setProperty("--mx", (x / r.width * 100) + "%");
      card.style.setProperty("--my", (y / r.height * 100) + "%");
      card.style.transform = `rotateX(${rx}deg) rotateY(${ry}deg)`;
    });
    card.addEventListener("mouseleave", () => {
      card.style.transform = "rotateX(0deg) rotateY(0deg)";
    });
  });

  // 3. Stardust Particles behind card
  const c = document.getElementById("twStars");
  if(c){
    const ctx = c.getContext("2d");
    let w = c.width = window.innerWidth, h = c.height = window.innerHeight;
    window.addEventListener("resize", () => { w = c.width = window.innerWidth; h = c.height = window.innerHeight; });
    const pts = Array.from({length: 45}, () => ({
      x: Math.random() * w, y: Math.random() * h,
      r: Math.random() * 2 + 0.8,
      vx: (Math.random() - 0.5) * 0.6, vy: -Math.random() * 0.7 - 0.2,
      col: Math.random() > 0.5 ? "rgba(56,189,248,.75)" : "rgba(45,212,191,.75)"
    }));
    function animStars(){
      const ov = document.getElementById("tescaWelcomeOverlay");
      if(!ov || ov.style.display === "none") return;
      ctx.clearRect(0, 0, w, h);
      pts.forEach(p => {
        p.x += p.vx; p.y += p.vy;
        if(p.y < 0) p.y = h;
        if(p.x < 0) p.x = w;
        if(p.x > w) p.x = 0;
        ctx.fillStyle = p.col;
        ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2); ctx.fill();
      });
      requestAnimationFrame(animStars);
    }
    animStars();
  }
})();

function closeTescaWelcome() {
  const ov = document.getElementById("tescaWelcomeOverlay");
  document.querySelectorAll(".tw-box").forEach(b => b.classList.add("tw-zoom-out"));
  if(ov){
    ov.classList.add("tw-closing");
    setTimeout(() => { ov.style.display = "none"; }, 300);
  }
}

function openTescaKnowMore() {
  const wBox = document.getElementById("tescaWelcomeBox");
  const dBox = document.getElementById("tescaDescBox");
  wBox.classList.add("tw-zoom-out");
  setTimeout(() => {
    wBox.style.display = "none";
    wBox.classList.remove("tw-zoom-out");
    dBox.style.display = "block";
  }, 220);
}
</script>
<!-- TESCA_WELCOME_END -->
</body></html>""".replace("__STYLE__", STYLE).replace("__JS__", JS)








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
const ql=q.trim().toLowerCase();
let greetHtml="";
if(["hi","hello","hey","hiya","how are you","who are you"].includes(ql)){
  greetHtml=`<div style="background:linear-gradient(135deg,rgba(0,68,204,.1),rgba(20,184,166,.12));border:1.5px solid var(--cyan);border-radius:16px;padding:20px 22px;margin-bottom:20px"><div style="font-size:.78rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--acc);margin-bottom:6px">Tesca Assistant</div><h3 style="margin-bottom:6px">Hi I'm Tesca</h3><p style="line-height:1.55">Ask me about any topic and feel free to play the built-in <a href="/game" style="color:var(--acc);font-weight:700">Tesca Space</a> game!</p></div>`;
}
try{
const [r,spR]=await Promise.all([
  fetch(WIKI+"/w/api.php?action=opensearch&format=json&origin=*&limit=6&profile=engine_autoselect&search="+encodeURIComponent(q)),
  fetch(WIKI+"/w/api.php?action=query&list=search&srinfo=suggestion&srlimit=1&format=json&origin=*&srsearch="+encodeURIComponent(q))
]);
let didYouMeanHtml="";
try{
  const spD=await spR.json();
  const sug=spD&&spD.query&&spD.query.searchinfo&&spD.query.searchinfo.suggestion;
  if(sug && sug.toLowerCase()!==q.trim().toLowerCase()){
    didYouMeanHtml=`<div style="margin-bottom:16px;font-size:.98rem;color:var(--sub)">Did you mean: <a href="/search?q=${encodeURIComponent(sug)}" style="color:var(--acc);font-weight:700;font-style:italic;text-decoration:none">${esc(sug)}</a>?</div>`;
  }
}catch(e){}
const d=await r.json(),titles=Array.isArray(d)?d.at(1)||[]:[],urls=Array.isArray(d)?d.at(3)||[]:[];
if(!titles.length){out.innerHTML=(didYouMeanHtml+greetHtml)||"<p>No articles found for <strong>"+esc(q)+"</strong>.</p>";return;}
if(lucky&&urls.at(0)){location.href=urls.at(0);return;}
const cKey="tesca-cache-v7-"+q.toLowerCase();
const cached=sessionStorage.getItem(cKey);
if(cached){out.innerHTML=cached;return;}
out.innerHTML=[1,2,3].map(()=>'<div class="item"><div class="skel" style="width:92px;height:92px;flex-shrink:0"></div><div style="flex:1"><div class="skel" style="height:20px;width:55%;margin-bottom:10px"></div><div class="skel" style="height:14px;width:90%;margin-bottom:8px"></div><div class="skel" style="height:14px;width:75%"></div></div></div>').join("");
const summaries=await Promise.all(titles.map(t=>fetch(WIKI+"/api/rest_v1/page/summary/"+encodeURIComponent(t.replace(/ /g,"_"))).then(res=>res.ok?res.json():null).catch(()=>null)));
try{
  const cr=await fetch("/chat?q="+encodeURIComponent(q));
  const cd=await cr.json();
  if(cd&&cd.title){
    const label=cd.type==="meme"?"Tesca Meme Drop":"Tesca Chat";
    
    greetHtml+=`<div style="background:linear-gradient(135deg,rgba(0,68,204,.1),rgba(20,184,166,.12));border:1.5px solid var(--cyan);border-radius:16px;padding:18px 20px;margin-bottom:20px"><div style="font-size:.75rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--acc);margin-bottom:4px">${label}</div><h3 style="margin-bottom:6px">${esc(cd.title)}</h3><p style="line-height:1.55">${esc(cd.text)}</p>${cd.img?`<img src="${esc(cd.img)}" alt="Meme" style="max-width:100%;max-height:340px;border-radius:12px;margin-top:10px;display:block">`:""}</div>`;
  }
}catch(e){}
out.innerHTML=didYouMeanHtml+greetHtml;
summaries.forEach((info,i)=>{
if(!info)return;
const t=titles[i],el=document.createElement("div");el.className="item";
const img=info.thumbnail&&info.thumbnail.source?`<img src="${esc(info.thumbnail.source)}" class="thumb" alt="">`:"";
const pageUrl=(info.content_urls&&info.content_urls.desktop&&info.content_urls.desktop.page)||WIKI+"/wiki/"+encodeURIComponent(t);
el.innerHTML=`${img}<div><a href="${esc(pageUrl)}" target="_blank" rel="noopener" class="r-title">${esc(info.title||t)}</a><div class="r-desc">${esc(info.description||"General Topic")}</div><p>${esc(info.extract)}</p><button type="button" class="speak-btn" onclick="speakText(this)">Listen to Summary</button></div>`;
el.querySelector("button").setAttribute("data-text",info.extract||"");
out.appendChild(el);
});
const valid=summaries.filter(x=>x&&x.extract);
const dateWords={"today":0,"what is today":0,"todays date":0,"today's date":0,"tomorrow":1,"what is tomorrow":1,"tomorrows date":1,"tomorrow's date":1,"yesterday":-1,"what was yesterday":-1};
const dOff=dateWords[q.trim().toLowerCase().replace(/[?]/g,"")];
let dateBullet="";
if(dOff!==undefined){
  const dt=new Date();dt.setDate(dt.getDate()+dOff);
  const label=dOff===0?"Today is":(dOff===1?"Tomorrow is":"Yesterday was");
  const fmt=dt.toLocaleDateString("en-US",{weekday:"long",year:"numeric",month:"long",day:"numeric"});
  dateBullet=`<li><strong>${label} ${fmt}.</strong></li>`;
}
if(valid.length || dateBullet){
  const points=valid.slice(0,3).map(x=>{
    const firstSent=x.extract.split(". ")[0].replace(/\.$/,"");
    return `<li><strong>${esc(x.title)}:</strong> ${esc(firstSent)}.</li>`;
  }).join("");
  const plainSummary=valid.slice(0,3).map(x=>x.extract.split(". ")[0]).join(". ");
  const aiBox=document.createElement("div");
  aiBox.style.cssText="margin-top:24px;padding:20px 22px;border-radius:16px;background:linear-gradient(135deg,rgba(0,68,204,.08),rgba(20,184,166,.12));border:1.5px solid var(--cyan);box-shadow:var(--sh);";
  aiBox.innerHTML=`<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px"><span style="font-size:.82rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--acc)">&#10024; Tesca AI Overview</span><span style="font-size:.75rem;color:var(--sub)">Synthesized from ${valid.slice(0,3).length} sources</span></div><ul style="padding-left:18px;line-height:1.6;margin-bottom:12px">${dateBullet}${points}</ul><button type="button" class="speak-btn" onclick="speakText(this)">&#128266; Listen to AI Overview</button>`;
  aiBox.querySelector("button").setAttribute("data-text",plainSummary);
  out.appendChild(aiBox);
}
sessionStorage.setItem(cKey,out.innerHTML);
}catch(e){out.innerHTML="<p>Search failed. Check your internet connection.</p>";}}
</script>
"""


HOME_HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Tesca</title><style>__STYLE__h1.tesca-title{font-size:4.2rem!important;font-family:"Bauhaus 93","Arial Rounded MT Bold","Trebuchet MS",sans-serif!important;font-weight:900!important;letter-spacing:6px!important;line-height:1.05!important;background:linear-gradient(90deg,#001f7a 0%,#0055cc 45%,#14b8a6 100%)!important;-webkit-background-clip:text!important;background-clip:text!important;-webkit-text-fill-color:transparent!important;-webkit-text-stroke:1px #000000!important;paint-order:stroke fill!important;border:none!important;margin:10px auto 24px!important;padding:0!important;display:inline-block!important}.fab-game{position:fixed!important;bottom:24px!important;right:24px!important;left:auto!important;background:linear-gradient(135deg,#0044cc,#00b4ff)!important;color:#fff!important;padding:12px 20px!important;border-radius:30px!important;display:inline-flex!important;align-items:center!important;gap:8px!important;font-size:1rem!important;font-weight:700!important;text-decoration:none!important;box-shadow:0 8px 24px rgba(0,119,255,.4)!important}.top-bar,.hero{position:relative;z-index:1}@media(max-width:932px),(pointer:coarse){.bg-rings{display:none!important}}.mobile-aurora{display:none}@media(max-width:932px),(pointer:coarse){.bg-rings{display:none!important}.mobile-aurora{display:block;position:fixed;top:-90px;left:50%;transform:translateX(-50%);width:130vw;height:280px;border-radius:50%;background:radial-gradient(ellipse at 50% 35%,rgba(0,119,255,.32) 0%,rgba(20,184,166,.22) 45%,transparent 75%);filter:blur(22px);pointer-events:none;z-index:0}}.mob-tab{display:none!important}.desk-tab{display:inline!important;writing-mode:vertical-rl;text-orientation:mixed}@media(max-width:950px),(pointer:coarse){.desk-tab{display:none!important}.mob-tab{display:inline!important;font-size:1.15rem;line-height:1}.bg-rings{display:none!important}}@media(orientation:landscape) and (max-height:520px){html,body{overflow-y:auto!important;height:auto!important;min-height:100vh!important}.hero{padding-top:54px!important;padding-bottom:20px!important}h1.tesca-title{font-size:2.4rem!important;margin:4px auto 10px!important}.trend-card{margin-top:10px!important}.fab-game{bottom:10px!important;right:10px!important;padding:8px 14px!important;font-size:.85rem!important}}</style></head><body>
<header class="top-bar"><div></div><div class="top-actions"><button type="button" class="icon-pill" onclick="toggleTheme()">Theme</button><button type="button" class="icon-pill" onclick="toggleSet()">Settings</button><div id="setMenu" class="set-menu"><div>Press <strong>/</strong> to focus search</div><div>Voice search via Mic icon</div></div><a href="/"><img src="/dod.png" alt="Tesca Logo" class="corner-logo"></a></div></header>
<main class="hero"><h1 id="tescaLogoTitle" class="tesca-title">TESCA</h1><form action="/search" method="GET" class="search-wrap"><div class="search-pill"><span class="s-icon">&#128269;</span><input id="qInput" name="q" class="search-box" placeholder="Search Tesca..." autocomplete="off" required><button type="button" class="mic-btn" onclick="startVoice()" title="Voice Search">&#127908;</button></div><div id="sugBox" class="suggestions"></div><div class="btn-row"><button type="submit" class="btn">Tesca Search</button><button type="submit" name="lucky" value="1" class="btn btn-sec">I'm Feeling Lucky</button></div></form><div class="trend-card"><div class="trend-head">Trending Topics</div><div class="chips"><a href="/search?q=Python+(programming+language)" class="chip">Python</a><a href="/search?q=Space+exploration" class="chip">Space Exploration</a><a href="/search?q=Artificial+intelligence" class="chip">Artificial Intelligence</a><a href="/search?q=Bengaluru" class="chip">Bengaluru</a></div></div></main>
<a href="/game" class="fab-game" style="z-index:9999!important;pointer-events:auto!important" title="Play Tesca Space"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="20" height="12" rx="6"/><path d="M6 12h4M8 10v4"/><circle cx="15" cy="11" r="1" fill="currentColor"/><circle cx="17" cy="13" r="1" fill="currentColor"/></svg><span>Game</span></a>
__JS__<div class="bg-rings" style="position:fixed;inset:0;pointer-events:none;overflow:hidden;z-index:0"><div style="position:absolute;width:420px;height:420px;border-radius:50%;top:15%;left:-140px;background:radial-gradient(circle,rgba(0,68,204,.22),transparent 70%)"></div><div style="position:absolute;width:440px;height:440px;border-radius:50%;bottom:10%;right:-140px;background:radial-gradient(circle,rgba(20,184,166,.22),transparent 70%)"></div><div style="position:absolute;width:240px;height:240px;border-radius:50%;top:34%;left:-95px;border:3px solid rgba(0,119,255,.22);box-shadow:0 0 0 34px rgba(20,184,166,.08)"></div><div style="position:absolute;width:280px;height:280px;border-radius:50%;top:22%;right:-115px;border:3px solid rgba(20,184,166,.24);box-shadow:0 0 0 38px rgba(0,68,204,.08)"></div></div><div class="mobile-aurora"></div><style>.side-panel{display:none;position:fixed;top:50%;transform:translateY(-50%);width:215px;background:var(--pill);border:1px solid var(--bdr);border-radius:18px;padding:16px;box-shadow:var(--sh);z-index:1100;font-size:.85rem;text-align:left;transition:transform .2s,border-color .2s}.side-panel:hover{border-color:var(--cyan)}.side-left{left:22px}.side-right{right:22px}.sp-title{font-size:.75rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--acc);margin-bottom:10px;display:flex;align-items:center;justify-content:space-between}.sp-clock{font-size:1.35rem;font-weight:800;color:var(--text);margin-bottom:2px}.sp-date{font-size:.78rem;color:var(--sub);margin-bottom:12px}.sp-btn{display:block;width:100%;text-align:left;background:var(--card);border:1px solid var(--bdr);color:var(--text);padding:8px 11px;border-radius:12px;font-size:.82rem;font-weight:600;cursor:pointer;margin-bottom:8px;text-decoration:none}.sp-btn:hover{border-color:var(--cyan);color:var(--acc)}.sp-fact{font-size:.78rem;color:var(--sub);line-height:1.4;background:var(--card);padding:8px 10px;border-radius:10px;min-height:48px}.sp-score{font-size:1.4rem;font-weight:800;color:var(--acc);margin:4px 0 10px}.sp-rec a{display:block;padding:5px 8px;border-radius:8px;color:var(--text);text-decoration:none;font-size:.8rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.sp-rec a:hover{background:var(--card);color:var(--acc)}@media(max-width:932px),(pointer:coarse){.bg-rings{display:none!important}}.mobile-aurora{display:none}@media(max-width:932px),(pointer:coarse){.bg-rings{display:none!important}.mobile-aurora{display:block;position:fixed;top:-90px;left:50%;transform:translateX(-50%);width:130vw;height:280px;border-radius:50%;background:radial-gradient(ellipse at 50% 35%,rgba(0,119,255,.32) 0%,rgba(20,184,166,.22) 45%,transparent 75%);filter:blur(22px);pointer-events:none;z-index:0}}</style>
<button type="button" onclick="toggleSide('leftPanel')" style="position:fixed;left:0;top:50%;transform:translateY(-50%);z-index:1250;background:linear-gradient(135deg,#0044cc,#00b4ff);color:#fff;border:none;border-radius:0 14px 14px 0;padding:12px 10px;cursor:pointer;font-weight:700;box-shadow:0 4px 14px rgba(0,119,255,.35)" title="Toggle Live Pulse"><span class="desk-tab">⏱ Pulse</span><span class="mob-tab" id="leftArrow">&#9654;</span></button><aside id="leftPanel" class="side-panel side-left" style="left:44px"><div class="sp-title"><span>Live Pulse</span><span>&#9201;</span></div><div id="spClk" class="sp-clock">--:--</div><div id="spDt" class="sp-date">Loading...</div><button type="button" class="sp-btn" onclick="randWiki()">&#127922; Random Article</button><button type="button" class="sp-btn" onclick="loadFact()">&#128161; Quick Fact</button><div id="spFact" class="sp-fact">Click "Quick Fact" for a bite-sized discovery!</div></aside>
<button type="button" onclick="toggleSide('rightPanel')" style="position:fixed;right:0;top:50%;transform:translateY(-50%);z-index:1250;background:linear-gradient(135deg,#0044cc,#14b8a6);color:#fff;border:none;border-radius:14px 0 0 14px;padding:12px 10px;cursor:pointer;font-weight:700;box-shadow:0 4px 14px rgba(20,184,166,.35)" title="Toggle Tesca Space"><span class="desk-tab">🚀 Space</span><span class="mob-tab" id="rightArrow">&#9664;</span></button><aside id="rightPanel" class="side-panel side-right" style="right:44px"><div class="sp-title"><span>Tesca Space</span><span>&#128640;</span></div><div style="font-size:.78rem;color:var(--sub)">Your High Score</div><div id="spHi" class="sp-score">0 pts</div><a href="/game" class="sp-btn" style="text-align:center;background:linear-gradient(135deg,#0044cc,#00b4ff);color:#fff;border:none">Play Now</a><div class="sp-title" style="margin-top:12px"><span>Recent</span><span>&#128337;</span></div><div id="spRec" class="sp-rec"><span style="font-size:.78rem;color:var(--sub)">No searches yet</span></div></aside>
<script>function toggleSide(id){const el=document.getElementById(id);if(!el)return;const open=el.style.display!=="block";el.style.display=open?"block":"none";const arr=document.getElementById(id==="leftPanel"?"leftArrow":"rightArrow");if(arr)arr.innerHTML=(id==="leftPanel")?(open?"&#9664;":"&#9654;"):(open?"&#9654;":"&#9664;");}function tick(){const d=new Date(),c=document.getElementById("spClk"),dt=document.getElementById("spDt");if(c)c.textContent=d.toLocaleTimeString([],{hour:"2-digit",minute:"2-digit",second:"2-digit"});if(dt)dt.textContent=d.toLocaleDateString([],{weekday:"short",month:"short",day:"numeric"});}tick();setInterval(tick,1000);const hi=document.getElementById("spHi");if(hi)hi.textContent=(localStorage.getItem("tesca-hi")||0)+" pts";const recBox=document.getElementById("spRec"),hist=JSON.parse(localStorage.getItem("tesca-hist")||"[]");if(recBox&&hist.length){recBox.innerHTML=hist.slice(0,3).map(x=>`<a href="/search?q=${encodeURIComponent(x)}">&#128269; ${esc(x)}</a>`).join("");}const sf=document.querySelector("form[action='/search']");if(sf)sf.addEventListener("submit",()=>{const v=document.getElementById("qInput").value.trim();if(v){const h=[v,...hist.filter(i=>i!==v)].slice(0,5);localStorage.setItem("tesca-hist",JSON.stringify(h));}});async function randWiki(){try{const r=await fetch("/fact"),d=await r.json();if(d.title)location.href="/search?q="+encodeURIComponent(d.title);else alert("Could not fetch article.");}catch(e){alert("Error fetching article.");}}async function loadFact(){const box=document.getElementById("spFact");if(!box)return;box.textContent="Fetching...";try{const r=await fetch("/fact"),d=await r.json();box.textContent=d.extract||"Could not load fact.";}catch(e){box.textContent="Could not load fact.";}}</script>
<!-- TESCA_WELCOME_START -->
<style>
.tw-backdrop{position:fixed;inset:0;background:rgba(4,7,17,.78);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);display:flex;align-items:center;justify-content:center;z-index:2500;padding:16px;perspective:1000px;transition:opacity .32s ease}
.tw-backdrop.tw-closing{opacity:0;pointer-events:none}
#twStars{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.tw-box{position:relative;width:100%;max-width:450px;background:rgba(13,22,48,.82);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);color:#f8fafc;border:2px solid #00b4ff;border-radius:22px;padding:38px 28px 58px;text-align:center;transform-style:preserve-3d;transition:transform .12s ease-out,box-shadow .3s ease,opacity .28s ease;animation:twPop .35s cubic-bezier(.16,1,.3,1),twNeon 3s ease-in-out infinite alternate;overflow:hidden}
.tw-box.tw-zoom-out{transform:scale(.9) translateY(8px)!important;opacity:0}
.tw-sheen{position:absolute;inset:0;pointer-events:none;background:radial-gradient(circle at var(--mx,50%) var(--my,50%),rgba(56,189,248,.22),transparent 60%);opacity:0;transition:opacity .25s}
.tw-box:hover .tw-sheen{opacity:1}
.tw-close{position:absolute;top:12px;right:14px;background:transparent;border:none;color:#e2e8f0;font-size:1.35rem;font-weight:700;cursor:pointer;line-height:1;padding:5px 9px;border-radius:10px;opacity:.85;z-index:2}
.tw-close:hover{opacity:1;background:rgba(56,189,248,.18)}
.tw-title{font-size:1.8rem;font-weight:800;letter-spacing:.5px;margin:6px 0;background:linear-gradient(90deg,#38bdf8,#2dd4bf,#60a5fa,#38bdf8);background-size:200% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;animation:twShimmer 3.5s linear infinite;min-height:2.4rem}
.tw-cursor{display:inline-block;width:3px;height:1.45rem;background:#38bdf8;margin-left:3px;vertical-align:middle;animation:twBlink .75s step-end infinite}
.tw-know{position:absolute;bottom:14px;right:16px;background:linear-gradient(135deg,#0044cc,#00b4ff);color:#fff;border:none;border-radius:999px;padding:8px 18px;font-size:.86rem;font-weight:700;cursor:pointer;box-shadow:0 4px 16px rgba(0,180,255,.4);opacity:0;transform:translateY(6px);transition:opacity .45s ease,transform .45s ease,box-shadow .2s;z-index:2}
.tw-know.tw-show{opacity:1;transform:translateY(0)}
.tw-know:hover{box-shadow:0 6px 22px rgba(45,212,191,.55)}
.tw-desc{font-size:.95rem;line-height:1.55;color:#cbd5e1;margin:12px 0 18px;text-align:left}
@keyframes twPop{from{opacity:0;transform:scale(.9)}to{opacity:1;transform:scale(1)}}
@keyframes twNeon{from{border-color:#00b4ff;box-shadow:0 0 22px rgba(0,180,255,.35),inset 0 0 14px rgba(0,180,255,.12)}to{border-color:#2dd4bf;box-shadow:0 0 34px rgba(45,212,191,.55),inset 0 0 20px rgba(45,212,191,.18)}}
@keyframes twShimmer{to{background-position:200% center}}
@keyframes twBlink{50%{opacity:0}}
</style>

<div id="tescaWelcomeOverlay" class="tw-backdrop">
  <canvas id="twStars"></canvas>

  <!-- Box 1: Welcome to Tesca -->
  <div id="tescaWelcomeBox" class="tw-box">
    <div class="tw-sheen"></div>
    <button type="button" class="tw-close" onclick="closeTescaWelcome()" title="Close">&#10005;</button>
    <div class="tw-title"><span id="twTypeText"></span><span id="twCursor" class="tw-cursor"></span></div>
    <button type="button" id="twKnowBtn" class="tw-know" onclick="openTescaKnowMore()">Know more</button>
  </div>

  <!-- Box 2: Description of Tesca -->
  <div id="tescaDescBox" class="tw-box" style="display:none;padding-bottom:26px">
    <div class="tw-sheen"></div>
    <button type="button" class="tw-close" onclick="closeTescaWelcome()" title="Close">&#10005;</button>
    <div class="tw-title" style="font-size:1.5rem">About Tesca</div>
    <p class="tw-desc">
      <strong>Tesca</strong> is a fast, modern search engine built by <strong>Jayden</strong>. Explore instant answers, discover live facts in <strong>Live Pulse</strong>, switch between light and dark themes, or launch your ship in the built-in <strong>Tesca Space</strong> arcade game.
    </p>
    <button type="button" class="btn" onclick="closeTescaWelcome()" style="width:100%;padding:11px;position:relative;z-index:2">Start Exploring</button>
  </div>
</div>

<script>
(function(){
  // 1. Typewriter Text Reveal
  const msg = "Welcome to Tesca";
  const target = document.getElementById("twTypeText");
  const knowBtn = document.getElementById("twKnowBtn");
  let idx = 0;
  function typeNext(){
    if(!target) return;
    if(idx < msg.length){
      target.textContent += msg.charAt(idx++);
      setTimeout(typeNext, 55);
    } else if(knowBtn) {
      knowBtn.classList.add("tw-show");
    }
  }
  setTimeout(typeNext, 180);

  // 2. Smooth 3D Hover Tilt & Light Sheen (Desktop)
  document.querySelectorAll(".tw-box").forEach(card => {
    card.addEventListener("mousemove", e => {
      const r = card.getBoundingClientRect();
      const x = e.clientX - r.left, y = e.clientY - r.top;
      const rx = ((y / r.height) - 0.5) * -10;
      const ry = ((x / r.width) - 0.5) * 10;
      card.style.setProperty("--mx", (x / r.width * 100) + "%");
      card.style.setProperty("--my", (y / r.height * 100) + "%");
      card.style.transform = `rotateX(${rx}deg) rotateY(${ry}deg)`;
    });
    card.addEventListener("mouseleave", () => {
      card.style.transform = "rotateX(0deg) rotateY(0deg)";
    });
  });

  // 3. Stardust Particles behind card
  const c = document.getElementById("twStars");
  if(c){
    const ctx = c.getContext("2d");
    let w = c.width = window.innerWidth, h = c.height = window.innerHeight;
    window.addEventListener("resize", () => { w = c.width = window.innerWidth; h = c.height = window.innerHeight; });
    const pts = Array.from({length: 45}, () => ({
      x: Math.random() * w, y: Math.random() * h,
      r: Math.random() * 2 + 0.8,
      vx: (Math.random() - 0.5) * 0.6, vy: -Math.random() * 0.7 - 0.2,
      col: Math.random() > 0.5 ? "rgba(56,189,248,.75)" : "rgba(45,212,191,.75)"
    }));
    function animStars(){
      const ov = document.getElementById("tescaWelcomeOverlay");
      if(!ov || ov.style.display === "none") return;
      ctx.clearRect(0, 0, w, h);
      pts.forEach(p => {
        p.x += p.vx; p.y += p.vy;
        if(p.y < 0) p.y = h;
        if(p.x < 0) p.x = w;
        if(p.x > w) p.x = 0;
        ctx.fillStyle = p.col;
        ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2); ctx.fill();
      });
      requestAnimationFrame(animStars);
    }
    animStars();
  }
})();

function closeTescaWelcome() {
  const ov = document.getElementById("tescaWelcomeOverlay");
  document.querySelectorAll(".tw-box").forEach(b => b.classList.add("tw-zoom-out"));
  if(ov){
    ov.classList.add("tw-closing");
    setTimeout(() => { ov.style.display = "none"; }, 300);
  }
}

function openTescaKnowMore() {
  const wBox = document.getElementById("tescaWelcomeBox");
  const dBox = document.getElementById("tescaDescBox");
  wBox.classList.add("tw-zoom-out");
  setTimeout(() => {
    wBox.style.display = "none";
    wBox.classList.remove("tw-zoom-out");
    dBox.style.display = "block";
  }, 220);
}
</script>
<!-- TESCA_WELCOME_END -->
</body></html>""".replace("__STYLE__", STYLE).replace("__JS__", JS)








