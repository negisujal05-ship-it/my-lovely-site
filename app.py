# --- OPTIMIZED GALAXY BACKGROUND (STARS + SNOW + HEARTS) ---
def apply_slow_cosmic_animation():
    cosmic_elements = ["✨", "❄️", "❤️", "⭐", "💫"]
    animation_elements_list = []
    
    animation_elements_list.append("<style>")
    animation_elements_list.append("""
    body { margin: 0; overflow: hidden; background: transparent; }
    .cosmic-item { 
        position: fixed; 
        top: -10%; 
        z-index: 0; 
        pointer-events: none; 
        animation: rainLinear linear infinite; 
        filter: drop-shadow(0 0 5px rgba(255,255,255,0.8));
    }
    @keyframes rainLinear {
        0% { top: -10%; transform: translateY(0) rotate(0deg); opacity: 0; }
        50% { opacity: 0.8; }
        100% { top: 110%; transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    """)
    animation_elements_list.append("</style>")
    
    # 25 elements kaafi hain site ko lightweight rakhne ke liye
    for _ in range(25):
        symbol = random.choice(cosmic_elements)
        left = random.randint(0, 100)
        duration = random.uniform(15.0, 25.0) # Slow movement
        delay = random.uniform(0.0, 10.0)
        size = random.randint(10, 20)
        
        element = (
            f'<div class="cosmic-item" style="left: {left}%; '
            f'animation-duration: {duration}s; '
            f'animation-delay: {delay}s; '
            f'font-size: {size}px;">{symbol}</div>'
        )
        animation_elements_list.append(element)
        
    full_html = "".join(animation_elements_list)
    str.components.v1.html(full_html, height=0, scrolling=False)
