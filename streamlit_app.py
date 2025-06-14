import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Greenhouse Dashboard")

st.subheader("Current Conditions")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Temperature", "72°F")
col2.metric("Humidity", "68%")
col3.metric("CO₂ levels", "850 ppm")
col4.metric("Soil Moisture", "32%")

st.subheader("Temperature")
data = pd.DataFrame({
    'Time': pd.date_range(start='2025-06-14 00:00', periods=12, freq='H'),
    'Temperature (°F)': [72, 70, 68, 65, 62, 60, 63, 66, 68, 69, 70, 72]
})
chart = alt.Chart(data).mark_line().encode(
    x='Time',
    y='Temperature (°F)'
).properties(width=700, height=300)
st.altair_chart(chart, use_container_width=True)

st.subheader("Recommendations")
with st.container():
    st.markdown("### Open vents to lower the temperature")
    st.markdown("The temperature is above the optimal range, opening the vents can help reduce it.")
