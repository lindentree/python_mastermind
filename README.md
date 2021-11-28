# Mastermind Game

This is a command-line implementation of the code-breaking game Mastermind(https://en.wikipedia.org/wiki/Mastermind_(board_game) where you play against the computer.

## Usage

Git clone or download this repo to play the game. You need a Python installation on your computer. \*Note: this was designed to run with Python 3.10.0, but Python 3.7 and up should be fine.

After you cd into the repo folder, install all the relevant packages first.

`pip install pipenv --user`

`pipenv install`

Then use `pipenv shell` to activate the virtual environment, and run `python main.py`

Alternatively, if Docker is available on your machine, you can use that to run the app.

Use `docker build -t <image_name> .` to build the image.

Then `docker run -it <image_name>` \*\*The it flag makes the container interactive.

## Development

This project uses pytest for TDD; run `pytest tests` to see the ouptut of the current unit tests.
Currently you have to manually rebuild the Docker image after making code changes.

## Acceptance Criteria

Please implement a mastermind game, which can be played by a user "against" the computer. This is a game where a player tries to guess the number combinations. At the end of each attempt to guess the 4 number combinations, the computer will provide feedback whether the player had guessed a number correctly, or/and a number and digit correctly. A player must guess the right number combinations within 10 attempts to win the game.

### Game rules

• At the start of the game the computer will randomly select a pattern of four different numbers from a total of 8 different numbers.
• A player will have 10 attempts to guess the number combinations
• At the end of each guess, computer will provide one of the following response
as feedback:
• The player had guessed a correct number
• The player had guessed a correct number and its correct location
• The player’s guess was incorrect
\*\*Note that the computer’s feedback should not reveal which number the player guessed correctly

## Implementation Details

Uses the Random API to generate random number combinations.
Example format: https://www.random.org/integers/?num=4&min=0&max=4&col=4&base=10&format=plain&rnd=new

## Extra Features

Sample extension ideas include:

• Add support to give hints [-]

• Add a configurable “difficulty level” and adjust the number of numbers that are used [x]

• Draw all of graphical components, add animations and sounds []

• Change numbers into colored pegs, shapes, animals, etc []

• Keep track of scores(arcade style leaderboard) []

• Add a timer for the entire game, or each guess attempt []

• Anything else that you come up with to make the game more fun/interesting! []
