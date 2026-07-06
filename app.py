import streamlit as str
import time
import random

# Page Setup
str.set_page_config(page_title="Our Cosmic Milky Way ❤️", page_icon="🌌", layout="centered")

# Custom CSS - Deep Galaxy, Milky Way, White Moon, White Stars & Rain-like White Snow
str.markdown("""
    <style>
    /* Full App Background - Deep Milky Way Galaxy Theme */
    .stApp {
        background: radial-gradient(circle at 75% 25%, rgba(100, 50, 200, 0.45), transparent 50%),
                    radial-gradient(circle at 25% 75%, rgba(180, 50, 150, 0.35), transparent 60%),
                    linear-gradient(135deg, #04020a 0%, #0a061c 40%, #140b2a 80%, #250b2b 100%);
        font-family: 'Georgia', serif;
        color: #ffffff;
        overflow-x: hidden;
    }
    
    /* Main Heading - Glowing White/Pink Romantic Text */
    h1 {
        color: #ffffff;
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        text-shadow: 0 0 15px rgba(255, 255, 255, 0.8), 2px 2px 5px rgba(0, 0, 0, 0.9);
        margin-top: 10px;
    }
    
    /* Subtitle Text */
    .romantic-sub {
        color: #e0e0e0;
        font-size: 20px;
        text-align: center;
        font-style: italic;
        margin-bottom: 30px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
    }
    
    /* Love Letter Box */
    .love-letter {
        background-color: rgba(8, 5, 20, 0.92);
        padding: 30px;
        border-radius: 25px;
        border: 2px solid #ffffff;
        box-shadow: 0px 0px 30px rgba(255, 255, 255, 0.3);
        text-align: center;
        animation: fadeIn 2.5s;
    }
    
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    /* Button Styling Customization */
    div.stButton > button {
        background: linear-gradient(90deg, #ffffff 0%, #e0e0e0 100%) !important;
        color: #100a26 !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 50px !important;
        padding: 12px 30px !important;
        border: none !important;
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.5) !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:hover {
        transform: scale(1.08) !important;
        box-shadow: 0 0 30px rgba(255, 255, 255, 0.9) !important;
    }
    
    /* Cosmic Falling Elements (White Stars, White Raindrops/Snow) */
    .cosmic-item {
        position: fixed;
        top: -10%;
        z-index: 9999;
        pointer-events: none;
        color: #ffffff !important; /* Everything forced to Pure White */
        text-shadow: 0 0 8px rgba(255, 255, 255, 0.8);
    }
    
    /* Rain-like straight falling animation */
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
        color: #ffffff;
        opacity: 0.9;
        filter: drop-shadow(0 0 25px rgba(255, 255, 255, 0.85)) brightness(2); /* Pure White Glowing Moon */
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

# Glowing White Moon Always on Screen
str.markdown('<div class="milkyway-moon">🌙</div>', unsafe_allow_html=True)

# Main Screen Text
str.markdown("<h1>For Someone Special... ✨❤️</h1>", unsafe_allow_html=True)
str.markdown('<div class="romantic-sub">Ye choti si jagah maine sirf aapke liye banayi hai. Apne dil par haath rakhein aur neeche click karein... 👇</div>', unsafe_allow_html=True)

# Centered Button Layout
col1, col2, col3 = str.columns([1, 1.2, 1])
with col2:
    click_me = str.button("Open My Heart 💖", use_container_width=True)

if click_me:
    with str.spinner("Aapke liye tare aur baarish ki boondein saja raha hoon... 🌌"):
        time.sleep(1.8)
    
    # Mix pool of White Stars, White Snow, and Raindrops
    # Gaping text-shadow handles the color overlay perfectly
    cosmic_html = ""
    white_items = ["✨", "❄️", "⭐", "💧", "✦", "✧"]
    
    # Generating 45 pure white elements falling like a beautiful rain shower
    for i in range(45):
        element = random.choice(white_items)
        left_pos = random.randint(2, 98)
        duration = random.uniform(4.0, 7.5) # Fast like rain, smooth like snow
        delay = random.uniform(0.0, 4.0)
        size = random.randint(14, 26)
        
        cosmic_html += f'<div class="cosmic-item rain-fall" style="left: {left_pos}%; animation-duration: {duration}s; animation-delay: {delay}s; font-size: {size}px;">{element}</div>'
    
    str.markdown(cosmic_html, unsafe_allow_html=True)
    
    # Pure Romantic Love Letter content
    str.markdown("""
    <div class="love-letter">
        <h2 style="color: #ffffff; font-family: 'Brush Script MT', cursive; font-size: 35px; text-shadow: 0 0 10px rgba(255,255,255,0.5);">Dear Special Someone, 🌸</h2>
        <p style="font-size: 19px; color: #f0f0f0; line-height: 1.8; font-style: italic;">
            "Kuch log zindagi mein aate hain aur use hamesha ke liye khubsurat bana dete hain...<br>
            Aap unhi mein se ek ho. Aapka sikhna, badhna aur har pal muskurana dil ko chu jata hai."
        </p>
        <hr style="border: 0; height: 1px; background: linear-gradient(to right, rgba(255,255,255,0), rgba(255,255,255,0.6), rgba(255,255,255,0)); margin: 20px 0;">
        <p style="font-size: 18px; color: #ffffff; font-weight: bold; text-shadow: 0 0 5px rgba(255,255,255,0.4);">
            Radha-Krishna ji ke prem ki tarah, aapki zindagi bhi hamesha sacha prem, <br>
            anant khushiyan aur sukoon se bhari rahe. ✨✨
        </p>
        <p style="font-size: 15px; color: #ccc; margin-top: 15px;">❤️ Always keep smiling, because your smile belongs to this world ❤️</p>
    </div>
    """, unsafe_allow_html=True)
    
    str.write("") # Blank space
    
    # 100% Working Beautiful Divine Radha Krishna Image Artwork
    str.image("https://images.unsplash.com/photo-1601931649911-37911b33346d?w=600", caption="✨ Radhe Radhe - Shaswat Prem ✨", use_container_width=True)
