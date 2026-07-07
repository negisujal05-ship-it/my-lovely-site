import streamlit as str
import random

# Page Setup
str.set_page_config(page_title="Cosmic Love ❤️", page_icon="🌌", layout="centered")

if "page" not in str.session_state:
    str.session_state.page = 1

# --- LIGHTWEIGHT GALAXY THEME ---
CSS_BASE_STYLE = """
<style>
/* Real Galaxy Background */
.stApp {
    background: radial-gradient(circle at center, #1b2735 0%, #090a0f 100%);
    color: #ffffff;
    font-family: 'Georgia', serif;
}

/* Elegant Content Box */
.stylish-box {
    background: rgba(255, 255, 255, 0.05);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    text-align: center;
    backdrop-filter: blur(5px);
}

/* Minimalist Button */
div.stButton > button {
    background: transparent !important;
    color: #ffffff !important;
    border: 1px solid #ffffff !important;
    border-radius: 50px !important;
    padding: 10px 25px !important;
    transition: 0.3s !important;
}
div.stButton > button:hover {
    background: #ffffff !important;
    color: #000 !important;
}

/* Lightweight Galaxy Particles */
.particle {
    position: fixed;
    top: -5%;
    pointer-events: none;
    z-index: 0;
    animation: fall linear infinite;
    opacity: 0.6;
}
@keyframes fall {
    to { transform: translateY(105vh) rotate(360deg); }
}
</style>
"""
str.markdown(CSS_BASE_STYLE, unsafe_allow_html=True)

# --- LIGHTWEIGHT ANIMATION ENGINE ---
def apply_galaxy_animation():
    # Sirf 15 particles taaki site heavy na ho
    elements = ["✨", "❄️", "❤️", "⭐"]
    particles = ""
    for _ in range(15):
        left = random.randint(0, 100)
        delay = random.uniform(0, 15)
        duration = random.uniform(10, 20)
        size = random.randint(10, 18)
        char = random.choice(elements)
        particles += f'<div class="particle" style="left:{left}%; animation-delay:{delay}s; animation-duration:{duration}s; font-size:{size}px;">{char}</div>'
    str.components.v1.html(particles, height=0)

# --- PAGE LOGIC ---
apply_galaxy_animation()

if str.session_state.page == 1:
    str.markdown("<h1>Cosmic Journey ✨</h1>", unsafe_allow_html=True)
    if str.button("Begin the Voyage"):
        str.session_state.page = 2
        str.rerun()

elif str.session_state.page == 2:
    str.markdown('<div class="stylish-box"><h2>Aapka Swagat Hai</h2><p>Ye safar sirf aapke liye hai.</p></div>', unsafe_allow_html=True)
    if str.button("Next"):
        str.session_state.page = 3
        str.rerun()

# (Aap yahan apne baaki pages isi format mein add kar sakte hain)
