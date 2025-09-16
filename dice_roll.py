import random  

total_rolls = 0
while True :
    choice = input("you want to rol dice y / n : ").lower()
    if choice == "y" :
        role = int(input("how many time you want to rol dice : "))
        for i in range(role):
            Dice1 = random.randint(1,6)
            Dice2 = random.randint(1,6)
            print(f"your dice sequence ({Dice1},{Dice2})")
        total_rolls += role   
    elif choice == "n" :
        print("thanku for playing game")
        print(f"total rolls {total_rolls}")
        break
    else :
        print("invalid")
