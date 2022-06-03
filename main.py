import random

game_options = ["r", "p", "s"]


game_end = False
while not game_end:
    user_input = input(f"Please pick an option R for Rock; P for paper and S for scissors: ").lower()
    computer_choice = random.choice(game_options)
    if user_input not in game_options:
        print("Please your input was invalid. Kindly pick again.")
    elif user_input == computer_choice:
        print(f"You chose {user_input} and the computer chose {computer_choice}.")
        print("It's a Tie! Kindly pick again.")
    elif user_input == "r" and computer_choice == "s":
        print(f"You chose {user_input} and the computer chose {computer_choice}.")
        print("Yaayyy! You Win. Rock crushes Scissors")
        game_end = True
    elif user_input == "s" and computer_choice == "p":
        print(f"You chose {user_input} and the computer chose {computer_choice}.")
        print("Yaayyy! You Win. Scissors cuts Paper")
        game_end = True
    elif user_input == "p" and computer_choice == "r":
        print(f"You chose {user_input} and the computer chose {computer_choice}.")
        print("Yaayyy! You Win. Paper covers Rock")
        game_end = True
    elif user_input == "r" and computer_choice == "p":
        print(f"You chose {user_input} and the computer chose {computer_choice}.")
        print("Oops! You Lose")
        game_end = True
    elif user_input == "p" and computer_choice == "s":
        print(f"You chose {user_input} and the computer chose {computer_choice}.")
        print("Oops! You Lose")
        game_end = True
    elif user_input == "s" and computer_choice == "r":
        print(f"You chose {user_input} and the computer chose {computer_choice}.")
        print("Oops! You Lose")
        game_end = True
