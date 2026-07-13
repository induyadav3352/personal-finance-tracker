import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

FILE_NAME = "transactions.csv"

# Create CSV file if not exists
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=[
        "Date",
        "Type",
        "Category",
        "Amount",
        "Description"
    ])
    df.to_csv(FILE_NAME, index=False)


def add_transaction(transaction_type):
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    description = input("Enter Description: ")

    date = datetime.now().strftime("%Y-%m-%d")

    new_data = pd.DataFrame([[
        date,
        transaction_type,
        category,
        amount,
        description
    ]], columns=[
        "Date",
        "Type",
        "Category",
        "Amount",
        "Description"
    ])

    new_data.to_csv(
        FILE_NAME,
        mode="a",
        header=False,
        index=False
    )

    print("\nTransaction Added Successfully!\n")


def view_transactions():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("\nNo transactions found.\n")
        return

    print("\nTransactions:\n")
    print(df.to_string(index=False))


def show_summary():
    df = pd.read_csv(FILE_NAME)

    income = df[df["Type"] == "Income"]["Amount"].sum()
    expense = df[df["Type"] == "Expense"]["Amount"].sum()

    balance = income - expense

    print("\n========== SUMMARY ==========")
    print(f"Total Income  : ₹{income}")
    print(f"Total Expense : ₹{expense}")
    print(f"Balance       : ₹{balance}")
    print("=============================\n")


def category_summary():
    df = pd.read_csv(FILE_NAME)

    expense_df = df[df["Type"] == "Expense"]

    if expense_df.empty:
        print("No expense records found.")
        return

    print("\nCategory Wise Expenses:\n")
    print(
        expense_df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )


def generate_chart():
    df = pd.read_csv(FILE_NAME)

    expense_df = df[df["Type"] == "Expense"]

    if expense_df.empty:
        print("No expense data available.")
        return

    category_data = (
        expense_df.groupby("Category")["Amount"]
        .sum()
    )

    plt.figure(figsize=(8, 8))

    plt.figure(figsize=(8, 5))

    category_data.plot(kind="bar")

    plt.title("Category Wise Expenses")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.tight_layout()

    plt.savefig("expense_chart.png")

    plt.show()

    print("\nChart saved as expense_chart.png\n")


def delete_transaction():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("No transactions found.")
        return

    print(df)

    index = int(input("\nEnter Row Number to Delete: "))

    df.drop(index=index, inplace=True)
    df.reset_index(drop=True, inplace=True)

    df.to_csv(FILE_NAME, index=False)

    print("Transaction Deleted Successfully.\n")


while True:
    print("\n===== PERSONAL FINANCE TRACKER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Summary")
    print("5. Category-wise Expense Summary")
    print("6. Generate Expense Chart")
    print("7. Delete Transaction")
    print("8. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        add_transaction("Income")

    elif choice == "2":
        add_transaction("Expense")

    elif choice == "3":
        view_transactions()

    elif choice == "4":
        show_summary()

    elif choice == "5":
        category_summary()

    elif choice == "6":
        generate_chart()

    elif choice == "7":
        delete_transaction()

    elif choice == "8":
        print("\nThank you for using Personal Finance Tracker.")
        break

    else:
        print("\nInvalid Choice.")