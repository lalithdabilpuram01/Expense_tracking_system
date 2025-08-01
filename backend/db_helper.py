import mysql.connector
from contextlib import contextmanager
import os
import sys
from logging_setup import setup_logger

logger = setup_logger('db_helper')


#print("**file**",__file__)


@contextmanager
def get_db_cursor(commit = False):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "rootroot",
        database = "expense_manager"

    )

    cursor = connection.cursor(dictionary =True)
    yield cursor
    if commit:
        connection.commit()

    print("closing cursor")
    cursor.close()
    connection.close()

def fetch_all_data():
    logger.info(f"fetch_all_data called .")
    query = "SELECT * from expenses"

    with get_db_cursor() as cursor :
        cursor.execute(query)
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)

def fetch_expenses_by_date(expense_date):
    logger.info(f"fetch_expense_by_date called with {expense_date}")
    with get_db_cursor() as cursor :
        cursor.execute("SELECT * from expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        print("printing expenses by date****")
        for expense in expenses:
            print(expense)
        return expenses

def insert_expense(expense_date,amount,category,notes):
    logger.info(f"insert_expense called with {expense_date}")
    with get_db_cursor(commit = True) as cursor :
        cursor.execute("INSERT INTO expenses (expense_date,amount,category, notes) VALUES (%s,%s,%s,%s)",
                       (expense_date,amount,category,notes))

def delete_expense_for_date(expense_DATE):
    logger.info(f"delete_expense_for_date called with {expense_DATE}")
    with get_db_cursor(commit=True) as cursor :
        cursor.execute("DELETE  FROM expenses WHERE expense_date = %s", (expense_DATE,))

def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary is called with {start_date} and {end_date}")
    with get_db_cursor() as cursor :
        cursor.execute('''SELECT category, SUM(amount) as total
                                    FROM expenses WHERE expense_date
                                    BETWEEN %s and %s 
                                    GROUP BY category''',(start_date,end_date) )
        data = cursor.fetchall()
        return data

def fetch_data_by_month(start_date, end_date):
    logger.info(f"fetch_data_by_month is called with {start_date} and {end_date}")
    with get_db_cursor() as cursor :
        cursor.execute('''SELECT 
                                DATE_FORMAT(expense_date, '%Y-%m') AS month,
                                SUM(amount) AS total_expenses
                            FROM 
                                expense_manager.expenses
                            WHERE
                            	expense_date Between %s and %s

                            GROUP BY 
                                DATE_FORMAT(expense_date, '%Y-%m')
                            ORDER BY 
                                 month;''',(start_date,end_date))
        data = cursor.fetchall()
        return data





if __name__ == "__main__" :

    #fetch_expenses_by_date("2024-08-20")
    #insert_expense("2024-08-20", 300, "Food", "Panipuri")
    #fetch_all_data()
    #print("*******deleting ********")
    #delete_expense_for_date("2024-08-20")
    #fetch_all_data()
    #print(fetch_expense_summary("2024-08-01","2024-08-05"))
    #project_root = os.path.join(os.path.dirname(__file__),'..')
    #sys.path.insert(0,project_root)
    print(fetch_data_by_month("2024-08-01","2024-09-05"))
    #print("**file**",project_root)