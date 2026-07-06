import streamlit as str
import time
import random

# Page Setup
str.set_page_config(page_title="Our Cosmic Milky Way ❤️", page_icon="🌌", layout="centered")

if "page" not in str.session_state:
    str.session_state.page = 1

# --- CSS & ANIMATION ---
CSS_BASE_STYLE = """
<style>
/* Page Entry Animation: Smooth Slide Down */
@keyframes slideDown {
    0% { opacity: 0; transform: translateY(-30px); }
    100% { opacity: 1; transform: translateY(0); }
}

.stApp {
    background: linear-gradient(135deg, #020105 0%, #050312 40%, #0b0518 80%, #11031c 100%);
    color: #ffffff;
    font-family: 'Georgia', serif;
}

/* Applying animation to the main block */
.block-container {
    animation: slideDown 1.2s ease-out forwards;
}

.stylish-box {
    background: rgba(10, 5, 20, 0.85);
    padding: 40px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.2);
    position: relative;
    overflow: hidden;
    text-align: center;
}

.watermark {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%) rotate(-10deg);
    font-size: 80px;
    font-weight: bold;
    color: rgba(255, 255, 255, 0.03);
    pointer-events: none;
}

div.stButton > button {
    background: #ffffff !important;
    color: #000 !important;
    border-radius: 50px !important;
    font-weight: bold !important;
    transition: 0.3s !important;
}
</style>
"""
str.markdown(CSS_BASE_STYLE, unsafe_allow_html=True)

# Navigation Logic Helper
def go_to_page(page_num):
    with str.spinner("Loading..."):
        time.sleep(0.5) # Slight delay for smooth effect
        str.session_state.page = page_num
        str.rerun()

# --- CONTENT PAGES ---

# Page 1
if str.session_state.page == 1:
    str.markdown("<h1>For Someone Special ✨</h1>", unsafe_allow_html=True)
    str.markdown('<div class="stylish-box"><div class="watermark">LOVE</div>Ye jagah sirf aapke liye...</div>', unsafe_allow_html=True)
    if str.button("Open Heart 💖"): go_to_page(2)

# Page 2
elif str.session_state.page == 2:
    str.markdown("<h1>Our Universe ✨</h1>", unsafe_allow_html=True)
    str.markdown('<div class="stylish-box"><div class="watermark">UNIVERSE</div>Aapka hona kisi tohfe se kam nahi.</div>', unsafe_allow_html=True)
    if str.button("Next Page"): go_to_page(3)

# Page 3
elif str.session_state.page == 3:
    str.markdown("<h1>Eternal Love ✨</h1>", unsafe_allow_html=True)
    str.markdown('<div class="stylish-box"><div class="watermark">ETERNAL</div>Rishtey aatma se judte hain...</div>', unsafe_allow_html=True)
    if str.button("Next Page"): go_to_page(4)

# Page 4
elif str.session_state.page == 4:
    str.markdown("<h1>The Destination ❤️</h1>", unsafe_allow_html=True)
    str.markdown('<div class="stylish-box"><div class="watermark">DESTINY</div>Prem mehsoos kiya jata hai.</div>', unsafe_allow_html=True)
    if str.button("Next Page"): go_to_page(5)

# Page 5
elif str.session_state.page == 5:
    str.markdown("<h1>Vikaro Se Mukti 🌌</h1>", unsafe_allow_html=True)
    str.markdown('<div class="stylish-box"><div class="watermark">MUKTI</div>Prem se sab vikar mit jate hain.</div>', unsafe_allow_html=True)
    if str.button("Prem ka asal matlab jano ✨"): go_to_page(6)

# Page 6
elif str.session_state.page == 6:
    str.markdown("<h1>Prem Ka Sach 🌌</h1>", unsafe_allow_html=True)
    str.markdown('''
        <div class="stylish-box">
            <div class="watermark">PREM</div>
            <p>Prem wo sthiti hai jahan aap apni khushi doosre mein dhundte hain.<br>
            Yahan koi shart nahi, bas aatma ka milan hai.</p>
        </div>
    ''', unsafe_allow_html=True)
    if str.button("Enter the Love World 🚀"): go_to_page(1)
