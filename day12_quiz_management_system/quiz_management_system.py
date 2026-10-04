"""
Author: Mehreen
Project: Quiz Management System
Day 12 of 30 Days of Python Challenge

This program is a console-based Quiz Management System
that allows users to start quizzes, add questions, view
questions, delete questions, and view quiz score history.

This project uses Object-Oriented Programming (OOP),
CSV file handling, randomization, and date/time handling.
"""

import csv
import datetime
import random
import os
class Quiz:
    def __init__(self):
        self.file = "questions_file.csv"
        self.file_2 = "score_file.csv"
    def predefined_questions(self):
        questions = [
            {
                "question": "What is the correct way to define a function in Python?",
                "options": {
                    "A": "function myFunc():",
                    "B": "def myFunc():",
                    "C": "define myFunc():",
                    "D": "func myFunc():"
                },
                "answer": "B"
            },
            {
                "question": "Which data type is used to store multiple values in an ordered collection?",
                "options": {
                    "A": "List",
                    "B": "Integer",
                    "C": "Boolean",
                    "D": "Float"
                },
                "answer": "A"
            },
            {
                "question": "Which symbol is used for a comment in Python?",
                "options": {
                    "A": "//",
                    "B": "/*",
                    "C": "#",
                    "D": "--"
                },
                "answer": "C"
            },
            {
                "question": "What is the output of 10 // 3?",
                "options": {
                    "A": "3.33",
                    "B": "3",
                    "C": "1",
                    "D": "4"
                },
                "answer": "B"
            },
            {
                "question": "Which keyword is used to create a loop over a sequence?",
                "options": {
                    "A": "repeat",
                    "B": "loop",
                    "C": "for",
                    "D": "iterate"
                },
                "answer": "C"
            }
        ]
        return questions
    def initialize_questions(self):
        if not os.path.exists(self.file):
            questions = self.predefined_questions()
            with open(self.file, "w", newline="") as file:
                fieldnames = [
                    'question',
                    'option_a',
                    'option_b',
                    'option_c',
                    'option_d',
                    'answer'
                ]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for question in questions:
                    writer.writerow({
                        'question': question['question'],
                        'option_a': question['options']['A'],
                        'option_b': question['options']['B'],
                        'option_c': question['options']['C'],
                        'option_d': question['options']['D'],
                        'answer': question['answer']
                    })
        else:
            with open(self.file, 'r', newline="") as file:
                questions = list(csv.DictReader(file))
            if not questions:
                questions = self.predefined_questions()
                with open(self.file, "w", newline="") as file:
                    fieldnames = [
                        'question',
                        'option_a',
                        'option_b',
                        'option_c',
                        'option_d',
                        'answer'
                    ]
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    for question in questions:
                        writer.writerow({
                            'question': question['question'],
                            'option_a': question['options']['A'],
                            'option_b': question['options']['B'],
                            'option_c': question['options']['C'],
                            'option_d': question['options']['D'],
                            'answer': question['answer']
                        })
    def quiz(self):
        self.initialize_questions()
        with open(self.file, 'r', newline="") as file:
            questions = list(csv.DictReader(file))
        if not questions:
            print("No questions available.")
            return
        random.shuffle(questions)
        limit = questions[:5]
        score = 0
        for i, question in enumerate(limit, start=1):
            print(f"\nQuestion {i}: {question['question']}")
            print(f"A. {question['option_a']}")
            print(f"B. {question['option_b']}")
            print(f"C. {question['option_c']}")
            print(f"D. {question['option_d']}")
            while True:
                user_choice = input(
                    "Enter your choice (A, B, C, or D): "
                ).strip().upper()
                if user_choice in ['A', 'B', 'C', 'D']:
                    if user_choice == question['answer']:
                        print("Correct answer!")
                        score += 1
                    else:
                        print(
                            f"Wrong answer! The correct answer is: "
                            f"{question['answer']}"
                        )
                    break
                else:
                    print(
                        "Invalid choice. Please enter A, B, C, or D."
                    )
        print(
            f"\nYou answered {score} out of "
            f"{len(limit)} questions correctly."
        )
        if score == len(limit):
            print("Excellent! You got a perfect score.")
            remarks = "Excellent."
        elif score >= 3:
            print("Good job! You did well.")
            remarks = "Good."
        else:
            print("You need to improve your performance.")
            remarks = "Poor."
        file_exists = os.path.exists(self.file_2)
        with open(self.file_2, 'a', newline="") as file:
            fieldnames = ['date', 'time', 'score', 'remarks']
            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )
            if not file_exists or os.path.getsize(self.file_2) == 0:
                writer.writeheader()
            writer.writerow({
                'date': datetime.date.today(),
                'time': datetime.datetime.now().strftime("%H:%M:%S"),
                'score': score,
                'remarks': remarks
            })
    def add_question(self):
        self.initialize_questions()
        while True:
            question = input("Enter the question: ").strip()
            if question == "":
                print("Question cannot be empty.")
                continue
            break
        while True:
            option_a = input("Enter option A: ").strip()
            if option_a == "":
                print("Option cannot be empty. Please enter a valid option.")
                continue
            break
        while True:
            option_b = input("Enter option B: ").strip()
            if option_b == "":
                print("Option cannot be empty. Please enter a valid option.")
                continue
            break
        while True:
            option_c = input("Enter option C: ").strip()
            if option_c == "":
                print("Option cannot be empty. Please enter a valid option.")
                continue
            break
        while True:
            option_d = input("Enter option D: ").strip()
            if option_d == "":
                print("Option cannot be empty. Please enter a valid option.")
                continue
            break
        while True:
            answer = input(
                "Enter the correct answer (A, B, C, or D): "
            ).strip().upper()
            if answer not in ['A', 'B', 'C', 'D']:
                print(
                    "Invalid answer. Please enter A, B, C, or D."
                )
                continue
            break
        with open(self.file, 'a', newline="") as file:
            fieldnames = [
                'question',
                'option_a',
                'option_b',
                'option_c',
                'option_d',
                'answer'
            ]
            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )
            writer.writerow({
                'question': question,
                'option_a': option_a,
                'option_b': option_b,
                'option_c': option_c,
                'option_d': option_d,
                'answer': answer
            })
        print("Question added successfully.")
    def view_question(self):
        self.initialize_questions()
        with open(self.file, 'r', newline="") as file:
            questions = list(csv.DictReader(file))
        if not questions:
            print("No questions available.")
            return
        for i, question in enumerate(questions, start=1):
            print(f"\nQuestion {i}: {question['question']}")
            print(f"A. {question['option_a']}")
            print(f"B. {question['option_b']}")
            print(f"C. {question['option_c']}")
            print(f"D. {question['option_d']}")
    def delete_question(self):
        self.initialize_questions()
        self.view_question()
        while True:
            try:
                question_num = int(
                    input(
                        "\nEnter the question number you want to delete: "
                    )
                )
                with open(self.file, 'r', newline="") as file:
                    questions = list(csv.DictReader(file))
                if question_num < 1 or question_num > len(questions):
                    print(
                        "Invalid question number. "
                        "Please enter a valid number."
                    )
                    continue
                del questions[question_num - 1]
                with open(self.file, 'w', newline="") as file:
                    fieldnames = [
                        'question',
                        'option_a',
                        'option_b',
                        'option_c',
                        'option_d',
                        'answer'
                    ]
                    writer = csv.DictWriter(
                        file,
                        fieldnames=fieldnames
                    )
                    writer.writeheader()
                    for question in questions:
                        writer.writerow({
                            'question': question['question'],
                            'option_a': question['option_a'],
                            'option_b': question['option_b'],
                            'option_c': question['option_c'],
                            'option_d': question['option_d'],
                            'answer': question['answer']
                        })
                print("Question deleted successfully.")
                break
            except ValueError:
                print("Enter numbers only.")
    def view_score_history(self):
        if not os.path.exists(self.file_2):
            print("No quiz attempted yet.")
            return
        with open(self.file_2, 'r', newline="") as file:
            scores = list(csv.DictReader(file))
        if not scores:
            print("No score history available.")
            return
        for i, score in enumerate(scores, start=1):
            print(
                f"\nAttempt {i}"
                f"\nDate: {score['date']}"
                f"\nTime: {score['time']}"
                f"\nScore: {score['score']}"
                f"\nRemarks: {score['remarks']}"
            )
test = Quiz()
def menu():
    print("-" * 8 + "QUIZ MANAGEMENT SYSTEM" + "-" * 8)
    print()
    try:
        choice = int(
            input(
                "1. Start Quiz\n"
                "2. Add Question\n"
                "3. View Questions\n"
                "4. Delete Question\n"
                "5. View Score History\n"
                "6. Exit\n\n"
                "Enter choice: "
            )
        )
        if choice == 1:
            test.quiz()
        elif choice == 2:
            test.add_question()
        elif choice == 3:
            test.view_question()
        elif choice == 4:
            test.delete_question()
        elif choice == 5:
            test.view_score_history()
        elif choice == 6:
            print("Exiting...")
            return False
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
    except ValueError:
        print("Invalid input. Enter numbers only.")
    return True
while True:
    if not menu():
        break