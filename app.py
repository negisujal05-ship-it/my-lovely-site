import streamlit as str
import time
import random

# Page Setup
str.set_page_config(page_title="Our Cosmic Milky Way ❤️", page_icon="🌌", layout="centered")

# Page tracking system
if "page" not in str.session_state:
    str.session_state.page = 1

# --- GLOBAL STYLING (PURE PYTHON STRINGS) ---
CSS_BASE_STYLE = """
<style>
/* Main App Transparency to show the Background Galaxy Canvas */
.stApp {
    background: transparent;
    font-family: 'Georgia', serif;
    color: #ffffff;
}
h1 {
    color: #ffffff;
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    text-shadow: 0 0 20px rgba(255, 255, 255, 0.9), 0 0 40px rgba(255, 107, 139, 0.5);
    margin-top: 30px;
    margin-bottom: 20px;
}
/* Premium Glowing Cosmic Box */
.stylish-box {
    background: linear-gradient(145deg, rgba(15, 8, 38, 0.9) 0%, rgba(5, 3, 15, 0.95) 100%);
    border: 2px solid rgba(255, 255, 255, 0.8);
    box-shadow: 0 0 25px rgba(255, 255, 255, 0.25), inset 0 0 15px rgba(255, 255, 255, 0.1);
    padding: 35px;
    border-radius: 25px;
    text-align: center;
    margin-bottom: 25px;
    backdrop-filter: blur(10px);
}
/* Sub-boxes inside Page 5 for Vikars */
.vikar-box {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.3);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    text-align: left;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}
/* Premium Round Buttons */
div.stButton > button {
    background: linear-gradient(90deg, #ffffff 0%, #e0e0e0 100%) !important;
    color: #050312 !important;
    font-size: 18px !important;
    font-weight: bold !important;
    border-radius: 50px !important;
    padding: 12px 35px !important;
    border: none !important;
    box-shadow: 0 0 20px rgba(255, 255, 255, 0.5) !important;
    transition: all 0.3s ease !important;
    display: block;
    margin: 0 auto !important;
}
div.stButton > button:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 0 35px rgba(255, 255, 255, 0.9) !important;
}
</style>
"""

str.markdown(CSS_BASE_STYLE, unsafe_allow_html=True)

# --- PURE PYTHON GALAXY ENGINE AND ANIMATOR ---
def render_brahmand_galaxy_view():
    cosmic_symbols = ["💧", "❄️", "❤️", "💖", "💘"]
    canvas_html = []
    
    # Building the moving universe background & falling nodes
    canvas_html.append("""
    <style>
    :root { color-scheme: dark; }
    body, html {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
        background: radial-gradient(circle at 50% 50%, #0c051f 0%, #05020a 70%, #010003 100%);
    }
    /* Infinite Dynamic Moving Galaxy (Deep Space View) */
    .galaxy-stars {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: 
            radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
            radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 30px),
            radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 40px);
        background-size: 550px 550px, 350px 350px, 250px 250px;
        background-position: 0 0, 40px 60px, 130px 270px;
        animation: galaxyOrbit 120s linear infinite;
        opacity: 0.6;
        z-index: -2;
    }
    @keyframes galaxyOrbit {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    /* Nebula Cosmic Glow Dust */
    .nebula-glow {
        position: fixed;
        top: -50%; left: -50%; width: 200%; height: 200%;
        background: radial-gradient(circle at 30% 40%, rgba(80, 20, 120, 0.25) 0%, transparent 40%),
                    radial-gradient(circle at 70% 60%, rgba(20, 50, 100, 0.25) 0%, transparent 40%);
        animation: nebulaShift 30s ease-in-out infinite alternate;
        z-index: -3;
    }
    @keyframes nebulaShift {
        0% { transform: translate(0, 0) scale(1); }
        100% { transform: translate(5%, 5%) scale(1.1); }
    }
    /* Falling Space Nodes Control */
    .cosmic-node {
        position: fixed;
        top: -15%;
        z-index: -1;
        pointer-events: none;
        animation: deepFall linear infinite;
    }
    @keyframes deepFall {
        0% { top: -15%; transform: translateX(0) rotate(0deg); opacity: 0; }
        10% { opacity: 0.8; }
        90% { opacity: 0.8; }
        100% { top: 115%; transform: translateX(60px) rotate(60deg); opacity: 0; }
    }
    </style>
    <div class="nebula-glow"></div>
    <div class="galaxy-stars"></div>
    """)
    
    # Injecting 45 floating symbols dynamically using python execution
    for i in range(45):
        sym = random.choice(cosmic_symbols)
        x_coordinate = random.randint(1, 99)
        slow_pacing = random.uniform(12.0, 18.0)  # Very smooth and slow
        delay_stagger = random.uniform(0.0, 8.0)
        size_pixels = random.randint(16, 26)
        
        glow = "rgba(255, 75, 75, 0.8)" if sym in ["❤️", "💖", "💘"] else "rgba(255, 255, 255, 0.6)"
        
        node_div = (
            f'<div class="cosmic-node" style="left: {x_coordinate}%; '
            f'animation-duration: {slow_pacing}s; '
            f'animation-delay: {delay_stagger}s; '
            f'font-size: {size_pixels}px; '
            f'text-shadow: 0 0 10px {glow};">{sym}</div>'
        )
        canvas_html.append(node_div)
        
    full_space_code = "".join(canvas_html)
    
    # Injecting directly into Fullscreen Document Object Model via an absolute positioning container
    str.components.v1.html(
        f'<div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -999; pointer-events: none;">{full_space_code}</div>',
        height=0,
        scrolling=False
    )

# Render the dynamic full screen universe view on every single rerun
render_brahmand_galaxy_view()


# --- PAGE 1 ---
if str.session_state.page == 1:
    str.markdown("<h1>For Someone Special... ✨❤️</h1>", unsafe_allow_html=True)
    
    # Inside a Premium Stylish Box
    str.markdown('<div class="stylish-box">', unsafe_allow_html=True)
    str.markdown('<p style="font-size: 22px; color: #f0f0f0; line-height: 1.6; font-style: italic;">Ye choti si jagah maine sirf aapke liye banayi hai. Apne dil par haath rakhein aur neeche click karein... 👇</p>', unsafe_allow_html=True)
    str.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = str.columns([1, 1.5, 1])
    with col2:
        if str.button("Open My Heart 💖", use_container_width=True):
            str.session_state.page = 2
            str.rerun()

# --- PAGE 2 ---
elif str.session_state.page == 2:
    str.markdown("<h1>Our Cosmic Universe ✨</h1>", unsafe_allow_html=True)
    
    str.markdown('<div class="stylish-box">', unsafe_allow_html=True)
    str.markdown('<h2 style="color: #ffffff; font-size: 36px; margin-bottom: 20px;">Dear Special Someone, 🌸</h2>', unsafe_allow_html=True)
    str.markdown('<p style="font-size: 20px; color: #fdfdfd; line-height: 1.9; font-style: italic;">"Is anant aasmaan mein laakhon sitare hain,<br>par hamare is chote se brahmand mein,<br>sabsay haseen aur pyari chamak aapki muskurahat ki hai.<br><br>Aapka zindagi mein hona kisi tohfe se kam nahi,<br>aap har pal ko khubsurat aur sukoon se bhar dete ho."</p>', unsafe_allow_html=True)
    str.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = str.columns([1, 1.5, 1])
    with col2:
        if str.button("Next Page ❤️", use_container_width=True):
            str.session_state.page = 3
            str.rerun()

# --- PAGE 3 ---
elif str.session_state.page == 3:
    str.markdown("<h1>The Eternal Love ✨🙏</h1>", unsafe_allow_html=True)
    
    str.markdown('<div class="stylish-box">', unsafe_allow_html=True)
    str.markdown('<h3 style="color: #ff6b8b; font-size: 28px; margin-bottom: 15px;">✨ Radhe Radhe - Shaswat Prem ✨</h3>', unsafe_allow_html=True)
    str.markdown('<p style="font-size: 19px; color: #e8e8e8; line-height: 1.8; font-style: italic;">"Prem ka matlab ek dusre ko paana nahi,<br>balki ek dusre mein poori tarah kho jaana hai.<br><br>Radha Krishna ka prem sikhata hai ki rishtey aatma se judte hain,<br>jahan dooriyan bhi dono ko alag nahi kar saktin.<br>Aapki zindagi bhi isi pavitra prem aur sukoon se hamesha mehakti rahe."</p>', unsafe_allow_html=True)
    str.markdown('</div>', unsafe_allow_html=True)
    
    str.image("https://images.unsplash.com/photo-1601931649911-37911b33346d?w=600", caption="🙏 Radhe Krishna Ki Kripa Aap Par Bani Rahe 🙏", use_container_width=True)
    
    col1, col2, col3 = str.columns([1, 1.5, 1])
    with col2:
        if str.button("Eternal Prem ✨", use_container_width=True):
            str.session_state.page = 4
            str.rerun()

# --- PAGE 4 ---
elif str.session_state.page == 4:
    str.markdown("<h1>The Ultimate Destination ❤️</h1>", unsafe_allow_html=True)
    
    str.markdown('<div class="stylish-box">', unsafe_allow_html=True)
    str.markdown('<h3 style="color: #ffffff; font-size: 28px; margin-bottom: 15px;">🌌 Sacha Prem Hi Brahmand Hai 🌌</h3>', unsafe_allow_html=True)
    str.markdown('<p style="font-size: 19px; color: #e8e8e8; line-height: 1.8; font-style: italic;">"Prem wo nahi jo kuch samay ke liye ho,<br>prem toh wo hai jo sadiyon tak rooh mein bas jaye.<br><br>Aapki is yatra ka aakhri padaav yahi sikhata hai ki<br>duniya ki sabsay khoobsoorat cheez ko na dekha ja sakta hai, <br>na chhua ja sakta hai... use sirf dil se mehsoos kiya jata hai."</p>', unsafe_allow_html=True)
    str.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = str.columns([0.1, 2.8, 0.1])
    with col2:
        if str.button("Agar duniya se alag hona chahty ho prem ke mamle main to click a eternal o god ✨", use_container_width=True):
            str.session_state.page = 5
            str.rerun()

# --- PAGE 5 (COMPLETE DATA INSIDE BOX WITH COSMIC GALAXY ATTRIBUTES) ---
elif str.session_state.page == 5:
    str.markdown("<h1>Vikaro Se Mukti: Sacha Prem 🌌</h1>", unsafe_allow_html=True)
    
    str.markdown('<div class="stylish-box">', unsafe_allow_html=True)
    str.markdown('<h3 style="color: #ff6b8b; font-size: 30px; margin-bottom: 25px;">✨ Prem Se Vikaro Ka Naash ✨</h3>', unsafe_allow_html=True)
    str.markdown('<p style="font-size: 18px; color: #e0e0e0; font-style: italic; margin-bottom: 35px;">"Jab jivan mein sachay aur pavitra prem ka agaman hota hai, toh mann ke saare vikar (vices) khud-ba-khud vileen ho jaate hain..."</p>', unsafe_allow_html=True)
    
    # vikar 1
    str.markdown('<div class="vikar-box">', unsafe_allow_html=True)
    str.markdown('<h4 style="color: #ffffff; margin: 0 0 8px 0; font-size: 20px;">1. डर (Bhay) — <span style="color: #ffb3c1;">Fear</span></h4>', unsafe_allow_html=True)
    str.markdown('<p style="color: #dfdfdf; font-size: 16px; margin: 0; line-height: 1.6;">Sacha prem har tarah ke darr ko mita deta hai. Jab aap kisi se nishwarth prem karte hain, toh khone ka ya zamane ka koi bhay nahi rehta, kyunki prem aatma ko nirbhay (fearless) bana deta hai.</p>', unsafe_allow_html=True)
    str.markdown('</div>', unsafe_allow_html=True)
    
    # vikar 2
    str.markdown('<div class="vikar-box">', unsafe_allow_html=True)
    str.markdown('<h4 style="color: #ffffff; margin: 0 0 8px 0; font-size: 20px;">2. मोह (Moh) — <span style="color: #ffb3c1;">Attachment</span></h4>', unsafe_allow_html=True)
    str.markdown('<p style="color: #dfdfdf; font-size: 16px; margin: 0; line-height: 1.6;">Moh insaan ko bandhan mein baandhta hai aur swarthi banata hai, jisse sacha prem azaad karna sikhata hai. Prem mein \'paane\' ki zidd nahi, balki samarpit hone ka sukoon hota hai.</p>', unsafe_allow_html=True)
    str.markdown('</div>', unsafe_allow_html=True)
    
    # vikar 3
    str.markdown('<div class="vikar-box">', unsafe_allow_html=True)
    str.markdown('<h4 style="color: #ffffff; margin: 0 0 8px 0; font-size: 20px;">3. क्रोध (Krodh) — <span style="color: #ffb3c1;">Anger</span></h4>', unsafe_allow_html=True)
    str.markdown('<p style="color: #dfdfdf; font-size: 16px; margin: 0; line-height: 1.6;">Krodh mann ki agni hai jo sab kuch jala deti hai. Par jahan sacha prem hota hai, wahan krodh ke liye koi jagah nahi hoti; prem us agni par kshama (forgiveness) aur shanti ka thanda jal chhidak deta hai.</p>', unsafe_allow_html=True)
    str.markdown('</div>', unsafe_allow_html=True)
    
    # vikar 4
    str.markdown('<div class="vikar-box">', unsafe_allow_html=True)
    str.markdown('<h4 style="color: #ffffff; margin: 0 0 8px 0; font-size: 20px;">4. ईर्ष्या (Irshya) — <span style="color: #ffb3c1;">Zero Jealousy</span></h4>', unsafe_allow_html=True)
    str.markdown('<p style="color: #dfdfdf; font-size: 16px; margin: 0; line-height: 1.6;">Irshya tab paida hoti hai jab hum doosron se tulna karte hain. Sacha prem hume doosron ki khushi mein apni khushi dekhna sikhata hai, jisse jalan poori tarah se mit jaati hai.</p>', unsafe_allow_html=True)
    str.markdown('</div>', unsafe_allow_html=True)
    
    # vikar 5
    str.markdown('<div class="vikar-box">', unsafe_allow_html=True)
    str.markdown('<h4 style="color: #ffffff; margin: 0 0 8px 0; font-size: 20px;">5. अहंकार (Ahankar) — <span style="color: #ffb3c1;">Ego</span></h4>', unsafe_allow_html=True)
    str.markdown('<p style="color: #dfdfdf; font-size: 16px; margin: 0; line-height: 1.6;">Ahankar kehta hai \'Main sabsay upar hoon\', lekin prem kehta hai \'Main toh kuch bhi nahi\'. Prem mein \'Main\' (Ego) mit jata hai aur sirf \'Hum\' baaki reh jata hai. Sacha prem ahankar ko poori tarah shunya kar deta hai.</p>', unsafe_allow_html=True)
    str.markdown('</div>', unsafe_allow_html=True)
    
    str.markdown('<p style="font-size: 17px; color: #ff6b8b; font-weight: bold; margin-top: 25px;">✨ Jo Prem Ko Chunndta Hai, Wo Saare Vikaro Se Mukt Ho Jata Hai ✨</p>', unsafe_allow_html=True)
    str.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = str.columns([1, 1.5, 1])
    with col2:
        if str.button("Go to Start 🔄", use_container_width=True):
            str.session_state.page = 1
            str.rerun()
