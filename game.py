import random

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

print("Welcome to Rock, Paper, Scissors!")
user_choice = input("Enter your choice (rock, paper, scissors): ")

if user_choice == computer_choice:
    print("It's a tie!")

elif (user_choice == "rock" and computer_choice == "scissors") 
     (user_choice == "paper" and computer_choice == "rock") 
     (user_choice == "scissors" and computer_choice == "paper"):

    print("You win!")
else:
    print("Computer wins!")

print(f"Computer chose: {computer_choice}")
play_again = True
while play_again:
    

    
    play_again_input = input("Do you want to play again? (yes/no): ").lower()
    if play_again_input != "yes":
        play_again = False

