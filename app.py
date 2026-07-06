import streamlit as str
import time

# Page Setup
str.set_page_config(page_title="Our Cosmic Milky Way ❤️", page_icon="🌌", layout="centered")

# Page tracking system
if "page" not in str.session_state:
    str.session_state.page = 1

# --- STYLING ---
CSS_STYLE = """
<style>
.stApp {background: linear-gradient(135deg, #020105 0%, #050312 40%, #0b0518 80%, #11031c 100%); color: #ffffff; font-family: 'Georgia', serif;}
.stylish-box {background: rgba(255, 255, 255, 0.05); padding: 40px; border-radius: 25px; border: 1px solid #ffffff; text-align: center;}
div.stButton > button {background: #ffffff !important; color: #000000 !important; font-weight: bold !important; border-radius: 50px !important; padding: 10px 30px !important; border: none !important;}
</style>
"""
str.markdown(CSS_STYLE, unsafe_allow_html=True)

# --- PAGE LOGIC ---

# PAGE 1 se 4 (Aapka pehle ka content)
if str.session_state.page <= 4:
    str.title(f"Hamari Kahani - Page {str.session_state.page}")
    str.write("Yahan aapka pehle ka content hai...")
    if str.button("Next Page"):
        str.session_state.page += 1
        str.rerun()

# PAGE 5
elif str.session_state.page == 5:
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
