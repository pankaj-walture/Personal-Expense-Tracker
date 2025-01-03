import json
import os

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.budget = 0

    # Set monthly budget
    def set_budget(self):
        while True:
            try:
                budget = float(input("Enter your monthly budget: "))
                self.budget = budget
                print(f"Monthly budget set to: ₹{self.budget:.2f}")
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    # Add a new expense
    def add_expense(self):
        try:
            description = input("Enter expense description: ")
            category = input("Enter expense category (e.g., Food, Rent, Shopping): ")
            amount = float(input("Enter amount spent: ₹"))
            expense = {
                "description": description,
                "category": category,
                "amount": amount
            }
            self.expenses.append(expense)
            print("Expense added successfully!")
        except ValueError:
            print("Invalid amount! Please try again.")

    # Display all expenses
    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        print("\n--- Expenses ---")
        total_spent = 0
        for idx, expense in enumerate(self.expenses, start=1):
            print(f"{idx}. {expense['description']} | Category: {expense['category']} | Amount: ₹{expense['amount']:.2f}")
            total_spent += expense['amount']
        print(f"\nTotal spent: ₹{total_spent:.2f}")
        if self.budget > 0:
            print(f"Remaining budget: ₹{self.budget - total_spent:.2f}")
        else:
            print("Budget not set yet.")

    # Save expenses to file
    def save_to_file(self):
        try:
            filename = "expenses.json"
            data = {"budget": self.budget, "expenses": self.expenses}
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Expenses saved to '{filename}'.")
        except Exception as e:
            print(f"Error saving data: {e}")

    # Load expenses from file
    def load_from_file(self):
        filename = "expenses.json"
        if os.path.exists(filename):
            try:
                with open(filename, "r") as file:
                    data = json.load(file)
                    self.budget = data.get("budget", 0)
                    self.expenses = data.get("expenses", [])
                print("Expenses loaded successfully!")
            except Exception as e:
                print(f"Error loading data: {e}")
        else:
            print("No saved data found.")

    # Main menu
    def menu(self):
        while True:
            print("\n--- Personal Expense Tracker ---")
            print("1. Set Monthly Budget")
            print("2. Add Expense")
            print("3. View Expenses")
            print("4. Save Expenses")
            print("5. Load Expenses")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.set_budget()
            elif choice == "2":
                self.add_expense()
            elif choice == "3":
                self.view_expenses()
            elif choice == "4":
                self.save_to_file()
            elif choice == "5":
                self.load_from_file()
            elif choice == "6":
                print("Exiting... Thank you for using the Expense Tracker!")
                break
            else:
                print("Invalid choice! Please select from 1 to 6.")


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.menu()
