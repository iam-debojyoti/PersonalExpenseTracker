# Personal Expense Tracker

A simple Python application to help you track your daily expenses, manage your budget, and monitor your spending habits.

## Features

- Add daily expenses with date, category, amount, and description
- View all expenses in a formatted table
- Set monthly budgets and track spending against them
- Save and load expenses from a CSV file
- Simple menu-driven interface for easy navigation

## Installation

No special installation is required beyond having Python installed. Simply download the script and run it:

```bash
python expense_tracker.py
```

## Code Explanation

### 1. Imports and Global Variables

```python
import csv
import os
from datetime import datetime

# Global variables
expenses = []
monthly_budget = 0
```

This section imports necessary modules:
- `csv`: Used for reading and writing CSV files
- `os`: Used to check if files exist on the system
- `datetime`: Used for validating date formats

Two global variables are defined:
- `expenses`: A list that will store all expense entries as dictionaries
- `monthly_budget`: A variable to track the user's set budget amount

### 2. Add Expense Function

```python
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
```

This function:
1. Prompts the user for expense details (date, category, amount, description)
2. Includes data validation to ensure:
   - Date is in the correct YYYY-MM-DD format
   - Amount is a valid number greater than zero
3. Creates a dictionary for each expense with the collected information
4. Adds the expense dictionary to the global list of expenses

### 3. View Expenses Function

```python
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
            print(f"{expense['date']:<12} {expense['category']:<15} ${expense['amount']:<9.2f} {expense['description']:<30}")
        else:
            print("Incomplete expense entry found and skipped.")
    
    # Display total
    total = sum(expense['amount'] for expense in expenses if 'amount' in expense)
    print("-" * 67)
    print(f"Total expenses: ${total:.2f}")
```

This function:
1. Checks if there are any expenses to display
2. Creates a formatted table header
3. Loops through all expenses and displays them in a readable format
4. Validates each expense to ensure all required fields exist before displaying
5. Calculates and displays the total amount spent

### 4. Budget Management Functions

```python
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
```

These two functions handle budget management:

The `set_budget()` function:
1. Prompts the user to enter their monthly budget amount
2. Validates that the input is a number greater than zero
3. Updates the global monthly_budget variable

The `track_budget()` function:
1. Checks if a budget has been set
2. Calculates the total expenses
3. Compares expenses to the budget
4. Displays either a warning if over budget or the remaining amount if under budget

### 5. File Handling Functions

```python
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
```

These functions handle saving and loading expense data:

The `save_expenses()` function:
1. Opens a CSV file for writing
2. Creates a CSV writer that converts dictionaries to rows
3. Writes all expenses to the CSV file
4. Includes error handling to catch any issues during the save process

The `load_expenses()` function:
1. Checks if the expenses file exists
2. Opens and reads the CSV file
3. Converts each row back into a dictionary
4. Converts the amount string back to a float
5. Adds each expense to the global expenses list
6. Includes error handling to ensure the program continues even if the file can't be read

### 6. Menu Interface Functions

```python
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
```

These functions manage the program's control flow:

The `display_menu()` function:
1. Displays a list of options for the user
2. Gets and validates the user's choice
3. Returns the validated choice

The `main()` function:
1. Displays a welcome message
2. Loads any previously saved expenses
3. Enters a loop to continuously display the menu and process user choices
4. Calls the appropriate function based on user selection
5. Offers to save expenses before exiting

The final `if __name__ == "__main__":` line ensures the program runs when executed directly.

## How Expense History is Loaded and Displayed

When you select "View Expenses" from the menu (option 2), the program calls the `view_expenses()` function. Here's how the expense history is handled:

1. **Automatic Loading at Startup**: When the program starts, the `main()` function automatically calls `load_expenses()`, which reads any previously saved expenses from the 'expenses.csv' file into the global `expenses` list.

2. **Current Session + Previous Sessions**: The expenses you see come from both:
   - Expenses added during the current session
   - Expenses loaded from the CSV file from previous sessions

3. **Formatted Display**: The `view_expenses()` function creates a neatly formatted table showing:
   - Date, category, amount, and description of each expense
   - Data validation to ensure each expense is complete
   - Total expenses calculated and displayed at the bottom

4. **Data Persistence**: Your expenses persist between sessions because they're saved to and loaded from a CSV file, allowing you to track expenses over time.

## Usage Example

1. Start the program
2. Add your expenses through the menu
3. Set a monthly budget
4. Track your spending against your budget
5. View your expenses in a formatted table
6. Save your data for the next session

## Note

This is a simple command-line application designed for educational purposes. It demonstrates basic Python programming concepts like:
- Functions and modular code
- Data validation and error handling
- File I/O operations
- User interaction through the console
