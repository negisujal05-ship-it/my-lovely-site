import streamlit as str
import time
import random

# Page Setup
str.set_page_config(page_title="A true Love ❤️", page_icon="🌌", layout="centered")

if "page" not in str.session_state:
    str.session_state.page = 1

# --- CSS STYLING ---
CSS_BASE_STYLE = """
<style>
/* Background aur Animation Layering */
.stApp {
    background: radial-gradient(circle at center,#ffb347 0%,#ff8c00 5%,transparent 10%),
                radial-gradient(circle at 20% 30%,rgba(0,191,255,0.15),transparent 30%),
                radial-gradient(circle at 80% 70%,rgba(138,43,226,0.15),transparent 30%),
                linear-gradient(180deg,#000814,#001d3d,#000000) !important;
    color: #ffffff;
}

/* Layering Fixes */
.block-container {
    position: relative;
    z-index: 10;
}

.stylish-box {
    position: relative;
    z-index: 20;
    background: rgba(5, 3, 12, 0.85);
    padding: 40px;
    border-radius: 25px;
    border: 1px solid #ffffff;
}

/* Solar System Background */
.solar-system {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 700px;
    height: 700px;
    z-index: -1; 
    pointer-events: none;
}

/* Solar System Elements (Red Debug Mode Active) */
.sun {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 80px;
    height: 80px;
    background: red !important;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    box-shadow: 0 0 80px red;
}

.orbit {
    position: absolute;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 50%;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.orbit1 { width: 180px; height: 180px; animation: orbit 12s linear infinite; }
.orbit2 { width: 280px; height: 280px; animation: orbit 18s linear infinite; }
.orbit3 { width: 400px; height: 400px; animation: orbit 26s linear infinite; }
.orbit4 { width: 550px; height: 550px; animation: orbit 32s linear infinite; }

.planet { position: absolute; top: -10px; left: 50%; border-radius: 50%; }
.p1 { width: 12px; height: 12px; background: #00d4ff; box-shadow: 0 0 15px #00d4ff; }
.p2 { width: 16px; height: 16px; background: #ff6b6b; box-shadow: 0 0 15px #ff6b6b; }
.p3 { width: 20px; height: 20px; background: #8a2be2; box-shadow: 0 0 20px #8a2be2; }

@keyframes orbit { from { transform: translate(-50%,-50%) rotate(0deg); } to { transform: translate(-50%,-50%) rotate(360deg); } }
</style>
"""

str.markdown(CSS_BASE_STYLE, unsafe_allow_html=True)

# Solar System HTML
SOLAR_SYSTEM = """
<div class="solar-system">
    <div class="sun"></div>
    <div class="orbit orbit1"><div class="planet p1"></div></div>
    <div class="orbit orbit2"><div class="planet p2"></div></div>
    <div class="orbit orbit3"><div class="planet p3"></div></div>
    <div class="orbit orbit4"><div class="planet p3"></div></div>
</div>
"""
str.markdown(SOLAR_SYSTEM, unsafe_allow_html=True)

# Stars Generator
stars_html = ""
for i in range(150):
    stars_html += f"""
    <div style="
    position:fixed;
    left:{random.randint(0,100)}%;
    top:{random.randint(0,100)}%;
    color:white;
    font-size:{random.randint(6,16)}px;
    opacity:{random.uniform(0.3,1)};
    z-index:-1;
    pointer-events:none;
    ">
    ✦
    </div>
    """
str.markdown(stars_html, unsafe_allow_html=True)

# --- APP LOGIC ---
if str.session_state.page == 1:
    str.markdown("<h1>For Someone Special... ✨</h1>", unsafe_allow_html=True)
    str.markdown('<div class="stylish-box">Welcome to your Cosmic Journey... The Sun is glowing Red for debug mode!</div>', unsafe_allow_html=True)
    if str.button("Next Page"):
        str.session_state.page = 2
        str.rerun()

elif str.session_state.page == 2:
    str.markdown("<h1>Our Cosmic Universe ✨</h1>", unsafe_allow_html=True)
    str.markdown('<div class="stylish-box">Background is fixed with Z-Index layering.</div>', unsafe_allow_html=True)
    if str.button("Back"):
        str.session_state.page = 1
        str.rerun()
        # --- PAGE LOGIC ---

# PAGE 1
if str.session_state.page == 1:
    str.markdown("<h1>For Someone Special... ✨❤️</h1>", unsafe_allow_html=True)
    str.markdown('<div class="stylish-box">Ye choti si jagah maine sirf aapke liye banayi hai.</div>', unsafe_allow_html=True)
    if str.button("Open My Heart 💖"):
        str.session_state.page = 2
        str.rerun()

# PAGE 2
elif str.session_state.page == 2:
    str.markdown("<h1>Our Cosmic Universe ✨</h1>", unsafe_allow_html=True)
    str.markdown('<div class="stylish-box">"Aapka zindagi mein hona kisi tohfe se kam nahi."</div>', unsafe_allow_html=True)
    if str.button("Next Page ❤️"):
        str.session_state.page = 3
        str.rerun()

# PAGE 3
elif str.session_state.page == 3:
    str.markdown("<h1>The Eternal Love ✨🙏</h1>", unsafe_allow_html=True)
    str.markdown('<div class="stylish-box">"Radha Krishna ka prem sikhata hai ki rishtey aatma se judte hain."</div>', unsafe_allow_html=True)
    if str.button("Eternal Prem ✨"):
        str.session_state.page = 4
        str.rerun()

# PAGE 4
elif str.session_state.page == 4:
    str.markdown("<h1>The Ultimate Destination ❤️</h1>", unsafe_allow_html=True)
    str.markdown('<div class="stylish-box">"Sacha prem dil se mehsoos kiya jata hai."</div>', unsafe_allow_html=True)
    if str.button("Click for Mukti ✨"):
        str.session_state.page = 5
        str.rerun()

# PAGE 5
elif str.session_state.page == 5:
    str.markdown("<h1>Vikaro Se Mukti: Sacha Prem 🌌</h1>", unsafe_allow_html=True)
    str.markdown(''' 
        <div class="stylish-box"> 
            <h3>✨ Prem Se Vikaro Ka Naash ✨</h3> 
            <p>Jab jivan mein sacha prem hota hai, toh saare vikar vileen ho jaate hain.</p>
        </div> 
    ''', unsafe_allow_html=True)
    
    # Button to go to Page 6
    if str.button("Enter to Love World 💖"):
        str.session_state.page = 6
        str.rerun()

# PAGE 6 (Krishna Prem Definition)
elif str.session_state.page == 6:
    str.markdown("<h1>Krishna Prem: Param Satya ✨</h1>", unsafe_allow_html=True)
    str.markdown(''' 
        <div class="stylish-box"> 
            <h3>🌌 Bhagwan Krishna ka Prem Sandesh 🌌</h3> 
            <p style="font-size: 20px; line-height: 1.8; font-style: italic;"> 
                "Prem ka arth hai 'Samarpan'. Krishna ke anusar, prem wahi hai jisme koi maang nahi hoti.<br><br>
                Jab hum dusro ki khushi mein apni khushi dhoondhte hain, wahi ishwar ka swaroop hai.<br>
                Prem bandhan nahi, balki aatma ki mukti hai. Jab tum khud ko bhool kar keval priya ke liye jeete ho, 
                tab tumhare bhitar 'Main' mit jata hai aur 'Krishna' ka prem jag uthta hai." 
            </p> 
        </div> 
    ''', unsafe_allow_html=True)
    
    if str.button("Go to Start 🔄"):
        str.session_state.page = 1
        str.rerun()
        # --- PAGE 7 ---
elif str.session_state.page == 7:
    apply_slow_cosmic_animation()
    str.markdown("<h1>Sudh Prem Ki Pribhasha 🌌</h1>", unsafe_allow_html=True)
    
    str.markdown('''
        <div class="stylish-box">
            <div class="image-watermark"></div>
            <div class="watermark" style="font-size:50px;">PURE</div>
            <div class="box-content">
                <h3 style="color: #ff6b8b; font-size: 28px; margin-bottom: 20px;">✨ Nishwarth Prem ✨</h3>
                <p style="font-size: 20px; color: #ffffff; line-height: 1.8; font-weight: bold; font-style: italic;">
                    "Prem wo hai jo nishwarth bhaw se aatma se ho, na ki sharir se."
                </p>
                <p style="font-size: 18px; color: #e8e8e8; margin-top: 20px;">
                    Sacha prem wahi hai jahan koi shart na ho, koi maang na ho, bas ek dusre ki aatma ka samman ho.
                </p>
            </div>
        </div>
    ''', unsafe_allow_html=True)
    
    # Updated button for Page 8
    if str.button("Final Page for You ✨", use_container_width=True):
        str.session_state.page = 8
        str.rerun()

# --- PAGE 8 (Final Page) ---
elif str.session_state.page == 8:
    apply_slow_cosmic_animation()
    str.markdown("<h1>A Heartfelt Thank You ❤️</h1>", unsafe_allow_html=True)
    
    str.markdown('''
        <div class="stylish-box" style="border: 2px solid #ff6b8b;">
            <div class="image-watermark"></div>
            <div class="watermark" style="font-size:50px; color: rgba(255,107,139,0.05);">THANKS</div>
            <div class="box-content">
                <h3 style="color: #ff6b8b; font-size: 32px; margin-bottom: 20px;">🌹 Ek Pyari Si Shayari 🌹</h3>
                <p style="font-size: 20px; color: #ffffff; line-height: 1.8; font-style: italic; margin-bottom: 30px;">
                    "Na jaane kab aapki aadat si ho gayi,<br>
                    Aapki har baat mein barkat si ho gayi.<br>
                    Is chote se safar mein, aapke hone se,<br>
                    Meri zindagi ab ek khoobsurat ibaadat si ho gayi."
                </p>
                <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.2);">
                <h4 style="color: #ffffff; font-size: 22px; margin-top: 20px;">✨ Special Thanks to Visit My Site ✨</h4>
                <p style="font-size: 16px; color: #cccccc;">Aapka yahan aana mere liye kisi vardaan se kam nahi.</p>
            </div>
        </div>
    ''', unsafe_allow_html=True)
    
    if str.button("Back to Start 🔄", use_container_width=True):
        str.session_state.page = 1
        str.rerun()
