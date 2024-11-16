import streamlit as st
import pandas as pd


##################### PAGE SETUP ###################

# Set up the page
st.set_page_config(
    page_title="RJ",
    layout="centered", # or wide
    page_icon="🚗", # choose your favorite icon
    initial_sidebar_state="collapsed" # or expanded
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


rnumber = st.number_input("Choose your favorite number:")
st.write(f"Your favorite number is, {rnumber}!")


if st.button("Generate your favorite app") == True:
  selectbox = st.selectbox("Choose an option:", ["Visual Studio Code", "jupyter notebook", "idk"])
  st.write(f"You selected: {selectbox}")


 