# Day 10 – Contact Manager

> **30 Days of Python Challenge**

## Project Description

This project is a **console-based Contact Manager** developed as part of my **30 Days of Python Challenge**.

The program allows users to manage contact information stored in a CSV file. Users can add, view, search, edit, delete, sort, and filter contacts through a menu-driven interface.

## Features

* Add new contacts
* View all contacts
* Search contacts by ID, name, or phone number
* Edit contact information
* Delete contacts
* Sort contacts by ID
* Sort contacts by name
* Sort contacts by category
* Filter contacts by category
* Prevent duplicate contact IDs
* Validate contact names
* Validate 11-digit phone numbers
* Validate email input
* Validate contact categories
* Store contact information permanently in a CSV file

## Contact Information

Each contact contains:

* Contact ID
* Name
* Phone Number
* Email
* Category

Available categories:

* Family
* Friends
* Work
* Other

## Concepts Used

* Python Functions
* Lists
* Dictionaries
* File Handling
* CSV Files
* `csv` Module
* `csv.DictReader`
* `csv.DictWriter`
* `os` Module
* `os.path.exists()`
* `os.path.getsize()`
* `for` Loops
* `while` Loops
* Conditional Statements
* List Comprehension
* `enumerate()`
* `sorted()`
* Lambda Functions
* Filtering
* Searching
* Updating and deleting records
* Input Validation
* Exception Handling
* `try-except`
* `ValueError`

## Sorting

The program allows contacts to be sorted according to:

* Contact ID
* Name
* Category

The `sorted()` function and lambda functions are used to organize the contact records.

## Filtering

Contacts can also be filtered according to their category:

```text
Family
Friends
Work
Other
```

Only contacts belonging to the selected category are displayed.

## CSV File Handling

The project uses a CSV file named `contacts.csv` to store contact information.

`csv.DictReader` is used to read contact records as dictionaries, while `csv.DictWriter` is used to write and update contact records.

## How to Run

Make sure Python 3.x is installed on your system.

Run the program using:

```bash
python contact_manager.py
```

The program will create and use `contacts.csv` to store contact records.

## Learning Outcome

Through this project, I practiced working with CSV files and learned how to read and write structured data using `DictReader` and `DictWriter`.

I also improved my understanding of CRUD operations, sorting, filtering, searching, data validation, and lambda functions.

This project helped me move from basic text-file applications to structured data management using CSV files.

## Author

**Mehreen**

**Day 10 of 30 Days of Python Challenge**
