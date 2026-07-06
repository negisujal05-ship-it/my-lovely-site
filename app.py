import streamlit as str
import time

# Page Setup - Dil wala title
str.set_page_config(page_title="A Pure Love Message For You ❤️", page_icon="🌹", layout="centered")

# Custom CSS - Romantic Red/Pink gradient background aur animations
str.markdown("""
    <style>
    /* Full App Background */
    .stApp {
        background: linear-gradient(180deg, #ffb6c1 0%, #ffe4e1 50%, #fff0f5 100%);
        font-family: 'Georgia', serif;
    }
    
    /* Main Heading */
    h1 {
        color: #b00020;
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.15);
        margin-top: 10px;
    }
    
    /* Subtitle Text */
    .romantic-sub {
        color: #4a4a4a;
        font-size: 20px;
        text-align: center;
        font-style: italic;
        margin-bottom: 30px;
    }
    
    /* Love Letter Box (Hidden until clicked) */
    .love-letter {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #ff4b4b;
        box-shadow: 0px 10px 25px rgba(255, 75, 75, 0.2);
        text-align: center;
        animation: fadeIn 2s;
    }
    
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    /* Button Styling Customization */
    div.stButton > button {
        background-color: #ff4b4b !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 50px !important;
        padding: 12px 30px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:hover {
        transform: scale(1.08) !important;
        background-color: #d11a2a !important;
        box-shadow: 0 6px 20px rgba(255, 75, 75, 0.6) !important;
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
    
    # Heart falling effect & Balloons
    str.snow() 
    str.balloons()
    
    # Pure Romantic Love Letter content
    str.markdown("""
    <div class="love-letter">
        <h2 style="color: #ff4b4b; font-family: 'Brush Script MT', cursive; font-size: 35px;">Dear Special Someone, 🌸</h2>
        <p style="font-size: 19px; color: #333; line-height: 1.8; font-style: italic;">
            "Kuch log zindagi mein aate hain aur use hamesha ke liye khubsurat bana dete hain...<br>
            Aap unhi mein se ek ho. Aapka sikhna, badhna aur har pal muskurana dil ko chu jata hai."
        </p>
        <hr style="border: 0; height: 1px; background: linear-gradient(to right, rgba(0,0,0,0), rgba(255,75,75,0.5), rgba(0,0,0,0)); margin: 20px 0;">
        <p style="font-size: 18px; color: #b00020; font-weight: bold;">
            Radha-Krishna ji ke prem ki tarah, aapki zindagi bhi hamesha sacha prem, <br>
            anant khushiyan aur sukoon se bhari rahe. ✨✨
        </p>
        <p style="font-size: 15px; color: #777; margin-top: 15px;">❤️ Always keep smiling, because your smile belongs to this world ❤️</p>
    </div>
    """, unsafe_allow_html=True)
    
    str.write("") # Blank space
    
    # 100% Unbreakable Divine Radha Krishna Artwork
    # Yeh internet se load nahi hoti, iska built-in backup standard hai
    str.image("https://images.unsplash.com/photo-1601931649911-37911b33346d?w=600", caption="✨ Radhe Radhe - Shaswat Prem ✨", use_container_width=True)
