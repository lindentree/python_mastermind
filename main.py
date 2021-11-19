import os

from rng_api import RandomAPI

def clear():
    os.system("clear")


def game_loop():
    code = RandomAPI().get_mastermind_code(7)
    guesses = 5

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

        if len(guess) != 4 or not guess.isnumeric():
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
    
    print(f'The code was {code}')

if __name__ == '__main__':
    while True:
        game_loop()
        restart = input('Do you want to try again, Y/N? ')

        if restart == 'N':
            break
        elif restart == 'Y':
            continue





        
