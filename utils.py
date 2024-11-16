import pandas as pd

def load_data():
    ev_sales_df = "https://api.iea.org/evs?parameters=EVsales&category=Historical&mode=Cars&csv=true"
    ev_sales_df = pd.read_csv(ev_sales_df)
    ev_sales_df = ev_sales_df[ev_sales_df["parameter"] == "EV sales"]
    cols_to_drop = ["mode", "category", "parameter"]
    ev_sales_df = ev_sales_df.drop(columns=cols_to_drop)
    
    return ev_sales_df

