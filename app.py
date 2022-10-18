
# Example of the custom front end.
import streamlit as st
from streamlit_custom_slider import st_custom_slider
from streamlit_custom_slider import st_range_slider

v_custom = st_custom_slider('First Custom Slider', 0, 100, 50, key="slider1")
st.write(v_custom)

# Add a range slider
v_custom_range = st_range_slider('Range Slider', 0, 100, (20, 60), key="slider2")
st.write(v_custom_range)