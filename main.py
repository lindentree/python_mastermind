import os

from rng_api import RandomAPI

def clear():
    os.system("clear")

if __name__ == '__main__':
    code = RandomAPI().get_mastermind_code(7)
    guesses = 10

    turn = 0

    while turn < guesses:
        print("Guess the mastermind code")

        try:    
            guess = input("Enter your choice: ")
            print(guess)
        except ValueError:
            clear()
            print("\tWrong choice!! Try again!!")
            continue

        if len(guess) != 4:
            clear()
            print(guess)
            print(len(guess))
            print("\t Invalid choice!! Try again!!")
            continue

        if guess == code:
            clear()
            print("Congratulations!! YOU WIN!!!!")
            break
        else:
            #clear()
            print("Sorry, try again")
            turn += 1
            continue

        
