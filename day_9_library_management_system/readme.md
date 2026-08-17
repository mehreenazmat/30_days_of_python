# Day 9 – Library Management System

> **30 Days of Python Challenge**

## Project Description

This project is a **console-based Library Management System** developed as part of my **30 Days of Python Challenge**.

The program allows users to manage a collection of books using a text file. Users can add, view, search, borrow, return, and delete books while tracking borrowing dates and calculating fines for overdue books.

## Features

* Add new books
* View all books
* Search books by ID or name
* Borrow books
* Return borrowed books
* Track borrowing dates
* Calculate overdue fines
* Delete available books
* Prevent duplicate book IDs
* Prevent deletion of borrowed books
* Validate book names and authors
* Store book records permanently in a text file
* Handle missing and empty files

## Library Rules

* Books can be borrowed for **7 days**
* A fine of **Rs. 20 per day** is charged for overdue books
* Borrowed books cannot be deleted
* Only available books can be deleted
* Each book must have a unique ID

## Book Information

Each book record contains:

* Book ID
* Book Name
* Book Author
* Status
* Borrowed Date

The data is stored in the following format:

```text
Book ID, Book Name, Book Author, Status, Borrowed Date
```

For available books, the borrowed date is not stored.

## Concepts Used

* Python Functions
* Lists
* File Handling
* Text Files
* `open()`
* Append, Read, and Write Modes
* `os` Module
* `os.path.exists()`
* `os.path.getsize()`
* `datetime` Module
* `datetime.date.today()`
* `datetime.datetime.strptime()`
* Date Calculations
* String Manipulation
* `split()`
* `enumerate()`
* Conditional Statements
* `while` Loops
* `for` Loops
* Exception Handling
* `try-except`
* `ValueError`

## Borrowing and Fine Calculation

When a book is borrowed, the program automatically records the current date.

When the book is returned, the program calculates how many days it was borrowed.

If the borrowing period exceeds **7 days**, the program calculates the fine:

```text
Fine = Late Days × Rs. 20
```

For example:

```text
Days Borrowed = 10
Allowed Days = 7
Late Days = 3

Fine = 3 × 20
Fine = Rs. 60
```

## How to Run

Make sure Python 3.x is installed on your system.

Run the program using:

```bash
python library_management_system.py
```

The `books.txt` file will be used to store the library records.

## Learning Outcome

Through this project, I practiced combining file handling with Python's `datetime` module to create a more realistic management system.

I learned how to store persistent data, update records in a text file, calculate dates, track borrowing periods, apply business rules, and calculate fines based on overdue days.

This project helped me move from simple console applications toward building more practical and structured Python programs.

## Author

**Mehreen**

**Day 9 of 30 Days of Python Challenge**
