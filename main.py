import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('Hello, *World!* :sunglasses:')


df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
st.write('Below is a DataFrame:', df2, 'Above is a dataframe.',1234)

st.markdown("###TEXT")

slider = st.slider("Select a value", 0, 100)
st.write("The value selected is", slider)

st.code("""
slider = st.slider("Select a value", 0, 100)
st.write("The value selected is", slider)
"""
)


st.subheader('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')

 
st.subheader("subheader")
st.caption("caption")
st.text("text")

   

# Sidebar
st.sidebar.header("About")
st.sidebar.markdown(
    "[Streamlit](https://streamlit.io) is a Python library that allows the creation of interactive, data-driven web applications in Python."
)

st.sidebar.header("Resources")
st.sidebar.markdown(
    """
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Cheat sheet](https://docs.streamlit.io/library/cheatsheet)
- [Book](https://www.amazon.com/dp/180056550X) (Getting Started with Streamlit for Data Science)
- [Blog](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/) (How to master Streamlit for data science)
"""
)

st.sidebar.header("Deploy")
st.sidebar.markdown(
    "You can quickly deploy Streamlit apps using [Streamlit Community Cloud](https://streamlit.io/cloud) in just a few clicks."
)
