import streamlit as st
import pandas as pd
from utils import load_data


##################### PAGE SETUP #####################

st.set_page_config(
    page_title="Super Hero App",
    layout="centered",
    page_icon="🚗",
    initial_sidebar_state="collapsed"
)

##################### DATA LOAD  #####################

ev_sales_df = load_data()

##################### PAGE SETUP #####################


 st,bar_chart(ev_sales_df, x="year", y="value"