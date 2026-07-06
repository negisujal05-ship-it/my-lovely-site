import streamlit as str
import time
import random

# Page Setup
str.set_page_config(page_title="Our Cosmic Milky Way ❤️", page_icon="🌌", layout="centered")

# Multi-page system ko track karne ke liye session_state
if "page" not in str.session_state:
    str.session_state.page = 1

# Custom CSS - Deep Black Galaxy Background, Glowing Moon, Fixed White Stars
str.markdown("""
    <style>
    /* Full App Background - True Deep Cosmic Galaxy View */
    .stApp {
        background: linear-gradient(135deg, #020105 0%, #050312 40%, #0b0518 80%, #11031c 100%);
        font-family: 'Georgia', serif;
        color: #ffffff;
        overflow-x: hidden;
    }
    
    /* Background mein fixed chamakte hue sitare (Static Stars) */
    .stApp::before {
        content: "⭐  .  ✨  .  ✦  .  ✧  .  ⭐  .  ✨  .  ✦  .  ✧  .  ⭐  .  ✨  .  ✦  .  ✧  .  ⭐  .  ✨  .  ✦  .  ✧";
        position: fixed;
        top: 5%;
        left: 5%;
        right: 5%;
        bottom: 5%;
        font-size: 18px;
        color: rgba(255, 255, 255, 0.4);
        word-spacing: 40px;
        line-height: 5;
        pointer-events: none;
        z-index: 0;
        opacity: 0.8;
    }
    
    /* Headings Styling */
    h1 {
        color: #ffffff;
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        text-shadow: 0 0 15px rgba(255, 255, 255, 0.8), 2px 2px 5px rgba(0, 0, 0, 0.9);
        margin-top: 40px;
        position: relative;
        z-index: 2;
    }
    
    /* Subtitle Text */
    .romantic-sub {
        color: #e0e0e0;
        font-size: 20px;
        text-align: center;
        font-style: italic;
        margin-bottom: 40px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
        position: relative;
        z-index: 2;
    }
    
    /* Content Box / Love Letter Styling */
    .love-letter {
        background-color: rgba(5, 3, 12, 0.95);
        padding: 35px;
        border-radius: 25px;
        border: 2px solid #ffffff;
        box-shadow: 0px 0px 30px rgba(255, 255, 255, 0.25);
        text-align: center;
        animation: fadeIn 1.5s;
        position: relative;
        z-index: 2;
        margin-bottom: 30px;
    }
    
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    /* White Buttons Customization */
    div.stButton > button {
        background: linear-gradient(90deg, #ffffff 0%, #e0e0e0 100%) !important;
        color: #050312 !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 50px !important;
        padding: 12px 35px !important;
        border: none !important;
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.4) !important;
        transition: all 0.3s ease !important;
        display: block;
        margin: 0 auto !important;
    }
    div.stButton > button:hover {
        transform: scale(1.08) !important;
        box-shadow: 0 0 30px rgba(255, 255, 255, 0.8) !important;
    }
    
    /* Falling Elements Styles */
    .cosmic-item {
        position: fixed;
        top: -10%;
        z-index: 9999;
        pointer-events: none;
    }
    .rain-fall {
        animation: rainLinear linear infinite;
    }
    @keyframes rainLinear {
        0% { top: -10%; transform: translateX(0); opacity: 0; }
        10% { opacity: 0.9; }
        90% { opacity: 0.9; }
        100% { top: 110%; transform: translateX(20px); opacity: 0; }
    }
    
    /* Floating White Moon Element */
    .milkyway-moon {
        position: fixed;
        top: 15%;
        right: 8%;
        font-size: 65px;
        opacity: 0.9;
        filter: drop-shadow(0 0 25px rgba(255, 255, 255, 0.85)) brightness(2);
        z-index: 1;
        animation: float 6s ease-in-out infinite;
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    </style>
""", unsafe_allow_html=True)

# Function to generate falling effect (Hearts & Rain)
def start_falling_effects():
    falling_html = ""
    rain_items = ["💧", "❄️"]
    red_hearts = ["❤️", "💖", "💘"]
    for i in range(45):
        if random.random() > 0.4:
            element = random.choice(rain_items)
            shadow_color = "rgba(255, 255, 255, 0.6)"
            text_color = "#ffffff"
        else:
            element = random.choice(red_hearts)
            shadow_color = "rgba(255, 75, 75, 0.8)"
            text_color = "inherit" 
        left_pos = random.randint(2, 98)
        duration = random.uniform(4.5, 7.5) 
        delay = random.uniform(0.0, 4.0)
        size = random.randint(14, 26)
        falling_html += f'<div class="cosmic-item rain-fall" style="left: {left_pos}%; animation-duration: {duration}s; animation-delay: {delay}s; font-size: {size}px; color: {text_color}; text-shadow: 0 0 8px {shadow_color};">{element}</div>'
    str.markdown(falling_html, unsafe_allow_html=True)

# Glowing White Moon Always on Screen
str.markdown('<div class="milkyway-moon">🌙</div>', unsafe_allow_html=True)


# --- PAGE 1: FIRST INTERFACE ---
if str.session_state.page == 1:
    str.markdown("<h1>For Someone Special... ✨❤️</h1>", unsafe_allow_html=True)
    str.markdown('<div class="romantic-sub">Ye choti si jagah maine sirf aapke liye banayi hai. Apne dil par haath rakhein aur neeche click karein... 👇</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = str.columns([1, 1.5, 1])
    with col2:
        if str.button("Open My Heart 💖", use_container_width=True):
            with str.spinner("Saja raha hoon aapke liye ek nayi duniya... 🌌"):
                time.sleep(1.2)
            str.session_state.page = 2
            str.rerun()


# --- PAGE 2: SECOND INTERFACE ---
elif str.session_state.page == 2:
    start_falling_effects()
    str.markdown("<h1>Our Cosmic Universe ✨</h1>", unsafe_allow_html=True)
    
    str.markdown("""
    <div class="love-letter">
        <h2 style="color: #ffffff; font-family: 'Brush Script MT', cursive; font-size: 38px; text-shadow: 0 0 10px rgba(255,255,255,0.5); margin-bottom: 20px;">Dear Special Someone, 🌸</h2>
        <p style="font-size: 20px; color: #fdfdfd; line-height: 1.8; font-style: italic; font-weight: 500;">
            "Is anant aasmaan mein laakhon sitare hain,<br>
            par hamare is chote se brahmand mein,<br>
            sabsay haseen aur pyari chamak aapki muskurahat ki hai.<br><br>
            Aapka zindagi mein hona kisi tohfe se kam nahi,<br>
            aap har pal ko khubsurat aur sukoon se bhar dete ho."
        </p>
        <hr style="border: 0; height: 1px; background: linear-gradient(to right, rgba(255,255,255,0), rgba(255,255,255,0.6), rgba(255,255,255,0)); margin: 25px 0;">
        <p style="font-size: 16px; color: #ffb3c1; letter-spacing: 1px;">💖 Ek sacha ehsaas jo hamesha qayam rahega 💖</p>
    </div>
    """, unsafe_allow_html=True)
    
    str.markdown("<p style='text-align: center; font-size: 18px; color: #ff6b8b; font-weight: bold;'>Agla surprise dekhne ke liye neeche dil par click karein... 👇</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = str.columns([1, 1.5, 1])
    with col2:
        if str.button("Next Page ❤️", use_container_width=True):
            str.session_state.page = 3
            str.rerun()


# --- PAGE 3: THIRD INTERFACE ---
elif str.session_state.page == 3:
    start_falling_effects()
    str.markdown("<h1>The Eternal Love ✨🙏</h1>", unsafe_allow_html=True)
    
    str.markdown("""
    <div class="love-letter">
        <h3 style="color: #ff6b8b; font-size: 28px; font-family: 'Brush Script MT', cursive; margin-bottom: 15px;">✨ Radhe Radhe - Shaswat Prem ✨</h3>
        <p style="font-size: 19px; color: #e8e8e8; line-height: 1.8; font-style: italic;">
            "Prem ka matlab ek dusre ko paana nahi,<br>
            balki ek dusre mein poori tarah kho jaana hai.<br><br>
            Radha Krishna ka prem sikhata hai ki rishtey aatma se judte hain,<br>
            jahan dooriyan bhi dono ko alag nahi kar saktin.<br>
            Aapki zindagi bhi isi pavitra prem aur sukoon se hamesha mehakti rahe."
        </p>
        <hr style="border: 0; height: 1px; background: linear-gradient(to right, rgba(255,255,255,0), rgba(255,255,255,0.5), rgba(255,255,255,0)); margin: 20px 0;">
        <p style="font-size: 17px; color: #ffffff; font-weight: bold;">✨ Anant Prem Aur Atut Vishwas ✨</p>
    </div>
    """, unsafe_allow_html=True)
    
    str.image("https://images.unsplash.com/photo-1601931649911-37911b33346d?w=600", caption="🙏 Radhe Krishna Ki Kripa Aap Par Bani Rahe 🙏", use_container_width=True)
    
    str.write("")
    str.markdown("<p style='text-align: center; font-size: 18px; color: #ff6b8b; font-weight: bold;'>Agar prem ko jaana ho to... 👇</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = str.columns([1, 1.5, 1])
    with col2:
        if str.button("Eternal Prem ✨", use_container_width=True):
            str.session_state.page = 4
            str.rerun()


# --- PAGE 4: FOURTH INTERFACE (Image Updated to Radha Krishna) ---
elif str.session_state.page == 4:
    start_falling_effects()
    str.markdown("<h1>The Ultimate Destination ❤️</h1>", unsafe_allow_html=True)
    
    str.markdown("""
    <div class="love-letter">
        <h3 style="color: #ffffff; font-size: 28px; font-family: 'Brush Script MT', cursive; margin-bottom: 15px;">🌌 Sacha Prem Hi Brahmand Hai 🌌</h3>
        <p style="font-size: 19px; color: #e8e8e8; line-height: 1.8; font-style: italic;">
            "Prem wo nahi jo kuch samay ke liye ho,<br>
            prem toh wo hai jo sadiyon tak rooh mein bas jaye.<br><br>
            Aapki is yatra ka aakhri padaav yahi sikhata hai ki<br>
            duniya ki sabsay khoobsoorat cheez ko na dekha ja sakta hai, <br>
            na chhua ja sakta hai... use sirf dil se mehsoos kiya jata hai."
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Updated to a beautiful divine silhouette style Radha Krishna Image
    str.image("https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?w=600", caption="🙏 Radhe Krishna - Prem Hi Poornata Hai 🙏", use_container_width=True)
    
    str.write("")
    col1, col2, col3 = str.columns([1, 1.5, 1])
    with col2:
        if str.button("Go to Start 🔄", use_container_width=True):
            str.session_state.page = 1
            str.rerun()
