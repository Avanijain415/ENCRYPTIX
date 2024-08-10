import random

def determine_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    if (user_choice == 'rock' and computer_choice == 'scissors') :
         return 'user'
    elif (user_choice == 'paper' and computer_choice == 'rock') :
         return 'user'
    elif (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'user'
    else:
        return 'computer'

def play_game():
    user_score = 0
    computer_score = 0
    list_choice = ['rock', 'paper', 'scissors']
    while True:
        print("\nRock-Paper-Scissors Game")
        print("-------------------------")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '4':
            print("\nGame Over!")
            print(f"Your score: {user_score}")
            print(f"Computer's score: {computer_score}")
            break
        elif choice not in ['1', '2', '3']:
            print("Invalid input. Please try again.")
            continue
        user_choice = list_choice[int(choice) - 1]
        computer_choice = determine_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")
        winner = determine_winner(user_choice, computer_choice)
        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'user':
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        print(f"Your score: {user_score}")
        print(f"Computer's score: {computer_score}")

play_game()
print("-------------------------")
print("Thank You For Playing Game...") 


s = {1,2,4,5}
l = []
for i in range(len(s)):
    l += [1+i]
print(l)