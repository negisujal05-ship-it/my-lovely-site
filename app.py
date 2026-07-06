import streamlit as str
import time
import random

# Page Setup
str.set_page_config(page_title="Our Cosmic Milky Way ❤️", page_icon="🌌", layout="centered")

# Page tracking system
if "page" not in str.session_state:
    str.session_state.page = 1

# --- GLOBAL STYLING ---
CSS_BASE_STYLE = """
<style>
.stApp {background: linear-gradient(135deg, #020105 0%, #050312 40%, #0b0518 80%, #11031c 100%); font-family: 'Georgia', serif; color: #ffffff;}
.stylish-box {background: rgba(5, 3, 12, 0.96); padding: 45px; border-radius: 25px; border: 2px solid #ffffff; text-align: center; margin-bottom: 30px;}
div.stButton > button {background: linear-gradient(90deg, #ffffff 0%, #e0e0e0 100%) !important; color: #050312 !important; font-weight: bold !important; border-radius: 50px !important; padding: 12px 35px !important; border: none !important; margin: 20px auto !important;}
</style>
"""
str.markdown(CSS_BASE_STYLE, unsafe_allow_html=True)

# --- PAGE LOGIC ---

# PAGE 5
if str.session_state.page == 5:
    str.markdown("<h1>Vikaro Se Mukti: Sacha Prem 🌌</h1>", unsafe_allow_html=True)
    str.markdown(''' 
        <div class="stylish-box"> 
            <h3>✨ Prem Se Vikaro Ka Naash ✨</h3> 
            <p>Jab jivan mein sachay aur pavitra prem ka agaman hota hai, toh mann ke saare vikar (vices) khud-ba-khud vileen ho jaate hain...</p> 
        </div> 
    ''', unsafe_allow_html=True)
    
    # Button to go to Page 6
    if str.button("Enter to Love World 💖"):
        str.session_state.page = 6
        str.rerun()

# PAGE 6 (Naya Page)
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

# (Agar aapka page 1-4 ka code pehle se hai, toh use iske upar rakhein)
