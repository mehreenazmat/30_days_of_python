#Rock,paper,scissors game
import random
no_of_draws=0
computer_wins=0
player_wins=0
def player_choice():
    choice=input("Enter your choice (rock , paper , scissors) : ").strip().lower()
    while choice not in ["rock","paper","scissors"]:
        print("Invalid input.Please try again")
        choice=input("Enter your choice (rock , paper , scissors) : ").strip().lower()
    return choice
def computer_choice():
    choice=random.choice(["rock","paper","scissors"])
    return choice
def game_result(player,computer):
    if (player==computer):
        return "It's a draw"
    elif (player=="rock" and computer=="scissors") or (player=="scissors" and computer=="paper") or (player=="paper" and computer=="rock"):
        return "You win"
    else:
        return "Computer wins"
def count(result):
    global no_of_draws, computer_wins, player_wins
    if result=="It's a draw":
        no_of_draws+=1
    elif result=="You win":
        player_wins+=1
    else:
        computer_wins+=1
#main code
ask=input("Do you want to play a game of rock , paper and scissors? (yes/no) :") .strip().lower()
matches=5
if ask=="yes":
    print(f"You have total {matches} matches to play")
    print("Let's play . Are you ready to lose...")
    for i in range(matches):
        print(f"============== Round {i+1} ==============")
        player=player_choice()
        computer=computer_choice()
        print(f"Your choice : {player}")
        print(f"Computer's choice : {computer}")
        result=game_result(player,computer)
        print(result)
        print(f"Number of matches left : {matches-i-1}")
        count(result)
    print(f"============== FINAL RESULT ==============")
    print(f"\n\nTotal number of matches played : {matches}")
    print(f"Draws : {no_of_draws}")
    print(f"Player wins : {player_wins}")
    print(f"Computer wins : {computer_wins}")
    if player_wins>computer_wins:
        print("You won!")
    elif player_wins<computer_wins:
        print("Computer won!")
    else:
        print("\nIt's a tie!")
else:
    print("Thank you for your time, see you next time!")