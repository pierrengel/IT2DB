import streamlit as st

# ---- Page Setup ----
st.set_page_config(layout="wide")

# ---- Hide Streamlit's UI Elements ----
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .small-dropdown .stSelectbox div[data-baseweb="select"] {
        font-size: 0.8rem;
        padding: 0.25rem 0.5rem;
    }

    .logo-title-container {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ---- Top Layout ----
nav_col, main_col = st.columns([2, 6])

with nav_col:
    # LOGO + TITLE (aligned)
    st.markdown(
        """
        <div class='logo-title-container'>
            <img src='https://via.placeholder.com/100x60.png?text=LOGO' width='100'>
            <h2>Dashboard</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Navigation")

    # Smaller toggles using class styling
    with st.container():
        st.markdown('<div class="small-dropdown">', unsafe_allow_html=True)
        main_category = st.selectbox("Main Category", ["C1", "C2", "C3"], key="main")
        sub_category = st.selectbox("Subcategory", ["CAT1", "CAT2", "CAT3"], key="sub")
        st.markdown('</div>', unsafe_allow_html=True)

with main_col:
    st.write(f"### You selected: {main_category} > {sub_category}")
