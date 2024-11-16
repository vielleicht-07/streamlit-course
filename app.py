import streamlit as st
import pandas as pd


##################### PAGE SETUP ###################

st.set_page_config(
    page_title="Personalized Favorites App",
    layout="centered",
    page_icon="🚗",
    initial_sidebar_state="collapsed"
)

##################### PAGE SETUP ###################



# 1. Title
st.title("Streamlit Components Demo")

# 2. Header
st.header("This is a Header")

# 3. Subheader
st.subheader("This is a Subheader")

# 4. Text
st.text("Streamlit makes it easy to create web apps for data science.")

# 5. Markdown
st.markdown("**Markdown** lets you style text with *italics*, **bold**, and [links](https://streamlit.io).")

# 6. Input Widgets
name = st.text_input("Enter your name:")
st.write(f"My name is, {name}!")

# 6. Input Widgets
color = st.text_input("Enter your favorite color:")
st.write(f"Your favorite color is, {color}!")

# 6. Input Widgets
animal = st.text_input("Enter your favorite animal:")
st.write(f"Your favorite animal is, {animal}!")



if "selectbox_visible" not in st.session_state:
    st.session_state.selectbox_visible = False

favorite_number = st.number_input("Choose your favorite number:")
st.write(f"Your favorite number is {favorite_number}!")

if st.button("Generate your favorite app"):
    st.session_state.selectbox_visible = True

if st.session_state.selectbox_visible:
    selectbox = st.selectbox("Choose an option:", ["Visual Studio Code", "Jupyter Notebook", "I don't know"])
    st.write(f"You selected: {selectbox}")