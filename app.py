import streamlit as str
import time
import random

# Page Setup
str.set_page_config(page_title="A true Love ❤️", page_icon="🌌", layout="centered")

if "page" not in str.session_state:
    str.session_state.page = 1

# --- CSS ---
CSS_BASE_STYLE = """
<style>
.stApp { background: radial-gradient(circle at center, #1b2735 0%, #090a0f 100%); color: #ffffff; }
.stylish-box { background: rgba(5, 3, 12, 0.96); padding: 40px; border-radius: 25px; border: 2px solid #ffffff; text-align: center; }
div.stButton > button { background: #ffffff !important; color: #000 !important; font-weight: bold !important; border-radius: 50px !important; }
</style>
"""
str.markdown(CSS_BASE_STYLE, unsafe_allow_html=True)

# --- ANIMATION ---
def apply_slow_cosmic_animation():
    elements = ["✨", "❄️", "❤️", "⭐", "💫"]
    style = "<style>.cosmic { position: fixed; top: -10%; animation: rain 15s linear infinite; pointer-events: none; }</style>"
    html = style + "".join([f'<div class="cosmic" style="left: {random.randint(0,100)}%; animation-delay: {random.uniform(0,10)}s; font-size: {random.randint(10,20)}px;">{random.choice(elements)}</div>' for _ in range(20)])
    str.components.v1.html(html, height=0)

# --- PAGES ---
if str.session_state.page == 1:
    apply_slow_cosmic_animation()
    str.markdown("<h1>For Someone Special ✨</h1>", unsafe_allow_html=True)
    if str.button("Open My Heart 💖"):
        str.session_state.page = 2
        str.rerun()

elif str.session_state.page == 2:
    apply_slow_cosmic_animation()
    str.markdown("<h1>Our Cosmic Universe 🌌</h1>", unsafe_allow_html=True)
    if str.button("Next Page"):
        str.session_state.page = 3
        str.rerun()

elif str.session_state.page == 3:
    apply_slow_cosmic_animation()
    str.markdown("<h1>Eternal Love ✨</h1>", unsafe_allow_html=True)
    if str.button("Next Page"):
        str.session_state.page = 4
        str.rerun()

elif str.session_state.page == 4:
    apply_slow_cosmic_animation()
    str.markdown("<h1>The Ultimate Destination ❤️</h1>", unsafe_allow_html=True)
    if str.button("Enter to Eternal Life"):
        str.session_state.page = 5
        str.rerun()

elif str.session_state.page == 5:
    apply_slow_cosmic_animation()
    str.markdown("<h1>Vikaro Se Mukti ✨</h1>", unsafe_allow_html=True)
    if str.button("Definition of Pure Love"):
        str.session_state.page = 6
        str.rerun()

elif str.session_state.page == 6:
    apply_slow_cosmic_animation()
    str.markdown("<h1>Pure Love Definition 🌌</h1>", unsafe_allow_html=True)
    str.markdown('<div class="stylish-box">Prem wo hai jo nishwarth bhaw se aatma se ho, na ki sharir se.</div>', unsafe_allow_html=True)
    if str.button("Final Page"):
        str.session_state.page = 7
        str.rerun()

elif str.session_state.page == 7:
    apply_slow_cosmic_animation()
    str.markdown("<h1>Thank You ❤️</h1>", unsafe_allow_html=True)
    str.markdown('<div class="stylish-box">Special thanks for visiting my site!</div>', unsafe_allow_html=True)
    if str.button("Back to Start"):
        str.session_state.page = 1
        str.rerun()
