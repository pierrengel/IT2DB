import streamlit as st

# Page setup
st.set_page_config(layout="wide")

# Custom CSS
st.markdown("""
<style>
/* Hide Streamlit native UI */
#MainMenu, footer, header {
    visibility: hidden;
}

/* Flexbox for header layout */
.header-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
}

/* Left: logo and title */
.logo-title {
    display: flex;
    align-items: center;
    gap: 1rem;
}
.logo-title img {
    height: 80px;
}

/* Right: small dropdown */
.dropdown-container {
    display: flex;
    align-items: center;
}
.dropdown-container > div {
    width: 120px !important;
    margin-top: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# Header row layout
st.markdown("""
<div class="header-bar">
    <div class="logo-title">
        <img src="35beea88-4e55-4293-81fd-a79450eed37e.png" alt="Logo">
        <h1>BODO</h1>
    </div>
    <div class="dropdown-container">
""", unsafe_allow_html=True)

# Very small right-aligned selectbox
st.selectbox(" ", ["C1", "C2", "C3"], label_visibility="collapsed", key="main_category")

# Close the header layout
st.markdown("</div></div>", unsafe_allow_html=True)

# Content placeholder
st.empty()
