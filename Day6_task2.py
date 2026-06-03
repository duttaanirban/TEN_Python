import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expenses.append({
        "name": name,
        "amount": amount
    })

    save_expenses(expenses)
    print("Expense added successfully.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - ₹{expense['amount']}")


def delete_expense(expenses):
    view_expenses(expenses)

    if expenses:
        index = int(input("Enter expense number to delete: ")) - 1

        if 0 <= index < len(expenses):
            expenses.pop(index)
            save_expenses(expenses)
            print("Expense deleted.")
        else:
            print("Invalid choice.")


def total_spending(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print("Total Spending: ₹", total)


def main():
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Total Spending")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            delete_expense(expenses)

        elif choice == "4":
            total_spending(expenses)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()