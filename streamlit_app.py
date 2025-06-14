import streamlit as st

# ---- Page Setup ----
st.set_page_config(layout="wide")

# ---- Page Navigation via Session State ----
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# ---- Custom CSS Styling ----
st.markdown("""
<style>
button[kind="secondary"], div[data-baseweb="select"] {
    background-color: #134e4a !important;
    color: white !important;
    border-radius: 8px !important;
    height: 42px !important;
}
button[kind="secondary"]:hover {
    background-color: #0f3e3a !important;
}
.stButton>button, .stSelectbox > div {
    height: 42px !important;
    margin-top: 20px !important;
}
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ---- Header: Logo + Spacer + Controls ----
col_logo, col_spacer, col_controls = st.columns([2, 7, 3])

with col_logo:
    # BODO logo (not clickable here)
    st.image("LOGOBODO.jpg", width=140)

with col_spacer:
    st.write("")  # Just push controls to the right

with col_controls:
    c1, c2, c3 = st.columns([1,1,1], gap="small")
    with c1:
        category_map = {"Paprika": "C1", "Karotten": "C2"}
        choice = st.selectbox("", list(category_map.keys()), label_visibility="collapsed")
        category = category_map[choice]
    with c2:
        if st.button("To-Do"):
            st.session_state.page = "Recommendations"
    with c3:
        if st.button("Home"):
            st.session_state.page = "Dashboard"

# ---- PAGE 1: DASHBOARD ----
if st.session_state.page == "Dashboard":
    c1, c2, c3 = st.columns(3)

    # Prepare data...
    # (same klima_data / boden_data / wasser_data logic here)

    with c1:
        st.image("KLimaüberwachung.jpg", width=120)
        # render klima_data cards

    with c2:
        st.image("Pflanzenüberwachung.jpg", width=120)
        # render boden_data cards

    with c3:
        st.image("Wassermanagement.jpg", width=120)
        # render wasser_data cards

# ---- PAGE 2: HANDLUNGSEMPFEHLUNGEN ----
elif st.session_state.page == "Recommendations":
    st.markdown("### 📋 Handlungsempfehlungen")
    st.markdown("Hier erscheinen Ihre individuellen Empfehlungen basierend auf aktuellen Messwerten.")

    a, b = st.columns(2)
    with a:
        st.markdown("#### ⚙️ Automatisierte Maßnahmen (Auto)")
    with b:
        st.markdown("#### 👨‍🌾 Manuelle Anweisungen (Manuell)")
