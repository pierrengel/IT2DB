import streamlit as st

# ---- Page Setup ----
st.set_page_config(layout="wide")

# ---- Page Navigation via Session State ----
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# ---- Custom CSS Styling ----
st.markdown("""
<style>
body {
    background-color: white;
    color: #111;
}
[data-testid="stAppViewContainer"] {
    background-color: white;
    color: #111;
}
.card {
    background-color: #f2f2f2;
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 1rem;
}
button[kind="secondary"], div[data-baseweb="select"] {
    background-color: #134e4a !important;
    color: white !important;
    border-radius: 8px !important;
    height: 42px !important;
}
button[kind="secondary"]:hover {
    background-color: #0f3e3a !important;
}
.stButton>button {
    height: 42px !important;
    margin-top: 20px;
}
.stSelectbox > div {
    height: 42px !important;
    margin-top: 20px;
}
#MainMenu, footer, header {
    visibility: hidden;
}
a { text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# ---- Header Layout with Logo, Dropdown, and Button ----
col1, col2, col3, col4 = st.columns([2, 5, 1, 1])

with col1:
    # Logo as dashboard button
    if st.button("", key="logo_click"):
        st.session_state.page = "Dashboard"
    st.image("LOGOBODO.jpg", width=140)

with col2:
    st.write("")

with col3:
    category_map = {
        "Paprika": "C1",
        "Karotten": "C2"
    }
    selection = st.selectbox(" ", list(category_map.keys()), label_visibility="collapsed")
    category = category_map[selection]

with col4:
    if st.button("Handlungsempfehlungen"):
        st.session_state.page = "Recommendations"

# ---- PAGE 1: DASHBOARD ----
if st.session_state.page == "Dashboard":
    col1, col2, col3 = st.columns(3)

    if category == "C1":
        klima_data = [
            ("Temperatur (Luft)", "25 °C", "18–24 °C", "🔴 Zu hoch"),
            ("Luftfeuchtigkeit", "81 %", "60–80 %", "🟠 Grenzwertig"),
            ("CO₂-Konzentration", "1001 ppm", "600–1000 ppm", "🟠 Grenzwertig"),
            ("Lichtintensität", "225 µmol/m²/s", "150–300 µmol/m²/s", "🟢 OK"),
            ("Blatt-Temperatur", "27 °C", "18–26 °C", "🔴 Zu hoch")
        ]
        boden_data = [
            ("Bodenfeuchte", "41 %", "25–40 %", "🟠 Leicht erhöht"),
            ("EC-Wert (Düngesalze)", "3.0 mS/cm", "1.0–2.0 mS/cm", "🔴 Deutlich zu hoch"),
            ("pH-Wert (Wasser)", "7.5", "5.8–6.5", "🔴 Zu basisch")
        ]
        wasser_data = [
            ("Wasserqualität (NTU)", "5.0 NTU", "0–2 NTU", "🔴 Kritisch – Wasser evtl. gekippt")
        ]

    elif category == "C2":
        klima_data = [
            ("Temperatur (Luft)", "21.0 °C", "18–24 °C", "🟢 OK"),
            ("Luftfeuchtigkeit", "70.0 %", "60–80 %", "🟢 OK"),
            ("CO₂-Konzentration", "800.0 ppm", "600–1000 ppm", "🟢 OK"),
            ("Lichtintensität", "225.0 µmol/m²/s", "150–300 µmol/m²/s", "🟢 OK"),
            ("Blatt-Temperatur", "22.0 °C", "18–26 °C", "🟢 OK")
        ]
        boden_data = [
            ("Bodenfeuchte", "32.5 %", "25–40 %", "🟢 OK"),
            ("EC-Wert (Düngesalze)", "1.5 mS/cm", "1.0–2.0 mS/cm", "🟢 OK"),
            ("pH-Wert (Wasser)", "6.15", "5.8–6.5", "🟢 OK")
        ]
        wasser_data = [
            ("Wasserqualität (NTU)", "1.0 NTU", "0–2 NTU", "🟢 OK")
        ]

    # --- Column 1: Klimaüberwachung ---
    with col1:
        st.image("KLimaüberwachung.jpg", width=120)
        for param, ist, soll, status in klima_data:
            st.markdown(f"""
            <div class='card'>
                <strong>{param}</strong><br>
                Ist-Wert: <span>{ist}</span><br>
                Sollbereich: <span style='color:#555;'>{soll}</span><br>
                Status: <span style='font-weight:bold;'>{status}</span>
            </div>
            """, unsafe_allow_html=True)

    # --- Column 2: Bodenüberwachung ---
    with col2:
        st.image("Pflanzenüberwachung.jpg", width=120)
        for param, ist, soll, status in boden_data:
            st.markdown(f"""
            <div class='card'>
                <strong>{param}</strong><br>
                Ist-Wert: <span>{ist}</span><br>
                Sollbereich: <span style='color:#555;'>{soll}</span><br>
                Status: <span style='font-weight:bold;'>{status}</span>
            </div>
            """, unsafe_allow_html=True)

    # --- Column 3: Wassermanagement ---
    with col3:
        st.image("Wassermanagement.jpg", width=120)
        for param, ist, soll, status in wasser_data:
            st.markdown(f"""
            <div class='card'>
                <strong>{param}</strong><br>
                Ist-Wert: <span>{ist}</span><br>
                Sollbereich: <span style='color:#555;'>{soll}</span><br>
                Status: <span style='font-weight:bold;'>{status}</span>
            </di
