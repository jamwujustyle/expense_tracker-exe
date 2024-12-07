import matplotlib.pyplot as plt
from file_handler import load_expenses_from_csv  # Assuming file_handler.py is in the same directory
from collections import defaultdict

def visualize_expenses(file_path='expenses.csv'):
    # Load expenses from CSV
    expenses = load_expenses_from_csv(file_path)

    # Aggregate expenses by category
    category_totals = defaultdict(float)
    for expense in expenses:
        category_totals[expense.category] += expense.amount

    # Prepare data for visualization
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    # Create a pie chart for expense categories
    plt.figure(figsize=(8, 8))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
    plt.title("Expense Breakdown by Category")
    plt.show()

    # # You can also create a bar chart if you prefer
    # plt.figure(figsize=(10, 6))
    # plt.bar(categories, amounts)
    # plt.xlabel('Category')
    # plt.ylabel('Amount')
    # plt.title('Expenses by Category')
    # plt.xticks(rotation=45)
    # plt.show()

if __name__ == "__main__":
    visualize_expenses()  # This will show the pie chart for expenses
