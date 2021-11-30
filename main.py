import os
import click
import timg

from rng_api import RandomAPI
from game_session import GameSession

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

difficulty_settings = {
   "Easy": {
       "digits": 4,
       "upper_limit": 5,
       "guesses": 12
   },
   "Normal": {
       "digits": 4,
       "upper_limit": 7,
       "guesses": 10
   },
   "Hard": {
       "digits": 5,
       "upper_limit": 9,
       "guesses": 8
   }
}

@click.command()
@click.option('--difficulty', prompt=True, type=click.Choice(['Easy', 'Normal', 'Hard'], case_sensitive=False))

def set_difficulty(difficulty):
    click.echo(f"You chose {difficulty} mode!")
    return difficulty


def game_loop():

    user_choice = set_difficulty(standalone_mode=False)

    settings = difficulty_settings[user_choice]

    code = RandomAPI().get_mastermind_code(settings)
    active_game = GameSession(code)

    guesses = settings["guesses"]
    limit = settings["upper_limit"]
    digits = settings["digits"]

    turn = 0

    while turn < guesses:
        print(f"Guess the Mastermind code. Choose {digits} digits between 0 and {limit} inclusive.")

        try:

            if turn:
                active_game.display_guess_history()
            print(f"You have {guesses-turn} guesses left.")

            guess = input("Enter your choice: ")

        except ValueError:
            clear()
            print("\tWrong choice! Try again!")
            continue

        if not guess.isnumeric() or len(guess) != digits or any(int(x) > limit for x in guess):
            clear()
            print(f"Please choose NUMBERS between 0 and {limit} inclusive.")
            continue

        if any(guess in x for x in active_game.guesses):
            clear()
            print("You already guessed that!")
            continue

        if guess == code:
            clear()
            print(f"Congratulations! You solved it in {turn+1} guesses!")
            break

        else:
            feedback = active_game.provide__guess_feedback(guess)
            entry = (guess, feedback)
            active_game.guesses.append(entry)
            turn += 1

            if feedback:
                print(f"Sorry, try again. You have {guesses-turn} guesses remaining. Here's a hint: {feedback}")
            else:
                print(f"None of the numbers you guessed were correct or in the right place. You have {guesses-turn} guesses remaining. ")

            continue

    active_game.display_guess_history()
    print(f"The code was {code}")

if __name__ == '__main__':

    obj = timg.Renderer()
    obj.load_image_from_file("./images/logo.jpeg")
    obj.resize(15,15)
    obj.render(timg.Ansi8HblockMethod) #renders image in terminal, does not work in Windows shell

    print("Welcome to Mastermind!")
    print("Your mission is to guess the secret code!")
    print("You get a hint after each guess: an O means you got a number correct in the right spot, while X means you got a number correct in the wrong spot.")
    print("The Os and Xs are not ordered, and duplicate numbers are not shown in feedback.")

    while True:

        game_loop()
        restart = input("Do you want to try again, Y/N? ").lower()

        if restart == 'n':
            quit()
        elif restart == 'y':
            continue
