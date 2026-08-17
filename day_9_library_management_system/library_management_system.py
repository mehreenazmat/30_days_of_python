"""
Author: Mehreen


Project: Library Management System

Day 9 of 30 Days of Python Challenge

This program is a console-based Library Management System
that allows users to add, view, search, borrow, return,
and delete books while managing borrowing dates and
calculating fines for overdue books.
"""
import os
import datetime
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "books.txt")
borrow_days_limit = 7
def book_formate(book_id, book_name, book_author, status, borrowed_date=None):
    return f"{book_id}, {book_name}, {book_author}, {status}" + (f", {borrowed_date}" if borrowed_date else "")
def add_books(file):
    while True:
        book_id = input("Enter book ID: ").strip()
        if os.path.exists(file) and os.path.getsize(file) > 0:
            with open(file, "r") as book_file:
                books=book_file.readlines()
            found = False
            for line in books:
                data = [item.strip() for item in line.strip().split(",")]
                if book_id == data[0]:
                    print("Book ID already exists! Please enter a unique ID.")
                    found = True 
            if found:
                continue
            else:
                break
        else:
            break
    while True:
        book_name = input("Enter book name: ")
        if book_name.strip() :
            book_name = book_name.title()
            break
        else:
            print("Book name cannot be empty. Please enter a valid name.")
    while True:
        book_author = input("Enter book author: ")
        if book_author.strip():
            book_author = book_author.title()
            break
        else:
            print("Author name cannot be empty. Please enter a valid name.")
    status = "Available"
    with open(file, "a") as book_file:
        book_file.write(book_formate(book_id, book_name, book_author, status) + "\n")
    print("Book successfully added")
def view_books(file):
    if os.path.exists(file):
        if os.path.getsize(file) == 0:
            print("File is empty")
        else:
            print("===== Lists of books =====")
            with open(file, "r") as books_file:
                for i,line in enumerate(books_file, start=1):
                    data = [item.strip() for item in line.strip().split(",")]
                    book_id, book_name, book_author, status = data[:4]
                    borrowed_date = data[4] if len(data) > 4 else "N/A"
                    print(f"Book {i}")
                    print("-"*28+"\n")
                    print(f"Book ID: {book_id}\nBook name: {book_name}\nBook author: {book_author}\nStatus: {status}\nBorrowed date: {borrowed_date}\n")
    else:
        print("No file exists")
def search_books(file):
    if os.path.exists(file):
        if os.path.getsize(file) == 0:
            print("File is empty")
        else:
            search = input("Enter book ID or name you want to search: ").strip()
            with open(file, "r") as books_file:
                found = False
                for line in books_file:
                    data = [item.strip() for item in line.strip().split(",")]
                    book_id, book_name, book_author, status = data[:4]
                    borrowed_date = data[4] if len(data) > 4 else "N/A"
                    if book_id == search or search.lower() in book_name.lower():
                        print("Book found.")
                        print(f"Book ID: {book_id}\nBook name: {book_name}\nBook author: {book_author}\nStatus: {status}\nBorrowed date: {borrowed_date}\n")
                        found = True
                if not found:
                    print("No book found")
    else:
        print("No file exists")
def borrow_books(file):
    if os.path.exists(file):
        if os.path.getsize(file) == 0:
            print("File is empty")
        else:
            view_books(file)
            borrow_choice = input ("Enter book id or name you want to borrow: ").strip()
            found = False
            with open(file, "r") as book_file:
                lines = book_file.readlines()
            with open(file, "w") as book_file:
                for line in lines:
                    data = [item.strip() for item in line.strip().split(",")]
                    book_id, book_name, book_author, status = data[:4]
                    borrowed_date = data[4] if len(data) > 4 else None
                    if book_id == borrow_choice or borrow_choice.lower() in book_name.lower():
                        if status == "Available":
                            status = "Borrowed"
                            found = True
                            borrowed_date = datetime.date.today().strftime("%Y-%m-%d")
                            print(f"You have successfully borrowed the book: {book_name}")
                        else:
                            found = True
                            print(f"Sorry, the book is already borrowed.")
                    book_file.write(book_formate(book_id, book_name, book_author, status, borrowed_date) + "\n")
            if not found:
                print("Book not found.")
    else:
        print("No file exists")
def return_books(file,borrow_days_limit):
    if os.path.exists(file):
        if os.path.getsize(file) == 0:
            print("File is empty")
        else:
            view_books(file)
            return_choice = input("Enter book id or name you want to return: ").strip()
            found = False
            with open(file , "r") as book_file:
                lines = book_file.readlines()
            with open(file , "w") as book_file:
                for line in lines:
                    data = [item.strip() for item in line.strip().split(",")]
                    book_id, book_name, book_author, status = data[:4]
                    borrowed_date = data[4] if len(data) > 4 else None
                    if book_id == return_choice or return_choice.lower() in book_name.lower():
                        if status == "Borrowed":
                            if borrowed_date:
                                borrowed_date_obj = datetime.datetime.strptime(borrowed_date,"%Y-%m-%d").date()
                                returned_date = datetime.date.today()
                                days_borrowed = (returned_date - borrowed_date_obj).days
                                if days_borrowed > borrow_days_limit:
                                    late_days = days_borrowed-borrow_days_limit
                                    print("You have exceeded the borrowing limit. Please return the book within 7 days.")
                                    fine= late_days * 20
                                    print(f"Please pay a fine Rs.{fine}")
                            status = "Available"
                            borrowed_date = None
                            print("You have successfully returned the book.")
                            found = True
                        else:
                            found = True
                            print("This book is not borrowed.")
                    book_file.write(book_formate(book_id, book_name, book_author, status, borrowed_date)+ "\n")
            if not found:
                print("Book not found.")
    else:
        print("No file exists")
def delete_books(file):
    if os.path.exists(file):
        if os.path.getsize(file) == 0:
            print("File is empty")
        else:
            view_books(file)
            found = False
            delete_choice=input("Enter book ID or book name you want to delete: ")
            with open(file, "r") as book_file:
                lines=book_file.readlines()
            with open(file, "w") as book_file:
                for line in lines:
                    data = [item.strip() for item in line.strip().split(",")]
                    book_id, book_name, book_author, status = data[:4]
                    borrowed_date = data[4] if len(data) > 4 else None
                    if book_id == delete_choice or delete_choice.lower() in book_name.lower():
                        if status == "Available":
                            found = True
                            print(f"Book {book_name} has been deleted successfully.")
                            continue
                        else:
                            found = True
                            print("Book is borrowed it cannot be deleted.")
                    book_file.write(book_formate(book_id, book_name, book_author, status, borrowed_date)+ "\n")
                if not found:
                    print("No book found.")    
    else:
        print("No file exists")
def menu():
    print("===== Library Management System =====")
    try:
        choice = int(input("1. Add Book\n2. View Books\n3. Search Book\n4. Borrow Book\n5. Return Book\n6. Delete Book\n7. Exit\nEnter your choice: "))
        if choice == 1:
            add_books(file)
        elif choice == 2:
            view_books(file)
        elif choice == 3:
            search_books(file)
        elif choice == 4:
            borrow_books(file)
        elif choice == 5:
            return_books(file,borrow_days_limit)
        elif choice == 6:
            delete_books(file)
        elif choice == 7:
            print("Exiting program. ")
            return False
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")
    except ValueError:
        print("Invalid input! please enter a number. ")
while True:
    menu()
