# my-lovely-site
import streamlit as str
import time

# Page configuration
str.set_page_config(page_title="A Special Message For You", page_icon="❤️", layout="centered")

# Custom CSS for a lovely look
str.markdown("""
    <style>
    .main { background-color: #fff0f5; }
    h1 { color: #ff4b4b; text-align: center; font-family: 'Helvetica Neue', sans-serif; }
    p { color: #4a4a4a; font-size: 18px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Title
str.title("Hey there! ✨")
str.write("Maine aapke liye ek chota sa surprise banaya hai. Neeche diye gaye button par click karein! 👇")

# Button interaction
if str.button("Click Me! ❤️"):
    with str.spinner("Kucch special load ho raha hai..."):
        time.sleep(1.5)
    
    str.balloons() # Screen par balloons urenge
    
    str.markdown("### 🥰 To Someone Special...")
    str.write("Aap hamesha sikhne aur naye cheezein try karne ke liye ready rehte ho, and that is amazing! ✨")
    str.write("Hope aapka din aaj ka bahut lovely aur badiya rahe! 🌸")
    
    # Image or GIF (Aap koi bhi achi URL yahan daal sakte hain)
    str.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3g1cXg1cXg1cXg1cXg1cXg1cXg1cXg1cXg1cXg1cXg1cXg1cXg1&ep=v1_gifs_search&rid=giphy.gif&ct=g", width=300)
