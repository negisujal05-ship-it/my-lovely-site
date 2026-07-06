import streamlit as st

st.set_page_config(
    page_title="Radhe Krishna Love Galaxy",
    page_icon="❤️",
    layout="wide"
)

if "entered" not in st.session_state:
    st.session_state.entered = False

if not st.session_state.entered:

    st.markdown("""
    <style>
    .stApp{
        background: radial-gradient(circle at center,
        #1a1a40,
        #0a0a20,
        #000000);
    }

    .welcome-box{
        text-align:center;
        margin-top:120px;
        color:white;
    }

    .title{
        font-size:70px;
        text-shadow:0 0 25px pink;
    }

    .subtitle{
        font-size:28px;
        color:#ffd6f5;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="welcome-box">
        <div class="title">❤️ Radhe Krishna ❤️</div>
        <br>
        <div class="subtitle">
            ✨ Welcome To The Lovely Galaxy Of Love ✨
        </div>
        <br><br>
        <h2>🌙 Where Love Meets The Stars 🌙</h2>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    col1,col2,col3 = st.columns([2,1,2])

    with col2:
        if st.button("💖 CLICK HERE TO ENTER 💖",
                     use_container_width=True):
            st.session_state.entered = True
            st.rerun()

else:

    st.markdown("""
    <style>
    .stApp{
        background:black;
        color:white;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("❤️ Radhe Krishna Galaxy ❤️")

    st.markdown("""
    ## 💕 Lovely Thoughts 💕

    * Saccha pyar kabhi dooriyon se kam nahi hota.
    * Jo dil mein rehta hai woh hamesha paas rehta hai.
    * Mohabbat dil se shuru hoti hai aur rooh tak pahunchti hai.

    ## 💞 Lovely Shayari 💞

    Teri yaadon ka sitara meri raaton mein chamakta hai,  
    Tera naam hi mere dil mein har pal dhadakta hai.

    Chand bhi feeka lagta hai teri muskaan ke saamne,  
    Mera har khwab bas tera hi chehra rakhta hai.
    """)
