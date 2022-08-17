import datetime

class Guess:
    def __init__(self, id: int = None, gameId: int = None, date: datetime = None, guesses: list = []):
        self.id = id
        self.gameId = gameId
        self.date = date
        self.guesses = guesses

    def __str__(self):
        return "[Guess -> id: " + str(self.id) + ", gameId: " + str(self.gameId) + ", date: " + self.date.strftime("%m/%d/%Y, %H:%M:%S") + ", guesses: " + str(self.guesses) + "]"
