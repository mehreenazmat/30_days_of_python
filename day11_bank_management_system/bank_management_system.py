"""
Author: Mehreen

Project: Bank Account Manager

Day 11 of 30 Days of Python Challenge

This program is a console-based Bank Account Manager
that allows users to create accounts, deposit and withdraw
money, check balances, view accounts, search accounts,
view transaction history, and delete accounts.

This project introduces Object-Oriented Programming (OOP)
using classes and objects along with CSV file handling.
"""

import csv
import os
import datetime
class BankAccount:
    def __init__(self):
        self.file = "bank.csv"
        self.file_2 = "transactions.csv"
    def add_account(self):
        while True:
            account_id = input("Enter account ID: ").strip()
            if not account_id:
                    print("Account ID cannot be empty.")
                    continue
            found = False
            if os.path.exists(self.file) and os.path.getsize(self.file) > 0:
                with open(self.file, "r") as account_file:
                    accounts = csv.DictReader(account_file)
                    for account in accounts:
                        if account_id == account["account_id"]:
                            print("Account ID already exists! Please enter a unique ID.")
                            found = True
                            break
                    if found:
                        continue
            break
        while True:
            name = input("Enter name: ").strip().title()
            if not name:
                print("Name cannot be empty.")
                continue
            else:
                break
        while True:
            account_type = input("Enter account type ['Self', 'Joint', 'Work', 'Other']: ").strip().title()
            if account_type in ['Self', 'Joint', 'Work', 'Other']:
                break
            if not account_type:
                print("Account type cannot be empty.")
            else:
                print("Invalid input. Please enter from options only. ")
        while True:
            balance = input("Enter initial deposit: ").strip()
            if not balance.isdigit():
                print("Invalid input. Add numbers only.")
                continue
            balance = int(balance)
            if balance > 0 :
                break
            else:
                print("Deposit must be greater than zero.")
        with open(self.file, "a", newline="") as account_file:
            fieldnames = ['account_id', 'name', 'type','balance']
            accounts = csv.DictWriter(account_file, fieldnames = fieldnames)
            if os.path.getsize(self.file) == 0:
                accounts.writeheader()
            accounts.writerow({"account_id" : account_id,
                                     "name" : name,
                                     "type" : account_type,
                                     "balance" : balance
                                     })
    def transactions(self,account_id, transaction_type, amount, current_balance):
        with open(self.file_2, "a", newline="") as transaction_file:
            fieldnames = ["account_id", "transaction_type", "amount", "current_balance","date_and_time"]
            writer = csv.DictWriter(transaction_file, fieldnames= fieldnames)
            if os.path.getsize(self.file_2) == 0:
                writer.writeheader()
            date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow({"account_id" : account_id,
                            "transaction_type" : transaction_type,
                            "amount" : amount,
                            "current_balance" : current_balance,
                            "date_and_time" : date_time})
    def deposit_money(self):
        if os.path.exists(self.file):
            if os.path.getsize(self.file) == 0:
                print("File is empty.")
            else:
                while True:
                    deposit_choice = input("Enter ID of bank account to deposit: ").strip()
                    found = False
                    with open(self.file, "r") as account_file:
                        accounts = list(csv.DictReader(account_file))
                        for account in accounts:
                            if deposit_choice == account["account_id"]:
                                while True:
                                    deposit_money = input("Enter deposit: ").strip()
                                    if not deposit_money.isdigit():
                                        print("Invalid input. Please input numbers only.")
                                        continue
                                    deposit_money = int(deposit_money)
                                    if deposit_money <=0:
                                        print("Deposit must be greater than 0.")
                                        continue
                                    else:
                                        account["balance"] = int (account["balance"])
                                        account["balance"] += deposit_money
                                        break
                                found = True
                                break
                    if found:
                        with open(self.file, "w") as account_file:
                            fieldnames = ["account_id", "name", 'type','balance']
                            writer = csv.DictWriter(account_file,fieldnames=fieldnames)
                            writer.writeheader()
                            writer.writerows(accounts)
                       
                        self.transactions(account["account_id"],
                                          transaction_type = "deposit",
                                          amount = deposit_money,
                                          current_balance = account["balance"])
                        print("Amount deposited.")
                        print(f"Current Balance : {account['balance']}")
                        break
                    else:
                        print("No such ID found.")
        else:
            print("File does not exists.")
    def withdraw_money(self):
        if os.path.exists(self.file):
            if os.path.getsize(self.file) == 0:
                print("File is empty.")
            else:
                while True:
                    withdraw_choice = input("Enter ID of bank account to withdraw: ").strip()
                    found = False
                    with open(self.file, "r") as account_file:
                        accounts = list(csv.DictReader(account_file))
                        for account in accounts:
                            if withdraw_choice == account["account_id"]:
                                while True:
                                    withdraw_money = input("Enter amount to withdraw: ").strip()
                                    if not withdraw_money.isdigit():
                                        print("Invalid input. Please input numbers only.")
                                        continue
                                    withdraw_money = int(withdraw_money)
                                    if withdraw_money <= 0:
                                        print("Withdrawal amount must be greater than 0.")
                                        continue
                                    elif withdraw_money > int(account["balance"]):
                                        print("Balance insufficient.")
                                        continue
                                    else:
                                        account["balance"] = int (account["balance"])
                                        account["balance"] -= withdraw_money
                                        break
                                found = True
                                break
                        if found:
                            with open(self.file, "w", newline="") as account_file:
                                fieldnames = ["account_id", "name", 'type','balance']
                                writer = csv.DictWriter(account_file,fieldnames=fieldnames)
                                writer.writeheader()
                                writer.writerows(accounts)
                               
                                self.transactions(account["account_id"],
                                                  transaction_type = "withdraw",
                                                  amount = withdraw_money,
                                                  current_balance = account["balance"])
                                print("Amount Withdrawn.")
                                print(f"Current Balance : {account['balance']}")
                                break
                        else:
                            print("No such ID found.")
        else:
            print("File does not exists.")
    def check_balance(self):
        if os.path.exists(self.file):
            if os.path.getsize(self.file) == 0:
                print("File is empty.")
            else:
                while True:
                    with open(self.file, "r") as bank_file:
                        accounts = csv.DictReader(bank_file)
                        id_account = input("Enter account ID to check balance: ").strip()
                        found = False
                        for account in accounts:
                            if id_account == account["account_id"]:
                                print(f"Your account balance is: {account['balance']}")
                                found = True
                                break
                        if found:
                            break
                        else:
                            print("No such ID found.")
                            continue
        else:
            print("File does not exists.")
    def view_accounts(self):
        if os.path.exists(self.file):
            if os.path.getsize(self.file) == 0:
                print("File is empty.")
            else:
                with open(self.file, "r") as bank_file:
                    accounts = csv.DictReader(bank_file)
                    print("\n"+"-"*8 + "List of Accounts" + "-"*8)
                    for i,account in enumerate(accounts, start=1):
                        print(f"Account{i}")
                        print(f"\nAccount ID: {account['account_id']}\nName: {account['name']}\nType: {account['type']}\nBalance: {account['balance']}")
                        print("\n"+"-"*30+"\n")
        else:
            print("File does not exists.")
    def search_account(self):
        if os.path.exists(self.file):
            if os.path.getsize(self.file) == 0:
                print("File is empty.")
            else:
                while True:
                    with open(self.file, "r") as bank_file:
                        accounts = csv.DictReader(bank_file)
                        id_account = input("Enter account ID to search: ").strip()
                        found = False
                        for account in accounts:
                            if id_account == account["account_id"]:
                                print("Account found.")
                                print(f"Account ID: {account['account_id']}\nName: {account['name']}\nType: {account['type']}\nBalance: {account['balance']}")
                                found = True
                        if found:
                            break
                        else:
                            print("No such ID exists.")
                            continue
        else:
            print("File does not exists.")
    def transaction_history(self):
        if os.path.exists(self.file_2):
            if os.path.getsize(self.file_2) == 0:
                print("File is empty.")
            else:
                while True:
                    with open(self.file_2, "r") as transaction_file:
                        transactions = csv.DictReader(transaction_file)
                        id_account= input("Enter account ID to view transactions history: ").strip()
                        found = False
                        i = 1
                        for transaction in transactions:
                            if id_account == transaction['account_id']:
                                print(f"Transaction{i}")
                                print(f"\nAccount ID: {transaction['account_id']}\nTransaction type: {transaction['transaction_type']}\nAmount: {transaction['amount']}\nCurrent balance: {transaction['current_balance']}\nDate and time: {transaction['date_and_time']}")
                                found = True
                                i +=1
                        if found:
                            break
                        else: 
                            print("No such ID exists.")
                            continue
        else:
            print("File does not exists.")
    def delete_account(self):
         if os.path.exists(self.file):
            if os.path.getsize(self.file) == 0:
                 print("File is empty.")
            else:
                while True:
                    with open(self.file, "r") as account_file:
                        accounts = list(csv.DictReader(account_file))
                        id_account = input("Enter account ID to delete: ").strip()
                        found = False
                        for account in accounts:
                            if id_account == account["account_id"]:
                                accounts.remove(account)
                                found = True
                                break
                        if found:
                            with open(self.file, "w", newline="") as account_file:
                                fieldnames = ["account_id","name", "type", "balance"]
                                writer = csv.DictWriter(account_file, fieldnames=fieldnames)
                                writer.writeheader()
                                writer.writerows(accounts)
                            print("Account deleted successfully.")
                            break
                        else:
                            print("No such ID exists.")
                            continue
         else:
                     print("File does not exists.")
account = BankAccount()
def menu():
    print("-"*8 + "Bank Account Manager" + "-"*8)
    try:
        choice = int(input("\n\n1. Add Account\n2. Deposit Money\n3. Withdraw Money\n4. Check Balance\n5. View Accounts\n6. Search Account\n7. Transaction History\n8. Delete Account\n9. Exit\nEnter your choice: "))
        if choice == 1:
            account.add_account()
        elif choice == 2:
            account.deposit_money()
        elif choice == 3:
            account.withdraw_money()
        elif choice == 4:
            account.check_balance()
        elif choice == 5:
            account.view_accounts()
        elif choice == 6:
            account.search_account()
        elif choice == 7:
            account.transaction_history()
        elif choice == 8:
            account.delete_account()
        elif choice == 9:
            print("Exiting account")
            return False
        else:
            print("Invalid input. Please enter a number between 1 - 9.")
    except ValueError:
        print("Invalid input. Please enter numbers only")
while True:
    if not menu():
        break
    else: 
        continue