import streamlit as st

st.set_page_config(
    page_title="Radhe Krishna Galaxy",
    page_icon="🦚",
    layout="wide"
)

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
html, body {
    margin:0;
    padding:0;
    overflow:hidden;
    background: radial-gradient(circle at center, #111133, #000000);
}

.main-container{
    position:fixed;
    inset:0;
    overflow:hidden;
}

.center-box{
    position:absolute;
    top:50%;
    left:50%;
    transform:translate(-50%,-50%);
    text-align:center;
    color:white;
    z-index:100;
}

.center-box h1{
    font-size:55px;
    text-shadow:0 0 20px pink;
}

.center-box img{
    width:420px;
    border-radius:20px;
    box-shadow:0 0 40px rgba(255,255,255,0.5);
}

.star{
    position:absolute;
    color:white;
    animation:starMove linear infinite;
}

.snow{
    position:absolute;
    color:#dff6ff;
    animation:fall linear infinite;
}

.heart{
    position:absolute;
    color:pink;
    animation:fall linear infinite;
}

.moon{
    position:absolute;
    top:40px;
    right:60px;
    font-size:90px;
}

@keyframes fall{
    from{
        transform:translateY(-50px);
    }
    to{
        transform:translateY(110vh);
    }
}

@keyframes starMove{
    from{
        transform:translateX(-10vw);
    }
    to{
        transform:translateX(110vw);
    }
}
</style>
</head>
<body>

<div class="main-container">

<div class="moon">🌙</div>

<div class="center-box">
    <h1>❤️ Radhe Radhe ❤️</h1>
    <img src="https://images.unsplash.com/photo-1518562180175-34a163b1a9a6?w=1200">
    <h2>जय श्री राधे कृष्णा 🦚</h2>
</div>

<script>

for(let i=0;i<120;i++){
    let s=document.createElement("div");
    s.className="star";
    s.innerHTML="✦";
    s.style.left=Math.random()*100+"vw";
    s.style.top=Math.random()*100+"vh";
    s.style.fontSize=(5+Math.random()*15)+"px";
    s.style.animationDuration=(20+Math.random()*40)+"s";
    document.body.appendChild(s);
}

for(let i=0;i<150;i++){
    let s=document.createElement("div");
    s.className="snow";
    s.innerHTML="❄";
    s.style.left=Math.random()*100+"vw";
    s.style.fontSize=(8+Math.random()*12)+"px";
    s.style.animationDuration=(15+Math.random()*20)+"s";
    s.style.animationDelay=Math.random()*10+"s";
    document.body.appendChild(s);
}

for(let i=0;i<60;i++){
    let h=document.createElement("div");
    h.className="heart";
    h.innerHTML="❤";
    h.style.left=Math.random()*100+"vw";
    h.style.fontSize=(12+Math.random()*18)+"px";
    h.style.animationDuration=(20+Math.random()*20)+"s";
    h.style.animationDelay=Math.random()*10+"s";
    document.body.appendChild(h);
}

</script>

</div>
</body>
</html>
"""

st.components.v1.html(html_code, height=900, scrolling=False)
