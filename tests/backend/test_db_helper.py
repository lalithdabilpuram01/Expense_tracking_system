from backend import db_helper

def test_fetch_expenses_by_date():
    expenses =  db_helper.fetch_expenses_by_date("2024-08-1")

    assert len(expenses) ==1
    print("testing expense amount********")
    assert expenses[0]['amount'] == 300.0
    print("testing expense category********")
    assert expenses[0]['category'] == 'Food'
    #print("printing expensesss***************")
    #print(expenses)
