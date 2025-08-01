from datetime import datetime

import pandas as pd
import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000"

def analytic_by_category_tab():
    col1,col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024,8,1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024,8,8))

    if st.button("Get Analytics") :
        payload = {
            "start_date" : start_date.strftime("%Y-%m-%d"),
            "end_date" : end_date.strftime("%Y-%m-%d")
        }
        response = requests.post(f"{API_URL}/analytics_by_category/",json=payload)
        response = response.json()

        data = {"Category" : list(response.keys()),
                "Total" : [response[category]["total"] for category in response],
                "Percentage" : [response[category]["percentage"] for category in response]

                }

        df = pd.DataFrame(data)
        df_sorted = df.sort_values("Percentage", ascending=False)
        st.table(df_sorted)
        st.title("Expense Breakdown in Bar Chart ")
        st.bar_chart(data=df_sorted.set_index("Category")["Percentage"])
        #st.write(response)

#if __name__ == "__main__":
#    print(analytic_tab())


