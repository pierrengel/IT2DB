import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# ---- Page Setup ----
st.set_page_config(layout="wide")

# ---- Custom CSS Styling ----
st.markdown("""
<style>
#MainMenu, footer, header {
    visibility: hidden;
}
.card-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# ---- Header Layout: Logo | Title | Dropdown ----
col_logo, col_title, col_dropdown = st.columns([1, 4, 1])

with col_logo:
    st.image("LOGOBODO.jpg", width=80)

with col_title:
    st.markdown("<h1 style='margin-top: 20px;'>BODO</h1>", unsafe_allow_html=True)

with col_dropdown:
    category_map = {
        "Paprika": "C1",
        "Karotten": "C2"
    }
    selection = st.selectbox(" ", list(category_map.keys()), label_visibility="collapsed", key="main_category")
    category = category_map[selection]

# ---- Dynamic Content Data ----
content = {
    "C1": {
        "Haha": {"desc": "Description blah blah for Haha", "data": np.random.randn(100)},
        "Huhu": {"desc": "Something about Huhu being awesome", "data": np.random.randn(70)},
    },
    "C2": {
        "Haha": {"desc": "C2 Haha content here", "data": np.random.randn(90)},
        "Huhu": {"desc": "All about C2 Huhu", "data": np.random.randn(60)},
    }
}

# ---- Main Card Layout ----
col1, col2, col3 = st.columns(3)

# -- Left Column: Klimaüberwachung Block --
with col1:
    if os.path.exists("KLimaüberwachung.jpg"):
        st.image("KLimaüberwachung.jpg", width=30)
    st.markdown("### Klimaüberwachung")
    st.markdown("**Gewächshaus Paprika**")

    klima_data = [
        ("Temperatur (Luft)", "25 °C", "18–24 °C", "🔴 Zu hoch"),
        ("Luftfeuchtigkeit", "81 %", "60–80 %", "🟠 Grenzwertig"),
        ("CO₂-Konzentration", "1001 ppm", "600–1000 ppm", "🟠 Grenzwertig"),
        ("Lichtintensität", "225 µmol/m²/s", "150–300 µmol/m²/s", "🟢 OK"),
        ("Blatt-Temperatur", "27 °C", "18–26 °C", "🔴 Zu hoch")
    ]

    for param, ist, soll, status in klima_data:
        st.markdown(f"""
        <div style='margin-bottom: 1rem; padding: 0.5rem; background-color: #1e1e1e; border-radius: 8px;'>
            <strong>{param}</strong><br>
            Ist-Wert: <span style='color:#fff;'>{ist}</span><br>
            Sollbereich: <span style='color:#aaa;'>{soll}</span><br>
            Status: <span style='font-weight:bold;'>{status}</span>
        </div>
        """, unsafe_allow_html=True)

# -- Middle Column: Haha --
with col2:
    st.image("https://via.placeholder.com/30", width=30)
    st.markdown("### Haha")
    st.write(content[category]["Haha"]["desc"])

    fig, ax = plt.subplots()
    ax.hist(content[category]["Haha"]["data"], bins=20, color="#69b3a2", edgecolor="black")
    ax.set_title("Haha Histogram")
    st.pyplot(fig)

# -- Right Column: Huhu --
with col3:
    st.image("https://via.placeholder.com/30", width=30)
    st.markdown("### Huhu")
    st.write(content[category]["Huhu"]["desc"])

    fig, ax = plt.subplots()
    ax.hist(content[category]["Huhu"]["data"], bins=20, color="#69b3a2", edgecolor="black")
    ax.set_title("Huhu Histogram")
    st.pyplot(fig)
