from random import randint


def main():
    # Display a welcome message and the rules of the game
    welcome()

    # Generate a random number from 1 - 100
 
    options = ['easy', 'medium', 'hard', '1', '2', '3']
    agree = ['y', 'yes']
    disagree = ['n', 'no']
    menu = "Choose the game difficulty: \n1.Easy (10 chances)\n2.Medium (5 chances)\n3.Hard (3 chances)"
    again = True

    # Ask the user for the difficulty
    while again == True:  
        number = randint(1, 100)
        while True:
            difficulty = input(menu).lower()
            if difficulty in options:
                break
            print("Invalid choice. Please enter a valid number or difficulty.\n")
        chances = num_chances(difficulty) # Getting the number of chances
        play(chances, number)
        
        while True:
            var = input("Do you want to play again? [y/n]").lower()
            if var in disagree:
                again = False
                break
            elif var in agree:
                again = True
                break
            else:
                print('Please insert a valid answer [y/n]')


def welcome():
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")


def num_chances(diff):
    if diff in ['easy', '1']:
        return 10
    elif diff in ['medium', '2']:
        return 5
    elif diff in ['hard', '3']:
        return 3


def play(chances, number):
    for i in range(chances):
        attempts = chances - i - 1
        while True:
            try:
                guess = int(input("What's your guess ?"))
                if guess < 1 or guess > 100:
                    print("Out of bounds! Please guess a number between 1 and 100.")
                    continue
                break
            except ValueError:
                print("Please insert your number in digits: ")
        
        if guess == number:
            print(f"Nice job! You did it in {i + 1} attempts!")
            break

        elif guess != number and attempts != 0:
            if guess < number:
                print(f"Incorrect! The number is more than {guess}")
            else:
                print(f"Incorrect! The number is less than {guess}")
            print(f"Try again you still got {attempts} chances left")
    
    else:
        print(f"You ran out of chances GG, The number was : {number}")


if __name__ == "__main__":
    main()