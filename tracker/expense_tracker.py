import sys
import datetime 
import calendar 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QComboBox, QTableWidget, QTableWidgetItem, QMessageBox
from expenses import Expense

class ExpenseTrackerApp(QWidget):
    def __init__(self): 
        super().__init__()
        self.expenses = []
        self.setWindowTitle("expense tracker")
        self.setGeometry(200, 200, 800, 600)
        self.layout = QVBoxLayout()
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("expense name: ")
        self.layout.addWidget(self.name_input)
        

        self.category_combobox = QComboBox(self)
        self.category_combobox.addItems(['🍔 Food', '🏠 Home', '💼 Work', '🎉 Fun', '✨ Misc'])
        self.layout.addWidget(self.category_combobox)

        self.amount_input = QLineEdit(self)
        self.amount_input.setPlaceholderText("enter amount: ")
        self.layout.addWidget(self.amount_input)
        
        self.add_button = QPushButton("add expense", self)
        self.add_button.clicked.connect(self.add_expense)
        self.layout.addWidget(self.add_button)

        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["id", "name", "category", 'amount'])
        self.layout.addWidget(self.table)

        self.summary_button = QPushButton("show summary", self)
        self.summary_button.clicked.connect(self.show_summary)
        self.layout.addWidget(self.summary_button)
        self.name_input.setFixedHeight(40)
        self.name_input.setStyleSheet("font-size: 16px;")
        self.amount_input.setFixedHeight(40)
        self.amount_input.setStyleSheet("font-size: 16px;")
        self.category_combobox.setFixedHeight(40)
        self.category_combobox.setStyleSheet("font-size: 16px;")
        self.add_button.setFixedHeight(40)
        self.add_button.setStyleSheet("font-size: 16px;")
        self.summary_button.setFixedHeight(40)
        self.summary_button.setStyleSheet("font-size: 16px;")
        self.table.setStyleSheet("font-size: 16px;")
        self.setLayout(self.layout)
    
    def add_expense(self):
        name = self.name_input.text()
        category = self.category_combobox.currentText()
        try:
            amount = float(self.amount_input.text())
        except ValueError:
            self.show_error("invalid amount try again")
            return

        new_expense = Expense(name, category, amount)
        self.expenses.append(new_expense)

        self.name_input.clear()
        self.amount_input.clear()

        self.load_expenses()

    def load_expenses(self):
        self.table.setRowCount(0)

        for row, expense in enumerate(self.expenses):
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(row + 1))) 
            self.table.setItem(row, 1, QTableWidgetItem(expense.name))
            self.table.setItem(row, 2, QTableWidgetItem(expense.category))
            self.table.setItem(row, 3, QTableWidgetItem(f"{expense.amount:.2f}"))

    def show_summary(self):
        total_spent = sum([expense.amount for expense in self.expenses])
        categories = {}
        for expense in self.expenses:
            if expense.category in categories:
                categories[expense.category] += expense.amount
        else:
            categories[expense.category] = expense.amount

        remaining_budget = 2000 - total_spent

        summary_message = 'expensees summary:\n\n'
        for category, amount in categories.items():
            summary_message += f"{category}: {amount:.2f}\n"
        summary_message += f"\ntotal spent: ${total_spent:.2f}\n"
        summary_message += f"remaining: ${remaining_budget:.2f}\n"

        now = datetime.datetime.now()
        days_in_month = calendar.monthrange(now.year, now.month)[1]
        remaining_days = days_in_month - now.day
        daily_budget = remaining_budget / remaining_days if remaining_days > 0 else 0

        summary_message += f"\nremaining days: {remaining_days} days\n"
        summary_message +=f"budget per day: {daily_budget:.2f}"
        QMessageBox.information(self, "summary", summary_message)
    
    def show_error(self, message):
        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText(message)
        error_dialog.setWindowTitle("error")
        error_dialog.exec_() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTrackerApp()
    window.show()
    sys.exit(app.exec_())