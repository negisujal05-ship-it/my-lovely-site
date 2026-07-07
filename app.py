import streamlit as str
import time
import random

# Page Setup
str.set_page_config(page_title="Our Cosmic Milky Way ❤️", page_icon="🌌", layout="centered")

# Page tracking system
if "page" not in str.session_state:
    str.session_state.page = 1

# --- GLOBAL STYLING (WITH IMAGE + TEXT WATERMARK & ADVANCED TRANSITION) ---
CSS_BASE_STYLE = """
<style>
/* Smooth Top-to-Bottom Premium Transition */
@keyframes fadeInDown {
    0% {
        opacity: 0;
        transform: translateY(-40px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

html {
    scroll-behavior: smooth;
}

.stApp {
    background: linear-gradient(135deg, #020105 0%, #050312 40%, #0b0518 80%, #11031c 100%);
    font-family: 'Georgia', serif;
    color: #ffffff;
    overflow-x: hidden;
}

/* Page container gets hardware accelerated smooth transition */
.block-container {
    animation: fadeInDown 1.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    will-change: transform, opacity;
}

h1 {
    color: #ffffff;
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    text-shadow: 0 0 15px rgba(255, 255, 255, 0.8), 2px 2px 5px rgba(0, 0, 0, 0.9);
    margin-top: 40px;
}

/* Premium Box with BOTH Text & Image Watermark Capabilities */
.stylish-box {
    background: rgba(5, 3, 12, 0.96);
    padding: 45px 35px;
    border-radius: 25px;
    border: 2px solid #ffffff;
    box-shadow: 0px 0px 35px rgba(255, 255, 255, 0.25);
    text-align: center;
    position: relative;
    z-index: 2;
    margin-bottom: 30px;
    overflow: hidden;
}

/* IMAGE WATERMARK LAYER (Placed perfectly in background inside the box) */
.image-watermark {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    /* Aap apni pasand ki transparent PNG background image ka link yahan daal sakte hain */
    background-image: url('https://raw.githubusercontent.com/negisujal05-ship-it/my-lovely-site/main/cosmic_heart.png'); 
    background-size: contain;
    background-position: center;
    background-repeat: no-repeat;
    opacity: 0.04; /* Bilkul halka subtle effect */
    pointer-events: none;
    z-index: 1;
}

/* TEXT WATERMARK LAYER */
.watermark {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) rotate(-12deg);
    font-size: 75px;
    font-weight: 900;
    color: rgba(255, 255, 255, 0.025);
    white-space: nowrap;
    pointer-events: none;
    z-index: 1;
    font-family: 'Impact', 'Arial Black', sans-serif;
    letter-spacing: 8px;
}

/* Content wrapper inside box to stay on top of watermarks */
.box-content {
    position: relative;
    z-index: 3;
}

/* Sub-boxes inside Page 5 for Vikars */
.vikar-box {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    text-align: left;
    box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    position: relative;
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
    box-shadow: 0 0 20px rgba(255, 255, 255, 0.4) !important;
    transition: all 0.3s ease !important;
    display: block;
    margin: 40px auto !important;
}

div.stButton > button:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 0 30px rgba(255, 255, 255, 0.8) !important;
}

.milkyway-moon {
    position: fixed;
    top: 15%;
    right: 8%;
    font-size: 65px;
    opacity: 0.9;
    filter: drop-shadow(0 0 25px rgba(255, 255, 255, 0.85)) brightness(2);
    z-index: 1;
}
</style>
"""

str.markdown(CSS_BASE_STYLE, unsafe_allow_html=True)
str.markdown('<div class="milkyway-moon">🌙</div>', unsafe_allow_html=True)


# --- BACKGROUND COSMIC RAIN (Optimized) ---
def apply_slow_cosmic_animation():
    cosmic_symbols = ["💧", "❄️", "❤️", "💖", "💘"]
    animation_elements_list = []
    
    animation_elements_list.append("<style>")
    animation_elements_list.append("""
    body { margin: 0; overflow: hidden; background: transparent; }
    .cosmic-item { position: fixed; top: -10%; z-index: 1; pointer-events: none; animation: rainLinear linear infinite; }
    @keyframes rainLinear {
        0% { top: -10%; transform: translateX(0); opacity: 0; }
        10% { opacity: 0.6; }
        90% { opacity: 0.6; }
        100% { top: 110%; transform: translateX(40px); opacity: 0; }
    }
    """)
    animation_elements_list.append("</style>")
    
    for item_index in range(30):
        chosen_symbol = random.choice(cosmic_symbols)
        left_coordinate = random.randint(2, 98)
        slow_speed_duration = random.uniform(12.0, 18.0)
        staggered_delay = random.uniform(0.0, 6.0)
        pixel_size = random.randint(14, 24)
        
        glow_color = "rgba(255, 75, 75, 0.4)" if chosen_symbol in ["❤️", "💖", "💘"] else "rgba(255, 255, 255, 0.3)"
        
        element_string = (
            f'<div class="cosmic-item" style="left: {left_coordinate}%; '
            f'animation-duration: {slow_speed_duration}s; '
            f'animation-delay: {staggered_delay}s; '
            f'font-size: {pixel_size}px; '
            f'text-shadow: 0 0 8px {glow_color};">{chosen_symbol}</div>'
        )
        animation_elements_list.append(element_string)
        
    full_html_canvas = "".join(animation_elements_list)
    str.components.v1.html(full_html_canvas, height=0, scrolling=False)


# --- PAGE 1 ---
if str.session_state.page == 1:
    apply_slow_cosmic_animation()
    str.markdown("<h1>For Someone Special... ✨❤️</h1>", unsafe_allow_html=True)
    
    str.markdown('''
        <div class="stylish-box">
            <div class="image-watermark"></div>
            <div class="watermark">COSMIC LOVE</div>
            <div class="box-content">
                <p style="font-size: 22px; color: #f0f0f0; line-height: 1.6; font-style: italic;">
                    Ye choti si jagah maine sirf aapke liye banayi hai. Apne dil par haath rakhein aur neeche click karein... 👇
                </p>
            </div>
        </div>
    ''', unsafe_allow_html=True)
    
    if str.button("Open My Heart 💖", use_container_width=True):
        with str.spinner("Transitioning Through Space..."):
            time.sleep(1.0)
        str.session_state.page = 2
        str.rerun()

# --- PAGE 2 ---
elif str.session_state.page == 2:
    apply_slow_cosmic_animation()
    str.markdown("<h1>Our Cosmic Universe ✨</h1>", unsafe_allow_html=True)
    
    str.markdown('''
        <div class="stylish-box">
            <div class="image-watermark"></div>
            <div class="watermark">FOREVER</div>
            <div class="box-content">
                <h2 style="color: #ffffff; font-size: 38px; margin-bottom: 20px;">Dear Special Someone, 🌸</h2>
                <p style="font-size: 20px; color: #fdfdfd; line-height: 1.8; font-style: italic;">
                    "Is anant aasmaan mein laakhon sitare hain,<br>par hamare is chote se brahmand mein,<br>sabsay haseen aur pyari chamak aapki muskurahat ki hai.<br><br>Aapka zindagi mein hona kisi tohfe se kam nahi,<br>aap har pal ko khubsurat aur sukoon se bhar dete ho."
                </p>
            </div>
        </div>
    ''', unsafe_allow_html=True)
    
    if str.button("Next Page ❤️", use_container_width=True):
        with str.spinner("Transitioning Through Space..."):
            time.sleep(1.0)
        str.session_state.page = 3
        str.rerun()

# --- PAGE 3 ---
elif str.session_state.page == 3:
    apply_slow_cosmic_animation()
    str.markdown("<h1>The Eternal Love ✨🙏</h1>", unsafe_allow_html=True)
    
    str.markdown('''
        <div class="stylish-box">
            <div class="image-watermark"></div>
            <div class="watermark">RADHE RADHE</div>
            <div class="box-content">
                <h3 style="color: #ff6b8b; font-size: 28px; margin-bottom: 15px;">✨ Radhe Radhe - Shaswat Prem ✨</h3>
                <p style="font-size: 19px; color: #e8e8e8; line-height: 1.8; font-style: italic;">
                    "Prem ka matlab ek dusre ko paana nahi,<br>balki ek dusre mein poori tarah kho jaana hai.<br><br>Radha Krishna ka prem sikhata hai ki rishtey aatma se judte hain,<br>jahan dooriyan bhi dono ko alag nahi kar saktin.<br>Aapki zindagi bhi isi pavitra prem aur sukoon se hamesha mehakti rahe."
                </p>
            </div>
        </div>
    ''', unsafe_allow_html=True)
    
    if str.button("Eternal Prem ✨", use_container_width=True):
        with str.spinner("Transitioning Through Space..."):
            time.sleep(1.0)
        str.session_state.page = 4
        str.rerun()

# --- PAGE 4 ---
elif str.session_state.page == 4:
    apply_slow_cosmic_animation()
    str.markdown("<h1>The Ultimate Destination ❤️</h1>", unsafe_allow_html=True)
    
    str.markdown('''
        <div class="stylish-box">
            <div class="image-watermark"></div>
            <div class="watermark">ETERNAL</div>
            <div class="box-content">
                <h3 style="color: #ffffff; font-size: 28px; margin-bottom: 15px;">🌌 Sacha Prem Hi Brahmand Hai 🌌</h3>
                <p style="font-size: 19px; color: #e8e8e8; line-height: 1.8; font-style: italic;">
                    "Prem wo nahi jo kuch samay ke liye ho,<br>prem toh wo hai jo sadiyon tak rooh mein bas jaye.<br><br>Aapki is yatra ka aakhri padaav yahi sikhata hai ki<br>duniya ki sabsay khoobsoorat cheez ko na dekha ja sakta hai, <br>na chhua ja sakta hai... use sirf dil se mehsoos kiya jata hai."
                </p>
            </div>
        </div>
    ''', unsafe_allow_html=True)
    
    if str.button("Step away from the world: Enter the eternal life of God ✨", use_container_width=True):
        with str.spinner("Transitioning Through Space..."):
            time.sleep(1.0)
        str.session_state.page = 5
        str.rerun()

# --- PAGE 5 ---
elif str.session_state.page == 5:
    apply_slow_cosmic_animation()
    str.markdown("<h1>Vikaro Se Mukti: Sacha Prem 🌌</h1>", unsafe_allow_html=True)
    
    str.markdown('''
        <div class="stylish-box">
            <div class="image-watermark"></div>
            <div class="watermark" style="font-size:55px;">MUKTI</div>
            <div class="box-content">
                <h3 style="color: #ff6b8b; font-size: 30px; margin-bottom: 25px;">✨ Prem Se Vikaro Ka Naash ✨</h3>
                <p style="font-size: 18px; color: #e0e0e0; font-style: italic; margin-bottom: 30px;">"Jab jivan mein sachay aur pavitra prem ka agaman hota hai, toh mann ke saare vikar (vices) khud-ba-khud vileen ho jaate hain..."</p>
    ''', unsafe_allow_html=True)
    
    # 1. DAR / FEAR Block
    str.markdown('<div class="vikar-box">', unsafe_allow_html=True)
    str.markdown('<h4 style="color: #ffffff; margin: 0 0 8px 0; font-size: 20px;">1. डर (Bhay) — <span style="color: #ffb3c1;">Fear</span></h4>', unsafe_allow_html=True)
    str.markdown('<p style="color: #dfdfdf; font-size: 16px; margin: 0; line-height: 1.5;">Sacha prem har tarah ke darr ko mita deta hai. Jab aap kisi se nishwarth prem karte hain, toh khone ka ya zamane ka koi bhay nahi rehta, kyunki prem aatma ko nirbhay (fearless) bana deta hai.</p>', unsafe_allow_html=True)
    str.markdown('</div>', unsafe_allow_html=True)
    
    # 2. MOH / ATTACHMENT Block
    str.markdown('<div class="vikar-box">', unsafe_allow_html=True)
    str.markdown('<h4 style="color: #ffffff; margin: 0 0 8px 0; font-size: 20px;">2. मोह (Moh) — <span style="color: #ffb3c1;">Attachment</span></h4>', unsafe_allow_html=True)
    str.markdown('<p style="color: #dfdfdf; font-size: 16px; margin: 0; line-height: 1.5;">Moh insaan ko bandhan mein baandhta hai aur swarthi banata hai, jisse sacha prem azaad karna sikhata hai. Prem mein \'paane\' ki zidd nahi, balki samarpit hone ka sukoon hota hai.</p>', unsafe_allow_html=True)
    str.markdown('</div>', unsafe_allow_html=True)
    
    # 3. KRODH / ANGER Block
    str.markdown('<div class="vikar-box">', unsafe_allow_html=True)
    str.markdown('<h4 style="color: #ffffff; margin: 0 0 8px 0; font-size: 20px;">3. क्रोध (Krodh) — <span style="color: #ffb3c1;">Anger</span></h4>', unsafe_allow_html=True)
    str.markdown('<p style="color: #dfdfdf; font-size: 16px; margin: 0; line-height: 1.5;">Krodh mann ki agni hai jo sab kuch jala deti hai. Par jahan sacha prem hota hai, wahan krodh ke liye koi jagah nahi hoti; prem us agni par kshama (forgiveness) aur shanti ka thanda jal chhidak deta hai.</p>', unsafe_allow_html=True)
    str.markdown('</div>', unsafe_allow_html=True)
    
    # 4. IRSHYA / JEALOUSY Block
    str.markdown('<div class="vikar-box">', unsafe_allow_html=True)
    str.markdown('<h4 style="color: #ffffff; margin: 0 0 8px 0; font-size: 20px;">4. ईर्ष्या (Irshya) — <span style="color: #ffb3c1;">Zero Jealousy</span></h4>', unsafe_allow_html=True)
    str.markdown('<p style="color: #dfdfdf; font-size: 16px; margin: 0; line-height: 1.5;">Irshya tab paida hoti hai jab hum doosron se tulna karte hain. Sacha prem hume doosron ki khushi mein apni khushi dekhna sikhata hai, jisse jalan poori tarah se mit jaati hai.</p>', unsafe_allow_html=True)
    str.markdown('</div>', unsafe_allow_html=True)
    
    # 5. AHANKAR / EGO Block
    str.markdown('<div class="vikar-box">', unsafe_allow_html=True)
    str.markdown('<h4 style="color: #ffffff; margin: 0 0 8px 0; font-size: 20px;">5. अहंकार (Ahankar) — <span style="color: #ffb3c1;">Ego</span></h4>', unsafe_allow_html=True)
    str.markdown('<p style="color: #dfdfdf; font-size: 16px; margin: 0; line-height: 1.5;">Ahankar kehta hai \'Main sabsay upar hoon\', lekin prem kehta hai \'Main toh kuch bhi nahi\'. Prem mein \'Main\' (Ego) mit jata hai aur sirf \'Hum\' baaki reh jata hai. Sacha prem ahankar ko poori tarah shunya kar deta hai.</p>', unsafe_allow_html=True)
    str.markdown('</div>', unsafe_allow_html=True)
    
    str.markdown('<p style="font-size: 16px; color: #ff6b8b; font-weight: bold; text-align: center; margin-top: 25px;">✨ Jo Prem Ko Chunta Hai, Wo Saare Vikaro Se Mukt Ho Jata Hai ✨</p>', unsafe_allow_html=True)
    str.markdown('</div></div>', unsafe_allow_html=True)
    
    # if str.button("Go to Start 🔄", use_container_width=True):
    #     with str.spinner("Resetting Space..."):
    #         time.sleep(1.0)
    #     str.session_state.page = 1
    #     str.rerun()
       # Button to go to Page 6
    if str.button("Enter to Love World 💖"):
        str.session_state.page = 6
        str.rerun()

# PAGE 6 (Krishna Prem Definition)
elif str.session_state.page == 6:
    str.markdown("<h1>Krishna Prem: Param Satya ✨</h1>", unsafe_allow_html=True)
    str.markdown(''' 
        <div class="stylish-box"> 
            <h3>🌌 Bhagwan Krishna ka Prem Sandesh 🌌</h3> 
            <p style="font-size: 20px; line-height: 1.8; font-style: italic;"> 
                "Prem ka arth hai 'Samarpan'. Krishna ke anusar, prem wahi hai jisme koi maang nahi hoti.<br><br>
                Jab hum dusro ki khushi mein apni khushi dhoondhte hain, wahi ishwar ka swaroop hai.<br>
                Prem bandhan nahi, balki aatma ki mukti hai. Jab tum khud ko bhool kar keval prem ke liye jeete ho, 
                tab tumhare bhitar 'Main' mit jata hai aur 'Krishna' ka prem jag uthta hai." 
            </p> 
        </div> 
    ''', unsafe_allow_html=True)
    
    # if str.button("Go to Start 🔄"):
    #     str.session_state.page = 1
    #     str.rerun()
# English Button for Page 7
    if str.button("Definition of Pure Love ✨", use_container_width=True):
        str.session_state.page = 7
        str.rerun()

# --- PAGE 7 ---
elif str.session_state.page == 7:
    apply_slow_cosmic_animation()
    str.markdown("<h1>Sudh Prem Ki Pribhasha 🌌</h1>", unsafe_allow_html=True)
    
    str.markdown('''
        <div class="stylish-box">
            <div class="image-watermark"></div>
            <div class="watermark" style="font-size:50px;">PURE</div>
            <div class="box-content">
                <h3 style="color: #ff6b8b; font-size: 28px; margin-bottom: 20px;">✨ Nishwarth Prem ✨</h3>
                <p style="font-size: 20px; color: #ffffff; line-height: 1.8; font-weight: bold; font-style: italic;">
                    "Prem wo hai jo nishwarth bhaw se aatma se ho, na ki sharir se. 
                    Yeh koi vyakti nahi, ek sthiti hai. Jab aap apni khushi ko doosre ki muskurahat 
                    mein dhundne lagte hain, wahi prem hai.<br><br>"
                </p>
                <p style="font-size: 18px; color: #e8e8e8; margin-top: 20px;">
                    Sacha prem wahi hai jahan koi shart na ho, koi maang na ho, bas ek dusre ki aatma ka samman ho.
                </p>
            </div>
        </div>
    ''', unsafe_allow_html=True)
    
    # if str.button("Enter the Love World 🚀", use_container_width=True):
    #     with str.spinner("Returning to Cosmic Start..."):
    #         time.sleep(1.0)
    #     str.session_state.page = 1
    #     str.rerun()

