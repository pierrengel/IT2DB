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

.dropdown-container {
    display: flex;
    align-items: center;
}

.dropdown-container > div {
    width: 120px !important;
    margin-top: 0 !important;
}

.card-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 0.5rem;
}

.card-header img {
    height: 30px;
}
</style>
""", unsafe_allow_html=True)

# ---- Top Header Bar ----
st.markdown("""
<div class="header-bar">
    <div class="logo-title">
        <img src="LOGOBODO.jpg" alt="BODO Logo">
        <h1>BODO</h1>
    </div>
    <div class="dropdown-container">
""", unsafe_allow_html=True)

# ---- Category Selector ----
category = st.selectbox(" ", ["Paprika", "Karotten"], label_visibility="collapsed", key="main_category")

# ---- Close the Top Bar ----
st.markdown("</div></div>", unsafe_allow_html=True)

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
    },
    "C3": {
        "Hihi": {"desc": "Wow C3 Hihi is here", "data": np.random.randn(80)},
        "Haha": {"desc": "C3 Haha got a new thing", "data": np.random.randn(110)},
        "Huhu": {"desc": "And here's C3 Huhu's best bit", "data": np.random.randn(95)},
    }
}

# ---- Local logo paths for each card ----
logo_paths = {
    "Hihi": "hihi_logo.png",   # Replace with actual filenames
    "Haha": "haha_logo.png",
    "Huhu": "huhu_logo.png"
}

# ---- Main Card Layout ----
col1, col2, col3 = st.columns(3)
for col, name in zip([col1, col2, col3], ["Hihi", "Haha", "Huhu"]):
    with col:
        st.markdown(f"""
        <div class="card-header">
            <img src="{logo_paths[name]}" alt="{name} Logo">
            <h3>{name}</h3>
        </div>
        """, unsafe_allow_html=True)

        st.write(content[category][name]["desc"])

        fig, ax = plt.subplots()
        ax.hist(content[category][name]["data"], bins=20, color="#69b3a2", edgecolor="black")
        ax.set_title(f"{name} Histogram")
        st.pyplot(fig)
