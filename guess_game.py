import random

def play_guessing_game():
    print("Welcome to our guessing game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    numbers = get_numbers()
    target_number = random.randint(1, 50)
    attempts = 0

    while True:
        attempts +=1
        if numbers < target_number:
            print("Too low! Try again.")
            numbers = get_numbers()
        elif numbers > target_number:
            print("Too high! Try again.")
            numbers = get_numbers()
        else:
            print(f"Congratulations! You've guessed the number {target_number} in {attempts} attempts.")
            break

def get_numbers():
    while True:
        try:
            number = int(input("Enter a number between 1 and 100: "))
            if 1 <= number <= 50:
                return number
            else:
                print("Number out of range. Please try again.")
            continue
        except:
            raise ValueError("Invalid input. Please enter a valid integer.")    
        
if __name__ == "__main__":
    play_guessing_game()        