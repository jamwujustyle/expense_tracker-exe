import csv 
from expenses import Expense

def load_expenses_from_csv(file_path='../expenses.csv'):
    expenses = []
    try:
        with open(file_path, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 3: 
                    name, category, amount = row
                    expenses.append(Expense(name, category, float(amount)))
    except FileNotFoundError:
        pass
    except Exception as ex:
        print(f"Error reading CSV file: {ex}")
    return expenses

def save_expense_to_csv(expense, file_path='../expenses.csv'):
    try:
        with open(file_path, mode='a', encoding='utf-8') as f:
            appender = csv.writer(f)
            appender.writerow([expense.name, expense.category, f"{expense.amount:.2f}"])
    except Exception as ex:
        print(f"error saving expense to csv: {ex}")