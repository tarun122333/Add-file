
import streamlit as st
import base64

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title='Genbright World School',
    layout='wide'
)

# =========================================================
# LOAD IMAGE FUNCTION
# =========================================================

def get_base64(file):
    with open(file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

logo = get_base64('logo.png')

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(f'''

<style>

html, body, [class*="css"] {{
    background-color: #050505;
    color: white;
    font-family: Arial;
}}

#MainMenu {{visibility:hidden;}}
footer {{visibility:hidden;}}
header {{visibility:hidden;}}

.hero {{

    height: 100vh;

    display:flex;
    align-items:center;
    justify-content:center;
    flex-direction:column;

    background:
    linear-gradient(rgba(0,0,0,0.45),
    rgba(0,0,0,0.75)),
    url("12.jpeg");

    background-size: cover;
    background-position: center;

    border-radius: 35px;

    text-align:center;
}}

.logo {{
    width:280px;
    margin-bottom:30px;
}}

.hero h1 {{
    font-size:90px;
    font-weight:200;
    letter-spacing:6px;
}}

.hero p {{
    font-size:24px;
    color:#dddddd;
    line-height:1.8;
}}

.button {{

    background:white;
    color:black;

    padding:18px 45px;

    border-radius:50px;

    margin-top:30px;

    font-size:20px;
}}

.section-title {{
    font-size:60px;
    font-weight:200;
}}

.section-text {{
    color:#cccccc;
    font-size:20px;
    line-height:1.9;
}}

.card {{

    background:#111111;

    padding:30px;

    border-radius:30px;

    border:1px solid rgba(255,255,255,0.08);
}}

.card h2 {{
    font-size:30px;
    font-weight:300;
}}

.card p {{
    color:#cccccc;
    line-height:1.8;
}}

.footer {{
    text-align:center;
    padding:80px;
    color:#999999;
}}

</style>

''', unsafe_allow_html=True)

# =========================================================
# HERO SECTION
# =========================================================

st.markdown(f'''

<div class="hero">

<img src="data:image/png;base64,{logo}" class="logo">

<h1>
GENBRIGHT<br>
WORLD SCHOOL
</h1>

<p>
Admissions Open 2026–27<br>
Future Ready Premium Global Education
</p>

<div class="button">
Explore Campus
</div>

</div>

''', unsafe_allow_html=True)

st.write("")
st.write("")

# =========================================================
# ABOUT
# =========================================================

c1, c2 = st.columns(2)

with c1:

    st.markdown(
    '<div class="section-title">Future Ready Learning</div>',
    unsafe_allow_html=True
    )

    st.markdown(
    '<div class="section-text">Genbright World School combines innovation, creativity, technology, leadership, and experiential learning to inspire future global citizens.</div>',
    unsafe_allow_html=True
    )

with c2:

    st.image("intellectual.jpg", use_container_width=True)

# =========================================================
# CAMPUS
# =========================================================

st.write("")
st.write("")

st.markdown(
'<div class="section-title">3D Smart Campus</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="section-text">Modern architecture, smart classrooms, immersive learning spaces, and premium infrastructure.</div>',
unsafe_allow_html=True
)

st.image("12.jpeg", use_container_width=True)

# =========================================================
# ACTIVITIES
# =========================================================

st.write("")
st.write("")

c1, c2 = st.columns(2)

with c1:

    st.image("images.jpeg", use_container_width=True)

with c2:

    st.markdown(
    '<div class="section-title">Holistic Student Growth</div>',
    unsafe_allow_html=True
    )

    st.markdown(
    '<div class="section-text">Sports, martial arts, leadership, emotional intelligence, and creativity programs build confident future leaders.</div>',
    unsafe_allow_html=True
    )

# =========================================================
# CARDS
# =========================================================

st.write("")
st.write("")

a, b, c = st.columns(3)

with a:

    st.markdown('''

    <div class="card">

    <h2>Creative Innovation</h2>

    <p>
    Interactive learning experiences
    for imagination and innovation.
    </p>

    </div>

    ''', unsafe_allow_html=True)

with b:

    st.markdown('''

    <div class="card">

    <h2>AI Smart Classrooms</h2>

    <p>
    Advanced digital classrooms,
    robotics labs,
    and coding education.
    </p>

    </div>

    ''', unsafe_allow_html=True)

with c:

    st.markdown('''

    <div class="card">

    <h2>Holistic Development</h2>

    <p>
    Leadership,
    sports,
    arts,
    and emotional intelligence.
    </p>

    </div>

    ''', unsafe_allow_html=True)

# =========================================================
# NATURE
# =========================================================

st.write("")
st.write("")

st.markdown(
'<div class="section-title">Nature & Sustainability</div>',
unsafe_allow_html=True
)

st.image("farm.jpg", use_container_width=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown('''

<div class="footer">

<h2>GENBRIGHT WORLD SCHOOL</h2>

<p>
Mokila Campus<br>
+91 988 433 5050<br>
www.genbright.in
</p>

<p>
Premium Cinematic Interactive School Website
</p>

</div>

''', unsafe_allow_html=True)
