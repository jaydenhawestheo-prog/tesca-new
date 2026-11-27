GAME_HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Tesca Space</title><style>
*{box-sizing:border-box;margin:0;padding:0}
body{background:#050914;color:#e2e8f0;font-family:"Segoe UI",Arial,sans-serif;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;overflow:hidden}
.bar{position:fixed;top:0;left:0;right:0;padding:12px 24px;display:flex;justify-content:space-between;align-items:center;background:rgba(11,19,43,.95);border-bottom:2px solid #00b4ff;z-index:10}
.brand{font-size:1.3rem;font-weight:700;color:#00b4ff;text-decoration:none}
.hud{display:flex;gap:20px;font-size:1rem;font-weight:600}
.btns{display:flex;gap:10px}
.hbtn{background:#16203c;color:#7dd3fc;border:1px solid #00b4ff;padding:7px 14px;border-radius:18px;font-size:.88rem;font-weight:600;cursor:pointer}
.bbtn{background:#0044cc;color:#fff;padding:7px 16px;border-radius:18px;text-decoration:none;font-size:.88rem;font-weight:600}
canvas{touch-action:none;background:radial-gradient(circle at 50% 40%,#0f1e45 0%,#040711 100%);border:2px solid #00b4ff;border-radius:14px;margin-top:54px;max-width:95vw;box-shadow:0 0 30px rgba(0,180,255,.25)}
#ov{position:absolute;max-width:460px;width:92%;background:rgba(11,19,43,.97);padding:22px 26px;border-radius:16px;border:2px solid #00b4ff;z-index:20;box-shadow:0 16px 40px rgba(0,0,0,.7)}
#ov h1{color:#00b4ff;font-size:1.6rem;text-align:center;margin-bottom:2px}
#sub{text-align:center;color:#bae6fd;font-weight:600;margin-bottom:12px}
.box{background:#070d1f;border:1px solid #1e3a8a;border-radius:10px;padding:10px 14px;margin-bottom:10px;font-size:.86rem;line-height:1.5}
.box h3{color:#38bdf8;font-size:.92rem;margin-bottom:4px}
.box ul{padding-left:18px}
.tip{font-size:.8rem;color:#94a3b8;text-align:center;margin-bottom:12px}
.go{display:block;width:100%;background:linear-gradient(90deg,#0044cc,#00b4ff);color:#fff;border:none;padding:12px;border-radius:24px;font-size:1.05rem;font-weight:700;cursor:pointer}
.mctrls{display:none;gap:14px;margin-top:12px;width:95vw;max-width:460px;justify-content:space-between}.mbtn{flex:1;background:#16203c;color:#7dd3fc;border:2px solid #00b4ff;padding:14px 0;border-radius:18px;font-size:1.25rem;font-weight:700;user-select:none;-webkit-user-select:none;touch-action:none}@media(max-width:820px),(pointer:coarse){.mctrls{display:flex}}@media(orientation:landscape) and (max-height:500px){body{justify-content:flex-start!important;padding-top:46px!important;overflow-y:auto!important}.bar{padding:6px 16px!important}canvas{margin-top:4px!important;max-height:66vh!important;width:auto!important}.mctrls{margin-top:6px!important}.mbtn{padding:8px 0!important;font-size:1rem!important}}</style></head><body>
<div class="bar"><a href="/" class="brand">Tesca Space</a><div class="hud"><span>Score: <strong id="sc">0</strong></span><span>Best: <strong id="hi">0</strong></span><span>Lives: <strong id="lv">3</strong></span><span id="bdg" style="color:#38bdf8"></span></div>
<div class="btns"><button type="button" class="hbtn" onclick="showHelp()">How to Play</button><a href="/" class="bbtn">Back to Wiki</a></div></div>
<canvas id="cv" width="760" height="500" tabindex="0"></canvas><div class="mctrls"><button type="button" class="mbtn" id="mLeft">&#9664; Left</button><button type="button" class="mbtn" id="mFire" style="background:linear-gradient(135deg,#0044cc,#00b4ff);color:#fff">FIRE</button><button type="button" class="mbtn" id="mRight">Right &#9654;</button></div>
<div id="ov"><h1 id="ot">Tesca Space</h1><p id="sub">How to Play</p>
<div class="box"><h3>Controls</h3><ul><li><strong>Move Left:</strong> Left Arrow or <strong>A</strong></li><li><strong>Move Right:</strong> Right Arrow or <strong>D</strong></li><li><strong>Fire Lasers:</strong> <strong>Spacebar</strong></li></ul></div>
<div class="box"><h3>Rules and Scoring</h3><ul><li><strong>Objective:</strong> Blast incoming meteors before they hit your ship or reach the bottom.</li><li><strong>Scoring:</strong> +10 points per meteor. Speed increases as your score climbs.</li><li><strong>Lives:</strong> Start with 3 lives. Lose 1 if hit or a meteor slips past.</li></ul></div>
<p class="tip">Tip: Click inside the dark game window if keys do not respond right away.</p>
<button class="go" onclick="start()">Launch Ship</button></div>
<script>
const cv=document.getElementById("cv"),ctx=cv.getContext("2d"),scE=document.getElementById("sc"),hiE=document.getElementById("hi"),lvE=document.getElementById("lv"),bdg=document.getElementById("bdg"),ov=document.getElementById("ov"),ot=document.getElementById("ot"),sub=document.getElementById("sub");
const actx=new (window.AudioContext||window.webkitAudioContext)();
function sfx(f,t,d,v){try{if(actx.state==="suspended")actx.resume();const o=actx.createOscillator(),g=actx.createGain();o.type=t;o.frequency.setValueAtTime(f,actx.currentTime);o.frequency.exponentialRampToValueAtTime(f*0.35,actx.currentTime+d);g.gain.setValueAtTime(v,actx.currentTime);g.gain.exponentialRampToValueAtTime(0.001,actx.currentTime+d);o.connect(g);g.connect(actx.destination);o.start();o.stop(actx.currentTime+d);}catch(e){}}
let powers=[],triple=0,shield=false,boss=null,bossShots=[],nextBoss=500,pops=[];
window.addEventListener("keydown",e=>{if(typeof run!=="undefined"&&run){if(e.key.toLowerCase()==="h"){shield=!shield;sfx(600,"sine",0.12,0.08);}if(e.key.toLowerCase()==="b"&&!boss){vaporizeRocks();boss={x:380,y:82,r:54,vx:2.4,hp:24,maxHp:24,cd:45};pops.push({x:380,y:120,t:"BOSS INCOMING!",life:50,c:"#f43f5e"});}}});
let ship,lasers,rocks,sparks,stars,score,best=+(localStorage.getItem("tesca-hi")||0),lives,run=false,keys={},sec="",slow=false,shake=0;
hiE.textContent=best;
function initStars(){stars=Array.from({length:80},()=>({x:Math.random()*cv.width,y:Math.random()*cv.height,r:Math.random()*1.8+.4,s:Math.random()*1.8+.4,a:Math.random()}));}
function showHelp(){run=false;ot.textContent="Tesca Space";sub.textContent="How to Play";ov.style.display="block";}
function start(){ship={x:358,y:440,w:44,h:40,spd:6.5,cd:0};lasers=[];rocks=[];sparks=[];powers=[];triple=0;shield=false;boss=null;bossShots=[];nextBoss=500;pops=[];score=0;lives=3;run=true;slow=false;shake=0;bdg.textContent="";scE.textContent=0;lvE.textContent=3;ov.style.display="none";cv.focus();initStars();requestAnimationFrame(loop);}
document.addEventListener("keydown",e=>{keys[e.code]=true;if(e.code==="Space"&&run)e.preventDefault();if(e.key.length===1&&run){sec=(sec+e.key.toLowerCase()).slice(-4);if(sec==="slow"){slow=!slow;bdg.textContent=slow?"[SLOW-MO]":"";}}});
document.addEventListener("keyup",e=>{keys[e.code]=false;});
function boom(x,y,col){for(let i=0;i<14;i++){const a=Math.random()*Math.PI*2,v=Math.random()*4+1;sparks.push({x,y,vx:Math.cos(a)*v,vy:Math.sin(a)*v,life:24,col});}}
function vaporizeRocks(){rocks.forEach(rk=>boom(rk.x,rk.y,"#fb923c"));rocks=[];}
function hurt(direct=false){if(direct&&shield){shield=false;boom(ship.x+22,ship.y+20,"#2dd4bf");pops.push({x:ship.x+22,y:ship.y,t:"BLOCKED!",life:32,c:"#2dd4bf"});sfx(300,"sawtooth",0.2,0.1);return;}lives--;lvE.textContent=lives;shake=10;if(lives<=0){run=false;if(score>best){best=score;localStorage.setItem("tesca-hi",best);hiE.textContent=best;}ot.textContent="Game Over!";sub.textContent="Final Score: "+score+" | Best: "+best;ov.style.display="block";}}
function loop(){if(!run)return;ctx.save();if(shake>0){ctx.translate((Math.random()-.5)*shake,(Math.random()-.5)*shake);shake--;}
ctx.clearRect(0,0,cv.width,cv.height);const f=slow?0.3:1;
stars.forEach(st=>{st.y+=st.s*f;if(st.y>cv.height){st.y=0;st.x=Math.random()*cv.width;}ctx.fillStyle=`rgba(186,230,253,${0.4+st.a*0.6})`;ctx.beginPath();ctx.arc(st.x,st.y,st.r,0,Math.PI*2);ctx.fill();});
if((keys["ArrowLeft"]||keys["KeyA"])&&ship.x>12)ship.x-=ship.spd;
if((keys["ArrowRight"]||keys["KeyD"])&&ship.x<cv.width-ship.w-12)ship.x+=ship.spd;
if(ship.cd>0)ship.cd--;
if(keys["Space"]&&ship.cd===0){sfx(680,"square",0.09,0.06);if(triple>0){lasers.push({x:ship.x+4,y:ship.y,w:4,h:18,spd:10},{x:ship.x+ship.w/2-2,y:ship.y-6,w:4,h:18,spd:10},{x:ship.x+ship.w-8,y:ship.y,w:4,h:18,spd:10});triple--;}else{lasers.push({x:ship.x+ship.w/2-2,y:ship.y-6,w:4,h:18,spd:10});}ship.cd=12;}
ctx.fillStyle="#38bdf8";ctx.beginPath();ctx.moveTo(ship.x+16,ship.y+34);ctx.lineTo(ship.x+22,ship.y+44+Math.random()*8);ctx.lineTo(ship.x+28,ship.y+34);ctx.fill();
const g=ctx.createLinearGradient(ship.x,ship.y,ship.x,ship.y+ship.h);g.addColorStop(0,"#38bdf8");g.addColorStop(1,"#0044cc");
if(shield){ctx.save();ctx.strokeStyle="#2dd4bf";ctx.lineWidth=3;ctx.shadowColor="#2dd4bf";ctx.shadowBlur=14;ctx.beginPath();ctx.arc(ship.x+22,ship.y+20,28,0,Math.PI*2);ctx.stroke();ctx.restore();}ctx.fillStyle=g;ctx.beginPath();ctx.moveTo(ship.x+22,ship.y);ctx.lineTo(ship.x+44,ship.y+36);ctx.lineTo(ship.x+28,ship.y+30);ctx.lineTo(ship.x+22,ship.y+36);ctx.lineTo(ship.x+16,ship.y+30);ctx.lineTo(ship.x,ship.y+36);ctx.closePath();ctx.fill();
ctx.fillStyle="#e0f2fe";ctx.beginPath();ctx.ellipse(ship.x+22,ship.y+18,4,8,0,0,Math.PI*2);ctx.fill();
ctx.shadowBlur=10;ctx.shadowColor="#00b4ff";ctx.fillStyle="#7dd3fc";
for(let i=lasers.length-1;i>=0;i--){const b=lasers[i];b.y-=b.spd;ctx.fillRect(b.x,b.y,b.w,b.h);if(b.y<-20)lasers.splice(i,1);}
ctx.shadowBlur=0;
if(!boss&&Math.random()<(0.028+score*0.00018)*f){const r=15+Math.random()*12;rocks.push({x:r+Math.random()*(cv.width-r*2),y:-r,r,spd:2.1+Math.random()*2+score*0.008,rot:0,vr:(Math.random()-.5)*.06});}
for(let i=rocks.length-1;i>=0;i--){const rk=rocks[i];rk.y+=rk.spd*f;rk.rot+=rk.vr*f;
ctx.save();ctx.translate(rk.x,rk.y);ctx.rotate(rk.rot);
const rg=ctx.createRadialGradient(-rk.r*.3,-rk.r*.3,2,0,0,rk.r);
if(slow){rg.addColorStop(0,"#bae6fd");rg.addColorStop(1,"#0284c7");}else{rg.addColorStop(0,"#fdba74");rg.addColorStop(1,"#c2410c");}
ctx.fillStyle=rg;ctx.beginPath();ctx.arc(0,0,rk.r,0,Math.PI*2);ctx.fill();
ctx.fillStyle="rgba(0,0,0,.22)";ctx.beginPath();ctx.arc(-rk.r*.3,-rk.r*.2,rk.r*.25,0,Math.PI*2);ctx.arc(rk.r*.25,rk.r*.2,rk.r*.18,0,Math.PI*2);ctx.fill();
ctx.restore();
let hit=false;
for(let j=lasers.length-1;j>=0;j--){const b=lasers[j];if(Math.hypot(b.x+2-rk.x,b.y-rk.y)<rk.r+6){lasers.splice(j,1);rocks.splice(i,1);boom(rk.x,rk.y,slow?"#38bdf8":"#fb923c");sfx(160,"sawtooth",0.15,0.09);score+=10;scE.textContent=score;pops.push({x:rk.x,y:rk.y,t:"+10",life:26,c:"#38bdf8"});if(Math.random()<0.22){const ts=["triple","triple","shield","shield","life"];powers.push({x:rk.x,y:rk.y,t:ts[Math.floor(Math.random()*ts.length)]});}hit=true;break;}}
if(hit)continue;
if(Math.hypot(ship.x+22-rk.x,ship.y+20-rk.y)<rk.r+16){rocks.splice(i,1);boom(rk.x,rk.y,"#ef4444");hurt();}
else if(rk.y-rk.r>cv.height){rocks.splice(i,1);hurt(true);}
}
if(!boss&&score>=nextBoss){const hp=24+Math.floor(score/500)*8;vaporizeRocks();boss={x:380,y:82,r:54,vx:2.4,hp:hp,maxHp:hp,cd:45};nextBoss+=500;pops.push({x:380,y:120,t:"BOSS INCOMING!",life:50,c:"#f43f5e"});sfx(220,"sawtooth",0.3,0.1);}
if(boss){
  boss.x+=boss.vx*(slow?0.5:1);if(boss.x<65||boss.x>cv.width-65)boss.vx*=-1;
  boss.cd--;if(boss.cd<=0){bossShots.push({x:boss.x-18,y:boss.y+24},{x:boss.x+18,y:boss.y+24});boss.cd=slow?75:45;}
        ctx.save();ctx.translate(boss.x,boss.y);
  // Twin rear blue thruster flames behind the upper horns
  const fl=10+Math.random()*8;
  ctx.fillStyle="#38bdf8";
  ctx.beginPath();ctx.moveTo(-12,-34);ctx.lineTo(-6,-34);ctx.lineTo(-9,-34-fl);ctx.fill();
  ctx.beginPath();ctx.moveTo(6,-34);ctx.lineTo(12,-34);ctx.lineTo(9,-34-fl);ctx.fill();

  // 1. Upper twin red crescent horns & central engine block
  ctx.fillStyle="#27272a";ctx.fillRect(-7,-42,14,16);
  const hornG=ctx.createLinearGradient(0,-54,0,-20);hornG.addColorStop(0,"#dc2626");hornG.addColorStop(1,"#7f1d1d");
  ctx.fillStyle=hornG;ctx.strokeStyle="#18181b";ctx.lineWidth=1.2;
  // Left upper horn
  ctx.beginPath();ctx.moveTo(-7,-32);ctx.quadraticCurveTo(-20,-34,-21,-54);ctx.quadraticCurveTo(-27,-34,-21,-18);ctx.lineTo(-7,-20);ctx.closePath();ctx.fill();ctx.stroke();
  // Right upper horn
  ctx.beginPath();ctx.moveTo(7,-32);ctx.quadraticCurveTo(20,-34,21,-54);ctx.quadraticCurveTo(27,-34,21,-18);ctx.lineTo(7,-20);ctx.closePath();ctx.fill();ctx.stroke();

  // 2. Large swept outer sickle wings (gunmetal bridges + crimson crescent blades)
  // Gunmetal wing arms
  ctx.fillStyle="#292524";ctx.strokeStyle="#09090b";
  ctx.beginPath();ctx.moveTo(-22,-6);ctx.quadraticCurveTo(-38,-2,-46,-16);ctx.lineTo(-46,4);ctx.quadraticCurveTo(-36,8,-22,12);ctx.closePath();ctx.fill();ctx.stroke();
  ctx.beginPath();ctx.moveTo(22,-6);ctx.quadraticCurveTo(38,-2,46,-16);ctx.lineTo(46,4);ctx.quadraticCurveTo(36,8,22,12);ctx.closePath();ctx.fill();ctx.stroke();
  // Under-wing twin gun barrels
  ctx.fillStyle="#52525b";ctx.fillRect(-36,6,4,10);ctx.fillRect(32,6,4,10);
  // Outer crimson crescent blades (top & bottom tips)
  const bladeG=ctx.createLinearGradient(0,-34,0,38);bladeG.addColorStop(0,"#ef4444");bladeG.addColorStop(0.5,"#991b1b");bladeG.addColorStop(1,"#dc2626");
  ctx.fillStyle=bladeG;
  // Left crescent blade
  ctx.beginPath();ctx.moveTo(-45,-34);ctx.quadraticCurveTo(-58,-4,-41,38);ctx.quadraticCurveTo(-48,6,-44,-14);ctx.closePath();ctx.fill();ctx.stroke();
  // Right crescent blade
  ctx.beginPath();ctx.moveTo(45,-34);ctx.quadraticCurveTo(58,-4,41,38);ctx.quadraticCurveTo(48,6,44,-14);ctx.closePath();ctx.fill();ctx.stroke();

  // 3. Inner dark-olive/gunmetal wing pods flanking the hull
  ctx.fillStyle="#292524";
  ctx.beginPath();ctx.moveTo(-18,-18);ctx.lineTo(-28,-14);ctx.lineTo(-28,22);ctx.lineTo(-18,34);ctx.closePath();ctx.fill();ctx.stroke();
  ctx.beginPath();ctx.moveTo(18,-18);ctx.lineTo(28,-14);ctx.lineTo(28,22);ctx.lineTo(18,34);ctx.closePath();ctx.fill();ctx.stroke();

  // 4. Main crimson oval-tapered central fuselage
  const bodyG=ctx.createLinearGradient(-18,0,18,0);bodyG.addColorStop(0,"#7f1d1d");bodyG.addColorStop(0.5,"#dc2626");bodyG.addColorStop(1,"#7f1d1d");
  ctx.fillStyle=bodyG;
  ctx.beginPath();ctx.moveTo(0,-28);ctx.quadraticCurveTo(22,-10,16,32);ctx.lineTo(0,56);ctx.lineTo(-16,32);ctx.quadraticCurveTo(-22,-10,0,-28);ctx.closePath();ctx.fill();ctx.stroke();

  // 5. Central gunmetal armored cockpit deck & glowing crimson core
  ctx.fillStyle="#3f3f46";ctx.fillRect(-9,-4,18,22);
  ctx.fillStyle="#18181b";ctx.fillRect(-5,-18,10,14);
  ctx.fillStyle="#ef4444";ctx.shadowColor="#ef4444";ctx.shadowBlur=8;
  ctx.beginPath();ctx.moveTo(-6,22);ctx.lineTo(6,22);ctx.lineTo(0,32);ctx.closePath();ctx.fill();ctx.shadowBlur=0;
  // Twin nose laser tips
  ctx.fillStyle="#b91c1c";ctx.fillRect(-10,42,3,10);ctx.fillRect(7,42,3,10);

  // 6. Boss HP Bar above the upper horns
  ctx.fillStyle="rgba(2,6,23,.9)";ctx.fillRect(-54,-66,108,8);
  ctx.strokeStyle="#64748b";ctx.lineWidth=1;ctx.strokeRect(-54,-66,108,8);
  ctx.fillStyle="#ef4444";ctx.fillRect(-52,-64,104*(boss.hp/boss.maxHp),4);
  ctx.restore();
  for(let j=lasers.length-1;j>=0;j--){const b=lasers[j];if(Math.hypot(b.x+2-boss.x,b.y-boss.y)<boss.r){lasers.splice(j,1);boss.hp--;sfx(400,"square",0.05,0.05);if(boss.hp<=0){boom(boss.x,boss.y,"#a855f7");pops.push({x:boss.x,y:boss.y,t:"+150 BOSS!",life:45,c:"#a855f7"});sfx(150,"sawtooth",0.4,0.14);score+=150;scE.textContent=score;boss=null;break;}}}
}
for(let i=bossShots.length-1;i>=0;i--){const s=bossShots[i];s.y+=4.8*(slow?0.5:1);ctx.fillStyle="#f43f5e";ctx.beginPath();ctx.arc(s.x,s.y,5,0,Math.PI*2);ctx.fill();if(Math.hypot(s.x-(ship.x+22),s.y-(ship.y+20))<22){bossShots.splice(i,1);hurt(true);}else if(s.y>cv.height+15)bossShots.splice(i,1);}
for(let i=pops.length-1;i>=0;i--){const p=pops[i];p.y-=0.9;p.life--;ctx.save();ctx.globalAlpha=Math.max(0,p.life/30);ctx.fillStyle=p.c;ctx.font="bold 13px Arial";ctx.textAlign="center";ctx.fillText(p.t,p.x,p.y);ctx.restore();if(p.life<=0)pops.splice(i,1);}for(let i=powers.length-1;i>=0;i--){const w=powers[i];w.y+=2.2;ctx.fillStyle=w.t==="triple"?"#38bdf8":(w.t==="shield"?"#2dd4bf":"#f43f5e");ctx.beginPath();ctx.arc(w.x,w.y,11,0,Math.PI*2);ctx.fill();ctx.fillStyle="#fff";ctx.font="bold 11px Arial";ctx.textAlign="center";ctx.fillText(w.t==="triple"?"3X":(w.t==="shield"?"S":"+1"),w.x,w.y+4);if(Math.hypot(ship.x+22-w.x,ship.y+20-w.y)<28){sfx(880,"sine",0.18,0.1);if(w.t==="triple")triple=35;else if(w.t==="shield")shield=true;else{lives++;lvE.textContent=lives;}powers.splice(i,1);}else if(w.y>cv.height+20)powers.splice(i,1);}for(let i=sparks.length-1;i>=0;i--){const p=sparks[i];p.x+=p.vx;p.y+=p.vy;p.life--;ctx.globalAlpha=p.life/24;ctx.fillStyle=p.col;ctx.fillRect(p.x,p.y,3,3);if(p.life<=0)sparks.splice(i,1);}
ctx.globalAlpha=1;ctx.restore();requestAnimationFrame(loop);}
function bindTouchBtn(id, code) {
    const el = document.getElementById(id);
    if (!el) return;
    el.addEventListener("touchstart", e => { e.preventDefault(); keys[code] = true; }, { passive: false });
    el.addEventListener("touchend", e => { e.preventDefault(); keys[code] = false; }, { passive: false });
    el.addEventListener("touchcancel", () => { keys[code] = false; });
}
bindTouchBtn("mLeft", "ArrowLeft");
bindTouchBtn("mRight", "ArrowRight");
bindTouchBtn("mFire", "Space");

function moveShipToTouch(e) {
    if (!run || !ship) return;
    e.preventDefault();
    const rect = cv.getBoundingClientRect();
    const touch = e.touches;
    const scaleX = cv.width / rect.width;
    const targetX = (touch.clientX - rect.left) * scaleX - ship.w / 2;
    ship.x = Math.max(12, Math.min(cv.width - ship.w - 12, targetX));
    keys["Space"] = true;
}
cv.addEventListener("touchstart", moveShipToTouch, { passive: false });
cv.addEventListener("touchmove", moveShipToTouch, { passive: false });
cv.addEventListener("touchend", () => { keys["Space"] = false; });
</script></body></html>"""












