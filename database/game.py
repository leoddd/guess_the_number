class Game:
    def __init__(self, id, name, correctGuess, guesses):
        self.id = id
        self.name = name
        self.correctGuess = correctGuess
        self.guesses = guesses
        
    def toString(self):
        g = ""
        for guess in self.guesses:
            g = g + "\n\t" + guess.toString()
        return "Game -> id: " + str(self.id) + ", name: " + str(self.name) + ", guesses: " + g
