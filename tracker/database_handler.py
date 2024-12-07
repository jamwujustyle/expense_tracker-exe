import sqlite3 
from expenses import Expense

DATABASE_PATH = 'expenses.db'

def create_table():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                       id integer primary key autoincrement,
                       name TEXT,
                       category TEXT,
                       amount REAL
                       )
                       """)
        conn.commit()
        print("created successfully")
    except sqlite3.Error as ex:
        print(f"creation falied: {ex}")
    finally:
        conn.close()

def insert_expenses(expense): 
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO expenses (name, category, amount) VALUES (?,?,?)"""), (expense.name, expense.category, expense.amount)
        conn.commit()
    except sqlite3.Error as ex:
        print(f"error saving expense to database: {ex}")
    finally:
        conn.close()

def load_expenses_from_db():
    expenses = []
    try: 
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT name, category, amount FROM expenses")
        rows = cursor.fetchall()
        for row in rows:
            name, category, amount = row
            expenses.append(Expense(name, category, amount))
    except sqlite3.Error as ex:
        print(f"error loading expenses from database: {ex}")
    finally:
        conn.close()
    return expenses

if __name__ == "__main__":
    create_table()
