#task 4
import random

def get_choice():
    options = ["rock", "paper", "scissors"]
    while True:
        choice = input("Enter your choice (Rock, Paper, Scissors): ").strip().lower()
        if choice in options:
            return choice
        print("Invalid input. Please choose Rock, Paper, or Scissors.")

def main():
    print("Welcome to Rock, Paper, Scissors!")
    options = ["rock", "paper", "scissors"]

    while True:
        user = get_choice()
        comp = random.choice(options)

        print(f"You chose: {user.capitalize()}")
        print(f"Computer chose: {comp.capitalize()}")

        if user == comp:
            print("It's a draw!")
        elif (user == "rock" and comp == "scissors") or \
             (user == "paper" and comp == "rock") or \
             (user == "scissors" and comp == "paper"):
            print("You win!")
        else:
            print("You lose!")

        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            break

    print("Thanks for playing! Goodbye!")

main()
