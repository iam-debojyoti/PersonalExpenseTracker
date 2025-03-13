import csv
import os
from datetime import datetime

# Global variables
expenses = []
monthly_budget = 0


def add_expense():
    """Function to add a new expense"""
    print("\n===== Add Expense =====")

    # Get date with validation
    while True:
        date_str = input("Enter date (YYYY-MM-DD): ")
        try:
            # Validate date format
            datetime.strptime(date_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD.")

    # Get category
    category = input("Enter category (e.g., Food, Travel, Utilities): ")

    # Get amount with validation
    while True:
        amount_str = input("Enter amount spent: ")
        try:
            amount = float(amount_str)
            if amount <= 0:
                print("Amount must be greater than zero!")
            else:
                break
        except ValueError:
            print("Invalid amount! Please enter a number.")

    # Get description
    description = input("Enter a brief description: ")

    # Create expense dictionary and add to list
    expense = {
        'date': date_str,
        'category': category,
        'amount': amount,
        'description': description
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    """Function to view all expenses"""
    print("\n===== Your Expenses =====")

    if not expenses:
        print("No expenses recorded yet.")
        return

    # Display header
    print(f"{'Date':<12} {'Category':<15} {'Amount':<10} {'Description':<30}")
    print("-" * 67)

    # Loop through and display expenses
    for expense in expenses:
        # Validate that all fields exist
        if all(key in expense for key in ['date', 'category', 'amount', 'description']):
            print(
                f"{expense['date']:<12} {expense['category']:<15} ${expense['amount']:<9.2f} {expense['description']:<30}")
        else:
            print("Incomplete expense entry found and skipped.")

    # Display total
    total = sum(expense['amount'] for expense in expenses if 'amount' in expense)
    print("-" * 67)
    print(f"Total expenses: ${total:.2f}")


def set_budget():
    """Function to set monthly budget"""
    global monthly_budget

    print("\n===== Set Monthly Budget =====")

    while True:
        budget_str = input("Enter your monthly budget: ")
        try:
            monthly_budget = float(budget_str)
            if monthly_budget <= 0:
                print("Budget must be greater than zero!")
            else:
                break
        except ValueError:
            print("Invalid amount! Please enter a number.")

    print(f"Monthly budget set to ${monthly_budget:.2f}")


def track_budget():
    """Function to track expenses against budget"""
    print("\n===== Budget Tracker =====")

    if monthly_budget == 0:
        print("You haven't set a monthly budget yet!")
        choice = input("Would you like to set a budget now? (y/n): ")
        if choice.lower() == 'y':
            set_budget()
        else:
            return

    # Calculate total expenses
    total_expenses = sum(expense['amount'] for expense in expenses if 'amount' in expense)

    print(f"Monthly Budget: ${monthly_budget:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")

    # Compare with budget
    if total_expenses > monthly_budget:
        overspent = total_expenses - monthly_budget
        print(f"Warning: You have exceeded your budget by ${overspent:.2f}!")
    else:
        remaining = monthly_budget - total_expenses
        print(f"You have ${remaining:.2f} left for the month.")


def save_expenses():
    """Function to save expenses to a CSV file"""
    filename = "expenses.csv"

    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
            writer.writeheader()
            writer.writerows(expenses)

        print(f"\nExpenses saved to {filename} successfully!")
    except Exception as e:
        print(f"\nError saving expenses: {e}")


def load_expenses():
    """Function to load expenses from a CSV file"""
    global expenses
    filename = "expenses.csv"

    if not os.path.exists(filename):
        print(f"\nNo saved expenses found. Starting with an empty list.")
        return

    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            expenses = []
            for row in reader:
                # Convert amount from string to float
                if 'amount' in row:
                    row['amount'] = float(row['amount'])
                expenses.append(row)

        print(f"\nLoaded {len(expenses)} expenses from {filename}.")
    except Exception as e:
        print(f"\nError loading expenses: {e}")
        expenses = []


def display_menu():
    """Function to display the main menu"""
    print("\n===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Set Budget")
    print("4. Track Budget")
    print("5. Save Expenses")
    print("6. Exit")

    while True:
        choice = input("\nEnter your choice (1-6): ")
        if choice in ['1', '2', '3', '4', '5', '6']:
            return choice
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


def main():
    """Main function to run the expense tracker"""
    print("Welcome to Personal Expense Tracker!")

    # Load any previously saved expenses
    load_expenses()

    while True:
        choice = display_menu()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            set_budget()
        elif choice == '4':
            track_budget()
        elif choice == '5':
            save_expenses()
        elif choice == '6':
            save_choice = input("Do you want to save your expenses before exiting? (y/n): ")
            if save_choice.lower() == 'y':
                save_expenses()
            print("Thank you for using Personal Expense Tracker. Goodbye!")
            break


if __name__ == "__main__":
    main()