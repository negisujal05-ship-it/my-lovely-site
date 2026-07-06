import streamlit as st

st.set_page_config(
    page_title="❤️ Radhe Krishna Galaxy ❤️",
    page_icon="🌙",
    layout="wide"
)

html_code = """
<div style="
text-align:center;
color:white;
padding:20px;
font-family:Georgia, serif;
">

<h1 style="font-size:55px;">❤️ Radhe Radhe ❤️</h1>

<h3>🌙 Chand ki roshni mein, ✨ sitaron ki mehfil saji hai...</h3>

<p style="font-size:22px; max-width:900px; margin:auto;">
💖 Har dhadkan mein tera naam hai,
🦚 aur har saans mein Radha Krishna ka pyar basa hai.
</p>

<br>

<h2>💕 Lovely Thoughts 💕</h2>

<p style="font-size:20px;">
• Saccha pyar kabhi dooriyon se kam nahi hota.<br>
• Jo dil mein rehta hai, woh hamesha paas rehta hai.<br>
• Pyar ki sabse khoobsurat baat hai ki woh dil ko sukoon deta hai.<br>
• Har muskurahat ke peeche kisi khaas ki yaad hoti hai.<br>
• Mohabbat ek dua hai jo dil se nikalti hai aur rooh tak pahunchti hai.
</p>

<br>

<h2>💞 Lovely Shayari 💞</h2>

<p style="font-size:22px; line-height:1.8;">
Teri yaadon ka sitara meri raaton mein chamakta hai,<br>
Tera naam hi mere dil mein har pal dhadakta hai.<br><br>

Chand bhi feeka lagta hai teri muskaan ke saamne,<br>
Mera har khwab bas tera hi chehra rakhta hai.
</p>

<br>

<h2>✨ Radha Krishna ki kripa aur prem sada tumhare jeevan mein bana rahe. ✨</h2>

</div>
"""

st.markdown(
    """
    <style>
    .stApp{
        background: linear-gradient(
            180deg,
            #050816,
            #0b1026,
            #140f3a,
            #000000
        );
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(html_code, unsafe_allow_html=True)
