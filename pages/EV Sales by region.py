import streamlit as st
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

st.subheader("EV Sales by Region")
st.divider()

#region
regions = ev_sales_df["region"].unique()
selected_region = st.selectbox("Select a region:", regions)

#filter data region
filtered_data = ev_sales_df[ev_sales_df["region"] == selected_region]
st.divider()

#show sales chart regipn 
st.bar_chart(filtered_data, x="year", y="value", color="powertrain")

# filter power train
powertrains = filtered_data["powertrain"].unique()   
selected_powertrain = st.selectbox("Select a powertrain:", powertrains)

#filter powertrain
filtered_data_powertrain = filtered_data[filtered_data["powertrain"] == selected_powertrain]

#show  line chart powettrain
st.line_chart(filtered_data_powertrain.groupby("year")["value"].sum())



 
country_selection = st.multiselect("Filter country:", ev_sales_df["region"].unique())

powertrain = st.selectbox("Filter powertrain:", ev_sales_df["powertrain"].unique())

st.line_chart(ev_sales_df[(ev_sales_df.region.isin(country_selection)) & (ev_sales_df.powertrain == powertrain)], x="year", y="value", color="region")
