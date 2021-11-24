import os
import click
import timg


from rng_api import RandomAPI
from game_session import GameSession

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

difficulty_setting = {
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


def game_loop(choice):

    code = RandomAPI().get_mastermind_code(difficulty_setting[choice])
    active_game = GameSession(code)
    guesses = difficulty_setting[choice]["guesses"]

    turn = 0

    while turn < guesses:
        print("Guess the mastermind code")
        

        try:

            if turn:
                active_game.display_guess_history()
            print(f'You have {guesses-turn} guesses left.')  
           
            guess = input("Enter your choice: ")
            
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
    obj.render(timg.Ansi8HblockMethod)
    print("Welcome to Mastermind!")
    user_choice = set_difficulty(standalone_mode=False)

    while True:

        game_loop(user_choice)
        restart = input("Do you want to try again, Y/N? ").lower()

        if restart == 'n':
            print(restart)
            quit()
        elif restart == 'y':
            continue