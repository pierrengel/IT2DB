import streamlit as st

# ---- Page Setup ----
st.set_page_config(layout="wide")

# ---- Custom CSS ----
custom_css = """
<style>
#MainMenu, footer, header {
    visibility: hidden;
}

/* Top bar layout */
.header-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
}

/* Logo and BODO title */
.logo-title {
    display: flex;
    align-items: center;
    gap: 1rem;
}
.logo-title img {
    height: 80px;
}

/* Small dropdown */
.small-dropdown select {
    font-size: 0.85rem;
    padding: 0.3rem 0.5rem;
    width: 150px;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ---- Layout HTML ----
st.markdown("""
<div class="header-bar">
    <div class="logo-title">
        <img src="e686fd0a-024f-4539-96fa-dc9dd2dcb47f.png" alt="Logo">
        <h1>BODO</h1>
    </div>
    <div class="small-dropdown">
""", unsafe_allow_html=True)

# ---- Dropdown aligned right, small size ----
st.selectbox(" ", ["C1", "C2", "C3"], key="main", label_visibility="collapsed")

# ---- Close the divs ----
st.markdown("</div></div>", unsafe_allow_html=True)

# ---- Main Content Placeholder ----
st.empty()
