import streamlit as str
import time

# Page Setup - Dil aur Galaxy wala title
str.set_page_config(page_title="A Cosmic Love Message For You ❤️", page_icon="🌌", layout="centered")

# Custom CSS - Deep Galaxy space view background aur slow custom heart animations
str.markdown("""
    <style>
    /* Full App Background - Deep Galaxy Cosmic View */
    .stApp {
        background: linear-gradient(135deg, #0f0c20 0%, #15102a 30%, #2b1055 70%, #511242 100%);
        font-family: 'Georgia', serif;
        color: #ffffff;
    }
    
    /* Main Heading - Shining Silver/Pink text */
    h1 {
        color: #ffb6c1;
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(255, 182, 193, 0.6), 2px 2px 4px rgba(0, 0, 0, 0.5);
        margin-top: 10px;
    }
    
    /* Subtitle Text */
    .romantic-sub {
        color: #e0e0e0;
        font-size: 20px;
        text-align: center;
        font-style: italic;
        margin-bottom: 30px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    
    /* Love Letter Box in Space */
    .love-letter {
        background-color: rgba(20, 15, 35, 0.85);
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #ff4b4b;
        box-shadow: 0px 0px 25px rgba(255, 75, 75, 0.4);
        text-align: center;
        animation: fadeIn 2s;
    }
    
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    /* Button Styling Customization */
    div.stButton > button {
        background: linear-gradient(90deg, #ff4b4b 0%, #ff6b8b 100%) !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 50px !important;
        padding: 12px 30px !important;
        border: none !important;
        box-shadow: 0 0 15px rgba(255, 75, 75, 0.5) !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:hover {
        transform: scale(1.08) !important;
        box-shadow: 0 0 25px rgba(255, 75, 75, 0.8) !important;
    }
    
    /* Slow Heart Falling Custom CSS Overlay */
    .heart-fall {
        position: fixed;
        top: -10%;
        color: #ff4b4b;
        font-size: 24px;
        opacity: 0.8;
        z-index: 9999;
        animation: fall linear infinite;
    }
    @keyframes fall {
        0% { top: -10%; transform: translateX(0) rotate(0deg); opacity: 0.9; }
        100% { top: 110%; transform: translateX(100px) rotate(360deg); opacity: 0; }
    }
    </style>
""", unsafe_allow_html=True)

# Main Screen Text
str.markdown("<h1>For Someone Special... ✨❤️</h1>", unsafe_allow_html=True)
str.markdown('<div class="romantic-sub">Ye choti si jagah maine sirf aapke liye banayi hai. Apne dil par haath rakhein aur neeche click karein... 👇</div>', unsafe_allow_html=True)

# Centered Button Layout
col1, col2, col3 = str.columns([1, 1.2, 1])
with col2:
    click_me = str.button("Open My Heart 💖", use_container_width=True)

if click_me:
    with str.spinner("Aapke liye sacha pyaar dhoodh raha hoon... 🌹"):
        time.sleep(1.8)
    
    # Custom HTML code for Slow Red Hearts Falling (Balloons hatake slow heart effect)
    hearts_html = ""
    # Alag-alag positions aur slow animation speeds ke sath 15 hearts generate karna
    import random
    for i in range(15):
        left_pos = random.randint(5, 95)
        duration = random.uniform(5.0, 9.0) # 5 se 9 seconds ki slow speed
        delay = random.uniform(0.0, 3.0)
        hearts_html += f'<div class="heart-fall" style="left: {left_pos}%; animation-duration: {duration}s; animation-delay: {delay}s;">❤️</div>'
    
    str.markdown(hearts_html, unsafe_allow_html=True)
    
    # Pure Romantic Love Letter content
    str.markdown("""
    <div class="love-letter">
        <h2 style="color: #ff6b8b; font-family: 'Brush Script MT', cursive; font-size: 35px;">Dear Special Someone, 🌸</h2>
        <p style="font-size: 19px; color: #f0f0f0; line-height: 1.8; font-style: italic;">
            "Kuch log zindagi mein aate hain aur use hamesha ke liye khubsurat bana dete hain...<br>
            Aap unhi mein se ek ho. Aapka sikhna, badhna aur har pal muskurana dil ko chu jata hai."
        </p>
        <hr style="border: 0; height: 1px; background: linear-gradient(to right, rgba(0,0,0,0), rgba(255,107,139,0.5), rgba(0,0,0,0)); margin: 20px 0;">
        <p style="font-size: 18px; color: #ff4b4b; font-weight: bold;">
            Radha-Krishna ji ke prem ki tarah, aapki zindagi bhi hamesha sacha prem, <br>
            anant khushiyan aur sukoon se bhari rahe. ✨✨
        </p>
        <p style="font-size: 15px; color: #aaa; margin-top: 15px;">❤️ Always keep smiling, because your smile belongs to this world ❤️</p>
    </div>
    """, unsafe_allow_html=True)
    
    str.write("") # Blank space
    
    # 100% Working Beautiful Divine Radha Krishna Image Artwork
    str.image("https://images.unsplash.com/photo-1601931649911-37911b33346d?w=600", caption="✨ Radhe Radhe - Shaswat Prem ✨", use_container_width=True)
