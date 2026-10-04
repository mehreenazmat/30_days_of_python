# Day 12 – Quiz Management System

> **30 Days of Python Challenge**

## Project Description

This project is a console-based **Quiz Management System** developed as part of my 30 Days of Python Challenge.

The program allows users to start quizzes, add new questions, view available questions, delete questions, and view previous quiz score history.

The project uses **Object-Oriented Programming (OOP)** along with CSV file handling to store questions and quiz results.

## Features

* Start a quiz
* Randomly select questions
* Answer multiple-choice questions
* Calculate quiz scores
* Display performance remarks
* Add new questions
* View all questions
* Delete questions
* View score history
* Store questions permanently in a CSV file
* Store quiz results in a CSV file
* Record date and time of quiz attempts
* Validate user input
* Automatically create predefined questions when the question file is missing or empty

## Quiz Rules

* Each quiz contains up to 5 questions.
* Questions are selected randomly.
* Each question has four options: A, B, C, and D.
* The user must enter a valid option.
* The score is recorded after completing the quiz.

## Performance Remarks

| Score | Remark    |
| ----- | --------- |
| 5/5   | Excellent |
| 3–4/5 | Good      |
| 0–2/5 | Poor      |

## Files

### `quiz_management_system.py`

Contains the complete Quiz Management System and the `Quiz` class.

### `questions_file.csv`

Stores quiz questions, their four options, and correct answers.

### `score_file.csv`

Stores quiz attempt date, time, score, and performance remarks.

## Concepts Used

* Classes and Objects
* Object-Oriented Programming
* `__init__()` constructor
* Instance methods
* `self`
* Functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* Exception handling
* `try-except`
* CSV files
* `csv.DictReader`
* `csv.DictWriter`
* File handling
* `os.path.exists()`
* `os.path.getsize()`
* `random.shuffle()`
* `datetime`
* Input validation

## Menu Options

```text
--------QUIZ MANAGEMENT SYSTEM--------

1. Start Quiz
2. Add Question
3. View Questions
4. Delete Question
5. View Score History
6. Exit
```

## How to Run

Open the project folder in VS Code and run:

```bash
python quiz_management_system.py
```

## Learning Outcome

Through this project, I practiced combining **Object-Oriented Programming with CSV file handling**.

I also learned how to randomly select questions, validate multiple-choice answers, calculate scores, store quiz history, and manage persistent question data.

## Author

**Mehreen**

Day 12 of 30 Days of Python Challenge
