class GameSession:
    def __init__(self, code):
        self.code = code
        self.guesses = []

    def provide__guess_feedback(self, guess):
        code = list(self.code)
        guess = list(guess)
        feedback = ''


        for i in range(0, len(guess)):
            if guess[i] == code[i]:
                code[i] = '-'
                guess[i] = '*'
                feedback += "C"

        for i in range(0, len(guess)):
            if guess[i] in code:
                pos = code.index(guess[i])
                code[pos] = '-'
                guess[i] = '*'
                feedback += "W"
        return feedback

    def display_guess_history(self):
        for item in self.guesses:
            print(item)

