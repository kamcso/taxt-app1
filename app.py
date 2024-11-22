import streamlit as st
import seaborn as sns

st.markdown('# Hello this is my first website.')

st.header('This is my header.')
st.subheader("This is my subheader.")
st.write('This is normal text.')

columns = st.columns(2)

with columns[0]:
    st.image('image.jpeg')

    if st.checkbox('Click here'):
        st.write("I'm clicked")

    if st.button('Click me'):
        st.write('Yay')

with columns[1]:
    value = st.slider('My first slider', 0, 100)
    st.write(value)

    df = sns.load_dataset('tips')

    st.line_chart(df.tip)
