import streamlit as st
import requests

st.header("Let's get to know each other")

with st.form('my_form'):
    username = st.text_input("What's your github username?")
    #age = st.number_input("What's your age?")
    #time = st.time_input("What's the time?")
    st.form_submit_button('Submit')

response = requests.get('https://api.github.com/users/' + username).json()



img = st.file_uploader("Upload a picture")

if img:
    st.image(img)
