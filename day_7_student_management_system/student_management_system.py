"""
Author: Mehreen

Project: Student Management System

Day 7 of 30 Days of Python Challenge
This program is a console-based Student Management System
that allows users to add, view, search, remove, update,
and manage student records along with their marks and grades.
"""

students = []
def add_student():
    global students
    name=input("Enter full name of student: ").title()
    roll_number=input("Enter roll number: ")
    for student in students:
        if student[1]==roll_number:
            print("Roll number already exists")
            return
    while True:
        try:
            marks=int(input("Enter marks: "))
            if 0<=marks<=100:
                break
            else:
                print("Marks must be between 0 - 100")
        except ValueError:
            print("Enter numbers only")

    students.append([name,roll_number,marks])
    print("Student added successfully")
def view_student():
    global students
    if not students:
        print("No student in record")
    else:
        print("========= STUDENTS =========")
        for i,student in enumerate(students,start=1):
            print(f"Student {i}")
            print(f"Name: {student[0]}\nRoll number: {student[1]}\nMarks: {student[2]}")
            marks_of_student=student[2]
            if marks_of_student>=90:
                print("Grade: A+")
            elif 90>marks_of_student>=80:
                print("Grade: A")
            elif 80>marks_of_student>=70:
                print("Grade: B")
            elif 70>marks_of_student>=60:
                print("Grade: C")
            elif 60>marks_of_student>=50:
                print("Grade: D")
            elif 50>marks_of_student>=40:
                print("Grade: E")
            else:
                print("Grade: F")
            print()
            print("-"*30 + "\n")
        print(f"Total student: {len(students)}")
def search_student():
    global students
    if not students:
        print("No student in record")
    else:
        for i,student in enumerate(students,start=1):
            print(f"{i}. {student[0]}")
        print(f"Total student: {len(students)}")
        while True:
            try:
                student_search=int(input("Enter student number you want to see:"))-1
                if 0<=student_search<len(students):
                    break
                else:
                    print("Enter number present in the list")
            except ValueError:
                print("Enter numbers only")   
        print("Student found")
        print(f"Name: {students[student_search][0]}\nRoll number: {students[student_search][1]}\nMarks: {students[student_search][2]}")
        marks_of_student=students[student_search][2]
        if marks_of_student>=90:
            print("Grade: A+")
        elif 90>marks_of_student>=80:
            print("Grade: A")
        elif 80>marks_of_student>=70:
            print("Grade: B")
        elif 70>marks_of_student>=60:
            print("Grade: C")
        elif 60>marks_of_student>=50:
            print("Grade: D")
        elif 50>marks_of_student>=40:
            print("Grade: E")
        else:
            print("Grade: F")
def remove_student():
    global students
    if not students:
        print("No student in record")
    else:
        for i,student in enumerate(students,start=1):
            print(f"{i}. {student[0]}")
        print(f"Total student: {len(students)}")
        while True:
            try:
                student_remove_number=int(input("Enter student number to remove: "))-1 
                if 0<=student_remove_number<len(students):
                    break
                else:
                    print("Enter number present in the list")
            except ValueError:
                print("Enter numbers only")
        removed_student=students.pop(student_remove_number)
        print("Student removed from record")
        print(f"Name: {removed_student[0]}\nRoll number: {removed_student[1]}\nMarks: {removed_student[2]}") 
        marks_of_student=removed_student[2]
        if marks_of_student>=90:
            print("Grade: A+")
        elif 90>marks_of_student>=80:
            print("Grade: A")
        elif 80>marks_of_student>=70:
            print("Grade: B")
        elif 70>marks_of_student>=60:
            print("Grade: C")
        elif 60>marks_of_student>=50:
            print("Grade: D")
        elif 50>marks_of_student>=40:
            print("Grade: E")
        else:
            print("Grade: F")  
        print(f"Now total students: {len(students)}")
def update_student_info():
    global students
    if not students:
        print("No student in record")
    else:
        for i , student in enumerate(students,start=1):
            print(f"{i}. {student[0]}")
        while True:
            try:
                student_update_number=int(input("Enter number of student whom data you want to update: "))-1
                if 0<=student_update_number<len(students):
                    break
                else:
                    print(f"Enter number present in list")
            except ValueError:
                print("Enter numbers only")
        print(f"Name: {students[student_update_number][0]}\nRoll number: {students[student_update_number][1]}\nMarks: {students[student_update_number][2]}")
        while True:
            try:
                choice_to_update=int(input("1. Name\n2. Roll number\n3. Marks\nEnter number of what you want to update:"))
                if choice_to_update==1:
                    update_name=input("Enter Name to change: ")
                    students[student_update_number][0]=update_name
                    print("Name updated successfully")
                    break
                elif choice_to_update==2:
                    while True:
                        update_rollnumber=input("Enter Roll number to update: ")
                        if any(student[1]==update_rollnumber for idx,student in enumerate(students) if idx!=student_update_number):
                            print("Roll number already present. Try again")
                        else:
                            students[student_update_number][1]=update_rollnumber                                
                            print("Roll number updated successfully")
                            break
                    break
                elif choice_to_update==3:
                    while True:
                        try:
                            update_marks=int(input("Enter marks to update: "))
                            if 0<=update_marks<=100:
                                students[student_update_number][2]=update_marks
                                print("Marks updated successfully")
                                marks_of_student=students[student_update_number][2]
                                if marks_of_student>=90:
                                    print("Now Grade: A+")
                                elif 90>marks_of_student>=80:
                                    print("Now Grade: A")
                                elif 80>marks_of_student>=70:
                                    print("Now Grade: B")
                                elif 70>marks_of_student>=60:
                                    print("Now Grade: C")
                                elif 60>marks_of_student>=50:
                                    print("Now Grade: D")
                                elif 50>marks_of_student>=40:
                                    print("Now Grade: E")
                                else:
                                    print("Now Grade: F")  
                                break
                            else:
                                print("Enter marks between 0 - 100")
                        except ValueError:
                            print("Enter numbers only ")
                    break
                else:
                    print("Enter between 1 and 3")
            except ValueError:
                print("Enter numbers only")
def show_top_student():
    global students
    if not students:
        print("No student in record")
    else:
        highest_marks=max(s[2] for s in students)
        top_students=[s for s in students if s[2]==highest_marks]
        print("========= STUDENT(S) WITH HIGHEST MARKS =========")
        print()
        for top_student in top_students:
            print(f"Name: {top_student[0]}\nRoll number: {top_student[1]}\nMarks: {top_student[2]}")
            print()
def clear_all_student():
    global students
    if not students:
        print("Student list already cleared")
    else:
        total_students=len(students)
        students.clear()
        print("All students have been cleared")
        print(f"Total {total_students} students cleared")
def menu():
    print("========= STUDENT MANAGEMENT =========\n")
    try:
        choice=int(input("1. Add Student\n2. View Students\n3. Search Student\n4. Remove Student\n5. Update Student Marks\n6. Show Top Student\n7. Clear All Students\n8. Exit\nEnter your choice: "))
        if choice==1:
            add_student()
        elif choice==2:
            view_student()
        elif choice==3:
            search_student()
        elif choice==4:
            remove_student()
        elif choice==5:
            update_student_info()
        elif choice==6:
            show_top_student()
        elif choice==7:
            clear_all_student()
        elif choice==8:
            print("Exiting program...")
            exit()
        else:
            print("Invalid input please enter between 1-8 only")
    except ValueError:
        print("Enter numbers only")
while True:
    menu()