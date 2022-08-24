class Game:
    def __init__(self, id: int = None, name: str = "", correctGuess: int = 10, guesses: list = []):
        self.id = id
        self.name = name
        self.correctGuess = correctGuess
        self.guesses = guesses

    def is_won(self):
        if self.guesses == None or len(self.guesses) <= 0:
            return False
        else:
            for guess in self.guesses:
                if guess.guess == self.correctGuess:
                    print(guess.guess, self.correctGuess)
                    return True

        return False

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        g = ""
        for guess in self.guesses:
            g = g + "\n\t" + str(guess)

        if len(g) == 0:
            g = "\n\tNone"

        return "[Game (" + str(id(self)) + ") -> id: " + str(self.id) + ", name: " + str(self.name) + ", correctGuess: " + str(self.correctGuess) + ", guesses: " + g + "]"
