import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    This is the bio section for Ardit.  
    It can be updated as necessary
    """

    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python.  Feel free to contact me!
"""
st.write(content2)