import sqlite3
import datetime
from random import randrange
from .game import Game
from .guess import Guess

class Database:
    def __init__(self, clear=False):
        self.con = sqlite3.connect('scores.db', detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES, check_same_thread = False)
        cur = self.con.cursor()
        if clear:
            cur.execute('''DROP TABLE IF EXISTS games''')
            cur.execute('''DROP TABLE IF EXISTS guesses''')
        cur.execute('''CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, correctGuess INT NOT NULL)''')
        cur.execute('''CREATE TABLE IF NOT EXISTS guesses (id INTEGER PRIMARY KEY AUTOINCREMENT, gameId INT NOT NULL, date TIMESTAMP, guess INT NOT NULL, FOREIGN KEY (id) REFERENCES games (id) )''')
        self.con.commit()

    def getHighestScores(self, amount):
        cur = self.con.cursor()
        sqlite_select_game_with_param = """SELECT ga.id, ga.name, ga.correctGuess from games ga WHERE ga.correctGuess IN (SELECT gu.guess FROM guesses gu WHERE gu.gameId == ga.id) ORDER BY (SELECT COUNT(*) FROM guesses guu WHERE guu.gameId == ga.id) LIMIT (?)"""
        data_tuple = (amount,)
        cur.execute(sqlite_select_game_with_param, data_tuple)
        records = cur.fetchall()
        games = []
        for game in records:
            gameId = game[0]
            name = game[1]
            correctGuess = game[2]

            sqlite_select_guesses_with_param = """SELECT id, date, guess from guesses WHERE gameId == (?)"""
            data_tuple = (gameId,)
            cur.execute(sqlite_select_guesses_with_param, data_tuple)
            guessRecords = cur.fetchall()

            guesses = []
            for guess in guessRecords:
                guessId = guess[0]
                guessDate = guess[1]
                guessNumber = guess[2]
                guesses.append(Guess(guessId, gameId, guessDate, guessNumber))

            games.append(Game(gameId, name, correctGuess, guesses))

        return games

    def getUnfinishedGames(self):
        cur = self.con.cursor()
        sqlite_select_game_with_param = """SELECT ga.id, ga.name, ga.correctGuess from games ga WHERE ga.correctGuess NOT IN (SELECT gu.guess FROM guesses gu WHERE gu.gameId == ga.id)"""
        cur.execute(sqlite_select_game_with_param)
        records = cur.fetchall()
        games = []
        for game in records:
            gameId = game[0]
            name = game[1]
            correctGuess = game[2]

            sqlite_select_guesses_with_param = """SELECT id, date, guess from guesses WHERE gameId == (?)"""
            data_tuple = (gameId,)
            cur.execute(sqlite_select_guesses_with_param, data_tuple)
            guessRecords = cur.fetchall()

            guesses = []
            for guess in guessRecords:
                guessId = guess[0]
                guessDate = guess[1]
                guessNumber = guess[2]
                guesses.append(Guess(guessId, gameId, guessDate, guessNumber))

            games.append(Game(gameId, name, correctGuess, guesses))

        return games

    def getGamesOfPlayer(self, playerName):
        cur = self.con.cursor()
        sqlite_select_game_with_param = """SELECT id, name, correctGuess from games WHERE name == (?)"""
        data_tuple = (playerName,)
        cur.execute(sqlite_select_game_with_param, data_tuple)
        records = cur.fetchall()
        games = []
        for game in records:
            gameId = game[0]
            name = game[1]
            correctGuess = game[2]

            sqlite_select_guesses_with_param = """SELECT id, date, guess from guesses WHERE gameId == (?)"""
            data_tuple = (gameId,)
            cur.execute(sqlite_select_guesses_with_param, data_tuple)
            guessRecords = cur.fetchall()

            guesses = []
            for guess in guessRecords:
                guessId = guess[0]
                guessDate = guess[1]
                guessNumber = guess[2]
                guesses.append(Guess(guessId, gameId, guessDate, guessNumber))

            games.append(Game(gameId, name, correctGuess, guesses))

        return games

    def getGameById(self, id):
        cur = self.con.cursor()
        sqlite_select_game_with_param = """SELECT id, name, correctGuess from games WHERE id == (?)"""
        data_tuple = (id,)
        cur.execute(sqlite_select_game_with_param, data_tuple)
        records = cur.fetchall()
        if len(records) > 0:
            gameId = records[0][0]
            name = records[0][1]
            correctGuess = records[0][2]

            sqlite_select_guesses_with_param = """SELECT id, date, guess from guesses WHERE gameId == (?)"""
            data_tuple = (gameId,)
            cur.execute(sqlite_select_guesses_with_param, data_tuple)
            records = cur.fetchall()

            guesses = []
            for row in records:
                guessId = row[0]
                guessDate = row[1]
                guessNumber = row[2]
                guesses.append(Guess(guessId, gameId, guessDate, guessNumber))

            return Game(gameId, name, correctGuess, guesses)

    def createGame(self, name, correctGuess = -1):
        cur = self.con.cursor()
        sqlite_insert_with_param = """INSERT INTO 'games'('name', 'correctGuess')VALUES (?, ?);"""
        if correctGuess == -1:
            correctGuess = randrange(1,101)
        data_tuple = (name, correctGuess)
        cur.execute(sqlite_insert_with_param, data_tuple)
        self.con.commit()
        sqlite_select_query = """SELECT id from games ORDER BY id DESC LIMIT 1"""
        cur.execute(sqlite_select_query, ())
        records = cur.fetchall()
        id = records[0][0]
        cur.close()
        return Game(id, name, correctGuess, [])


    def addGuess(self, gameId, guess):
        cur = self.con.cursor()
        sqlite_insert_with_param = """INSERT INTO 'guesses'('gameId', 'date', 'guess')VALUES (?, ?, ?);"""
        data_tuple = (gameId, datetime.datetime.now(), guess)
        cur.execute(sqlite_insert_with_param, data_tuple)
        self.con.commit()
        cur.close()

    def __del__(self):
        self.con.close()

    def runTests(self):
        print("Starlord is playing")
        starlordGame = self.createGame("Starlord")
        self.addGuess(starlordGame.id, 12)
        self.addGuess(starlordGame.id, 76)
        self.addGuess(starlordGame.id, starlordGame.correctGuess)

        print("Gamoroa is playing")
        gamoraGame = self.createGame("Gamoroa")
        self.addGuess(gamoraGame.id, 43)
        self.addGuess(gamoraGame.id, 26)
        self.addGuess(gamoraGame.id, 34)
        self.addGuess(gamoraGame.id, 23)
        self.addGuess(gamoraGame.id, gamoraGame.correctGuess)

        print("Groot is playing")
        grootGame = self.createGame("Groot")
        self.addGuess(grootGame.id, 7)
        self.addGuess(grootGame.id, 4)
        self.addGuess(grootGame.id, 90)
        self.addGuess(grootGame.id, 1)
        self.addGuess(grootGame.id, 78)
        self.addGuess(grootGame.id, grootGame.correctGuess)

        print("Drax is playing")
        draxGame = self.createGame("Drax")
        self.addGuess(draxGame.id, 76)
        self.addGuess(draxGame.id, 4)
        self.addGuess(draxGame.id, 7)
        self.addGuess(draxGame.id, 24)
        self.addGuess(draxGame.id, 54)
        self.addGuess(draxGame.id, draxGame.correctGuess)

        print("Rocket is playing")
        rocketGame = self.createGame("Rocket")
        self.addGuess(rocketGame.id, 34)
        self.addGuess(rocketGame.id, 5)
        self.addGuess(rocketGame.id, 2)
        self.addGuess(rocketGame.id, 65)
        self.addGuess(rocketGame.id, 87)
        self.addGuess(rocketGame.id, rocketGame.correctGuess)

        print("Mantis is cheating")
        mantisGame = self.createGame("Mantis")

        print("Thor gives up")
        thorGame = self.createGame("Thor")
        self.addGuess(thorGame.id, 90)
        self.addGuess(thorGame.id, 43)
        self.addGuess(thorGame.id, 76)
        self.addGuess(thorGame.id, 2)
        self.addGuess(thorGame.id, 76)
        self.addGuess(thorGame.id, 3)
        self.addGuess(thorGame.id, 12)
        self.addGuess(thorGame.id, 7)
        self.addGuess(thorGame.id, 9)

        print("###   Highscores   ###")
        highScores = self.getHighestScores(4)
        for game in highScores:
            print(str(game))

        print("###   Mantis Games   ###")
        mantisScores = self.getGamesOfPlayer("Mantis")
        for game in mantisScores:
            print(str(game))

        print("###   Rocket Game   ###")
        rocketGameScore = self.getGameById(rocketGame.id)
        print(str(rocketGameScore))

if __name__ == "__main__":
    db = Database(clear=True)
    db.runTests()
