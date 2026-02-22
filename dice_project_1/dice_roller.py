import random

def roll_dice():
    """Simulates rolling a 6-sided dice."""
    return random.randint(1, 6)

def main():

    print("---Welcome to the Dice Simulator---")

    while True:
        user = input("roll a dice?(Y/N): ").strip().upper()

        if user == "Y":
            dice_number = roll_dice()
            print(f" 🎲 Your number is {dice_number}")
        elif user == "N":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("⚠️ Invalid input. Please type 'Y' or 'N'.")    

if __name__ == "__main__":
    main()



