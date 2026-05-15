
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
    font-family: Arial;
    background-color: #f6f4ef;
}

.hero {
    background: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.65)),
                url('https://images.unsplash.com/photo-1509062522246-3755977927d7?q=80&w=1800&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    padding: 140px 60px;
    border-radius: 30px;
    text-align: center;
    color: white;
}

.hero h1 {
    font-size: 72px;
    font-weight: 300;
    letter-spacing: 4px;
}

.hero p {
    font-size: 22px;
    margin-top: 20px;
    line-height: 1.8;
}

.section-title {
    font-size: 52px;
    font-weight: 300;
    margin-bottom: 20px;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 25px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.08);
}

.dark-section {
    background: black;
    color: white;
    padding: 80px 40px;
    border-radius: 30px;
}

.footer {
    background: black;
    color: white;
    padding: 50px;
    border-radius: 30px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="hero">

<h1>GENBRIGHT<br>WORLD SCHOOL</h1>

<p>
Admissions Open 2026–27<br>
Premium Future Ready Learning Environment
</p>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# =========================================================
# ABOUT SECTION
# =========================================================

col1, col2 = st.columns([1,1])

with col1:

    st.markdown(
    '<div class="section-title">Learning Beyond The Classroom</div>',
    unsafe_allow_html=True
    )

    st.write("""
Genbright World School blends world-class academics,
modern infrastructure, innovation, leadership,
creativity, and experiential learning.
""")

with col2:

    st.image(
    "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?q=80&w=1400&auto=format&fit=crop",
    use_container_width=True
    )

st.write("")
st.write("")

# =========================================================
# CAMPUS SECTION
# =========================================================

st.markdown("""
<div class="section-title">
Modern Campus Experience
</div>
""", unsafe_allow_html=True)

st.image(
"https://images.unsplash.com/photo-1498243691581-b145c3f54a5a?q=80&w=1800&auto=format&fit=crop",
use_container_width=True
)

st.write("")
st.write("")

# =========================================================
# STUDENT LIFE
# =========================================================

st.markdown("""
<div class="dark-section">

<h1 style="font-weight:300;">
Student Life & Holistic Learning
</h1>

<p style="font-size:20px; color:#cccccc;">
Technology, creativity, sports,
leadership, and emotional intelligence.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# =========================================================
# FEATURES
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="card">
    <h2>Creative Learning</h2>
    <p>
    Interactive learning experiences
    for imagination and innovation.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="card">
    <h2>Smart Education</h2>
    <p>
    Technology-enabled classrooms
    designed for future-ready growth.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="card">
    <h2>Holistic Growth</h2>
    <p>
    Sports, leadership, arts,
    and personality development.
    </p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# =========================================================
# ADMISSIONS
# =========================================================

st.markdown("""
<div class="hero">

<h1 style="font-size:60px;">
Admissions Open
</h1>

<p>
Join Genbright World School<br>
for Academic Year 2026–27
</p>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

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

<p style="margin-top:20px; color:#bbbbbb;">
Premium Interactive School Website Demo
</p>

</div>
""", unsafe_allow_html=True)

