import streamlit as st

st.title('Weather App')

name = st.text_input('Enter your name', '')
if name:
    st.write(f'Dear {name} , welcome to Weather App')