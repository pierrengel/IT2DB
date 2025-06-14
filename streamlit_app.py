import streamlit as st

# ---- Page Setup ----
st.set_page_config(layout="wide")

# ---- Hide Streamlit UI Elements ----
custom_css = """
    <style>
    #MainMenu, footer, header {
        visibility: hidden;
    }

    /* Layout: logo left, title next to it */
    .header-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2rem;
    }

    .logo-title {
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .logo-title img {
        height: 80px;
    }

    .small-selectbox select {
        font-size: 0.85rem;
        padding: 0.3rem 0.5rem;
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ---- Top Header Bar Layout ----
st.markdown("""
    <div class="header-bar">
        <div class="logo-title">
            <img src="ea9acaba-566c-48e5-8554-b5bdbd5461db.png" alt="Logo">
            <h1>BODO</h1>
        </div>
        <div class="small-selectbox">
""", unsafe_allow_html=True)

# Toggle in top-right
st.selectbox("Category", ["C1", "C2", "C3"], key="main")

st.markdown("</div></div>", unsafe_allow_html=True)

# ---- Main Area (Empty for now) ----
st.empty()
