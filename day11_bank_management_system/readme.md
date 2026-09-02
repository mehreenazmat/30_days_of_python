# Day 11 – Bank Account Manager

A console-based **Bank Account Manager** built with Python.

This project introduces **Object-Oriented Programming (OOP)** along with CSV file handling to manage bank accounts and transaction records.

## Features

* Create a new bank account
* Generate a unique account ID
* Choose an account type
* Add an initial deposit
* Deposit money into an account
* Withdraw money from an account
* Prevent withdrawals when the balance is insufficient
* Check account balance
* View all bank accounts
* Search for an account
* View transaction history
* Delete an account
* Store account information using CSV files
* Store transaction records with date and time

## Concepts Used

* Classes and Objects
* `__init__()` constructor
* Instance methods
* `self`
* Object-oriented programming
* Functions
* Conditional statements
* `while` loops
* `for` loops
* Exception handling
* `try-except`
* File handling
* CSV module
* Lists and dictionaries
* `os` module
* `datetime` module
* Input validation

## Files

### `bank_account_manager.py`

Contains the complete Bank Account Manager program and the `BankAccount` class.

### `bank.csv`

Stores bank account information including:

* Account ID
* Account name
* Account type
* Balance

### `transactions.csv`

Stores transaction information including:

* Account ID
* Transaction type
* Amount
* Current balance
* Date and time

## Menu Options

```text
1. Add Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. View Accounts
6. Search Account
7. Transaction History
8. Delete Account
9. Exit
```

## How It Works

The program uses a `BankAccount` class to organize the functionality of the application.

Account information is stored in `bank.csv`, while deposits and withdrawals are recorded in `transactions.csv`.

The program also validates user input to prevent invalid account IDs, deposits, withdrawals, and menu choices.

## Example

```text
--------Bank Account Manager--------

1. Add Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. View Accounts
6. Search Account
7. Transaction History
8. Delete Account
9. Exit
```

## Learning Outcome

Through this project, I practiced using **classes and objects** in Python and learned how OOP can be combined with CSV file handling to build a more organized application.

## Author

**Mehreen**

Part of my **30 Days of Python Challenge**.
