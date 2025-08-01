from datetime import datetime

import pandas as pd
import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000"

def analytic_by_month_tab():
    col1,col2 = st.columns(2)
    with col1 :
        start_date = st.date_input("start date")
    with col2 :
        end_date = st.date_input("end date")

    if st.button("Get Monthly Analysis") :
        payload = {
            "start_date" : start_date.strftime("%Y-%m-%d"),
            "end_date" : end_date.strftime("%Y-%m-%d")
        }
        response = requests.post(f"{API_URL}/analytics_by_month" , json=payload)
        response = response.json()
        data = {"month_index" : list(response.keys()),
                "total" :  [response[month] for month in response]
                }



        df = pd.DataFrame(data)

        #st.write(df)
        st.table(df)
        st.title("Expense chart by Month")
        st.bar_chart(data= df.set_index("month_index")["total"])

        #st.write(response)


