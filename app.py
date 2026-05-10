"""
CODE - ANIMATION Workstation v3.0
Sliders -> Live Animation + Code Editor -> Custom Animation
Deploy: GitHub -> share.streamlit.io
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CODE - ANIMATION | Workstation",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@700;900&display=swap');
:root {
    --bg:#05070F; --panel:#0A0D1A; --card:#0F1225; --glass:#121830;
    --cyan:#00F5FF; --purple:#9D00FF; --pink:#FF007A; --green:#00FF88;
    --t1:#E8F4FF; --t2:#6A7FA8; --td:#2E3D5C; --border:#1A2A4A;
}
html,body,.stApp{background:var(--bg)!important;color:var(--t1)!important;font-family:'Share Tech Mono',monospace!important;}
#MainMenu,footer,header{visibility:hidden;}
.block-container{padding-top:0.5rem!important;max-width:100%!important;padding-left:1rem!important;padding-right:1rem!important;}
.title-bar{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:8px 20px;display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;}
.logo{font-family:'Orbitron',monospace;font-size:1.2rem;font-weight:900;color:var(--cyan);letter-spacing:3px;}
.pill{padding:3px 10px;border-radius:20px;font-size:0.68rem;font-weight:bold;border:1px solid;display:inline-block;margin-left:6px;}
.pill-cyan{border-color:var(--cyan);color:var(--cyan);background:rgba(0,245,255,0.08);}
.pill-purple{border-color:var(--purple);color:var(--purple);background:rgba(157,0,255,0.08);}
.pill-green{border-color:var(--green);color:var(--green);background:rgba(0,255,136,0.08);}
.panel-title{font-family:'Orbitron',monospace;font-size:0.68rem;color:var(--cyan);letter-spacing:2px;margin-bottom:6px;padding:5px 10px;background:var(--card);border-radius:6px;border:1px solid rgba(0,245,255,0.2);}
.stTextArea textarea{background:#020408!important;color:#E8F4FF!important;font-family:'Share Tech Mono',monospace!important;font-size:0.8rem!important;border:1px solid var(--border)!important;border-radius:8px!important;}
.stTextArea textarea:focus{border-color:var(--cyan)!important;box-shadow:0 0 12px rgba(0,245,255,0.15)!important;}
.stButton>button{background:transparent!important;border:1px solid var(--cyan)!important;color:var(--cyan)!important;font-family:'Share Tech Mono',monospace!important;font-size:0.82rem!important;border-radius:6px!important;letter-spacing:1px;}
.stButton>button:hover{background:rgba(0,245,255,0.1)!important;box-shadow:0 0 14px rgba(0,245,255,0.3)!important;}
.stSelectbox>div>div{background:var(--glass)!important;border:1px solid rgba(0,245,255,0.3)!important;color:var(--cyan)!important;font-family:'Share Tech Mono',monospace!important;}
.stSlider>div>div>div{background:var(--cyan)!important;}
.status-bar{background:var(--panel);border:1px solid var(--border);border-radius:8px;padding:5px 14px;display:flex;align-items:center;justify-content:space-between;margin-top:8px;font-size:0.72rem;}
section[data-testid="stSidebar"]{background:var(--panel)!important;border-right:1px solid var(--border)!important;}
</style>
""", unsafe_allow_html=True)

# ── Title Bar ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="title-bar">
  <div class="logo">⬡ CODE<span> — </span>ANIMATION</div>
  <div>
    <span class="pill pill-cyan">◉ THREE.JS</span>
    <span class="pill pill-purple">◉ WEBGL</span>
    <span class="pill pill-green">◉ LIVE</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Session state ──────────────────────────────────────────────────────────────
if "mode" not in st.session_state:
    st.session_state.mode = "Preset"
if "running" not in st.session_state:
    st.session_state.running = True

# ── Toolbar ────────────────────────────────────────────────────────────────────
t1, t2, t3, t4, t5 = st.columns([2, 2, 1, 1, 1])
with t1:
    mode = st.selectbox("MODE", ["Preset Animations", "Custom Code Editor"],
                        label_visibility="collapsed")
with t2:
    if mode == "Preset Animations":
        preset = st.selectbox("PRESET", ["Cyber Sphere", "Matrix Rain", "Character Rig", "Quantum Grid"],
                              label_visibility="collapsed")
    else:
        preset = "Custom"
        st.markdown('<div style="color:#6A7FA8;font-size:0.8rem;padding:6px 0;">◈ CUSTOM CODE MODE</div>', unsafe_allow_html=True)
with t3:
    run = st.button("▶  RUN", use_container_width=True)
    if run:
        st.session_state.running = True
with t4:
    stop = st.button("◼  STOP", use_container_width=True)
    if stop:
        st.session_state.running = False
with t5:
    reset = st.button("⟳  RESET", use_container_width=True)
    if reset:
        st.session_state.running = True
        st.rerun()

# ── Layout ─────────────────────────────────────────────────────────────────────
left, right = st.columns([4, 6], gap="medium")

# ════════════════════════════════════════════════════════
#  LEFT PANEL — Controls
# ════════════════════════════════════════════════════════
with left:
    if mode == "Preset Animations":
        st.markdown('<div class="panel-title">◈  ANIMATION CONTROLS</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            sphere_color    = st.color_picker("Main Color",    "#00F5FF")
            particle_color  = st.color_picker("Particle Color","#FF007A")
            ring_color      = st.color_picker("Ring Color",    "#9D00FF")
        with col2:
            bg_color        = st.color_picker("Background",    "#05070F")
            emissive_color  = st.color_picker("Glow Color",    "#003344")

        st.markdown("---")
        speed       = st.slider("⚡ Speed",         0.1, 5.0, 1.0, 0.1)
        particle_ct = st.slider("✦ Particles",       0,   200,  80,   5)
        size        = st.slider("◎ Object Size",    0.5,  5.0,  2.0, 0.1)
        ring_size   = st.slider("○ Ring Size",      1.0,  8.0,  3.5, 0.1)
        spread      = st.slider("⊕ Particle Spread",1.0,  8.0,  4.0, 0.1)
        fog_near    = st.slider("≋ Fog Near",        5,   50,   20,   1)

        wireframe   = st.checkbox("⬡ Wireframe Overlay", value=True)
        rotate_cam  = st.checkbox("↻ Rotate Camera",     value=False)

    else:
        # ── Custom Code Editor ──
        st.markdown('<div class="panel-title">◈  CUSTOM THREE.JS CODE</div>', unsafe_allow_html=True)
        st.markdown('<div style="color:#6A7FA8;font-size:0.72rem;margin-bottom:6px;">Three.js r128 | Variables: scene, camera, renderer, canvas, w, h</div>', unsafe_allow_html=True)

        default_custom = """\
// ── Your Custom Three.js Animation ──
// scene, camera, renderer, canvas, w, h are pre-defined

scene.background = new THREE.Color(0x05070F);
camera.position.set(0, 2, 10);

// Create a glowing torus knot
const geo = new THREE.TorusKnotGeometry(2, 0.5, 128, 32);
const mat = new THREE.MeshPhongMaterial({
    color: 0x00F5FF,
    emissive: 0x002233,
    shininess: 120,
    wireframe: false
});
const knot = new THREE.Mesh(geo, mat);
scene.add(knot);

// Wireframe overlay
const wireMat = new THREE.MeshBasicMaterial({
    color: 0x9D00FF, wireframe: true,
    transparent: true, opacity: 0.2
});
scene.add(new THREE.Mesh(geo, wireMat));

// Lights
scene.add(new THREE.AmbientLight(0x111133, 3));
const pt1 = new THREE.PointLight(0x00F5FF, 4, 20);
pt1.position.set(5, 5, -5);
scene.add(pt1);
const pt2 = new THREE.PointLight(0xFF007A, 3, 15);
pt2.position.set(-5, -3, 3);
scene.add(pt2);

// Animate
let t = 0;
function animate() {
    requestAnimationFrame(animate);
    t += 0.016;
    knot.rotation.x += 0.008;
    knot.rotation.y += 0.012;
    const s = 1 + 0.1 * Math.sin(t * 2);
    knot.scale.set(s, s, s);
    pt1.color.setHSL((t * 0.05) % 1, 1, 0.5);
    renderer.render(scene, camera);
}
animate();
"""
        custom_code = st.text_area(
            "code",
            value=default_custom,
            height=440,
            label_visibility="collapsed",
            key="custom_editor"
        )

        col_a, col_b = st.columns(2)
        with col_a:
            custom_bg = st.color_picker("Background", "#05070F", key="cbg")
        with col_b:
            st.markdown('<div style="color:#6A7FA8;font-size:0.72rem;padding-top:28px;">Press ▶ RUN to apply</div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════
#  RIGHT PANEL — 3D Preview
# ════════════════════════════════════════════════════════
with right:
    st.markdown(f'<div class="panel-title">◈  3D PREVIEW — {"CUSTOM CODE" if mode != "Preset Animations" else preset.upper()}</div>', unsafe_allow_html=True)

    if not st.session_state.running:
        st.markdown("""
        <div style="height:520px;background:#05070F;border:1px solid #1A2A4A;
                    border-radius:10px;display:flex;align-items:center;
                    justify-content:center;flex-direction:column;gap:12px;">
            <div style="font-size:3rem;color:#00F5FF;opacity:0.3;">⬡</div>
            <div style="font-family:'Courier New',monospace;color:#00F5FF;opacity:0.4;
                        font-size:0.8rem;letter-spacing:3px;">PAUSED — PRESS ▶ RUN</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # ── Build Three.js scene based on mode ──────────────────────────────
        if mode == "Preset Animations":

            # Convert hex colors to Three.js hex ints
            def hex_to_int(h):
                return int(h.lstrip("#"), 16)

            sc  = hex_to_int(sphere_color)
            pc  = hex_to_int(particle_color)
            rc  = hex_to_int(ring_color)
            bgc = hex_to_int(bg_color)
            ec  = hex_to_int(emissive_color)
            spd = speed
            pct = int(particle_ct)
            sz  = size
            rs  = ring_size
            sp  = spread
            fn  = fog_near
            wf  = str(wireframe).lower()
            rotcam = str(rotate_cam).lower()

            if preset == "Cyber Sphere":
                scene_js = f"""
scene.background = new THREE.Color({bgc});
scene.fog = new THREE.Fog({bgc}, {fn}, {fn*3});
camera.position.set(0, 2, 10);

const sphereGeo = new THREE.SphereGeometry({sz}, 64, 64);
const sphereMat = new THREE.MeshPhongMaterial({{
    color: {sc}, emissive: {ec}, shininess: 100
}});
const sphere = new THREE.Mesh(sphereGeo, sphereMat);
scene.add(sphere);

if ({wf}) {{
    const wm = new THREE.MeshBasicMaterial({{color:{sc},wireframe:true,transparent:true,opacity:0.15}});
    scene.add(new THREE.Mesh(new THREE.SphereGeometry({sz}*1.005,24,24), wm));
}}

const ringGeo = new THREE.TorusGeometry({rs}, 0.05, 16, 100);
const ringMat = new THREE.MeshBasicMaterial({{color:{rc}}});
const ring = new THREE.Mesh(ringGeo, ringMat);
ring.rotation.x = 1.4;
scene.add(ring);

const ring2Geo = new THREE.TorusGeometry({rs}*0.7, 0.03, 16, 80);
const ring2Mat = new THREE.MeshBasicMaterial({{color:{sc},transparent:true,opacity:0.5}});
const ring2 = new THREE.Mesh(ring2Geo, ring2Mat);
ring2.rotation.x = 0.5; ring2.rotation.z = 0.8;
scene.add(ring2);

const particles = [];
for (let i = 0; i < {pct}; i++) {{
    const g = new THREE.SphereGeometry(Math.random()*0.08+0.04,8,8);
    const m = new THREE.MeshBasicMaterial({{color:{pc}}});
    const p = new THREE.Mesh(g, m);
    const angle = Math.random()*Math.PI*2;
    const r = {sp*0.5} + Math.random()*{sp*0.5};
    p.position.set(Math.cos(angle)*r,(Math.random()-0.5)*{sz*1.5},Math.sin(angle)*r);
    p.userData = {{speed:Math.random()*0.8+0.3, offset:Math.random()*Math.PI*2, r}};
    scene.add(p);
    particles.push(p);
}}

scene.add(new THREE.AmbientLight(0x111133, 2));
const pt = new THREE.PointLight({sc}, 4, 20); pt.position.set(4,6,-4); scene.add(pt);
const pt2 = new THREE.PointLight({rc}, 2, 15); pt2.position.set(-4,-4,4); scene.add(pt2);

let t = 0;
function animate() {{
    requestAnimationFrame(animate);
    t += 0.016 * {spd};
    sphere.rotation.y += 0.008 * {spd};
    const s = {sz}/2 + 0.06*Math.sin(t*2);
    sphere.scale.set(s,s,s);
    ring.rotation.z  += 0.005 * {spd};
    ring2.rotation.y += 0.007 * {spd};
    ringMat.color.setHSL((t*0.04)%1, 1, 0.5);
    pt.color.setHSL((t*0.06)%1, 1, 0.5);
    particles.forEach(p => {{
        const d = p.userData;
        const a = t*d.speed+d.offset;
        const r = d.r + Math.sin(t*d.speed+d.offset)*0.8;
        p.position.x = Math.cos(a)*r;
        p.position.z = Math.sin(a)*r;
        p.position.y = Math.sin(t*d.speed*2+d.offset)*{sz*0.8};
    }});
    if ({rotcam}) {{ camera.position.x = Math.sin(t*0.3)*5; camera.position.z = Math.cos(t*0.3)*10; camera.lookAt(0,0,0); }}
    renderer.render(scene, camera);
}}
animate();
"""

            elif preset == "Matrix Rain":
                scene_js = f"""
scene.background = new THREE.Color(0x000A00);
camera.position.set(0, 0, 18);

const chars = '01アイウエオカキクケコABCDEF@#$%';
const drops = [];
const c2d = document.createElement('canvas');
c2d.width=32; c2d.height=32;
const ctx = c2d.getContext('2d');

function makeT(ch, brightness) {{
    ctx.clearRect(0,0,32,32);
    ctx.fillStyle = `hsl(130,100%,${{brightness}}%)`;
    ctx.font='bold 22px monospace';
    ctx.textAlign='center';
    ctx.fillText(ch,16,24);
    return new THREE.CanvasTexture(c2d);
}}

for (let x=-14; x<=14; x+=1.6) {{
    for (let k=0; k<Math.floor(Math.random()*3)+1; k++) {{
        const geo = new THREE.PlaneGeometry(1, 1);
        const tex = makeT(chars[Math.floor(Math.random()*chars.length)], 60);
        const mat = new THREE.MeshBasicMaterial({{map:tex,transparent:true,opacity:0.9}});
        const mesh = new THREE.Mesh(geo, mat);
        mesh.position.set(x+(Math.random()-0.5)*0.4, Math.random()*20-5, Math.random()*4-6);
        mesh.userData = {{speed:(Math.random()*3+1.5)*{spd}, y:mesh.position.y}};
        scene.add(mesh);
        drops.push(mesh);
    }}
}}
scene.add(new THREE.AmbientLight(0x00FF88, 0.5));

let t=0;
function animate() {{
    requestAnimationFrame(animate);
    t += 0.016;
    drops.forEach(d => {{
        d.userData.y -= d.userData.speed*0.016;
        if (d.userData.y < -14) {{
            d.userData.y = Math.random()*10+10;
            const ch = chars[Math.floor(Math.random()*chars.length)];
            d.material.map = makeT(ch, Math.random()*30+40);
            d.material.map.needsUpdate = true;
        }}
        d.position.y = d.userData.y;
        d.material.opacity = 0.4+0.6*Math.abs(Math.sin(t*3+d.userData.y));
    }});
    renderer.render(scene, camera);
}}
animate();
"""

            elif preset == "Character Rig":
                scene_js = f"""
scene.background = new THREE.Color({bgc});
camera.position.set(0,3,10);
camera.lookAt(0,2,0);

function neonBox(sx,sy,sz,col) {{
    const g = new THREE.BoxGeometry(sx,sy,sz);
    const m = new THREE.MeshPhongMaterial({{color:col,emissive:col,emissiveIntensity:0.3}});
    return new THREE.Mesh(g,m);
}}

const sc = {sz};
const torso = neonBox(sc*0.5,sc*0.7,sc*0.25, {sc}); torso.position.set(0,2.2*sc/2,0);
const head  = new THREE.Mesh(new THREE.SphereGeometry(sc*0.19,32,32),
    new THREE.MeshPhongMaterial({{color:{sc},emissive:{ec},emissiveIntensity:0.4}}));
head.position.set(0,3.35*sc/2,0);
const lArm = neonBox(sc*0.14,sc*0.6,sc*0.14,{rc}); lArm.position.set(-sc*0.45,2.1*sc/2,0);
const rArm = neonBox(sc*0.14,sc*0.6,sc*0.14,{rc}); rArm.position.set( sc*0.45,2.1*sc/2,0);
const lLeg = neonBox(sc*0.16,sc*0.65,sc*0.16,{pc}); lLeg.position.set(-sc*0.175,sc/2,0);
const rLeg = neonBox(sc*0.16,sc*0.65,sc*0.16,{pc}); rLeg.position.set( sc*0.175,sc/2,0);

scene.add(torso,head,lArm,rArm,lLeg,rLeg);
scene.add(new THREE.GridHelper(20,20,0x1A2A4A,0x0F1820));
scene.add(new THREE.AmbientLight(0x111133,3));
const ptL = new THREE.PointLight({sc},4,20); ptL.position.set(3,7,-5); scene.add(ptL);
const ptR = new THREE.PointLight({pc},2,15); ptR.position.set(-3,2,3); scene.add(ptR);

let t=0;
function animate() {{
    requestAnimationFrame(animate);
    t += 0.016 * {spd};
    const swing = Math.sin(t*3)*0.5;
    const bob   = Math.sin(t*6)*0.05;
    lArm.rotation.x =  swing;
    rArm.rotation.x = -swing;
    lLeg.rotation.x = -swing;
    rLeg.rotation.x =  swing;
    torso.position.y = 2.2*sc/2 + bob;
    head.position.y  = 3.35*sc/2 + bob;
    torso.rotation.y += 0.007 * {spd};
    head.rotation.y  += 0.007 * {spd};
    ptL.color.setHSL((t*0.05)%1,1,0.5);
    renderer.render(scene, camera);
}}
animate();
"""

            elif preset == "Quantum Grid":
                scene_js = f"""
scene.background = new THREE.Color({bgc});
scene.fog = new THREE.Fog({bgc}, {fn}, {fn*3});
camera.position.set(0,5,0);
camera.rotation.x = -0.65;

const grid1 = new THREE.GridHelper(60,60,{pc},0x110011);
scene.add(grid1);
const grid2 = new THREE.GridHelper(60,30,{rc},0x110022);
scene.add(grid2);

const rings = [];
for (let i=0; i<6; i++) {{
    const g = new THREE.TorusGeometry(i*{sz*0.8}+1, 0.04, 8, 80);
    const m = new THREE.MeshBasicMaterial({{color:{sc},transparent:true,opacity:0.8}});
    const mesh = new THREE.Mesh(g,m);
    mesh.rotation.x = Math.PI/2;
    mesh.userData = {{phase: i*1.2}};
    scene.add(mesh);
    rings.push(mesh);
}}

for (let i=0; i<{pct//4}; i++) {{
    const g = new THREE.CylinderGeometry(0.03,0.03,Math.random()*4+1,8);
    const cols = [{sc},{rc},{pc}];
    const m = new THREE.MeshBasicMaterial({{color:cols[i%3],transparent:true,opacity:0.6}});
    const mesh = new THREE.Mesh(g,m);
    mesh.position.set((Math.random()-0.5)*40,Math.random()*2,(Math.random()-0.5)*40);
    mesh.userData = {{phase:Math.random()*Math.PI*2}};
    scene.add(mesh);
    rings.push(mesh);
}}

scene.add(new THREE.AmbientLight(0x110022,2));
let t=0;
function animate() {{
    requestAnimationFrame(animate);
    t += 0.016 * {spd};
    grid1.position.z = (t*2)%1;
    rings.forEach((r,i) => {{
        if (r.geometry.type==='TorusGeometry') {{
            const pulse = Math.sin(t*2 - r.userData.phase);
            r.material.opacity = 0.2+0.8*Math.max(0,pulse);
            const s = 1+0.04*Math.sin(t+r.userData.phase);
            r.scale.set(s,s,s);
        }} else {{
            r.material.opacity = 0.2+0.5*Math.abs(Math.sin(t+r.userData.phase));
        }}
    }});
    camera.position.x = Math.sin(t*0.2)*4;
    renderer.render(scene,camera);
}}
animate();
"""

        else:
            # Custom code mode
            scene_js = custom_code
            bg_color = custom_bg

        # ── Render HTML with Three.js ──────────────────────────────────────
        html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
  *{{margin:0;padding:0;box-sizing:border-box;}}
  body{{background:{bg_color if mode=='Preset Animations' else custom_bg};overflow:hidden;}}
  canvas{{display:block;width:100%!important;height:100%!important;}}
  #label{{position:absolute;bottom:10px;left:50%;transform:translateX(-50%);
          font-family:'Courier New',monospace;font-size:11px;
          color:rgba(0,245,255,0.45);letter-spacing:2px;pointer-events:none;}}
  #spd{{position:absolute;top:8px;right:10px;font-family:'Courier New',monospace;
        font-size:10px;color:rgba(0,245,255,0.5);}}
</style></head><body>
<canvas id="c"></canvas>
<div id="label">◈ {preset.upper() if mode=='Preset Animations' else 'CUSTOM'} — LIVE RENDER</div>
<div id="spd">SPD {speed if mode=='Preset Animations' else 1.0:.1f}×</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
(function(){{
  const canvas = document.getElementById('c');
  const w = window.innerWidth, h = window.innerHeight;
  canvas.width=w; canvas.height=h;
  const scene    = new THREE.Scene();
  const camera   = new THREE.PerspectiveCamera(60, w/h, 0.1, 200);
  const renderer = new THREE.WebGLRenderer({{antialias:true, canvas}});
  renderer.setSize(w,h);
  renderer.setPixelRatio(window.devicePixelRatio);
  renderer.shadowMap.enabled = true;

  {scene_js}

  window.addEventListener('resize',()=>{{
    const nw=window.innerWidth, nh=window.innerHeight;
    camera.aspect=nw/nh;
    camera.updateProjectionMatrix();
    renderer.setSize(nw,nh);
  }});
}})();
</script></body></html>"""

        components.html(html, height=520, scrolling=False)

# ── Status Bar ─────────────────────────────────────────────────────────────────
status = "● RENDERING LIVE" if st.session_state.running else "◼ PAUSED"
status_col = "#00FF88" if st.session_state.running else "#FFB800"
mode_label = f"{preset}" if mode == "Preset Animations" else "Custom Code"
st.markdown(f"""
<div class="status-bar">
  <div><span style="color:{status_col}">{status}</span>
       &nbsp;<span style="color:#2E3D5C">|</span>&nbsp;
       <span style="color:#6A7FA8">{mode_label}</span>
  </div>
  <div style="color:#2E3D5C">CODE-ANIMATION v3.0 &nbsp;|&nbsp; Three.js r128 &nbsp;|&nbsp; Streamlit Cloud</div>
</div>
""", unsafe_allow_html=True)
