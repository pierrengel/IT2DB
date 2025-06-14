import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Page setup
st.set_page_config(layout="wide")

# Custom CSS
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

# Top bar layout
st.markdown("""
<div class="header-bar">
    <div class="logo-title">
        <img src="35beea88-4e55-4293-81fd-a79450eed37e.png" alt="Logo">
        <h1>BODO</h1>
    </div>
    <div class="dropdown-container">
""", unsafe_allow_html=True)

# Toggle to select category
category = st.selectbox(" ", ["C1", "C2", "C3"], label_visibility="collapsed", key="main_category")
st.markdown("</div></div>", unsafe_allow_html=True)

# Sample content data (can be expanded or pulled from another file later)
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

# Get current category content
selected_content = content[category]

# Layout: 3 columns
col1, col2, col3 = st.columns(3)

for col, name in zip([col1, col2, col3], ["Hihi", "Haha", "Huhu"]):
    with col:
        st.markdown(f"""
        <div class="card-header">
            <img src="https://via.placeholder.com/30" alt="icon">
            <h3>{name}</h3>
        </div>
        """, unsafe_allow_html=True)

        st.write(selected_content[name]["desc"])

        # Histogram plot
        fig, ax = plt.subplots()
        ax.hist(selected_content[name]["data"], bins=20, color="#69b3a2", edgecolor="black")
        ax.set_title(f"{name} Histogram")
        st.pyplot(fig)
