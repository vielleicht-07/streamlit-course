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


st.title("🎨 Welcome to the Favorites App!")

st.header("Personalize your app with your favorites!")

st.text("This app helps you choose and display your favorite items interactively.")

st.markdown(
    """
    ### Features:
    - 📋 Input your favorites
    - 🎨 Style your choices
    - 🚀 See results dynamically!
    """
)

st.markdown("---")

st.subheader("Tell us about yourself!")

name = st.text_input("What's your name?", placeholder="Type your name here...")
if name:
    st.success(f"Hi, {name}! 👋")

color = st.text_input("What's your favorite color?", placeholder="Type a color here...")
if color:
    st.info(f"Your favorite color is **{color}** 🌈")

animal = st.text_input("What's your favorite animal?", placeholder="Type an animal here...")
if animal:
    st.warning(f"Wow, you like **{animal}**! 🐾")

number = st.number_input("Choose your favorite number:", step=1, min_value=0, max_value=100)
if number:
    st.write(f"Your favorite number is **{number}** 🎲")

st.markdown("---")

st.subheader("Generate your favorite app 🎛️")
if st.button("Show me options!"):
    selectbox = st.selectbox("Pick your favorite development tool:", ["Visual Studio Code", "Jupyter Notebook", "I don't know"])
    st.success(f"Great choice! You selected: **{selectbox}** 💻")

st.markdown(
    """
    ---
    ### Thank you for using the app! 🚀
    - Feel free to explore more options.
    """
)