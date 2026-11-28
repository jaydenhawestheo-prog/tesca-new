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
<button class="go" onclick="start()">Launch Ship</button></div><style>
@keyframes bwPop{0%{opacity:0;transform:scale(0.82) translateY(14px)}100%{opacity:1;transform:scale(1) translateY(0)}}
.bw-card{background:#ffffff;color:#000000;border:4px solid #000000;outline:3px solid #ffffff;border-radius:20px;padding:34px 28px;max-width:440px;width:100%;text-align:center;box-shadow:0 20px 60px rgba(0,0,0,0.9),0 0 0 8px #000000;animation:bwPop 0.32s cubic-bezier(0.16,1,0.3,1)}
.bw-badge{display:inline-block;background:#000000;color:#ffffff;font-size:0.75rem;font-weight:800;letter-spacing:2px;padding:5px 14px;border-radius:999px;text-transform:uppercase;margin-bottom:14px}
.bw-btn{background:#000000;color:#ffffff;border:2px solid #000000;padding:14px 32px;border-radius:999px;font-size:1.05rem;font-weight:800;cursor:pointer;width:100%;transition:all 0.18s ease;letter-spacing:0.5px}
.bw-btn:hover{background:#ffffff;color:#000000;transform:translateY(-2px);box-shadow:0 6px 0 #000000}
</style>
<div id="bwWin" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,0.88);backdrop-filter:blur(6px);z-index:50;align-items:center;justify-content:center;padding:20px">
  <div class="bw-card">
    <div class="bw-badge">&#9733; Sector Cleared &#9733;</div>
    <div style="font-size:3rem;line-height:1;margin-bottom:10px;filter:grayscale(100%)">&#127942;</div>
    <h2 style="font-size:1.85rem;font-weight:900;line-height:1.2;margin-bottom:10px;letter-spacing:-0.5px">Congrads You Beat the Boss !!</h2>
    <p style="font-size:0.95rem;font-weight:600;color:#333333;margin-bottom:22px;padding:8px 12px;background:#f2f2f2;border:1.5px dashed #000000;border-radius:10px">Boss Bonus: <strong>+150 PTS</strong> &bull; Total Score: <strong id="bwScore">0</strong></p>
    <button type="button" class="bw-btn" onclick="resumeGame()">Continue Playing &#9654;</button>
    <div style="font-size:0.76rem;color:#555555;margin-top:10px;font-weight:600">Press ENTER to continue</div>
  </div>
</div>
<script>
const cv=document.getElementById("cv"),ctx=cv.getContext("2d"),scE=document.getElementById("sc"),hiE=document.getElementById("hi"),lvE=document.getElementById("lv"),bdg=document.getElementById("bdg"),ov=document.getElementById("ov"),ot=document.getElementById("ot"),sub=document.getElementById("sub");
const actx=new (window.AudioContext||window.webkitAudioContext)();
function sfx(f,t,d,v){try{if(actx.state==="suspended")actx.resume();const o=actx.createOscillator(),g=actx.createGain();o.type=t;o.frequency.setValueAtTime(f,actx.currentTime);o.frequency.exponentialRampToValueAtTime(f*0.35,actx.currentTime+d);g.gain.setValueAtTime(v,actx.currentTime);g.gain.exponentialRampToValueAtTime(0.001,actx.currentTime+d);o.connect(g);g.connect(actx.destination);o.start();o.stop(actx.currentTime+d);}catch(e){}}
let powers=[],triple=0,shield=false,boss=null,bossShots=[],nextBoss=500,pops=[];
window.addEventListener("keydown",e=>{if(e.key==="Enter"&&document.getElementById("bwWin").style.display==="flex"){e.preventDefault();resumeGame();return;}if(typeof run!=="undefined"&&run){if(e.key.toLowerCase()==="h"){shield=!shield;sfx(600,"sine",0.12,0.08);}if(e.key.toLowerCase()==="b"&&!boss){vaporizeRocks();boss={x:380,y:82,r:54,vx:2.4,hp:24,maxHp:24,cd:45};pops.push({x:380,y:120,t:"BOSS INCOMING!",life:50,c:"#f43f5e"});}}});
let ship,lasers,rocks,sparks,stars,score,best=+(localStorage.getItem("tesca-hi")||0),lives,run=false,keys={},sec="",slow=false,shake=0;
hiE.textContent=best;
function initStars(){stars=Array.from({length:80},()=>({x:Math.random()*cv.width,y:Math.random()*cv.height,r:Math.random()*1.8+.4,s:Math.random()*1.8+.4,a:Math.random()}));}
function showHelp(){run=false;ot.textContent="Tesca Space";sub.textContent="How to Play";ov.style.display="block";}
function resumeGame(){document.getElementById("bwWin").style.display="none";run=true;cv.focus();requestAnimationFrame(loop);}function start(){document.getElementById("bwWin").style.display="none";ship={x:358,y:440,w:44,h:40,spd:6.5,cd:0};lasers=[];rocks=[];sparks=[];powers=[];triple=0;shield=false;boss=null;bossShots=[];nextBoss=500;pops=[];score=0;lives=3;run=true;slow=false;shake=0;bdg.textContent="";scE.textContent=0;lvE.textContent=3;ov.style.display="none";cv.focus();initStars();requestAnimationFrame(loop);}
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
if(Math.hypot(ship.x+22-rk.x,ship.y+20-rk.y)<rk.r+16){rocks.splice(i,1);boom(rk.x,rk.y,"#ef4444");hurt(true);}
else if(rk.y-rk.r>cv.height){rocks.splice(i,1);hurt();}
}
if(!boss&&score>=nextBoss){const hp=24+Math.floor(score/500)*8;vaporizeRocks();boss={x:380,y:82,r:54,vx:2.4,hp:hp,maxHp:hp,cd:45};nextBoss+=500;pops.push({x:380,y:120,t:"BOSS INCOMING!",life:50,c:"#f43f5e"});sfx(220,"sawtooth",0.3,0.1);}
if(boss){
  boss.x+=boss.vx*(slow?0.5:1);if(boss.x<65||boss.x>cv.width-65)boss.vx*=-1;
  boss.cd--;if(boss.cd<=0){bossShots.push({x:boss.x-18,y:boss.y+24},{x:boss.x+18,y:boss.y+24});boss.cd=slow?75:45;}
          ctx.save();ctx.translate(boss.x,boss.y);
  if(boss.flash>0){boss.flash--;ctx.filter="brightness(2.2)";}

  // Ambient red battle aura & 3D drop shadow
  ctx.shadowColor="rgba(220,38,38,0.5)";ctx.shadowBlur=22;ctx.shadowOffsetY=12;

  // Twin rear blue-white ion thruster plumes
  const fl=14+Math.random()*12;
  const eg=ctx.createLinearGradient(0,-34,0,-34-fl);
  eg.addColorStop(0,"#ffffff");eg.addColorStop(0.3,"#38bdf8");eg.addColorStop(0.75,"#0284c7");eg.addColorStop(1,"transparent");
  ctx.fillStyle=eg;
  ctx.beginPath();ctx.moveTo(-13,-34);ctx.lineTo(-6,-34);ctx.lineTo(-9.5,-34-fl);ctx.fill();
  ctx.beginPath();ctx.moveTo(6,-34);ctx.lineTo(13,-34);ctx.lineTo(9.5,-34-fl);ctx.fill();
  ctx.shadowOffsetY=0;ctx.shadowBlur=0;

  // 1. Rear engine manifold & twin 3D beveled crimson horns
  const engG=ctx.createLinearGradient(-9,0,9,0);engG.addColorStop(0,"#0f172a");engG.addColorStop(0.5,"#475569");engG.addColorStop(1,"#0f172a");
  ctx.fillStyle=engG;ctx.fillRect(-8,-44,16,18);
  const hornG=ctx.createLinearGradient(0,-58,0,-18);hornG.addColorStop(0,"#fca5a5");hornG.addColorStop(0.25,"#dc2626");hornG.addColorStop(0.75,"#7f1d1d");hornG.addColorStop(1,"#18181b");
  ctx.fillStyle=hornG;ctx.strokeStyle="#090d16";ctx.lineWidth=1.4;
  ctx.beginPath();ctx.moveTo(-7,-32);ctx.quadraticCurveTo(-21,-34,-22,-58);ctx.quadraticCurveTo(-29,-35,-22,-18);ctx.lineTo(-7,-20);ctx.closePath();ctx.fill();ctx.stroke();
  ctx.beginPath();ctx.moveTo(7,-32);ctx.quadraticCurveTo(21,-34,22,-58);ctx.quadraticCurveTo(29,-35,22,-18);ctx.lineTo(7,-20);ctx.closePath();ctx.fill();ctx.stroke();

  // 2. Heavy gunmetal wing bridges & dual rotary plasma cannons
  const armG=ctx.createLinearGradient(0,-14,0,14);armG.addColorStop(0,"#475569");armG.addColorStop(0.5,"#1e293b");armG.addColorStop(1,"#090d16");
  ctx.fillStyle=armG;
  ctx.beginPath();ctx.moveTo(-20,-8);ctx.quadraticCurveTo(-38,-3,-48,-18);ctx.lineTo(-48,6);ctx.quadraticCurveTo(-36,10,-20,14);ctx.closePath();ctx.fill();ctx.stroke();
  ctx.beginPath();ctx.moveTo(20,-8);ctx.quadraticCurveTo(38,-3,48,-18);ctx.lineTo(48,6);ctx.quadraticCurveTo(36,10,20,14);ctx.closePath();ctx.fill();ctx.stroke();
  // Twin under-wing gun pods with glowing muzzles
  ctx.fillStyle="#334155";ctx.fillRect(-39,6,6,13);ctx.fillRect(33,6,6,13);
  ctx.fillStyle="#f43f5e";ctx.shadowColor="#f43f5e";ctx.shadowBlur=8;
  ctx.beginPath();ctx.arc(-36,20,2.5,0,Math.PI*2);ctx.arc(36,20,2.5,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;

  // 3. Outer 3D swept crimson sickle blades with specular edge highlights
  const bladeL=ctx.createLinearGradient(-62,0,-40,0);bladeL.addColorStop(0,"#450a0a");bladeL.addColorStop(0.35,"#ef4444");bladeL.addColorStop(0.75,"#991b1b");bladeL.addColorStop(1,"#090d16");
  const bladeR=ctx.createLinearGradient(62,0,40,0);bladeR.addColorStop(0,"#450a0a");bladeR.addColorStop(0.35,"#ef4444");bladeR.addColorStop(0.75,"#991b1b");bladeR.addColorStop(1,"#090d16");
  ctx.fillStyle=bladeL;ctx.beginPath();ctx.moveTo(-46,-38);ctx.quadraticCurveTo(-64,-4,-42,42);ctx.quadraticCurveTo(-50,8,-45,-14);ctx.closePath();ctx.fill();ctx.stroke();
  ctx.fillStyle=bladeR;ctx.beginPath();ctx.moveTo(46,-38);ctx.quadraticCurveTo(64,-4,42,42);ctx.quadraticCurveTo(50,8,45,-14);ctx.closePath();ctx.fill();ctx.stroke();
  // Specular metallic blade edge glint
  ctx.strokeStyle="#fecaca";ctx.lineWidth=1.1;
  ctx.beginPath();ctx.moveTo(-46,-36);ctx.quadraticCurveTo(-61,-4,-43,39);ctx.stroke();
  ctx.beginPath();ctx.moveTo(46,-36);ctx.quadraticCurveTo(61,-4,43,39);ctx.stroke();

  // 4. Flanking armored thruster sponsons
  const podG=ctx.createLinearGradient(-30,0,30,0);podG.addColorStop(0,"#0f172a");podG.addColorStop(0.5,"#334155");podG.addColorStop(1,"#0f172a");
  ctx.fillStyle=podG;
  ctx.beginPath();ctx.moveTo(-18,-20);ctx.lineTo(-30,-14);ctx.lineTo(-30,24);ctx.lineTo(-18,36);ctx.closePath();ctx.fill();ctx.stroke();
  ctx.beginPath();ctx.moveTo(18,-20);ctx.lineTo(30,-14);ctx.lineTo(30,24);ctx.lineTo(18,36);ctx.closePath();ctx.fill();ctx.stroke();

  // 5. Main 3D cylindrical-shaded crimson fuselage
  const hullG=ctx.createLinearGradient(-22,0,22,0);
  hullG.addColorStop(0,"#18181b");hullG.addColorStop(0.22,"#991b1b");hullG.addColorStop(0.5,"#f87171");hullG.addColorStop(0.78,"#991b1b");hullG.addColorStop(1,"#18181b");
  ctx.fillStyle=hullG;
  ctx.beginPath();ctx.moveTo(0,-30);ctx.quadraticCurveTo(24,-10,17,34);ctx.lineTo(0,60);ctx.lineTo(-17,34);ctx.quadraticCurveTo(-24,-10,0,-30);ctx.closePath();ctx.fill();ctx.stroke();

  // 6. Layered gunmetal spine, radiator slats & 3D glowing crimson reactor core
  const spineG=ctx.createLinearGradient(-11,0,11,0);spineG.addColorStop(0,"#090d16");spineG.addColorStop(0.5,"#64748b");spineG.addColorStop(1,"#090d16");
  ctx.fillStyle=spineG;ctx.fillRect(-10,-6,20,24);ctx.strokeRect(-10,-6,20,24);
  ctx.fillStyle="#090d16";
  for(let y=-2;y<=12;y+=4){ctx.fillRect(-7,y,14,1.8);}
  // Glowing 3D command visor & forward twin needle cannons
  ctx.fillStyle="#ef4444";ctx.shadowColor="#ef4444";ctx.shadowBlur=12;
  ctx.beginPath();ctx.moveTo(-7,22);ctx.lineTo(7,22);ctx.lineTo(0,35);ctx.closePath();ctx.fill();
  ctx.fillStyle="#fee2e2";ctx.beginPath();ctx.arc(0,26,2.2,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;
  ctx.fillStyle="#475569";ctx.fillRect(-10,42,3,13);ctx.fillRect(7,42,3,13);

  ctx.filter="none";
  // Armored Boss HP Bar
  ctx.fillStyle="rgba(2,6,23,.92)";ctx.fillRect(-56,-70,112,9);
  ctx.strokeStyle="#64748b";ctx.lineWidth=1;ctx.strokeRect(-56,-70,112,9);
  const hpG=ctx.createLinearGradient(-54,0,54,0);hpG.addColorStop(0,"#dc2626");hpG.addColorStop(1,"#fca5a5");
  ctx.fillStyle=hpG;ctx.fillRect(-54,-68,108*(boss.hp/boss.maxHp),5);
  ctx.restore();
  for(let j=lasers.length-1;j>=0;j--){const b=lasers[j];if(Math.hypot(b.x+2-boss.x,b.y-boss.y)<boss.r){lasers.splice(j,1);boss.hp--;boss.flash=3;sfx(400,"square",0.05,0.05);if(boss.hp<=0){boom(boss.x,boss.y,"#a855f7");pops.push({x:boss.x,y:boss.y,t:"+150 BOSS!",life:45,c:"#a855f7"});sfx(150,"sawtooth",0.4,0.14);score+=150;scE.textContent=score;boss=null;bossShots=[];run=false;keys={};document.getElementById("bwScore").textContent=score;document.getElementById("bwWin").style.display="flex";sfx(523,"triangle",0.12,0.12);setTimeout(()=>sfx(659,"triangle",0.12,0.12),110);setTimeout(()=>sfx(784,"triangle",0.25,0.14),220);break;}}}
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
















