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
    margin-top: 20px !important;
}
.stSelectbox > div {
    height: 42px !important;
    margin-top: 20px !important;
}
#MainMenu, footer, header {
    visibility: hidden;
}
a { text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# ---- Header Layout with Logo, Spacer, Dropdown, To-Do, Home ----
col_logo, col_spacer, col_dd, col_todo, col_home = st.columns([2, 4, 1, 1, 1])

with col_logo:
    # Just the BODO logo
    st.image("LOGOBODO.jpg", width=140)
    # Clicking logo always returns to Dashboard
    if st.button("", key="logo_click", help="Zum Dashboard"):
        st.session_state.page = "Dashboard"

with col_spacer:
    st.write("")  # empty spacer

with col_dd:
    category_map = {"Paprika": "C1", "Karotten": "C2"}
    selection = st.selectbox("", list(category_map.keys()), label_visibility="collapsed")
    category = category_map[selection]

with col_todo:
    if st.button("To-Do"):
        st.session_state.page = "Recommendations"

with col_home:
    if st.button("Home"):
        st.session_state.page = "Dashboard"

# ---- PAGE 1: DASHBOARD ----
if st.session_state.page == "Dashboard":
    c1, c2, c3 = st.columns(3)

    # prepare data
    if category == "C1":
        klima = [
            ("Temperatur (Luft)", "25 °C", "18–24 °C", "🔴 Zu hoch"),
            ("Luftfeuchtigkeit", "81 %", "60–80 %", "🟠 Grenzwertig"),
            ("CO₂-Konzentration", "1001 ppm", "600–1000 ppm", "🟠 Grenzwertig"),
            ("Lichtintensität", "225 µmol/m²/s", "150–300 µmol/m²/s", "🟢 OK"),
            ("Blatt-Temperatur", "27 °C", "18–26 °C", "🔴 Zu hoch")
        ]
        boden = [
            ("Bodenfeuchte", "41 %", "25–40 %", "🟠 Leicht erhöht"),
            ("EC-Wert (Düngesalze)", "3.0 mS/cm", "1.0–2.0 mS/cm", "🔴 Deutlich zu hoch"),
            ("pH-Wert (Wasser)", "7.5", "5.8–6.5", "🔴 Zu basisch")
        ]
        wasser = [
            ("Wasserqualität (NTU)", "5.0 NTU", "0–2 NTU", "🔴 Kritisch – Wasser evtl. gekippt")
        ]
    else:
        klima = [
            ("Temperatur (Luft)", "21.0 °C", "18–24 °C", "🟢 OK"),
            ("Luftfeuchtigkeit", "70.0 %", "60–80 %", "🟢 OK"),
            ("CO₂-Konzentration", "800.0 ppm", "600–1000 ppm", "🟢 OK"),
            ("Lichtintensität", "225.0 µmol/m²/s", "150–300 µmol/m²/s", "🟢 OK"),
            ("Blatt-Temperatur", "22.0 °C", "18–26 °C", "🟢 OK")
        ]
        boden = [
            ("Bodenfeuchte", "32.5 %", "25–40 %", "🟢 OK"),
            ("EC-Wert (Düngesalze)", "1.5 mS/cm", "1.0–2.0 mS/cm", "🟢 OK"),
            ("pH-Wert (Wasser)", "6.15", "5.8–6.5", "🟢 OK")
        ]
        wasser = [
            ("Wasserqualität (NTU)", "1.0 NTU", "0–2 NTU", "🟢 OK")
        ]

    with c1:
        st.image("KLimaüberwachung.jpg", width=120)
        for p, i, s, stt in klima:
            st.markdown(f"""
                <div class='card'>
                  <strong>{p}</strong><br>
                  Ist-Wert: {i}<br>
                  Sollbereich: <span style='color:#555;'>{s}</span><br>
                  Status: <span style='font-weight:bold;'>{stt}</span>
                </div>
            """, unsafe_allow_html=True)

    with c2:
        st.image("Pflanzenüberwachung.jpg", width=120)
        for p, i, s, stt in boden:
            st.markdown(f"""
                <div class='card'>
                  <strong>{p}</strong><br>
                  Ist-Wert: {i}<br>
                  Sollbereich: <span style='color:#555;'>{s}</span><br>
                  Status: <span style='font-weight:bold;'>{stt}</span>
                </div>
            """, unsafe_allow_html=True)

    with c3:
        st.image("Wassermanagement.jpg", width=120)
        for p, i, s, stt in wasser:
            st.markdown(f"""
                <div class='card'>
                  <strong>{p}</strong><br>
                  Ist-Wert: {i}<br>
                  Sollbereich: <span style='color:#555;'>{s}</span><br>
                  Status: <span style='font-weight:bold;'>{stt}</span>
                </div>
            """, unsafe_allow_html=True)

# ---- PAGE 2: HANDLUNGSEMPFEHLUNGEN ----
elif st.session_state.page == "Recommendations":
    st.markdown("### 📋 Handlungsempfehlungen")
    st.markdown("Hier erscheinen Ihre individuellen Empfehlungen basierend auf aktuellen Messwerten.")

    a, b = st.columns(2)
    with a:
        st.markdown("#### ⚙️ Automatisierte Maßnahmen (Auto)")
    with b:
        st.markdown("#### 👨‍🌾 Manuelle Anweisungen (Manuell)")
