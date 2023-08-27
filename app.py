import streamlit as st

st.write('Hello world!')

slider = st.slider("Select a value", 0, 100)
st.write("The value selected is", slider)



st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')