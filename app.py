import streamlit as st
import time

# Page Setup
st.set_page_config(page_title="A true Love ❤️", page_icon="🌌", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = 1

# --- CSS STYLING (Fixed) ---
st.markdown("""
<style>
    /* Global Styles */
    .stApp {
        background: radial-gradient(circle at center, #000814 0%, #001d3d 100%) !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Content Styling - Text ko white aur readable banaya gaya hai */
    h1, h2, h3, p, div {
        color: #ffffff !important;
    }

    .content-box {
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }

    /* Animation Layer (Fixing visibility) */
    .solar-system {
        position: fixed;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        z-index: -1; 
        opacity: 0.6;
    }
</style>
""", unsafe_allow_html=True)

# --- SOLAR SYSTEM ANIMATION ---
st.markdown("""
<div class="solar-system">
    <div style="width: 300px; height: 300px; border: 1px solid #ffffff33; border-radius: 50%;"></div>
</div>
""", unsafe_allow_html=True)

# --- PAGE LOGIC ---
if st.session_state.page == 1:
    st.markdown("<h1>For Someone Special... ✨❤️</h1>", unsafe_allow_html=True)
    st.markdown('<div class="content-box">Ye choti si jagah maine sirf aapke liye banayi hai.</div>', unsafe_allow_html=True)
    if st.button("Open My Heart 💖"):
        st.session_state.page = 2
        st.rerun()

elif st.session_state.page == 2:
    st.markdown("<h1>Our Cosmic Universe ✨</h1>", unsafe_allow_html=True)
    st.markdown('<div class="content-box">"Is anant aasmaan mein laakhon sitare hain, par hamare is chote se brahmand mein, sabsay haseen chamak aapki muskurahat ki hai."</div>', unsafe_allow_html=True)
    if st.button("Next Page ❤️"):
        st.session_state.page = 3
        st.rerun()

# ... (Yahan aap apne baaki pages ka content isi format mein likh sakte hain) ...

elif st.session_state.page == 8:
    st.markdown("<h1>A Heartfelt Thank You ❤️</h1>", unsafe_allow_html=True)
    st.markdown('<div class="content-box">"Aapke hone se, meri zindagi ab ek khoobsurat ibaadat si ho gayi."</div>', unsafe_allow_html=True)
    
    # Sirf last page par Back to Start
    if st.button("Back to Start 🔄"):
        st.session_state.page = 1
        st.rerun()
