import streamlit as st

# ---- Page Setup ----
st.set_page_config(layout="wide")

# ---- Hide Streamlit's default UI ----
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ---- Layout Columns ----
nav_col, main_col = st.columns([1.5, 6])

# ---- Navigation Area (Left) ----
with nav_col:
    st.image("https://via.placeholder.com/150x80?text=LOGO")

    # Simulate toggles with selectboxes
    main_category = st.selectbox("Main Category", ["C1", "C2", "C3"], key="main")
    
    if main_category == "C1":
        sub_category = st.selectbox("Subcategory", ["CAT1", "CAT2", "CAT3"], key="sub_c1")
    elif main_category == "C2":
        sub_category = st.selectbox("Subcategory", ["CAT1", "CAT2", "CAT3"], key="sub_c2")
    else:
        sub_category = st.selectbox("Subcategory", ["CAT1", "CAT2", "CAT3"], key="sub_c3")

# ---- Main Content Area (Right) ----
with main_col:
    st.title("Dashboard Content")
    st.write(f"You selected: **{main_category} > {sub_category}**")
