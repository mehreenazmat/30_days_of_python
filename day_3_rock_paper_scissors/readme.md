# Day 3 – Rock Paper Scissors

## Project Description

This is the third project of my **30 Days of Python Challenge**.

This project is a console-based Rock, Paper, Scissors game where the player competes against the computer for 5 rounds. The computer randomly selects rock, paper, or scissors, while the player enters their choice.

After each round, the program displays the result and keeps track of the player's wins, computer wins, and draws. At the end, a final scoreboard determines the overall winner.

## Features

* Player vs computer gameplay
* 5 rounds per match
* Random computer choices
* Input validation
* Round-by-round results
* Tracks player wins
* Tracks computer wins
* Tracks draws
* Displays remaining rounds
* Shows the final scoreboard
* Determines the overall winner

## Python Concepts Used

* Functions
* Parameters and return values
* `random` module
* Lists
* Loops
* Conditional statements
* `while` loop
* `for` loop
* Global variables
* User input
* String methods

## Game Rules

* Rock beats Scissors
* Scissors beats Paper
* Paper beats Rock
* Same choices result in a draw

## Sample Output

```text
Do you want to play a game of rock, paper and scissors? (yes/no): yes

You have total 5 matches to play
Let's play. Are you ready to lose...

============== Round 1 ==============
Enter your choice (rock, paper, scissors): rock
Your choice : rock
Computer's choice : scissors
You win
Number of matches left : 4

============== Round 2 ==============
Enter your choice (rock, paper, scissors): paper
Your choice : paper
Computer's choice : paper
It's a draw
Number of matches left : 3

============== Round 3 ==============
Enter your choice (rock, paper, scissors): scissors
Your choice : scissors
Computer's choice : rock
Computer wins
Number of matches left : 2

============== Round 4 ==============
Enter your choice (rock, paper, scissors): paper
Your choice : paper
Computer's choice : rock
You win
Number of matches left : 1

============== Round 5 ==============
Enter your choice (rock, paper, scissors): rock
Your choice : rock
Computer's choice : scissors
You win
Number of matches left : 0

============== FINAL RESULT ==============

Total number of matches played : 5
Draws : 1
Player wins : 3
Computer wins : 1

You won!
```

## Learning Outcomes

Through this project, I practiced:

* Creating multiple reusable functions
* Using the `random` module
* Validating user input
* Managing game rounds using loops
* Tracking scores
* Using global variables
* Applying conditional logic to determine winners
* Building an interactive console-based game

---

**Challenge:** 30 Days of Python
**Day:** 3
**Project:** Rock Paper Scissors
