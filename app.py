import streamlit as str
import time

# Page configuration - Pyaara sa heart icon title mein
str.set_page_config(page_title="A Very Special Message For You ❤️", page_icon="💖", layout="centered")

# Custom CSS - Background ko soft romantic pink aur text ko attractive banane ke liye
str.markdown("""
    <style>
    /* Pure website ka background aur font style */
    .stApp {
        background: linear-gradient(135deg, #ffe4e1 0%, #fff0f5 100%);
        font-family: 'Georgia', serif;
    }
    /* Heading (Title) ka look */
    h1 {
        color: #d11a2a;
        text-align: center;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    /* Subtitle aur text ka style */
    .lovely-text {
        color: #4a4a4a;
        font-size: 20px;
        text-align: center;
        font-style: italic;
        margin-bottom: 30px;
    }
    /* Messages ka romantic background box */
    .love-box {
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 15px;
        border: 2px dashed #ffb6c1;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title
str.title("Hey Dear! ✨💖")
str.markdown('<div class="lovely-text">Maine aapke liye ek bahut hi pyaara sa surprise taiyar kiya hai. Neeche diye gaye dil par click karein! 👇</div>', unsafe_allow_html=True)

# Columns banaye taaki button ekdum center mein dikhe
col1, col2, col3 = str.columns([1, 1, 1])
with col2:
    click_button = str.button("Click Here ❤️", use_container_width=True)

# Button click hone par kya hoga
if click_button:
    with str.spinner("Aapke liye pyaar load ho raha hai... 🥰"):
        time.sleep(1.5)
    
    # Magical Effects 🌸
    str.balloons() # Balloons urenge
    str.snow() # Isse screen par sundar snowfall/heart jaisa effect aayega
    
    # Romantic Message Box
    str.markdown("""
    <div class="love-box">
        <h2 style="color: #ff4b4b; margin-bottom: 10px;">🥰 To Someone Truly Special...</h2>
        <p style="font-size: 18px; color: #555; line-height: 1.6;">
            Aapka har naye cheez ko sikhna aur muskurate rehna behad khubsurat hai! ✨<br>
            Aapki zindagi hamesha khushiyon aur prem se bhari rahe.<br>
            <b>Hope aapka har ek din is site ki tarah lovely aur badiya rahe! 🌸✨</b>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    str.write("") # Khali jagah spacing ke liye
    
    # Beautiful Divine Radha Krishna Image URL
    radha_krishna_url = "https://images.unsplash.com/photo-1628134712034-71bc56834eb7?w=600"
    str.image(radha_krishna_url, caption="✨ Prem Ke Prateek - Radhe Radhe ✨", use_container_width=True)
