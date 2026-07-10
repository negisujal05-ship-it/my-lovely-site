import streamlit as st
import time
import random

# Page Setup
st.set_page_config(page_title="A true Love ❤️", page_icon="🌌", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = 1

# --- CSS STYLING ---
CSS_BASE_STYLE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap');

html, body, [class*="css"]{
    font-family:'Cinzel', serif;
}

h1{
    color:#ffffff !important;
    text-shadow:
        0 0 10px rgba(255,255,255,0.8),
        0 0 20px rgba(255,255,255,0.6);
    font-weight:700;
}

/* Background aur Animation Layering */
.stApp {
    background:
    radial-gradient(circle at 20% 20%, rgba(0,191,255,0.2), transparent 30%),
    radial-gradient(circle at 80% 70%, rgba(138,43,226,0.2), transparent 30%),
    linear-gradient(180deg,#000814,#001d3d,#000000) !important;

    min-height: 100vh;
    width: 100%;
     overflow-x: hidden;
     overflow-y: auto;
    }

/* Mobile Responsive */
@media screen and (max-width: 768px) {

    .stApp {
        min-height: 100vh;
        background-attachment: scroll;
    }

    img {
        max-width: 100% !important;
        height: auto !important;
        object-fit: contain !important;
    }

    .main {
        padding-left: 10px !important;
        padding-right: 10px !important;
    }
}

/* Snow Effect */
.snowflake{
    position:fixed;
    top:-20px;
    color:white;
    pointer-events:none;
    z-index:-1;
    animation:fall linear infinite;
}

@keyframes fall{
    0%{ transform:translateY(-50px); opacity:0; }
    10%{ opacity:1; }
    100%{ transform:translateY(110vh); opacity:0; }
}

/* Solar System Container */
.solar-system {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width:1200px;
    height:1200px;
    z-index: -1;
    pointer-events: none;
}

.sun {
    position: absolute;
    top: 50%; left: 50%;
    width: 80px; height: 80px;
    background: #ffd700;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    box-shadow: 0 0 80px #ffd700;
}

.orbit { position: absolute; border: 1px solid rgba(255,255,255,0.1); border-radius: 50%; top: 50%; left: 50%; transform: translate(-50%, -50%); }
.orbit1 { width: 180px; height: 180px; animation: orbit 12s linear infinite; }
.orbit2 { width: 280px; height: 280px; animation: orbit 18s linear infinite; }
.orbit3 { width: 400px; height: 400px; animation: orbit 26s linear infinite; }
.orbit4 { width: 550px; height: 550px; animation: orbit 32s linear infinite; }
.orbit5{ width:650px; height:650px; animation:orbit 40s linear infinite; }
.orbit6{ width:760px; height:760px; animation:orbit 48s linear infinite; }
.orbit7{ width:880px; height:880px; animation:orbit 58s linear infinite; }
.orbit8{ width:1000px; height:1000px; animation:orbit 70s linear infinite; }

.p6::after{
    content:'';
    position:absolute;
    width:40px;
    height:8px;
    border:2px solid rgba(255,255,255,.6);
    border-radius:50%;
    top:10px;
    left:-6px;
}

.planet { position: absolute; top: -10px; left: 50%; border-radius: 50%; transform: translateX(-50%); }
.p1 { width: 12px; height: 12px; background: #00d4ff; box-shadow: 0 0 10px #00d4ff; }
.p2 { width: 16px; height: 16px; background: #ff6b6b; box-shadow: 0 0 10px #ff6b6b; }
.p3 { width: 20px; height: 20px; background: #8a2be2; box-shadow: 0 0 10px #8a2be2; }
.p5{ width:30px; height:30px; background:#d2b48c; box-shadow:0 0 15px #d2b48c; }
.p6{ width:28px; height:28px; background:#f4e2d8; box-shadow:0 0 15px #f4e2d8; }
.p7{ width:24px; height:24px; background:#87ceeb; box-shadow:0 0 15px #87ceeb; }
.p8{ width:22px; height:22px; background:#4169e1; box-shadow:0 0 15px #4169e1; }

@keyframes orbit { from { transform: translate(-50%,-50%) rotate(0deg); } to { transform: translate(-50%,-50%) rotate(360deg); } }

/* UI Box */
.block-container { z-index: 10 !important; }

/* Single combined box: background photo (darkened) + text on top */
.stylish-box{
    position:relative;
    overflow:hidden;
    min-height:420px;
    background: rgba(0,0,0,0.55);
    padding: 30px;
    border-radius: 25px;
    border: 1px solid rgba(255,255,255,0.15);
    color: white !important;
    box-shadow: 0 0 25px rgba(0,191,255,0.15);
}

/* the photo itself, filling the box, lightly darkened via filter */
/* !important used to override Streamlit's default <img> styling (which adds
   its own border-radius, box-shadow, and max-width) that was shrinking the photo
   into a smaller rounded rectangle instead of filling the whole box. */
.stylish-bg{
    position:absolute !important;
    top:0 !important;
    left:0 !important;
    width:100% !important;
    height:100% !important;
    max-width:100% !important;
    object-fit:cover !important;
    object-position:center !important;
    image-rendering:auto;
    filter:brightness(0.6) saturate(1.1);
    z-index:0;
    margin:0 !important;
    padding:0 !important;
    border:none !important;
    border-radius:0 !important;
    box-shadow:none !important;
    opacity:0;
    animation: photoFadeIn 0.9s ease forwards;
    animation-delay:0.1s;
}

@keyframes photoFadeIn{
    from{ opacity:0; }
    to{ opacity:0.9; }
}

/* light dark overlay - photo stays visible, just enough to help contrast */
.stylish-overlay{
    position:absolute;
    top:0; left:0;
    width:100%;
    height:100%;
    background: rgba(0,0,0,0.3);
    z-index:1;
}

/* actual text/content sits above the photo + overlay; text-shadow keeps it readable over the visible photo */
.box-content{
    position:relative;
    z-index:2;
}

.box-content h1, .box-content h2, .box-content h3, .box-content h4,
.box-content p, .box-content .watermark{
    text-shadow:
        0 2px 6px rgba(0,0,0,0.9),
        0 0 12px rgba(0,0,0,0.7);
}

.vikar-box { position:relative; z-index:2; margin-bottom: 15px; padding: 10px; border-left: 3px solid #ff6b8b; background: rgba(255,255,255,0.08); }

h1,h2,h3,h4{
    color:#ffffff !important;
    text-shadow:
        0 0 10px rgba(255,255,255,0.8),
        0 0 20px rgba(255,255,255,0.6);
    font-weight:700;
}
</style>
"""
st.markdown(CSS_BASE_STYLE, unsafe_allow_html=True)


def styled_box(image_path, inner_html, box_style=""):
    """
    One combined box: darkened background photo + overlay + text/content on top.
    NOTE: HTML must NOT be indented with 4+ spaces after a blank line,
    otherwise Streamlit/Markdown treats it as a code block and shows raw text.
    NOTE 2: Streamlit strips inline JS event handlers (onload, onclick, etc.)
    even with unsafe_allow_html=True, so the fade-in is done with a pure
    CSS animation (see .stylish-bg in CSS_BASE_STYLE) instead of JS.
    """
    image_url = f"https://raw.githubusercontent.com/negisujal05-ship-it/my-lovely-site/main/{image_path}"
    html = f"""<div class="stylish-box" style="{box_style}">
<img src="{image_url}" class="stylish-bg" loading="eager" fetchpriority="high">
<div class="stylish-overlay"></div>
<div class="box-content">
{inner_html}
</div>
</div>"""
    st.markdown(html, unsafe_allow_html=True)


# --- SNOW + HEARTS + ROSES FALLING EFFECT ---
falling_items = ""

# Snowflakes - more of them, falling slower
for i in range(35):
    falling_items += f"""<div style="position:fixed;left:{random.randint(0,100)}%;top:-20px;color:white;font-size:{random.randint(10,18)}px;animation: fall {random.randint(20,40)}s linear infinite;animation-delay:-{random.randint(0,40)}s;z-index:-1;">❄</div>"""

# Red hearts - falling slowly
for i in range(12):
    falling_items += f"""<div style="position:fixed;left:{random.randint(0,100)}%;top:-20px;color:#ff2d55;font-size:{random.randint(14,24)}px;animation: fall {random.randint(25,45)}s linear infinite;animation-delay:-{random.randint(0,45)}s;z-index:-1;text-shadow:0 0 8px rgba(255,45,85,0.7);">❤</div>"""

# Roses - falling slowly
for i in range(8):
    falling_items += f"""<div style="position:fixed;left:{random.randint(0,100)}%;top:-20px;font-size:{random.randint(16,26)}px;animation: fall {random.randint(28,50)}s linear infinite;animation-delay:-{random.randint(0,50)}s;z-index:-1;">🌹</div>"""

st.markdown(falling_items, unsafe_allow_html=True)

# --- SOLAR SYSTEM HTML ---
st.markdown("""<div class="solar-system">
<div class="sun"></div>
<div class="orbit orbit1"><div class="planet p1"></div></div>
<div class="orbit orbit2"><div class="planet p2"></div></div>
<div class="orbit orbit3"><div class="planet p3"></div></div>
<div class="orbit orbit4"><div class="planet p2"></div></div>
<div class="orbit orbit5"><div class="planet p5"></div></div>
<div class="orbit orbit6"><div class="planet p6"></div></div>
<div class="orbit orbit7"><div class="planet p7"></div></div>
<div class="orbit orbit8"><div class="planet p8"></div></div>
</div>""", unsafe_allow_html=True)


# --- PAGE LOGIC ---
def apply_slow_cosmic_animation():
    stars = ""
    for i in range(40):
        stars += f"""<div style="position:fixed;left:{random.randint(0,100)}%;top:{random.randint(0,100)}%;color:white;font-size:{random.randint(6,16)}px;opacity:{random.uniform(0.3,1)};z-index:-1;">✦</div>"""
    st.markdown(stars, unsafe_allow_html=True)


if st.session_state.page == 1:
    st.markdown("<h1 style='color:white;text-align:center;'>For Someone Special... ✨❤️</h1>", unsafe_allow_html=True)

    styled_box(
        "images/page1.JPG",
        """<h2>✨ For Someone Special ✨</h2>
<p>Ye choti si jagah maine sirf aapke liye banayi hai. 💖</p>"""
    )
    if st.button("🌌 Enter My Universe ✨"):
        st.session_state.page = 2
        st.rerun()

# --- PAGE 2 ---
elif st.session_state.page == 2:
    apply_slow_cosmic_animation()
    st.markdown("<h1>Our Cosmic Universe ✨</h1>", unsafe_allow_html=True)

    styled_box(
        "images/page2.JPG",
        """<div class="watermark">FOREVER</div>
<h2 style="color: #ffffff; font-size: 38px; margin-bottom: 20px;">Dear Special Someone, 🌸</h2>
<p style="font-size: 20px; color: #fdfdfd; line-height: 1.8; font-style: italic;">
"Is anant aasmaan mein laakhon sitare hain,<br>par hamare is chote se brahmand mein,<br>sabsay haseen aur pyari chamak aapki muskurahat ki hai.<br><br>Aapka zindagi mein hona kisi tohfe se kam nahi,<br>aap har pal ko khubsurat aur sukoon se bhar dete ho.
</p>"""
    )

    if st.button("Next Page ❤️", use_container_width=True):
        with st.spinner("Transitioning Through Space..."):
            time.sleep(1.0)
        st.session_state.page = 3
        st.rerun()

# --- PAGE 3 ---
elif st.session_state.page == 3:
    apply_slow_cosmic_animation()
    st.markdown("<h1>The Eternal Love ✨🙏</h1>", unsafe_allow_html=True)
    styled_box(
        "images/page3.JPG",
        """<div class="watermark">RADHE RADHE</div>
<h3 style="color: #ff6b8b; font-size: 28px; margin-bottom: 15px;">✨ Radhe Radhe - Shaswat Prem ✨</h3>
<p style="font-size: 19px; color: #e8e8e8; line-height: 1.8; font-style: italic;">
"Prem ka matlab ek dusre ko paana nahi,<br>balki ek dusre mein poori tarah kho jaana hai.<br><br>Radha Krishna ka prem sikhata hai ki rishtey aatma se judte hain,<br>jahan dooriyan bhi dono ko alag nahi kar saktin.<br>Aapki zindagi bhi isi pavitra prem aur sukoon se hamesha mehakti rahe.
</p>"""
    )

    if st.button("Eternal Prem ✨", use_container_width=True):
        with st.spinner("Transitioning Through Space..."):
            time.sleep(1.0)
        st.session_state.page = 4
        st.rerun()

# --- PAGE 4 ---
elif st.session_state.page == 4:
    apply_slow_cosmic_animation()
    st.markdown("<h1>The Ultimate Destination ❤️</h1>", unsafe_allow_html=True)
    styled_box(
        "images/page4.JPG",
        """<div class="watermark">ETERNAL</div>
<h3 style="color: #ffffff; font-size: 28px; margin-bottom: 15px;">🌌 Sacha Prem Hi Brahmand Hai 🌌</h3>
<p style="font-size: 19px; color: #e8e8e8; line-height: 1.8; font-style: italic;">
"Prem wo nahi jo kuch samay ke liye ho,<br>prem toh wo hai jo sadiyon tak rooh mein bas jaye.<br><br>Aapki is yatra ka aakhri padaav yahi sikhata hai ki<br>duniya ki sabsay khoobsoorat cheez ko na dekha ja sakta hai, <br>na chhua ja sakta hai... use sirf dil se mehsoos kiya jata hai.
</p>"""
    )

    if st.button("Step away from the world: Enter the eternal life of God ✨", use_container_width=True):
        with st.spinner("Transitioning Through Space..."):
            time.sleep(1.0)
        st.session_state.page = 5
        st.rerun()

# --- PAGE 5 ---
elif st.session_state.page == 5:
    apply_slow_cosmic_animation()
    st.markdown("<h1>Vikaro Se Mukti: Sacha Prem 🌌</h1>", unsafe_allow_html=True)
    vikar_items = [
        ("1. डर (Bhay)", "Fear", "Sacha prem har tarah ke darr ko mita deta hai. Jab aap kisi se nishwarth prem karte hain, toh khone ka ya zamane ka koi bhay nahi rehta, kyunki prem aatma ko nirbhay (fearless) bana deta hai."),
        ("2. मोह (Moh)", "Attachment", "Moh insaan ko bandhan mein baandhta hai aur swarthi banata hai, jisse sacha prem azaad karna sikhata hai. Prem mein 'paane' ki zidd nahi, balki samarpit hone ka sukoon hota hai."),
        ("3. क्रोध (Krodh)", "Anger", "Krodh mann ki agni hai jo sab kuch jala deti hai. Par jahan sacha prem hota hai, wahan krodh ke liye koi jagah nahi hoti; prem us agni par kshama (forgiveness) aur shanti ka thanda jal chhidak deta hai."),
        ("4. ईर्ष्या (Irshya)", "Zero Jealousy", "Irshya tab paida hoti hai jab hum doosron se tulna karte hain. Sacha prem hume doosron ki khushi mein apni khushi dekhna sikhata hai, jisse jalan poori tarah se mit jaati hai."),
        ("5. अहंकार (Ahankar)", "Ego", "Ahankar kehta hai 'Main sabsay upar hoon', lekin prem kehta hai 'Main toh kuch bhi nahi'. Prem mein 'Main' (Ego) mit jata hai aur sirf 'Hum' baaki reh jata hai. Sacha prem ahankar ko poori tarah shunya kar deta hai."),
    ]
    vikar_html = ""
    for heading, eng, desc in vikar_items:
        vikar_html += f"""<div class="vikar-box">
<h4 style="color: #ffffff; margin: 0 0 8px 0; font-size: 20px;">{heading} — <span style="color: #ffb3c1;">{eng}</span></h4>
<p style="color: #dfdfdf; font-size: 16px; margin: 0; line-height: 1.5;">{desc}</p>
</div>"""

    styled_box(
        "images/page5.JPG",
        f"""<div class="watermark" style="font-size:55px;">MUKTI</div>
<h3 style="color: #ff6b8b; font-size: 30px; margin-bottom: 25px;">✨ Prem Se Vikaro Ka Naash ✨</h3>
<p style="font-size: 18px; color: #e0e0e0; font-style: italic; margin-bottom: 30px;">"Jab jivan mein sachay aur pavitra prem ka agaman hota hai, toh mann ke saare vikar (vices) khud-ba-khud vileen ho jaate hain..."</p>
{vikar_html}
<p style="font-size: 16px; color: #ff6b8b; font-weight: bold; text-align: center; margin-top: 25px;">✨ Jo Prem Ko Chunta Hai, Wo Saare Vikaro Se Mukt Ho Jata Hai ✨</p>"""
    )

    if st.button("Enter to Love World 💖"):
        st.session_state.page = 6
        st.rerun()

# --- PAGE 6 (Krishna Prem Definition) ---
elif st.session_state.page == 6:
    st.markdown("<h1>Krishna Prem: Param Satya ✨</h1>", unsafe_allow_html=True)
    styled_box(
        "images/page6.JPG",
        """<h3>🌌 Bhagwan Krishna ka Prem Sandesh 🌌</h3>
<p style="font-size: 20px; line-height: 1.8; font-style: italic;">
"Prem ka arth hai 'Samarpan'. Krishna ke anusar, prem wahi hai jisme koi maang nahi hoti.<br><br>
Jab hum dusro ki khushi mein apni khushi dhoondhte hain, wahi ishwar ka swaroop hai.<br>
Prem bandhan nahi, balki aatma ki mukti hai. Jab tum khud ko bhool kar keval prem ke liye jeete ho,
tab tumhare bhitar 'Main' mit jata hai aur 'Krishna' ka prem jag uthta hai."
</p>"""
    )

    if st.button("Definition of Pure Love ✨", use_container_width=True):
        st.session_state.page = 7
        st.rerun()

# --- PAGE 7 ---
elif st.session_state.page == 7:
    apply_slow_cosmic_animation()
    st.markdown("<h1>Sudh Prem Ki Pribhasha 🌌</h1>", unsafe_allow_html=True)
    styled_box(
        "images/page7.JPG",
        """<div class="watermark" style="font-size:50px;">PURE</div>
<h3 style="color: #ff6b8b; font-size: 28px; margin-bottom: 20px;">✨ Nishwarth Prem ✨</h3>
<p style="font-size: 20px; color: #ffffff; line-height: 1.8; font-weight: bold; font-style: italic;">
"Prem wo hai jo nishwarth bhaw se aatma se ho, na ki sharir se.
Yeh koi vyakti nahi, ek sthiti hai. Jab aap apni khushi ko doosre ki muskurahat
mein dhundne lagte hain, wahi prem hai.<br><br>"
</p>
<p style="font-size: 18px; color: #e8e8e8; margin-top: 20px;">
Sacha prem wahi hai jahan koi shart na ho, koi maang na ho, bas ek dusre ki aatma ka samman ho.
</p>"""
    )

    if st.button("Final Page for You ✨", use_container_width=True):
        st.session_state.page = 8
        st.rerun()

# --- PAGE 8 (Final Page) ---
elif st.session_state.page == 8:
    apply_slow_cosmic_animation()

    st.markdown(
        "<h1>A Heartfelt Thank You ❤️</h1>",
        unsafe_allow_html=True
    )

    styled_box(
        "images/page8.JPG",
        """
        <div style="
        text-align:center;
        color:white;
        font-size:90px;
        font-weight:900;
        opacity:0.5;
        letter-spacing:8px;
        margin-bottom:30px;">
        THANKS
        </div>

        <h3 style="color: #ff6b8b; font-size: 32px; margin-bottom: 20px;">
        🌹 Ek Pyari Si Shayari 🌹
        </h3>

        <p style="font-size: 20px; color: #ffffff; line-height: 1.8; font-style: italic; margin-bottom: 30px;">
        "Na jaane kab aapki aadat si ho gayi,<br>
        Aapki har baat mein barkat si ho gayi.<br>
        Is chote se safar mein, aapke hone se,<br>
        Meri zindagi ab ek khoobsurat ibaadat si ho gayi."
        </p>

        <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.2);">

        <h4 style="color: #ffffff; font-size: 22px; margin-top: 20px;">
        ✨ Special Thanks to Visit My Site ✨
        </h4>

        <p style="font-size: 16px; color: #cccccc;">
        Aapka yahan aana mere liye kisi vardaan se kam nahi.
        </p>
        """,
        box_style="border: 2px solid #ff6b8b;"
    )

    if st.button("Back to Start 🔄", use_container_width=True):
        st.session_state.page = 1
        st.rerun()
