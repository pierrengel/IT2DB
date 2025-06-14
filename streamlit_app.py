import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ---- Page Setup ----
st.set_page_config(layout="wide")

# ---- Custom CSS Styling ----
st.markdown("""
<style>
#MainMenu, footer, header {
    visibility: hidden;
}

.card-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# ---- Header Layout: Logo | Title | Dropdown ----
col_logo, col_title, col_dropdown = st.columns([1, 4, 1])

with col_logo:
    st.image("LOGOBODO.jpg", width=80)

with col_title:
    st.markdown("<h1 style='margin-top: 20px;'>BODO</h1>", unsafe_allow_html=True)

with col_dropdown:
    category_map = {
        "Paprika": "C1",
        "Karotten": "C2"
    }
    selection = st.selectbox(" ", list(category_map.keys()), label_visibility="collapsed", key="main_category")
    category = category_map[selection]

# ---- Dynamic Content Data ----
content = {
    "C1": {
        "Hihi": {"desc": "Random stuff for Hihi under C1", "data": np.random.randn(50)},
        "Haha": {"desc": "Description blah blah for Haha", "data": np.random.randn(100)},
        "Huhu": {"desc": "Something about Huhu being awesome", "data": np.random.randn(70)},
    },
    "C2": {
        "Hihi": {"desc": "Different data for C2 Hihi", "data": np.random.randn(40)},
        "Haha": {"desc": "C2 Haha content here", "data": np.random.randn(90)},
        "Huhu": {"desc": "All about C2 Huhu", "data": np.random.randn(60)},
    }
}

# ---- Local logo paths for each card ----
logo_paths = {
    "Hihi": "hihi_logo.png",   # Make sure these exist in your project folder
    "Haha": "haha_logo.png",
    "Huhu": "huhu_logo.png"
}

# ---- Main Card Layout ----
col1, col2, col3 = st.columns(3)
for col, name in zip([col1, col2, col3], ["Hihi", "Haha", "Huhu"]):
    with col:
        st.image(logo_paths[name], width=30)
        st.markdown(f"### {name}")
        st.write(content[category][name]["desc"])

        fig, ax = plt.subplots()
        ax.hist(content[category][name]["data"], bins=20, color="#69b3a2", edgecolor="black")
        ax.set_title(f"{name} Histogram")
        st.pyplot(fig)
