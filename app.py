import streamlit as str
import time

# Page Setup
str.set_page_config(page_title="A true Love ❤️", page_icon="🌌", layout="centered")

if "page" not in str.session_state:
    str.session_state.page = 1

# --- CSS STYLING (Stylish Font & Dark Text Logic) ---
CSS_BASE_STYLE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

.stApp {
    background: linear-gradient(180deg, #000814 0%, #001d3d 100%) !important;
    font-family: 'Poppins', sans-serif;
}

h1, h2, h3, h4 { color: #ffffff !important; }
p { color: #e0e0e0 !important; }

.stylish-box { 
    background: rgba(255, 255, 255, 0.08); 
    padding: 30px; 
    border-radius: 20px; 
    border: 1px solid rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
}
.vikar-box { margin-bottom: 20px; padding: 15px; border-left: 4px solid #ff6b8b; background: rgba(0,0,0,0.3); }

/* Solar System (Behind) */
.solar-system { position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: -1; pointer-events: none; }
</style>
"""
str.markdown(CSS_BASE_STYLE, unsafe_allow_html=True)

# --- PAGE LOGIC ---
if str.session_state.page == 1:
    str.markdown("<h1>For Someone Special... ✨❤️</h1>", unsafe_allow_html=True)
    str.markdown('<div class="stylish-box">Ye choti si jagah maine sirf aapke liye banayi hai.</div>', unsafe_allow_html=True)
    if str.button("Open My Heart 💖"):
        str.session_state.page = 2
        str.rerun()

elif str.session_state.page == 2:
    str.markdown("<h1>Our Cosmic Universe ✨</h1>", unsafe_allow_html=True)
    str.markdown('''
        <div class="stylish-box">
            <h2 style="font-size: 32px;">Dear Special Someone, 🌸</h2>
            <p style="font-size: 18px; line-height: 1.8; font-style: italic;">
                "Is anant aasmaan mein laakhon sitare hain, par hamare is chote se brahmand mein, sabsay haseen aur pyari chamak aapki muskurahat ki hai."
            </p>
        </div>
    ''', unsafe_allow_html=True)
    if str.button("Next Page ❤️"):
        str.session_state.page = 3
        str.rerun()

elif str.session_state.page == 3:
    str.markdown("<h1>The Eternal Love ✨</h1>", unsafe_allow_html=True)
    str.markdown('''
        <div class="stylish-box">
            <h3 style="color: #ff6b8b !important;">✨ Radhe Radhe - Shaswat Prem ✨</h3>
            <p style="font-size: 18px;">"Radha Krishna ka prem sikhata hai ki rishtey aatma se judte hain. Aapki zindagi isi pavitra prem se mehakti rahe."</p>
        </div>
    ''', unsafe_allow_html=True)
    if str.button("Eternal Prem ✨"):
        str.session_state.page = 4
        str.rerun()

elif str.session_state.page == 4:
    str.markdown("<h1>The Ultimate Destination ❤️</h1>", unsafe_allow_html=True)
    str.markdown('''
        <div class="stylish-box">
            <p style="font-size: 18px;">"Duniya ki sabsay khoobsoorat cheez ko na dekha ja sakta hai, na chhua ja sakta hai... use sirf dil se mehsoos kiya jata hai."</p>
        </div>
    ''', unsafe_allow_html=True)
    if str.button("Continue..."):
        str.session_state.page = 5
        str.rerun()

elif str.session_state.page == 5:
    str.markdown("<h1>Vikaro Se Mukti 🌌</h1>", unsafe_allow_html=True)
    str.markdown('<div class="vikar-box"><h4>1. डर (Fear)</h4><p>Sacha prem har darr ko mita deta hai.</p></div>', unsafe_allow_html=True)
    str.markdown('<div class="vikar-box"><h4>2. मोह (Attachment)</h4><p>Prem mein paane ki zidd nahi, samarpit hone ka sukoon hota hai.</p></div>', unsafe_allow_html=True)
    if str.button("Next"):
        str.session_state.page = 6
        str.rerun()

elif str.session_state.page == 6:
    str.markdown("<h1>Krishna Prem ✨</h1>", unsafe_allow_html=True)
    str.markdown('<div class="stylish-box"><p>Prem bandhan nahi, aatma ki mukti hai.</p></div>', unsafe_allow_html=True)
    if str.button("Next"):
        str.session_state.page = 7
        str.rerun()

elif str.session_state.page == 7:
    str.markdown("<h1>Pure Love 🌌</h1>", unsafe_allow_html=True)
    str.markdown('<div class="stylish-box"><p>Sacha prem wahi hai jahan koi shart na ho, bas ek dusre ki aatma ka samman ho.</p></div>', unsafe_allow_html=True)
    if str.button("Final Page ✨"):
        str.session_state.page = 8
        str.rerun()

# --- LAST PAGE (Back to Start Button Only Here) ---
elif str.session_state.page == 8:
    str.markdown("<h1>A Heartfelt Thank You ❤️</h1>", unsafe_allow_html=True)
    str.markdown('''
        <div class="stylish-box">
            <p style="font-size: 20px;">"Is chote se safar mein, aapke hone se, meri zindagi ab ek khoobsurat ibaadat si ho gayi."</p>
        </div>
    ''', unsafe_allow_html=True)
    
    # Sirf yahan button dikhega
    if str.button("Back to Start 🔄"):
        str.session_state.page = 1
        str.rerun()
