"""
Author: Mehreen


Project: Contact Manager
Day 10 of 30 Days of Python Challenge

This program is a console-based Contact Manager that
allows users to add, view, search, edit, delete, sort,
and filter contacts stored in a CSV file.
"""
import os
import csv

file = "contacts.csv"
def add_contact(file):
    while True:
        contact_id = input("Enter contact ID:").strip()
        if not contact_id:
            print("ID cannot be empty")
            continue
        found = False
        if os.path.exists(file) and os.path.getsize(file) > 0:
            with open(file, "r") as contact_file:
                contacts = csv.DictReader(contact_file)
                for contact in contacts:
                    if contact_id == contact["contact_id"]:
                        print("Contact ID already exists! Please enter a unique ID.")
                        found = True
                        break
                if found:
                    continue
        break
    while True:
        contact_name = input("Enter contact name:").strip().title()
        if contact_name:
            break
        else:
            print("Contact name cannot be empty")
            continue
    while True:
            contact_number = input("Enter contact number: ")
            if contact_number.isdigit() and len(contact_number) == 11:
                break
            else:
                print("Invalid input! Please enter a valid 11-digit number.")
                continue
    while True:
        contact_email = input("Enter contact email:").strip()
        if contact_email:
            if "@" in contact_email and "." in contact_email:
                break
            else:
                print("Invalid input!Enter a valid email")
                continue
        else:
            print("Email cannot be empty.")
            continue
    while True:
        contact_category = input("Enter contact category like(Family, Friends, Work, Other): ").strip().title()
        if contact_category:
            if contact_category in ["Family", "Friends", "Work", "Other"]:
                break
            else:
                print("Invalid input. Please enter one from \n\tFamily, Friends, Work or Other.")
        else:
            print("Category cannot be empty")
    with open(file, "a",newline="") as contact_file:
        field_names = ["contact_id", "name", "number", "email", "category"]
        writer = csv.DictWriter(contact_file,fieldnames=field_names)
        if os.path.getsize(file) == 0:
            writer.writeheader()
        writer.writerow({"contact_id" : contact_id,
                         "name" : contact_name,
                         "number" : contact_number,
                         "email" : contact_email,
                         "category" : contact_category
                         })
def view_contacts(file):
    if os.path.exists(file):
        if os.path.getsize(file) == 0:
            print("File is empty")
        else:
            print("-"*8 + "Contacts" + "-"*28)
            with open(file, "r") as contacts_file:
                contacts = csv.DictReader(contacts_file)
                for i,contact in enumerate(contacts,start=1):
                    print(f"Contact{i}")
                    print("-"*28)
                    print(f'Contact ID: {contact["contact_id"]}\nContact name: {contact["name"]}\nContact number: {contact["number"]}\nContact email: {contact["email"]}\nContact category: {contact["category"]}\n')
    else:
        print("No file exists")        
def search_contact(file):
    if os.path.exists(file):
        if os.path.getsize(file) == 0:
            print("File is empty")
        else:
            search_choice = input("Enter ID ,name or number to search contact").strip()
            found = False
            with open(file, "r") as contact_file:
                contacts = csv.DictReader(contact_file)
                for contact in contacts:
                    if search_choice == contact["contact_id"] or search_choice == contact["number"] or search_choice.lower() == contact["name"].lower():
                        found = True
                        print("Contact found")
                        print(f"Contact ID: {contact['contact_id']}\nContact name: {contact['name']}\nContact number: {contact['number']}\nContact email: {contact['email']}\nContact category: {contact['category']}")
                        break
                if not found:
                    print("No such contact found")
    else:
        print("No file exists")
def edit_contact(file):
    if os.path.exists(file):
        if os.path.getsize(file) == 0:
            print("File is empty")
        else:
            view_contacts(file)
            edit_choice = input("Enter contact ID, name or number you want to edit: ").strip()
            found = False
            with open(file, "r") as contact_file:
                contacts = list(csv.DictReader(contact_file))
                for contact in contacts:
                    if edit_choice == contact["contact_id"] or edit_choice == contact["number"] or edit_choice.lower() == contact["name"].lower():
                        while True:
                            found = True
                            edit = input("Enter what do you want to edit [name, number, email, category]: ").strip().lower()
                            if edit.lower() == "name":
                                contact["name"] = input("Enter new name you want to edit: ").strip().title()
                                break
                            elif edit == "number":
                                while True:
                                    number = input("Enter number you want to edit: ").strip()
                                    if number.isdigit() and len(number) == 11:
                                        contact["number"] = number
                                        break
                                    else:
                                        print("Invalid input! Please enter a valid 11-digit number.")
                                        continue
                                break
                            elif edit == "email":
                                while True:
                                    email = input("Enter email you want to edit: ")
                                    if "@" in email and "." in email:
                                        contact["email"] = email
                                        break
                                    else:
                                        print("Invalid input! Please enter a valid email.")
                                break
                            elif edit == "category":
                                while True:
                                    category = input("Enter category you want to change like(Family, Friends, Work, Other): ").strip().title()
                                    if category in ["Family", "Friends", "Work", "Other"]:
                                        contact["category"] = category
                                        break
                                    else:
                                        print("Invalid input! please enter from (Family, Friends, Work, Other)")
                                        continue
                                break
                            else:
                                print("Invalid input! please enter from the given input which you want to change")
                                continue
                if found :
                    with open(file, "w", newline="") as contact_file:
                        fieldnames = ["contact_id", "name", "number", "email", "category"]
                        writer = csv.DictWriter(contact_file,fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(contacts)
                    print("Contact updated successfully")
                else:
                    print("No matching contact found")
    else:
        print("No file exists")
def delete_contact(file):
    if os.path.exists(file):
        if os.path.getsize(file) == 0:
            print("File is empty")
        else:
            view_contacts(file)
            delete_choice = input("Enter ID ,name or number you want to delete : ").strip().lower()
            found = False
            with open(file, "r") as contact_file:
                contacts = list(csv.DictReader(contact_file))
                remaining_contacts = []
                for contact in contacts:
                    if delete_choice == contact["contact_id"] or delete_choice.lower() == contact["name"].lower() or delete_choice == contact["number"]:
                        found = True
                        print("Contact deleted.")
                    else:
                        remaining_contacts.append(contact)
            if found:
                with open(file, "w", newline="") as contact_file:
                    fieldnames = ["contact_id", "name", "number", "email", "category"]
                    writer = csv.DictWriter(contact_file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(remaining_contacts)
                    print("Contact deleted succesfully.")
            else:
                print("No matching contact found")
    else:
        print("No file exists")
def sort_contacts(file):
    if os.path.exists(file):
        if os.path.getsize(file) == 0:
            print("File is empty")
        else:
            sort_choice = input("Enter ID, name or catgeroy you want to sort file: ").strip().lower()
            found = False
            with open(file, "r") as contact_file:
                contacts = list(csv.DictReader(contact_file))
                if sort_choice == "id":
                    sorted_contacts = sorted(contacts, key = lambda contact: int(contact["contact_id"]))
                    found = True
                elif sort_choice == "name":
                    sorted_contacts = sorted(contacts,key = lambda contact: contact["name"])                        
                    found = True
                elif sort_choice == "category":
                    sorted_contacts = sorted(contacts, key = lambda contact: contact["category"])
                    found = True
                else:
                    print("Invalid input")
            if found:
                with open(file, "w", newline="") as contact_file:
                    field_names = ["contact_id", "name", "number", "email", "category"]
                    writer = csv.DictWriter(contact_file,fieldnames = field_names)
                    writer.writeheader()
                    writer.writerows(sorted_contacts)
                    print("Contacts sorted")
                    view_contacts(file)
            else:
                print("No matching contact found.")
    else:
        print("No file exists")
def filter_by_category(file):
    if os.path.exists(file):
        if os.path.getsize(file) == 0:
            print("File is empty")
        else:
            with open(file, "r") as contact_file:
                contacts = list(csv.DictReader(contact_file))
                found = False
                filtered_category = []
                category_choice = input("Enter category ['family', 'friends', 'work', 'other'] you want to filter contacts: ").strip().lower()
                if category_choice not in ["family", "friends", "work", "other"]:
                    print("Invalid input")
                else:
                    for contact in contacts:
                        if category_choice == contact['category'].lower():
                            filtered_category.append(contact)
                            found = True
                if found:
                    for contact in filtered_category:
                        print()
                        print(f"Contact ID: {contact['contact_id']}\nContact name: {contact['name']}\nContact number: {contact['number']}\nContact email: {contact['email']}\nContact category: {contact['category']}")
                        print("-"*28)
                else:
                    print("No matching category found")
    else:
        print("No file exists")
def menu():
    print("--------- Contact Manager ---------")
    try:
        choice = int(input("1. Add contact\n2. View contacts\n3. Search contact\n4. Edit contact\n5. Delete contact\n6. Sort contacts\n7. Filter by category\n8. Exit\nEnter your choice: "))
        if choice == 1:
            add_contact(file)
        elif choice == 2:
            view_contacts(file)
        elif choice == 3:
            search_contact(file)
        elif choice == 4:
            edit_contact(file)
        elif choice == 5:
            delete_contact(file)
        elif choice == 6:
            sort_contacts(file)
        elif choice == 7:
            filter_by_category(file)
        elif choice == 8:
            print("Exiting the program...")
            return False
        else:
            print("Invalid input! Please enter a number between 1 and 8.")
    except ValueError: 
        print("Invalid input! Please enter numbers only.")
while True:
    if not menu():
        break