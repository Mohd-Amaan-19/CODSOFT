import random

user_score = 0
computer_score = 0

def get_user_choice():
    while True:
        user_choice = input("Choose rock(r), paper(p) or scissor(s):- ").lower()
        if user_choice in ['r', 'p', 's']:
            return user_choice
        else:
            print("Invalid choice. Please choose 'r', 'p', or 's'.")

def get_computer_choice():
    return random.choice(['r', 'p', 's'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return "You win!"
    else:
        return "Computer win!"

while True:
    print("\t The rules for the game:")
    print("Rock beats scissor, scissor beat paper, and paper beats rock.\n")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"You choose: {user_choice}")
    print(f"Computer choose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    if result == "You win!":
        user_score += 1
    elif result == "Computer win!":
        computer_score += 1
    
    print(f"Your Score: {user_score}, Computer Score: {computer_score}")
    
    play_again = input("Do you want to play again? (Yes(y)/No(n)): ").lower()
    if play_again != 'y':
        break

