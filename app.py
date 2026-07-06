import streamlit as str
import time
import random

# Page Setup - Cosmic Romantic Title
str.set_page_config(page_title="Our Cosmic Milky Way ❤️", page_icon="🌌", layout="centered")

# Custom CSS - Deep Galaxy, Milky Way effects, Moon, Stars, and Slow Animations
str.markdown("""
    <style>
    /* Full App Background - Milky Way & Deep Galaxy Theme */
    .stApp {
        background: radial-gradient(circle at 80% 20%, rgba(123, 50, 250, 0.4), transparent 50%),
                    radial-gradient(circle at 20% 80%, rgba(255, 75, 139, 0.3), transparent 60%),
                    linear-gradient(135deg, #060412 0%, #0f0a26 40%, #1d0f3a 80%, #36103b 100%);
        font-family: 'Georgia', serif;
        color: #ffffff;
        overflow-x: hidden;
    }
    
    /* Main Heading - Glowing Cosmic Text */
    h1 {
        color: #ffb6c1;
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        text-shadow: 0 0 15px rgba(255, 182, 193, 0.8), 2px 2px 5px rgba(0, 0, 0, 0.7);
        margin-top: 10px;
    }
    
    /* Subtitle Text */
    .romantic-sub {
        color: #e0e0e0;
        font-size: 20px;
        text-align: center;
        font-style: italic;
        margin-bottom: 30px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.6);
    }
    
    /* Love Letter Box inside the Milky Way */
    .love-letter {
        background-color: rgba(12, 8, 28, 0.88);
        padding: 30px;
        border-radius: 25px;
        border: 2px solid #ff6b8b;
        box-shadow: 0px 0px 30px rgba(255, 107, 139, 0.5);
        text-align: center;
        animation: fadeIn 2.5s;
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
        box-shadow: 0 0 20px rgba(255, 75, 75, 0.6) !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:hover {
        transform: scale(1.08) !important;
        box-shadow: 0 0 30px rgba(255, 107, 139, 0.9) !important;
    }
    
    /* Universal Cosmic Falling Element Styles (Hearts, Snow, Stars) */
    .cosmic-item {
        position: fixed;
        top: -10%;
        z-index: 9999;
        pointer-events: none;
        animation: fall linear infinite;
    }
    @keyframes fall {
        0% { top: -10%; transform: translateX(0) rotate(0deg); opacity: 0; }
        10% { opacity: 0.9; }
        90% { opacity: 0.9; }
        100% { top: 110%; transform: translateX(120px) rotate(360deg); opacity: 0; }
    }
    
    /* Fixed Chand (Moon) Background Element */
    .milkyway-moon {
        position: fixed;
        top: 15%;
        right: 8%;
        font-size: 65px;
        opacity: 0.85;
        filter: drop-shadow(0 0 20px rgba(255, 255, 255, 0.6));
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

# Static Moon Effect Always on Screen
str.markdown('<div class="milkyway-moon">🌙</div>', unsafe_allow_html=True)

# Main Screen Text
str.markdown("<h1>For Someone Special... ✨❤️</h1>", unsafe_allow_html=True)
str.markdown('<div class="romantic-sub">Ye choti si jagah maine sirf aapke liye banayi hai. Apne dil par haath rakhein aur neeche click karein... 👇</div>', unsafe_allow_html=True)

# Centered Button Layout
col1, col2, col3 = str.columns([1, 1.2, 1])
with col2:
    click_me = str.button("Open My Heart 💖", use_container_width=True)

if click_me:
    with str.spinner("Aapke liye sacha pyaar aur tare tod raha hoon... 🌌"):
        time.sleep(1.8)
    
    # Custom HTML code for Cosmic Mix: Hearts, Stars & Snow falling slowly
    cosmic_html = ""
    items_pool = ["❤️", "✨", "❄️", "⭐", "💖"]
    
    # Generating 30 distinct cosmic particles with smooth variations
    for i in range(30):
        element = random.choice(items_pool)
        left_pos = random.randint(3, 97)
        duration = random.uniform(6.0, 11.0) # Ekdum relaxing slow motion speed
        delay = random.uniform(0.0, 4.0)
        size = random.randint(16, 28) # Random sizing for deep galaxy depth
        
        cosmic_html += f'<div class="cosmic-item" style="left: {left_pos}%; animation-duration: {duration}s; animation-delay: {delay}s; font-size: {size}px;">{element}</div>'
    
    str.markdown(cosmic_html, unsafe_allow_html=True)
    
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
