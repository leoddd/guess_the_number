class Game:
    def __init__(self, id, name, correctGuess, guesses):
        self.id = id
        self.name = name
        self.correctGuess = correctGuess
        self.guesses = guesses

    def __str__(self):
        g = ""
        for guess in self.guesses:
            g = g + "\n\t" + guess.toString()

        if len(g) == 0:
            g = "\n\tNone"

        return "Game -> id: " + str(self.id) + ", name: " + str(self.name) + ", correctGuess: " + str(self.correctGuess) + ", guesses: " + g
