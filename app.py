import streamlit as str
import time
import random

# Page Setup
str.set_page_config(page_title="Our Cosmic Milky Way ❤️", page_icon="🌌", layout="centered")

if "page" not in str.session_state:
    str.session_state.page = 1

# --- STYLING ---
CSS_BASE_STYLE = """
<style>
.stApp {background: linear-gradient(135deg, #020105 0%, #050312 40%, #0b0518 80%, #11031c 100%); font-family: 'Georgia', serif; color: #ffffff;}
.stylish-box {background: rgba(5, 3, 12, 0.96); padding: 45px 35px; border-radius: 25px; border: 2px solid #ffffff; text-align: center; margin-bottom: 30px;}
.vikar-box {background: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 15px; margin-bottom: 20px; text-align: left; border: 1px solid rgba(255,255,255,0.1);}
div.stButton > button {background: linear-gradient(90deg, #ffffff 0%, #e0e0e0 100%) !important; color: #000000 !important; font-weight: bold !important; border-radius: 50px !important; padding: 12px 35px !important; border: none !important; margin: 20px auto !important;}
</style>
"""
str.markdown(CSS_BASE_STYLE, unsafe_allow_html=True)

# --- PAGE LOGIC ---

# PAGE 1-4 (Placeholder for your previous content)
if str.session_state.page <= 4:
    str.title(f"Page {str.session_state.page}")
    if str.button("Next Page"):
        str.session_state.page += 1
        str.rerun()

# PAGE 5: VIKAR DEFINITIONS
elif str.session_state.page == 5:
    str.markdown("<h1>Vikaro Se Mukti: Sacha Prem 🌌</h1>", unsafe_allow_html=True)
    str.markdown(''' 
        <div class="stylish-box"> 
            <h3>✨ Prem Se Vikaro Ka Naash ✨</h3> 
            <p>Jab jivan mein sacha prem hota hai, toh mann ke ye paanch vikar khud-ba-khud vileen ho jaate hain:</p>
        </div> 
    ''', unsafe_allow_html=True)
    
    str.markdown('<div class="vikar-box"><h4>1. डर (Bhay/Fear)</h4><p>Prem aatma ko nirbhay banata hai. Sacha prem khone ka darr mita deta hai.</p></div>', unsafe_allow_html=True)
    str.markdown('<div class="vikar-box"><h4>2. मोह (Moh/Attachment)</h4><p>Moh bandhan hai, jabki prem azaadi hai. Prem mein swarth nahi, samarpana hota hai.</p></div>', unsafe_allow_html=True)
    str.markdown('<div class="vikar-box"><h4>3. क्रोध (Krodh/Anger)</h4><p>Prem ki shanti krodh ki agni ko shaant kar deti hai.</p></div>', unsafe_allow_html=True)
    str.markdown('<div class="vikar-box"><h4>4. ईर्ष्या (Irshya/Jealousy)</h4><p>Sacha prem dusro ki khushi mein apni khushi dekhna sikhata hai.</p></div>', unsafe_allow_html=True)
    str.markdown('<div class="vikar-box"><h4>5. अहंकार (Ahankar/Ego)</h4><p>Prem mein "Main" mit kar sirf "Hum" ya "Woh" reh jata hai.</p></div>', unsafe_allow_html=True)
    
    # Button to go to Page 6
    if str.button("Enter to Love World 💖"):
        str.session_state.page = 6
        str.rerun()

# PAGE 6: KRISHNA PREM DEFINITION
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
