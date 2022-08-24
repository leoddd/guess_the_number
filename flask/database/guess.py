import datetime

class Guess:
    def __init__(self, id: int = None, gameId: int = None, date: datetime = None, guess: int = None):
        self.id = id
        self.gameId = gameId
        self.date = date
        self.guess = guess

    def __str__(self):
        return "[Guess -> id: " + str(self.id) + ", gameId: " + str(self.gameId) + ", guess: " + str(self.guess) + "]"
