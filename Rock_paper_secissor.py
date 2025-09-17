import random

ROCK = 'r'
PAPER= 'p'
SCISSOR = 's'

emoji = {"ROCK":"🪨",'SCISSOR':"✂️","PAPER":"📃"}

choice =tuple(emoji.keys())

def get_user_input():
    while True :
        user_choice= input("Rock, Paper or Secissor (r/p/s)? : ").lower()
        if user_choice in [ROCK, PAPER, SCISSOR]:
            return user_choice

        else :
            print("please select a valid option")

def display_choice(user_choice,computer_choice) :
    choice_map = {ROCK: "ROCK", PAPER: "PAPER", SCISSOR: "SCISSOR"}
    print(f"Your choice is {emoji[choice_map[user_choice].upper()]}")
    print(f"computer choice is {emoji[choice_map[computer_choice].upper()]}")

def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice :
        print("it's a tie")
    elif(
        (user_choice==ROCK and computer_choice == SCISSOR) or
        (user_choice == SCISSOR and computer_choice == PAPER) or
        (user_choice ==PAPER and computer_choice == ROCK)
                ) :
                print("Congratulation you win 🥳🥳")

    else :
        print("you loss")

def play_game():
    while True :
            user_choice = get_user_input()
            computer_choice = random.choice([ROCK, PAPER, SCISSOR])
            display_choice(user_choice,computer_choice)
            determine_winner(user_choice,computer_choice)

            should_continue = input("Continue y/n: ").lower()
            if should_continue != "y" :
                break

play_game()