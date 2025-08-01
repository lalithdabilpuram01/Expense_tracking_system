import pandas as pd
tt = [{'month': '2024-08', 'total_expenses': 12523.0}, {'month': '2024-09', 'total_expenses': 3380.0},{'month': '2025-09', 'total_expenses': 3380.0}]


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
    "December": "12"}
breakdown = {}
for row in tt :
    month_number =  row["month"][-2:]
    for key,value in month_dict.items():
        if value == month_number :
            breakdown_key = f"{row["month"][:5]}{key}"
            breakdown[breakdown_key] = row["total_expenses"]

print(breakdown)
data = {"month_index" : list(breakdown.keys()),
        "total" :  [breakdown[month] for month in breakdown]
        }


print(data)
