class GameSession:
    def __init__(self, code):
        self.code = code
        self.guesses = []

    def provide__guess_feedback(self, guess: str) -> str:

        """Compares guess against generated code and returns feedback"""

        code = list(self.code)
        guess = list(guess)
        feedback = ''

        # iterates through guess and code to find exact matches first, removing as it finds them
        for i, val in enumerate(guess):
            if val == code[i]:
                code[i] = '-'
                guess[i] = '*'
                feedback += "O"

        # identifies any remaining guesses that are in the code but not in the right place
        for i, val in enumerate(guess):
            if val in code:
                pos = code.index(val)
                code[pos] = '-'
                guess[i] = '*'
                feedback += "X"
        return feedback

    def display_guess_history(self):

        """Iterates through array of stored guess tuples and prints each one"""

        for item in self.guesses:
            print(item)
