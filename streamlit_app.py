import streamlit as st

# Set wide layout
st.set_page_config(layout="wide")

# ---- Sidebar Layout ----
with st.sidebar:
    # Placeholder logo
    st.image("https://via.placeholder.com/150x80?text=LOGO")

    # Main Category Selection
    main_category = st.radio("Select Main Category", ["C1", "C2", "C3"])

    # Sub-category Toggle based on Main Category
    st.markdown(f"### Submenu for {main_category}")
    sub_category = st.selectbox("Select Sub-category", ["CAT1", "CAT2", "CAT3"])

# ---- Main Area ----
st.title("Dashboard View")
st.write(f"You selected **{main_category}** > **{sub_category}**")
