"""
Author: Mehreen

Project: Percentage Calculator

Day 1 of 30 Days of Python Challenge

This program calculates percentage, highest marks,
lowest marks, and grade of a student and displays
a formatted report card.
"""

name = input("Enter your name : ")
total_subjects = int(input("Enter total number of subjects you want to calculate percentage of :"))
total_marks = total_subjects*100             # using this because total marks per subject is 100
i = 0
# creating empty list so that marks of every student is stroed together
marks = []
subjects = []
while i < total_subjects:
    subject = input(f"Enter name of subject {i+1} : ")
    mark = (int(input(f"Enter marks of {subject.title()} : "  ) ))
    # checking if the marks entered are valid or not
    if mark > 100 or mark < 0:
        print("Invalid marks please enter between 0 to 100")
        continue
    marks.append(mark)
    subjects.append(subject)
    i += 1
# function for printing report card
def printing_report_card(name,subjects,marks):
    print("=========REPORT CARD=========")
    print(f"Name : {name.title()}")
    print("Subjects\t\tMarks")
    print("-----------------------------")
    j = 0
    while j < len(subjects):
        print(f"{subjects[j].title():20}{marks[j]}")
        j += 1
    print("-----------------------------")
# higest marks and lowest marks calculator
def highest_marks(marks):
    return max(marks)
def lowest_marks(marks):
    return min(marks)
# using fuctions to calculate percentage and then grade
def percentage_calculator( obtained_marks , total_marks):
    per = (obtained_marks/total_marks)*100
    return per

percentage = percentage_calculator(sum(marks),total_marks)
def grade_cal(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"
grade = grade_cal(percentage)
printing_report_card(name,subjects,marks)
highest = highest_marks(marks)
lowest = lowest_marks(marks)
print(f"Highest : {highest} ({subjects[marks.index(highest)]})")
print(f"Lowest : {lowest} ({subjects[marks.index(lowest)]})")
print(f"Your percentage is {percentage:.2f}%\nYour grade is {grade}")
print("=============================")