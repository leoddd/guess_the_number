import unittest

def runTests():
    print("Starlord is playing")
    starlordGame = createGame("Starlord", 15)
    addGuess(starlordGame.id, 12)
    addGuess(starlordGame.id, 76)
    addGuess(starlordGame.id, 15)

    print("Gamoroa is playing")
    gamoraGame = createGame("Gamoroa", 99)
    addGuess(gamoraGame.id, 43)
    addGuess(gamoraGame.id, 26)
    addGuess(gamoraGame.id, 34)
    addGuess(gamoraGame.id, 23)
    addGuess(gamoraGame.id, 99)

    print("Groot is playing")
    grootGame = createGame("Groot", 40)
    addGuess(grootGame.id, 7)
    addGuess(grootGame.id, 90)
    addGuess(grootGame.id, 55)
    addGuess(grootGame.id, 23)
    addGuess(grootGame.id, 45)
    addGuess(grootGame.id, 40)

    print("Drax is playing")
    draxGame = createGame("Drax", 30)
    addGuess(draxGame.id, 1)
    addGuess(draxGame.id, 2)
    addGuess(draxGame.id, 3)
    addGuess(draxGame.id, 4)
    addGuess(draxGame.id, 5)
    addGuess(draxGame.id, 6)
    addGuess(draxGame.id, 7)
    addGuess(draxGame.id, 8)
    addGuess(draxGame.id, 9)
    addGuess(draxGame.id, 10)
    addGuess(draxGame.id, 11)
    addGuess(draxGame.id, 12)
    addGuess(draxGame.id, 13)
    addGuess(draxGame.id, 14)
    addGuess(draxGame.id, 15)
    addGuess(draxGame.id, 16)
    addGuess(draxGame.id, 17)
    addGuess(draxGame.id, 18)
    addGuess(draxGame.id, 19)
    addGuess(draxGame.id, 20)
    addGuess(draxGame.id, 21)
    addGuess(draxGame.id, 22)
    addGuess(draxGame.id, 23)
    addGuess(draxGame.id, 24)
    addGuess(draxGame.id, 25)
    addGuess(draxGame.id, 26)
    addGuess(draxGame.id, 27)
    addGuess(draxGame.id, 28)
    addGuess(draxGame.id, 29)
    addGuess(draxGame.id, 30)

    print("Rocket is playing")
    rocketGame = createGame("Rocket")
    addGuess(rocketGame.id, 34)
    addGuess(rocketGame.id, 5)
    addGuess(rocketGame.id, 2)
    addGuess(rocketGame.id, 65)
    addGuess(rocketGame.id, 87)
    addGuess(rocketGame.id, rocketGame.correctGuess)

    print("Mantis is cheating")
    mantisGame = createGame("Mantis")

    print("Thor gives up")
    thorGame = createGame("Thor")
    addGuess(thorGame.id, 90)
    addGuess(thorGame.id, 43)
    addGuess(thorGame.id, 76)
    addGuess(thorGame.id, 2)
    addGuess(thorGame.id, 76)
    addGuess(thorGame.id, 3)
    addGuess(thorGame.id, 12)
    addGuess(thorGame.id, 7)
    addGuess(thorGame.id, 9)

    print("###   Highscores   ###")
    highScores = getHighestScores(4)
    for game in highScores:
        print(str(game))

    print("###   Mantis Games   ###")
    mantisScores = getGamesOfPlayer("Mantis")
    for game in mantisScores:
        print(str(game))

    print("###   Rocket Game   ###")
    rocketGameScore = getGameById(rocketGame.id)
    print(str(rocketGameScore))

class TestStringMethods(unittest.TestCase):

    def test_(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_highscore(self):
        runTests()

if __name__ == '__main__':
    unittest.main()