import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

print("\n--- ROCK PAPER SCISSORS GAME ---")
print("Rules:")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")

while True:
    user_choice = input("\nEnter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)

    print(f"Your choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")

    result = decide_winner(user_choice, computer_choice)

    if result == "user":
        print("You win this round!")
        user_score += 1
    elif result == "computer":
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("It's a tie!")

    print(f"Score → You: {user_score} | Computer: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing!")
        break
s
