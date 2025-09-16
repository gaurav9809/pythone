import random

def guess_game():
    print("Welcome to the guessesing game ❤️😁")
    print("Think a number between 1 to 100")
    print("If you win you get 😘")
    numbers = get_number()
    target_number = random.randint(1,100)
    attempts = 0

    while True :
        attempts += 1
        if numbers < target_number :
            print("Number is to high 😒")
            print(target_number,"is target number")
            numbers = get_number()
        elif numbers > target_number :
            print("Number too low 🐕")
            print(target_number,"is target number")
            numbers = get_number()
        elif numbers == target_number :
            print('Congratulation you won tha game 🥳🥳🥳')
            print("Your reward is that 😘😘🤗🤗")
            print(f"your attempts in game {attempts}")
            numbers = get_number()
            break
def get_number():
    while True :
        try :
            number = int(input(f"my dear babe guess a number: ")) 
            if 1 <= number <= 100 :
                        return number
            else :
                    print("please select a number between 1 to 100 😒 ")
        except ValueError :
            print("please enter a valid number 🤗 ")
        
if __name__ == "__main__":
    guess_game()         