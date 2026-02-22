import random

def roll_dice(sides):
    #Return a random number between 1 and given sides.
    return random.randint(1, sides)

def get_positive_int(prompt):
    #Get valid positive integer as a input
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print('🔴 Enter a number greater than 0. 🔴')
        except ValueError:
            print('🔴 Invalid number. Try againg. 🔴')

def play_game():
    #One roll of a dice
    count = get_positive_int('How many dice you want to roll: ')
    sides = get_positive_int('How many sides should each die have: ')

    for i in range(count):
        print(f'🎲 Dice{i+1} side is {roll_dice(sides)}')
        print('--------------------')


def main():

    print("🎲 Welcome to Dice Simulator 🎲")

    while True:

        user_input = input("Roll dice? (Y/N): ").strip().upper()

        if user_input == 'Y':
            play_game()
        
        elif user_input == 'N':
            break
                
        else:
            print("Please enter Y or N.")

    print('🙏 Thanks for playing!')  

if __name__ == '__main__':
    main()