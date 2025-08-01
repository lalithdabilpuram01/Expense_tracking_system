from add_update_ui import add_update_tab
from analytic_by_category import analytic_by_category_tab
from analytic_by_month import analytic_by_month_tab
import streamlit as st


API_URL = "http://127.0.0.1:8000"

st.title("Expense Tracking System")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics by Category", "Analytics by Month"])

with tab1 :
    add_update_tab()

with tab2:
    analytic_by_category_tab()

with tab3:
    analytic_by_month_tab()





