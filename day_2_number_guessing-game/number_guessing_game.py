#Number guessing game
import random
total_number_of_guesses=6
def guessing_game(number,attempts):
    for i in range(attempts):
        guess=int(input("Enter your guess between 1 to 100: "))
        if guess < 1 or guess > 100:
            print("Invalid number!\nPlease enter a number between 1 and 100.")
            i=i-1
            continue
        if guess>number:
            print("Your guess is high,try again")
            print(f"Your remaining attempts are {attempts-i-1}")
        elif guess<number:
            print("Your guess is low,try again")
            print(f"Your remaining attempts are {attempts-i-1}")
        else:
            print(f"Congratulations you have guessed the number correctly!\nOn your {i+1} attempt")
            break
    else:
        print(f"Sorry you have used all of your attempts,the secret number was {number}\nBetter luck next time!")
        difference(number,guess)
def difference(number,guess):
    difference=abs(number-guess)
    if difference <=10:
        print(f"Very close! \nDifference:{difference}")
    elif difference >10 and difference<=20:
        print(f"close! \nDifference:{difference}")
    else:
        print(f"Very far! \nDiffernce:{difference}")    
#main part
choice=input("Do you want to play a number guessing game (yes/no): ").strip().lower()
if choice=="yes":
    print("You have total 6 guesses to guess the number between 1 to 100")
    secret_number=random.randint(1,100)
    guessing_game(secret_number, total_number_of_guesses)
else:
    print("Thank you for your time, see you next time!")