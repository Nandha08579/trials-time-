import random

def roll_dice():
    print("Rolling the dice...")
    dice_value = random.randint(1, 6)
    print(f"The dice rolled and landed on: {dice_value}")

def dice_simulator():
    while True:
        print("\n====== DICE ROLLING SIMULATOR ======")
        print("1. Roll the Dice")
        print("2. Quit")

        choice = input("Enter your choice (1-2): ")
        print()

        if choice == "1":
            roll_dice()
        elif choice == "2":
            print("Thank you for using the dice rolling simulator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the dice rolling simulator
dice_simulator()
