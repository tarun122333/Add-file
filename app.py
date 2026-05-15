
import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Genbright World School",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #050505;
    color: white;
    font-family: Arial;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.hero {
    height: 95vh;

    display:flex;
    align-items:center;
    justify-content:center;
    flex-direction:column;

    background:
    linear-gradient(rgba(0,0,0,0.55),
    rgba(0,0,0,0.75)),
    url('https://images.unsplash.com/photo-1509062522246-3755977927d7?q=80&w=2000&auto=format&fit=crop');

    background-size:cover;
    background-position:center;

    border-radius:35px;

    text-align:center;
}

.hero h1 {
    font-size:90px;
    font-weight:200;
    letter-spacing:6px;
}

.hero p {
    font-size:24px;
    color:#dddddd;
    line-height:1.8;
}

.button {
    background:white;
    color:black;
    padding:18px 45px;
    border-radius:50px;
    margin-top:30px;
    font-size:20px;
}

.section-title {
    font-size:60px;
    font-weight:200;
}

.section-text {
    color:#cccccc;
    font-size:20px;
    line-height:1.9;
}

.card {
    background:#111111;
    padding:30px;
    border-radius:30px;
    border:1px solid rgba(255,255,255,0.08);
}

.card h2 {
    font-size:30px;
    font-weight:300;
}

.card p {
    color:#cccccc;
    line-height:1.8;
}

.footer {
    text-align:center;
    padding:80px;
    color:#999999;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""

<div class="hero">

<h1>
GENBRIGHT<br>
WORLD SCHOOL
</h1>

<p>
Admissions Open 2026–27<br>
Premium Future Ready Global Education
</p>

<div class="button">
Explore Campus
</div>

</div>

""", unsafe_allow_html=True)

st.write("")
st.write("")

# =========================================================
# ABOUT SECTION
# =========================================================

col1, col2 = st.columns(2)

with col1:

    st.markdown(
    '<div class="section-title">Future Ready Learning</div>',
    unsafe_allow_html=True
    )

    st.markdown(
    '<div class="section-text">Genbright World School combines innovation, technology, creativity, leadership, and experiential learning to inspire future global citizens.</div>',
    unsafe_allow_html=True
    )

with col2:

    st.image(
    "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?q=80&w=1600&auto=format&fit=crop",
    use_container_width=True
    )

# =========================================================
# CAMPUS SECTION
# =========================================================

st.write("")
st.write("")

st.markdown(
'<div class="section-title">3D Smart Campus Experience</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="section-text">Modern architecture, smart classrooms, innovation labs, and immersive learning spaces.</div>',
unsafe_allow_html=True
)

st.image(
"https://images.unsplash.com/photo-1498243691581-b145c3f54a5a?q=80&w=2000&auto=format&fit=crop",
use_container_width=True
)

# =========================================================
# HITECH SECTION
# =========================================================

st.write("")
st.write("")

col1, col2 = st.columns(2)

with col1:

    st.image(
    "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?q=80&w=1800&auto=format&fit=crop",
    use_container_width=True
    )

with col2:

    st.markdown(
    '<div class="section-title">Hi-Tech Smart Education</div>',
    unsafe_allow_html=True
    )

    st.markdown(
    '<div class="section-text">AI-powered learning, robotics labs, coding education, and modern digital classrooms.</div>',
    unsafe_allow_html=True
    )

# =========================================================
# FEATURE CARDS
# =========================================================

st.write("")
st.write("")

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown("""

    <div class="card">

    <h2>Creative Innovation</h2>

    <p>
    Interactive learning experiences
    for creativity and innovation.
    </p>

    </div>

    """, unsafe_allow_html=True)

with c2:

    st.markdown("""

    <div class="card">

    <h2>AI Smart Classrooms</h2>

    <p>
    Advanced teaching systems
    and immersive learning methods.
    </p>

    </div>

    """, unsafe_allow_html=True)

with c3:

    st.markdown("""

    <div class="card">

    <h2>Holistic Growth</h2>

    <p>
    Sports, leadership,
    arts, and emotional intelligence.
    </p>

    </div>

    """, unsafe_allow_html=True)

# =========================================================
# GALLERY
# =========================================================

st.write("")
st.write("")

st.markdown(
'<div class="section-title">Student Life & Innovation</div>',
unsafe_allow_html=True
)

g1, g2, g3 = st.columns(3)

with g1:

    st.image(
    "https://images.unsplash.com/photo-1513258496099-48168024aec0?q=80&w=1200&auto=format&fit=crop",
    use_container_width=True
    )

with g2:

    st.image(
    "https://images.unsplash.com/photo-1509062522246-3755977927d7?q=80&w=1200&auto=format&fit=crop",
    use_container_width=True
    )

with g3:

    st.image(
    "https://images.unsplash.com/photo-1544717305-2782549b5136?q=80&w=1200&auto=format&fit=crop",
    use_container_width=True
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown("""

<div class="footer">

<h2>GENBRIGHT WORLD SCHOOL</h2>

<p>
Mokila Campus<br>
+91 988 433 5050<br>
www.genbright.in
</p>

<p>
Premium Cinematic School Website
</p>

</div>

""", unsafe_allow_html=True)
