# Mastermind Game

## Usage

Git clone or download this repo to play the game.
The game script(main.py) should work out of the box if you have Python installed on your machine. You can cd into the folder and run `python main.py`; however, you should use the pipenv package manager to install all the relevant packages first.

`pip install pipenv --user`
`pipenv install`

Then use `pipenv shell` to activate the virtual environment.

\*Note: this was designed to run with Python 3.10.0, but Python 3.7 and up should be fine.

## Development

This project uses pytest for TDD; run `pytest tests` to see the current tests.

## Acceptance Criteria

Please implement a mastermind game, which can be played by a user "against" the computer. This is a game where a player tries to guess the number combinations. At the end of each attempt to guess the 4 number combinations, the computer will provide feedback whether the player had guessed a number correctly, or/and a number and digit correctly. A player must guess the right number combinations within 10 attempts to win the game.

Game rules
• At the start of the game the computer will randomly select a pattern of four different numbers from a total of 8 different numbers.
• A player will have 10 attempts to guess the number combinations
• At the end of each guess, computer will provide one of the following response
as feedback:
• The player had guessed a correct number
• The player had guessed a correct number and its correct location
• The player’s guess was incorrect
\*\*Note that the computer’s feedback should not reveal which number the player guessed correctly

## Implementation Details

Uses the Random API to generate random combinations

https://www.random.org/integers/?num=4&min=0&max=${limit}&col=4&base=10&format=plain&rnd=new

## Extra Features

Sample extension ideas include:
• Add support to give hints []
• Add a configurable “difficulty level” and adjust the number of numbers that are used [x]
• Draw all of graphical components, add animations and sounds []
• Change numbers into colored pegs, shapes, animals, etc []
• Keep track of scores(arcade style leaderboard) []
• Add a timer for the entire game, or each guess attempt []
• Anything else that you come up with to make the game more fun/interesting!
