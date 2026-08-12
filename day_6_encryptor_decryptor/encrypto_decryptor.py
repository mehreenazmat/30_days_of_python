"""
Author: Mehreen
Project: Encryption and Decryption of Messages

Day 6 of 30 Days of Python Challenge

This program is a console-based Secure Message Locker
that allows users to encrypt and decrypt messages using
the Caesar Cipher algorithm, save encrypted messages,
delete saved messages, and recover deleted messages
from a backup.
"""

import random
saved_message=[]
backup_message=[]
last_message=""
last_shift=0
def encrypt_message(text,shifts,save):
    global last_message,last_shift
    encrypted_message=""
    for char in text:
        if char.isalpha():
            base= ord('A') if char.isupper() else ord('a')
            encrypted_message+=chr((ord(char)-base+shifts)%26+base)
        else:
            encrypted_message+=char
    record=f"Encrypted message: {encrypted_message} || Shifts: {shifts}"
    save.append(record)
    last_message=encrypted_message
    last_shift=shifts
    return encrypted_message
        
def decrypt_message(text,shifts):
    if not text:
        print("No message encrypted")
        return None
    decrypted_message=""
    for char in text:
        if char.isalpha():
            base=ord('A') if char.isupper() else ord('a')
            decrypted_message+=chr((ord(char)-base-shifts)%26+base)
        else:
            decrypted_message+=char
    return decrypted_message
def view_save_message(save):
    if not save:
        print("No encrypted message")
    else:
        for i,saves in enumerate(save,start=1):
            print(f"{i}. {saves}")
        print(f"Total number of encrypted messages saved are: {len(save)}")
def delete_message(save,backup):
    if not save:
        print("No encrypted messages saved to delete")
    else:
        for saves in save:
            backup.append(saves)
    save.clear()
    print("ALL SAVED MESSAGES DELETED.")
def backup_func(backup):
    return backup
def help_menu(backup):
    try:
        help_choice=int(input("How can we help you..\n1. Get you encrypted messages back \n2. Get information about this system\nEnter your choice: "))
        if help_choice==1:
            if len(backup)==0:
                print("EMPTY")
            else:
                print("Here are your encrypted messages:")
                deleted_backup=backup_func(backup)
                for i, backups in enumerate(deleted_backup,start=1):
                    print(f"{i}. {backups}")
        else:
            print("""
========= SYSTEM INFORMATION =========

Welcome to Secure Message Locker!

This system uses the Caesar Cipher encryption algorithm
to protect your messages.

Features:
1. Encrypt text using a custom shift.
2. Generate a random shift automatically.
3. Save encrypted messages.
4. View all saved messages.
5. Delete saved messages.
6. Recover deleted messages from backup.

Note:
- Only alphabetic characters are encrypted.
- Numbers, spaces and symbols remain unchanged.
- Valid shift values are between 1 and 25.

Thank you for using Secure Message Locker!
======================================
""")
    except ValueError:
        print("Enter a numbers only")
def menu():
    print("========= SECURE MESSAGE LOCKER =========")
    try:
        choice=int(input("1. Encrypt Message\n2. Decrypt Encrypted Message\n3. View Saved Messages\n4. Delete Saved Messages\n5. Help\n6. Exit\nEnter your choice: "))
    except ValueError:
        print("Invalid input ! Please enter number only...")
        choice=int(input("Enter you choice again: "))
    if choice==1:
        message=input("Enter message to encrypt :")
        choice_2=int(input("1. Do you want to enter number of shift yourself\n\t\tOR\n2. Machine decides number of shifts\nEnter your choice(1/2): "))
        if choice_2==1:
            try:
                shift=int(input("Enter number of shifts(1-25) :"))
                if  not 1<=shift<=25:
                    print("Invalid Input! Please enter number between 1-25")
                    return
            except ValueError:
                print("Invalid input ! Please enter number(1-25)...")
                shift=int(input("Enter number of shifts(1-25) :"))
            mesg=encrypt_message(message,shift,saved_message)
            print(f"Encrypted message: {mesg}")
        else:
            shift=random.randint(1,25)
            mesg=encrypt_message(message,shift,saved_message)
            print(f"Encrypted message: {mesg}")
    elif choice==2:
        if last_message:
            dec_mes=decrypt_message(last_message,last_shift)
            print(f"Decrypted message :{dec_mes}")
        else:
            print("No encrypted messages to decrypt!")
    elif choice==3:
        view_save_message(saved_message)
    elif choice==4:
        delete_message(saved_message,backup_message)
    elif choice==5:
        help_menu(backup_message)
    elif choice==6:
        print("Exiting program...")
        exit()
    else:
        print("Invalid choice please enter between 1-6")
        
while True:
    menu()