# app.py
import streamlit as st 

st.header('Tossing a Coin ')

number_of_trails = st.slider('Number of trials?', 1, 1000, 10)
start_button = st.button('Run')

if start_button:
    st.write(f'Running the expiriment of {number_of_trails} trials')

st.write('It is not a functional application yet. Under construction.:')