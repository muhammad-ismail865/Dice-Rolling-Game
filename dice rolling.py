import random
while True:
    dice=input("Roll the dice (y/n):").lower()
    if(dice=="y"):
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f"{die1,die2}")
    elif(dice=="n"):
        print("Thanks for Playing")
        break
    else:
        print("Invalid choice!")
