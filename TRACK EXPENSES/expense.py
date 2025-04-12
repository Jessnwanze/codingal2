import csv

def add_expense(expenses, name, amount):
    """Adds an expense to the list."""
    try:
        amount = float(amount)
        expenses.append((name, amount))
        return f"Expense added: {name} - ${amount:.2f}"
    except ValueError:
        return "Error: Please enter a valid amount."

def save_to_csv(expenses, filename="expenses.csv"):
    """Saves the expenses to a CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Expense Name", "Amount"])
        writer.writerows(expenses)
    return "Expenses saved to expenses.csv"

def show_expenses(expenses):
    """Displays all expenses."""
    if not expenses:
        return "No expenses recorded."
    return "\n".join([f"{name}: ${amount:.2f}" for name, amount in expenses])

def main():
    expenses = []
    actions = [
        ("Add Expense", lambda: add_expense(expenses, "Sample Expense", "100")),
        ("Show Expenses", lambda: show_expenses(expenses)),
        ("Save to CSV", lambda: save_to_csv(expenses)),
        ("Exit", lambda: "Exiting...")
    ]
    
    for index, (desc, action) in enumerate(actions, start=1):
        print(f"{index}. {desc}")
    
    results = [action() for _, action in actions]
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
