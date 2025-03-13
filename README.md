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

## How It Works

### 1. Imports and Global Variables

```python
import csv
import os
from datetime import datetime

# Global variables
expenses = []
monthly_budget = 0
```

The application uses:
- `csv` module for file operations
- `os` module to check if files exist
- `datetime` module for date validation
- Two global variables to store expenses and budget

### 2. Adding Expenses

Users can add expenses with:
- Date in YYYY-MM-DD format (with validation)
- Category (e.g., Food, Travel, Utilities)
- Amount (validated to ensure it's a positive number)
- Description

Each expense is stored as a dictionary in the expenses list.

### 3. Viewing Expenses

Displays all recorded expenses in a formatted table with:
- Headers for Date, Category, Amount, and Description
- Each expense on a separate row
- Data validation to ensure all required fields exist
- Total expenses calculated and displayed at the bottom

### 4. Budget Management

Two functions handle budget tracking:
- `set_budget()`: Allows users to set their monthly budget
- `track_budget()`: Compares total expenses against the budget and displays:
  - Monthly budget amount
  - Total expenses
  - Warning if over budget with the amount exceeded
  - Remaining balance if under budget

### 5. File Handling

The application saves and loads expenses from a CSV file:
- `save_expenses()`: Writes all expenses to expenses.csv
- `load_expenses()`: Reads expenses from the file when the program starts
- Automatic conversion between data types (float for amounts)
- Error handling for file operations

### 6. Menu Interface

A simple menu interface guides users through the application:
- Display of available options
- Input validation for menu choices
- Function calls based on user selection
- Option to save expenses before exiting

## Usage Example

1. Start the program
2. Add your expenses through the menu
3. Set a monthly budget
4. Track your spending against your budget
5. View your expenses in a formatted table
6. Save your data for the next session

## Data Persistence

Your expenses are saved to a CSV file ('expenses.csv') in the same directory as the script. When you restart the program, it automatically loads your previous expenses.

## Note

This is a simple command-line application designed for educational purposes. It demonstrates basic Python programming concepts like:
- Functions and modular code
- Data validation and error handling
- File I/O operations
- User interaction through the console
