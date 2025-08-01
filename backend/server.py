from typing import List
from fastapi import FastAPI, HTTPException
from datetime import date
from pydantic import BaseModel
import db_helper
from logging_setup import setup_logger


logger = setup_logger('server')

app = FastAPI()


class Expense(BaseModel):
    amount : float
    category : str
    notes : str
class DateRange(BaseModel):
    start_date : date
    end_date :date
@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    logger.info(f" get_expenses is called for {expense_date}")
    expenses = db_helper.fetch_expenses_by_date(expense_date)
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expenses(expense_date : date, expenses: List[Expense]):
    logger.info(f" add_or_update_expenses is called for {expense_date}")
    db_helper.delete_expense_for_date(expense_date)
    for expense in expenses :
        db_helper.insert_expense(expense_date, expense.amount, expense.category,expense.notes)
    return " expense request updated"

@app.post("/analytics_by_category")
def analytical_data_by_category(date_range : DateRange):
    logger.info(f" analytical_data_by_category is called from {date_range.start_date} to {date_range.end_date}")
    data = db_helper.fetch_expense_summary(date_range.start_date,date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500 , detail = "Failed to retrieve expense summary from database")
    breakdown = {}
    total = sum(row['total'] for row in data)
    for row in data:
        percentage = (row['total']/total)*100 if total != 0 else 0
        breakdown[row['category']] = {
            'total' : row['total'],
            'percentage' : percentage

        }

    return breakdown

@app.post("/analytics_by_month")
def  analytical_data_by_month(date_range :DateRange) :
    logger.info(f" analytical_data_by_month is called from {date_range.start_date} to {date_range.end_date}")
    data = db_helper.fetch_data_by_month(date_range.start_date,date_range.end_date)
    if data is None :
        raise HTTPException(status_code=500 , detail = "Failed to retrieve expense by month from database")
    breakdown = {}
    month_dict = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }
    for row in data :
        month_number =  row["month"][-2:]
        for key,value in month_dict.items():
            if value == month_number :
                breakdown_key = f"{row["month"][:5]}{key}"
                breakdown[breakdown_key] = row["total_expenses"]
    return breakdown







