"""
Author: Mehreen

Project: Expense Tracker

Day 8 of 30 Days of Python Challenge
This program is a console-based Expense Tracker that
allows users to add, view, search, delete, and manage
expenses while calculating total spending and
category-wise expense summaries.
"""
import os
file = "expense.txt"
def add_expense(file):
    while True:
        try:
            amount=int(input("Enter your expense amount: "))
            if amount < 0:
                print("Enter a positive number")
                continue
            break
        except ValueError:
            print("Enter numbers only")
    category=input("Enter category of your expense: ").title()
    date=input("Enter date (YYYY-MM-DD): ")
    note=input("Enter note: ")
    with open(file,"a") as expense_file:
        expense_file.write(f"{amount},{category},{date},{note}\n")
    print("Expense successfully added")
def view_expense(file):
    if os.path.exists(file):
        if os.path.getsize(file) == 0:
            print("File is empty")
        else:
            with open(file,"r") as expense_file:
                print("========= Expenses =========\n")
                for i,line in enumerate(expense_file,start=1):
                    print(f"Expense. {i}")
                    print("-"*28)
                    amount,category,date,note=line.strip().split(",")
                    print(f"Amount: {amount}\nCategory: {category.title()}\nDate: {date}\nNote: {note}\n")
    else:
        print("File does not exists")
def search_expense(file):
    if os.path.exists(file):
        if os.path.getsize(file) == 0:
            print("File is empty")
        else:
            choice_for_search = input("Enter category or date(YYYY-MM-DD) to search expense: ")
            found = False
            with open(file,"r") as expense_file:
                for line in expense_file:
                    amount, category, date, note= line.strip().split(",")
                    if choice_for_search.lower() in category.lower() or choice_for_search in date:
                        print(f"Amount: {amount}, Category: {category}, Date: {date}, Note: {note}")
                        found=True
            if not found:
                print("No such expense present")
    else:
        print("File does not exist")
def delete_expense(file):
    if os.path.exists(file):
        if os.path.getsize(file) == 0:
            print("File is empty")
        else:
            view_expense(file)
            with open(file, "r") as expense_file:
                expenses=expense_file.readlines()
            while True:
                try:
                    choice_for_delete=int(input("Enter number of expense to delete: "))
                    if choice_for_delete > len(expenses) or choice_for_delete <= 0:
                        print("Enter number present in list")
                        continue
                    break
                except ValueError:
                    print("Enter numbers only")
            found=False
            new_expense=[]
            for i,line in enumerate(expenses,start=1):
                amount, category, date, note=line.strip().split(",")
                if choice_for_delete == i:
                    print(f"Deleted Amount: {amount}\nDeleted category: {category}\nDeleted date: {date}\nDeleted note: {note}")
                    found=True
                else:
                    new_expense.append(line)
            with open(file, "w") as expense_file:
                for line in new_expense:
                    expense_file.write(line)
            if not found:
                print("No such expense present")
    else:
        print("File does not exist")        
def total_spent_expense(file):
    if os.path.exists(file):
        if os.path.getsize(file) == 0:
            print("File is empty")
        else:
            total_amount = 0
            with open(file, "r") as expense_file:
                for line in expense_file:
                    amount, category, date, note= line.strip().split(",")
                    total_amount += int(amount)

            print(f"Total amount: {total_amount}")
    else:
        print("File does not exists")
def category_summary(file):
    if os.path.exists(file):
        if os.path.getsize(file) == 0:
            print("File is empty")
        else:
            summary={}
            with open(file, "r") as expense_file:
                for line in expense_file:
                    amount, category, date, note= line.strip().split(",")
                    amount = int(amount)
                    if category in summary:
                        summary[category] += amount
                    else:
                        summary[category] = amount
                for cat,total in summary.items():
                    print(f"{cat} : {total}")
    else:
        print("File does not exists")
def menu():
    print("========= EXPENSE TRACKER =========")
    try:
        choice=int(input("1. Add Expense \n2. View Expenses \n3. Search by Category \n4. Delete Expense \n5. Show Total Spent \n6. Show Category Summary \n7. Exit \nEnter your choice: "))
        if choice==1:
            add_expense(file)
        elif choice==2:
            view_expense(file)
        elif choice==3:
            search_expense(file)
        elif choice==4:
            delete_expense(file)
        elif choice==5:
            total_spent_expense(file)
        elif choice==6:
            category_summary(file)
        elif choice==7:
            exit()
        else:
            print("Enter a choice between 1- 7")
    except ValueError:
        print("Enter numbers only")
while True:
    menu()