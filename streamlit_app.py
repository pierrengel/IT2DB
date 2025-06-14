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
#MainMenu, footer, header { visibility: hidden; }
a { text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# ---- HEADER: Logo / Spacer / Dropdown / To-Do / Home ----
col1, col2, col3, col4, col5 = st.columns([2, 4, 1, 1, 1], gap="small")
with col1:
    st.image("LOGOBODO.jpg", width=140)
with col2:
    st.write("")  # spacer
with col3:
    category_map = {"Paprika": "C1", "Karotten": "C2"}
    choice = st.selectbox("", list(category_map.keys()), label_visibility="collapsed")
    category = category_map[choice]
with col4:
    if st.button("To-Do"):
        st.session_state.page = "Recommendations"
with col5:
    if st.button("Home"):
        st.session_state.page = "Dashboard"

# ---- PAGE 1: DASHBOARD ----
if st.session_state.page == "Dashboard":
    c1, c2, c3 = st.columns(3)
    # ... (your existing climate/soil/water data and rendering) ...
    # For brevity I'm omitting unchanged dashboard code here.

# ---- PAGE 2: HANDLUNGSEMPFEHLUNGEN (To-Do) ----
elif st.session_state.page == "Recommendations":
    st.markdown("### 📋 Handlungsempfehlungen")
    st.markdown("Hier erscheinen Ihre individuellen Empfehlungen basierend auf aktuellen Messwerten.")

    colA, colB = st.columns(2, gap="large")
    # Column A: Automatisierte Maßnahmen
    with colA:
        st.markdown("#### ⚙️ Automatisierte Maßnahmen (Auto)")
        if category == "C1":
            st.markdown("""
- 🔴 Die Grenzwerte der Wasserqualität wurden überschritten (5 NTU statt max. 2 NTU). Die Bewässerung wurde deshalb automatisch gestoppt.  
- 🔴 Die Luftfeuchtigkeit liegt mit 81 % über dem optimalen Bereich. Die Lüftung wurde automatisch aktiviert.  
- 🔴 Die Lufttemperatur beträgt 25 °C, die Blatttemperatur liegt zwischen 27 und 29,5 °C. Das Kühlsystem wurde zur Temperatursenkung eingeschaltet.  
- 🔴 Der CO₂-Wert liegt bei 1001 ppm und damit über dem Grenzwert. Die CO₂-Zufuhr wurde automatisch deaktiviert.  
- 🔴 Mehrere kritische Werte wurden gleichzeitig festgestellt. Eine Alarmmeldung wurde an den Betreiber gesendet.
""")
        else:
            st.info("Keine automatischen Maßnahmen für Karotten verfügbar.")

    # Column B: Manuelle Anweisungen
    with colB:
        st.markdown("#### 👨‍🌾 Manuelle Anweisungen (Manuell)")
        if category == "C1":
            st.markdown("""
- 🔴 🧪 **Wassertank prüfen und ggf. reinigen**  
  NTU-Wert stark erhöht – kann auf Algen, Sedimente oder Bakterien im Tank hinweisen.  
- 🟠 🧴 **Frischwasser oder Filter tauschen**  
  Wasserqualität außerhalb Toleranz → evtl. Wasserquelle kontaminiert.  
- 🟠 ⚖️ **Düngergabe unterbrechen/anpassen**  
  EC-Wert bei 3.0–5.5 mS/cm = Überdüngung möglich → Nährstoffbrand vermeiden.  
- 🟠 🧫 **Blätter auf Schimmel / Schädlinge prüfen**  
  Hohe Luftfeuchte + Wärme = optimales Milieu für Pilze.  
- 🟡 🧯 **Manuelle Schattierung aktivieren**  
  Licht in Kombination mit hoher Temperatur kann Verbrennungen fördern.  
- 🟢 🌡️ **Zusätzliche Thermomatten entfernen (falls vorhanden)**  
  Zu hohe Temperaturen → Verdacht auf interne Wärmequellen.  
- 🟢 📋 **Daten manuell protokollieren**  
  Ggf. ergänzen, ob zusätzliche Beobachtungen gemacht wurden (Geruch, Trübung, Geräusche etc.).
""")
        else:
            st.info("Keine manuellen Anweisungen für Karotten verfügbar.")
