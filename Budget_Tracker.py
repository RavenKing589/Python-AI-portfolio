# budget.py
import os
import json
from datetime import datetime


FILE = "budget.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {"expenses": [], "income": 0}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_expense(data):
    amount = float(input("Amount: $"))
    desc = input("Description: ")
    data["expenses"].append({
        "amount": amount,
        "desc": desc,
        "date": datetime.now().strftime("%Y-%m-%d")
    })
    save_data(data)

def show_report(data):
    total = sum(e["amount"] for e in data["expenses"])
    print(f"\nTotal Spent: ${total:.2f}")
    print("Expenses:")
    for e in data["expenses"]:
        print(f"  • {e['date']} | ${e['amount']} | {e['desc']}")

def main():
    data = load_data()
    print("BUDGET TRACKER")
    
    while True:
        print("\n[1] Add Expense  [2] View Report  [3] Quit")
        choice = input("> ")
        
        if choice == '1':
            add_expense(data)
        elif choice == '2':
            show_report(data)
        elif choice == '3':
            print("Saved!")
            break

if __name__ == "__main__":
    main()