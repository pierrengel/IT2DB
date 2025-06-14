import streamlit as st
import os

# ---- Page Setup ----
st.set_page_config(layout="wide")

# ---- Custom CSS Styling ----
st.markdown("""
<style>
#MainMenu, footer, header {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ---- Header Layout: Logo + Title + Dropdown ----
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
    <div style="display: flex; align-items: center; gap: 1rem;">
        <img src="048a54e7-9b34-4bed-b931-9c4fd1edabeb.png" alt="BODO Logo" style="height: 100px;">
        <h1 style="margin: 0;">BODO</h1>
    </div>
    <div style="width: 150px;">
""", unsafe_allow_html=True)

# ---- Dropdown Selector ----
category_map = {
    "Paprika": "C1",
    "Karotten": "C2"
}
selection = st.selectbox(" ", list(category_map.keys()), label_visibility="collapsed", key="main_category")
category = category_map[selection]

st.markdown("</div></div>", unsafe_allow_html=True)

# ---- Three Column Layout ----
col1, col2, col3 = st.columns(3)

# ----------------------------- #
# --- 1. Klimaüberwachung ---  #
# ----------------------------- #
with col1:
    st.image("KLimaüberwachung.jpg", width=100)
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

# ------------------------------------------- #
# --- 2. Pflanzen- & Bodenüberwachung ---     #
# ------------------------------------------- #
with col2:
    st.image("Pflanzenüberwachung.jpg", width=100)
    st.markdown("**Gewächshaus Paprika**")

    boden_data = [
        ("Bodenfeuchte", "41 %", "25–40 %", "🟠 Leicht erhöht"),
        ("EC-Wert (Düngesalze)", "3.0 mS/cm", "1.0–2.0 mS/cm", "🔴 Deutlich zu hoch"),
        ("pH-Wert (Wasser)", "7.5", "5.8–6.5", "🔴 Zu basisch")
    ]

    for param, ist, soll, status in boden_data:
        st.markdown(f"""
        <div style='margin-bottom: 1rem; padding: 0.5rem; background-color: #1e1e1e; border-radius: 8px;'>
            <strong>{param}</strong><br>
            Ist-Wert: <span style='color:#fff;'>{ist}</span><br>
            Sollbereich: <span style='color:#aaa;'>{soll}</span><br>
            Status: <span style='font-weight:bold;'>{status}</span>
        </div>
        """, unsafe_allow_html=True)

# ------------------------------------------ #
# --- 3. Wassermanagement & Sicherheit ---   #
# ------------------------------------------ #
with col3:
    st.image("Wassermanagement.jpg", width=100)
    st.markdown("**Gewächshaus Paprika**")

    wasser_data = [
        ("Wasserqualität (NTU)", "5.0 NTU", "0–2 NTU", "🔴 Kritisch – Wasser evtl. gekippt")
    ]

    for param, ist, soll, status in wasser_data:
        st.markdown(f"""
        <div style='margin-bottom: 1rem; padding: 0.5rem; background-color: #1e1e1e; border-radius: 8px;'>
            <strong>{param}</strong><br>
            Ist-Wert: <span style='color:#fff;'>{ist}</span><br>
            Sollbereich: <span style='color:#aaa;'>{soll}</span><br>
            Status: <span style='font-weight:bold;'>{status}</span>
        </div>
        """, unsafe_allow_html=True)
