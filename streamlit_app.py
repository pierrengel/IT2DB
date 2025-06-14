import streamlit as st

# ---- Page Setup ----
st.set_page_config(layout="wide")

# ---- Hide Streamlit UI Elements ----
custom_css = """
    <style>
    #MainMenu, footer, header {
        visibility: hidden;
    }

    /* Align logo and title */
    .logo-title {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 2rem;
    }

    /* Smaller dropdown styling */
    .small-selectbox select {
        font-size: 0.85rem;
        padding: 0.3rem 0.5rem;
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ---- Layout Columns ----
nav_col, main_col = st.columns([2, 6])

with nav_col:
    # Logo and Title
    st.markdown("""
        <div class="logo-title">
            <img src="https://via.placeholder.com/100x60.png?text=LOGO" width="100">
            <h2>Dashboard</h2>
        </div>
    """, unsafe_allow_html=True)

    # Side-by-side dropdowns
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="small-selectbox">', unsafe_allow_html=True)
        st.selectbox("Main", ["C1", "C2", "C3"], key="main")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="small-selectbox">', unsafe_allow_html=True)
        st.selectbox("Sub", ["CAT1", "CAT2", "CAT3"], key="sub")
        st.markdown('</div>', unsafe_allow_html=True)

# Optional main column remains empty for now
with main_col:
    st.empty()
