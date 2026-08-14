# Day 8 – Expense Tracker

> **30 Days of Python Challenge**

## Project Description

This project is a **console-based Expense Tracker** developed as part of my **30 Days of Python Challenge**.

The program allows users to record and manage their expenses using a text file. Users can add, view, search, and delete expenses, as well as calculate their total spending and category-wise expense summary.

## Features

* Add a new expense
* View all saved expenses
* Search expenses by category or date
* Delete an expense
* Calculate total amount spent
* Display category-wise expense summary
* Store expenses in a text file
* Validate expense amounts
* Handle invalid user input
* Check whether the expense file exists
* Handle empty expense files

## Expense Information

Each expense stores:

* Amount
* Category
* Date
* Note

The information is stored in the following format:

```text
Amount,Category,Date,Note
```

## Concepts Used

* Python Functions
* Lists
* Dictionaries
* `while` Loops
* `for` Loops
* `if-elif-else` Conditions
* File Handling
* `open()`
* Reading and writing text files
* `os` Module
* `os.path.exists()`
* `os.path.getsize()`
* String Manipulation
* `split()`
* `enumerate()`
* Dictionary Aggregation
* Exception Handling
* `try-except`
* `ValueError`

## File Handling

The project uses a text file named `expense.txt` to store expense records.

The program uses:

* Append mode (`a`) to add new expenses
* Read mode (`r`) to view and search expenses
* Write mode (`w`) to update the file after deleting an expense

## How to Run

Make sure Python 3.x is installed on your system.

Run the program using:

```bash
python expense_tracker.py
```

## Learning Outcome

Through this project, I practiced working with files to store and manage data persistently. I also improved my understanding of lists, dictionaries, file handling, data searching, deletion, aggregation, and exception handling.

This project helped me understand how Python can be used to build a practical application that stores and processes user data.

## Author

**Mehreen**

**Day 8 of 30 Days of Python Challenge**
