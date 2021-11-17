# Acceptance Criteria

Mastermind Game
Please implement a mastermind game, which can be played by a user "against" the computer. Thisisagamewhereaplayertriestoguessthenumbercombinations. Attheendofeach attempt to guess the 4 number combinations, the computer will provide feedback whether the player had guess a number correctly, or/and a number and digit correctly. A player must guess the right number combinations within 10 attempts to win the game.
Game rules
• At the start of the game the computer will randomly select a pattern of four different numbers from a total of 8 different numbers.
• A player will have 10 attempts to guess the number combinations
• At the end of each guess, computer will provide one of the following response
as feedback:
• The player had guess a correct number
• The player had guessed a correct number and its correct location
• The player’s guess was incorrect
\*\*Note that the computer’s feedback should not reveal which number the player guessed correctly

# Implementation Details

https://www.random.org/integers/?num=4&min=0&max=${limit}&col=4&base=10&format=plain&rnd=new
