import streamlit as str
import time

# Page Setup
str.set_page_config(page_title="A true Love ❤️", page_icon="🌌", layout="centered")

if "page" not in str.session_state:
    str.session_state.page = 1

# --- CSS STYLING ---
CSS_BASE_STYLE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

.stApp {
    background: radial-gradient(circle, #000814 0%, #001d3d 100%) !important;
    font-family: 'Poppins', sans-serif;
}

/* Text ko dark background par dark (white) karne ke liye */
h1, h2, h3, h4, p, div { 
    color: #FFFFFF !important; 
    font-weight: 500 !important;
}

.stylish-box { 
    background: rgba(255, 255, 255, 0.05); 
    padding: 30px; 
    border-radius: 20px; 
    border: 1px solid rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(15px);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
}

.vikar-box { 
    margin-bottom: 20px; 
    padding: 15px; 
    border-left: 5px solid #ff6b8b; 
    background: rgba(255, 255, 255, 0.08); 
}

/* Solar System Animation Fix */
.solar-system { 
    position: fixed; 
    top: 50%; left: 50%; 
    transform: translate(-50%, -50%); 
    z-index: 0; 
    pointer-events: none; 
}
</style>
"""
str.markdown(CSS_BASE_STYLE, unsafe_allow_html=True)

# --- PAGE LOGIC ---
# Page logic wahi rahega, bas button ka check last page ke liye add kiya hai
if str.session_state.page == 1:
    str.markdown("<h1>For Someone Special... ✨❤️</h1>", unsafe_allow_html=True)
    str.markdown('<div class="stylish-box">Ye choti si jagah maine sirf aapke liye banayi hai.</div>', unsafe_allow_html=True)
    if str.button("Open My Heart 💖"):
        str.session_state.page = 2
        str.rerun()

elif str.session_state.page == 8: # Last Page
    str.markdown("<h1>A Heartfelt Thank You ❤️</h1>", unsafe_allow_html=True)
    str.markdown('''
        <div class="stylish-box">
            <p style="font-size: 20px;">"Is chote se safar mein, aapke hone se, meri zindagi ab ek khoobsurat ibaadat si ho gayi."</p>
        </div>
    ''', unsafe_allow_html=True)
    
    # Sirf yahan 'Back to Start' button dikhega
    if str.button("Back to Start 🔄"):
        str.session_state.page = 1
        str.rerun()

# Baki pages yahan add karein...
