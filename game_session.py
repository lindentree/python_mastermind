class GameSession:
    def __init__(self, code):
        self.code = code
        self.guesses = []

    def provide__guess_feedback(self, guess: str) -> str:

        code = list(self.code)
        guess = list(guess)
        feedback = ''

        for i, val in enumerate(guess):
            if val == code[i]:
                code[i] = '-'
                val = '*'
                feedback += "O"

        for i, val in enumerate(guess):
            if val in code:
                pos = code.index(val)
                code[pos] = '-'
                val = '*'
                feedback += "X"
        return feedback

    def display_guess_history(self):
        for item in self.guesses:
            print(item)

