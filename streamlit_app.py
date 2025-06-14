import streamlit as st

# ---- Page Setup ----
st.set_page_config(layout="wide")

# ---- Hide Streamlit UI ----
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

    /* Make dropdowns smaller */
    .small-selectbox .stSelectbox > div {
        font-size: 0.85rem !important;
        padding: 0.3rem 0.5rem !important;
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ---- Layout Columns ----
nav_col, main_col = st.columns([2, 6])

with nav_col:
    # Top Logo and Title aligned
    st.markdown("""
        <div class="logo-title">
            <img src="https://via.placeholder.com/100x60.png?text=LOGO" width="100">
            <h2>Dashboard</h2>
        </div>
    """, unsafe_allow_html=True)

    # Smaller dropdowns
    with st.container():
        st.markdown('<div class="small-selectbox">', unsafe_allow_html=True)
        st.selectbox("Main Category", ["C1", "C2", "C3"], key="main_cat")
        st.selectbox("Subcategory", ["CAT1", "CAT2", "CAT3"], key="sub_cat")
        st.markdown('</div>', unsafe_allow_html=True)

# ---- Main area can remain empty for now ----
with main_col:
    st.empty()
