"""
Author: Mehreen
Project: Calculator with History

Day 5 of 30 Days of Python Challenge

This program is a console-based calculator application
that performs different mathematical operations and
maintains a history and backup of previous calculations.
"""

history_list=[]
backup_list=[]
num1=0
num2=0
def add():
    global history_list,num1,num2
    try:
        num1=int(input("Enter number 1 :"))
        num2=int(input("Enter number 2 :"))
    except ValueError:
        print("Invalid input ! Please enter a number only...")
        add()
    sum=num1+num2
    print(f"Sum : {sum}")
    string_sum=f"{num1} + {num2} = {sum}"
    history_list.append(string_sum)
def difference():
    global history_list,num1,num2
    try:
        num1=int(input("Enter number 1 :"))
        num2=int(input("Enter number 2 :"))
    except ValueError:
        print("Invalid input ! Please enter a number only...")
        difference()
    diff=num1-num2
    print(f"Difference : {diff}")
    string_diff=f"{num1} - {num2} = {diff}"
    history_list.append(string_diff)
def multiplication():
    global history_list,num1,num2
    try:
        num1=int(input("Enter number 1 :"))
        num2=int(input("Enter number 2 :"))
    except ValueError:
        print("Invalid input ! Please enter a number only...")
        multiplication()
    mul=num1*num2
    print(f"Product : {mul}")
    string_mul=f"{num1} * {num2} = {mul}"
    history_list.append(string_mul)
def division():
    global history_list,num1,num2
    try:
        num1=int(input("Enter numerator :"))
        num2=int(input("Enter denominator :"))
        div=num1/num2
    except ValueError:
        print("Invalid input ! Please enter a number only...")
        return
    except ZeroDivisionError:
        print("Denominator cannot be zero")
        return
    print(f"Division : {div}")
    string_div=f"{num1} / {num2} = {div}"
    history_list.append(string_div)
def power_func():
    global history_list
    try:
        exp=int(input("Enter exponent :"))
        power=int(input("Enter power :"))
    except ValueError:
        print("Invalid input ! Please enter a number only...")
        power_func()
    pow=exp**power
    print(f"Answer : {pow}")
    string_pow=f"{exp} ^ {power} = {pow}"
    history_list.append(string_pow)
def modulus():
    global history_list,num1,num2
    try:
        num1=int(input("Enter number 1 :"))
        num2=int(input("Enter number 2 :"))
        mod=num1%num2
    except ValueError:
        print("Invalid input ! Please enter a number only...")
        modulus()
    except ZeroDivisionError:
        print("Modulo by zero is not allowed!")
        modulus()
    print(f"Modulus : {mod}")
    string_mod=f"{num1} % {num2} = {mod}"
    history_list.append(string_mod)
def history():
    global history_list
    if len(history_list)==0:
        print("History is already empty")
    else:
        for calculation in history_list:
            print(calculation)
def clear_history():
    global history_list,backup_list
    if len(history_list)==0:
        print("History is already empty.")
    else:
        for cal in history_list:
            backup_list.append(cal)
        history_list.clear()
        print("History of calculation is empty")
def backup():
    global backup_list
    if len(backup_list)==0:
        print("Sorry backup is deleted")
    else:
        for backup_calculation in backup_list:
            print(backup_calculation)
def menu():
    print("========= CALCULATOR =========")
    try:
        choice = int(input("1. Sum of numbers\n2. Difference of numbers\n3. Multiplication of number\n4. Division of numbers\n5. Power of numbers\n6. Modulus of numbers\n7. View history\n8. Clear History\n9. View Backup of History\n10. Exit\nChoose a number: "))
    except ValueError:
        print("Invalid input ! Please enter number only...")
        menu()
    if choice >10 or choice <1:
        print("Invalid choice.[Error]: Invalid choice. Please enter a valid number between 1 to 10. .")
        menu()
    else:
        if choice == 1:
            add()
        elif choice==2:
            difference()
        elif choice==3:
            multiplication()
        elif choice==4:
            division()
        elif choice==5:
            power_func()
        elif choice==6:
            modulus()
        elif choice==7:
            history()
        elif choice==8:
            clear_history()
        elif choice==9:
            backup()
        else:
            print("Thank you for visiting\nExiting program...")
            exit()
while True:
    menu()