import streamlit as str
import time
import random

# Page Setup
str.set_page_config(page_title="A true Love ❤️", page_icon="🌌", layout="centered")

if "page" not in str.session_state:
    str.session_state.page = 1

# --- CSS STYLING ---
CSS_BASE_STYLE = """
<style>
/* Background aur Animation Layering */
.stApp {
    background: radial-gradient(circle at center,#ffb347 0%,#ff8c00 5%,transparent 10%),
                radial-gradient(circle at 20% 30%,rgba(0,191,255,0.15),transparent 30%),
                radial-gradient(circle at 80% 70%,rgba(138,43,226,0.15),transparent 30%),
                linear-gradient(180deg,#000814,#001d3d,#000000) !important;
    color: #ffffff;
}

.block-container { position: relative; z-index: 10; }
.stylish-box { position: relative; z-index: 20; background: rgba(5, 3, 12, 0.85); padding: 40px; border-radius: 25px; border: 1px solid #ffffff; }

/* FIX: Solar System */
.solar-system {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 700px;
    height: 700px;
    z-index: -1; 
    pointer-events: none;
}

.sun {
    position: absolute;
    top: 50%; left: 50%;
    width: 80px; height: 80px;
    background: #ffd700; /* Red hatakar default wapas kar diya, aap change kar sakte hain */
    border-radius: 50%;
    transform: translate(-50%, -50%);
    box-shadow: 0 0 80px #ffd700;
}

.orbit { position: absolute; border: 1px solid rgba(255,255,255,0.08); border-radius: 50%; top: 50%; left: 50%; transform: translate(-50%, -50%); }
.orbit1 { width: 180px; height: 180px; animation: orbit 12s linear infinite; }
.orbit2 { width: 280px; height: 280px; animation: orbit 18s linear infinite; }
.orbit3 { width: 400px; height: 400px; animation: orbit 26s linear infinite; }
.orbit4 { width: 550px; height: 550px; animation: orbit 32s linear infinite; }

.planet { position: absolute; top: -10px; left: 50%; border-radius: 50%; transform: translateX(-50%); }
.p1 { width: 12px; height: 12px; background: #00d4ff; box-shadow: 0 0 15px #00d4ff; }
.p2 { width: 16px; height: 16px; background: #ff6b6b; box-shadow: 0 0 15px #ff6b6b; }
.p3 { width: 20px; height: 20px; background: #8a2be2; box-shadow: 0 0 20px #8a2be2; }

@keyframes orbit { from { transform: translate(-50%,-50%) rotate(0deg); } to { transform: translate(-50%,-50%) rotate(360deg); } }
</style>
"""
str.markdown(CSS_BASE_STYLE, unsafe_allow_html=True)

# --- ANIMATION FUNCTIONS ---
def apply_slow_cosmic_animation():
    # Aapka original logic
    pass

# --- SOLAR SYSTEM HTML ---
SOLAR_SYSTEM = """
<div class="solar-system">
    <div class="sun"></div>
    <div class="orbit orbit1"><div class="planet p1"></div></div>
    <div class="orbit orbit2"><div class="planet p2"></div></div>
    <div class="orbit orbit3"><div class="planet p3"></div></div>
    <div class="orbit orbit4"><div class="planet p2"></div></div>
</div>
"""
str.markdown(SOLAR_SYSTEM, unsafe_allow_html=True)

# --- STARS GENERATOR ---
stars_html = ""
for i in range(150):
    stars_html += f"""
    <div style="position:fixed; left:{random.randint(0,100)}%; top:{random.randint(0,100)}%; color:white; font-size:{random.randint(6,16)}px; opacity:{random.uniform(0.3,1)}; z-index:-1; pointer-events:none;">✦</div>
    """
str.markdown(stars_html, unsafe_allow_html=True)

# --- PAGE LOGIC (Aapka original logic continues...) ---
if str.session_state.page == 1:
    str.markdown("<h1>For Someone Special... ✨❤️</h1>", unsafe_allow_html=True)
    # ... baki ka code continue rakhein
