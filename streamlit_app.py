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
#MainMenu, footer, header {
    visibility: hidden;
}
a { text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# ---- Header Layout with Logo, Dropdown, and Button ----
col1, col2, col3, col4 = st.columns([2, 5, 1, 1])

with col1:
    if st.button(" ", key="logo_btn"):
        st.session_state.page = "Dashboard"
    st.image("LOGOBODO.jpg", width=140)

with col2:
    st.write("")  # Spacer

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

    if category == "Paprika":
        # --- Column 1 ---
        with col1:
            st.image("KLimaüberwachung.jpg", width=120)

            klima_data = [
                ("Temperatur (Luft)", "25 °C", "18–24 °C", "🔴 Zu hoch"),
                ("Luftfeuchtigkeit", "81 %", "60–80 %", "🟠 Grenzwertig"),
                ("CO₂-Konzentration", "1001 ppm", "600–1000 ppm", "🟠 Grenzwertig"),
                ("Lichtintensität", "225 µmol/m²/s", "150–300 µmol/m²/s", "🟢 OK"),
                ("Blatt-Temperatur", "27 °C", "18–26 °C", "🔴 Zu hoch")
            ]

            for param, ist, soll, status in klima_data:
                st.markdown(f"""
                <div class='card'>
                    <strong>{param}</strong><br>
                    Ist-Wert: <span>{ist}</span><br>
                    Sollbereich: <span style='color:#555;'>{soll}</span><br>
                    Status: <span style='font-weight:bold;'>{status}</span>
                </div>
                """, unsafe_allow_html=True)

        # --- Column 2 ---
        with col2:
            st.image("Pflanzenüberwachung.jpg", width=120)

            boden_data = [
                ("Bodenfeuchte", "41 %", "25–40 %", "🟠 Leicht erhöht"),
                ("EC-Wert (Düngesalze)", "3.0 mS/cm", "1.0–2.0 mS/cm", "🔴 Deutlich zu hoch"),
                ("pH-Wert (Wasser)", "7.5", "5.8–6.5", "🔴 Zu basisch")
            ]

            for param, ist, soll, status in boden_data:
                st.markdown(f"""
                <div class='card'>
                    <strong>{param}</strong><br>
                    Ist-Wert: <span>{ist}</span><br>
                    Sollbereich: <span style='color:#555;'>{soll}</span><br>
                    Status: <span style='font-weight:bold;'>{status}</span>
                </div>
                """, unsafe_allow_html=True)

        # --- Column 3 ---
        with col3:
            st.image("Wassermanagement.jpg", width=120)

            wasser_data = [
                ("Wasserqualität (NTU)", "5.0 NTU", "0–2 NTU", "🔴 Kritisch – Wasser evtl. gekippt")
            ]

            for param, ist, soll, status in wasser_data:
                st.markdown(f"""
                <div class='card'>
                    <strong>{param}</strong><br>
                    Ist-Wert: <span>{ist}</span><br>
                    Sollbereich: <span style='color:#555;'>{soll}</span><br>
                    Status: <span style='font-weight:bold;'>{status}</span>
                </div>
                """, unsafe_allow_html=True)

    else:
        # Empty layout for "Karotten"
        with col1:
            st.image("KLimaüberwachung.jpg", width=120)
            st.info("Keine Daten für Karotten – Klimaüberwachung.")

        with col2:
            st.image("Pflanzenüberwachung.jpg", width=120)
            st.info("Keine Daten für Karotten – Pflanzenüberwachung.")

        with col3:
            st.image("Wassermanagement.jpg", width=120)
            st.info("Keine Daten für Karotten – Wassermanagement.")

# ---- PAGE 2: Handlungsempfehlungen ----
elif st.session_state.page == "Recommendations":
    st.title("📋 Handlungsempfehlungen")
    st.markdown("Hier erscheinen Ihre individuellen Empfehlungen basierend auf aktuellen Messwerten.")

    st.info("Diese Seite ist derzeit leer – zukünftige Empfehlungen erscheinen hier automatisch.")
