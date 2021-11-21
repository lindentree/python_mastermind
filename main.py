import os

from rng_api import RandomAPI
from game_session import GameSession

def clear():
    os.system('cls' if os.name=='nt' else 'clear')


def game_loop():
    code = RandomAPI().get_mastermind_code(7)
    active_game = GameSession(code)
    guesses = 5
    limit = 7

    turn = 0

    while turn < guesses:
        print("Guess the mastermind code")

        try:

            if turn:
                active_game.display_guess_history()
            print(f'You have {guesses-turn} guesses left.')    
            guess = input("Enter your choice: ")
            #print(guess)
        except ValueError:
            clear()
            print("\tWrong choice!! Try again!!")
            continue

        if len(guess) != 4 or not guess.isnumeric():
            clear()
           
            print("\t Invalid choice!! Try again!!")
            continue

        if any(guess in x for x in active_game.guesses):
            print("\t You already guessed that!")
            continue

        if guess == code:
            clear()
            print("Congratulations!! YOU WIN!!!!")
            break
        else:
            
            feedback = active_game.provide__guess_feedback(guess)
            entry = { guess: feedback }
            active_game.guesses.append(entry)
            turn += 1

            if feedback:
                print(f"Sorry, try again. You have {guesses-turn} guesses remaining. Here's a hint: {feedback}")
            else:
                print(f"None of the numbers you guessed were correct or in the right place. You have {guesses-turn} guesses remaining. ")
            
            continue

    print(f"The code was {code}")

if __name__ == '__main__':
    while True:
        game_loop()
        restart = input('Do you want to try again, Y/N? ').lower()

        if restart == 'n':
            print(restart)
            quit()
        elif restart == 'y':
            continue