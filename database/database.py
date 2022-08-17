import sqlite3
import datetime
from random import randrange
from game import Game
from guess import Guess

con = sqlite3.connect('scores.db')

def init():
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, correctGuess INT NOT NULL)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS guesses (id INTEGER PRIMARY KEY AUTOINCREMENT, gameId INT NOT NULL, date DATETIME, guess INT NOT NULL, FOREIGN KEY (id) REFERENCES games (id) )''')
    con.commit()
    pass

def getHighestScores(amount):
    pass
    
def getGamesOfPlayer(playerName):
    pass
    
def createGame(name):
    pass
    
def addGuess(gameId, guess):
    pass

def cleanup():
    con.close()

def runTests():
    pass

if __name__ == "__main__":
    init()
    runTests()
    cleanup()
