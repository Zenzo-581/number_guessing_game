from random import randint
def main():
    # Display a welcome message and the rules of the game
    welcome()

    # Generate a random number from 1 - 100
    number = randint(1,100)
    print (number)  # DON'T FORGET TO DELETE THIS LINE.
    chances = 0
    # Ask the user for the difficulty
    difficulty = input("Choose the game difficulty: \n1.Easy (10 chances)\n2.Medium (5 chances)\n3.Hard (3 chances)").lower()
    while difficulty not in ['easy', 'medium', 'hard', '1' , '2', '3']:
        difficulty = input("Choose the game difficulty: \n1.Easy (10 chances)\n2.Medium (5 chances)\n3.Hard (3 chances)").lower()
    
    if difficulty in ['easy' , '1']:
        chances = 10
    elif difficulty in ["medium" , '2']:
        chances = 5
    elif difficulty in ["hard", '3']:
        chances = 3
    
    count = 0

    for i in range(chances):
        guess = int(input("What's your guess ?"))
        if guess == number:
            print("Nice job! You did it!")
            break
        elif guess != number:
            print(f"Whoops! Try again you still got {chances - i - 1} chances")
            count += 1
            if guess < number:
                print("Your guess is lower than the number")
            elif guess > number:
                print("Your guess is higher than the number")
    
    if count == chances:
        print(f"You ran out of chances GG, The number was : {number}")

def welcome():
    print("Hello and welcome to guess the number game. \nIn this game you have to guess a number between 1 and 100.")

if __name__ == "__main__":
    main()