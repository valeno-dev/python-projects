import random

while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "y" or choice == "yes":
        print(f"({dice1}, {dice2})")
    elif choice == "n" or choice == "no":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")