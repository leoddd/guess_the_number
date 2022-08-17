class Guess:
    def __init__(self, id, gameId, date, guess):
        self.id = id
        self.gameId = gameId
        self.date = date
        self.guess = guess

    def __str__(self):
        return "Guess -> id: " + str(self.id) + ", gameId: " + str(self.gameId) + ", date: " + self.date.strftime("%m/%d/%Y, %H:%M:%S") + ", guess: " + str(self.guess)
