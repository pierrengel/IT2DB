import streamlit as st

# ---- Page Setup ----
st.set_page_config(layout="wide")

# ---- Hide Streamlit's default menu and footer ----
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ---- Layout Starts ----

# Create three columns for layout: navigation | spacer | main content
nav_col, _, main_col = st.columns([1.5, 0.1, 6])

with nav_col:
    st.image("https://via.placeholder.com/150x80?text=LOGO")  # Placeholder logo

    # First toggle: Main Category
    with st.expander("C1", expanded=True):
        # Nested toggle: Sub-category
        with st.expander("CAT1", expanded=True):
            st.write("You selected: C1 > CAT1")
        with st.expander("CAT2"):
            st.write("You selected: C1 > CAT2")
        with st.expander("CAT3"):
            st.write("You selected: C1 > CAT3")

    with st.expander("C2"):
        with st.expander("CAT1"):
            st.write("You selected: C2 > CAT1")
        with st.expander("CAT2"):
            st.write("You selected: C2 > CAT2")
        with st.expander("CAT3"):
            st.write("You selected: C2 > CAT3")

    with st.expander("C3"):
        with st.expander("CAT1"):
            st.write("You selected: C3 > CAT1")
        with st.expander("CAT2"):
            st.write("You selected: C3 > CAT2")
        with st.expander("CAT3"):
            st.write("You selected: C3 > CAT3")

with main_col:
    st.title("Main Content Area")
    st.write("This is where your dashboard content would appear.")
