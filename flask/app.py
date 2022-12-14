from flask import Flask, render_template, request, redirect, url_for
from database.database import Database

app = Flask(__name__)
db = Database()

@app.route('/')
def requestName():
    return render_template('RequestName.html')

@app.route('/game')
def game():
    game_id = request.args.get('game_id', None, int)

    game = db.getGameById(
        game_id
    )

    if game is None:
        return new_game()

    if game.is_won():
        return redirect(url_for('correctGuess', **request.args))

    return render_template('Game.html', game = game)

@app.route('/leaderboard')
def leaderboard():
    return render_template(
        'Leaderboard.html',
        leaderboard = db.getHighestScores(10)
    )

@app.route('/running')
def runningGames():
    return render_template(
        'RunningGames.html',
        running_games = db.getUnfinishedGames()
    )

@app.route('/start', methods = ['POST'])
def startGame():
    name = request.form.get('name', None, str)
    if name is None:
        return new_game()

    game = db.createGame(name)
    if game is None:
        return new_game()

    return redirect(url_for('game', game_id = game.id))

@app.route('/guess', methods = ['POST'])
def makeGuess():
    game_id = request.form.get('game_id', None, int)
    guessed_number = request.form.get('guessed_number', None, int)

    if game_id is None or guessed_number is None:
        return new_game()

    game = db.getGameById(game_id)
    if game is None:
        return new_game()

    db.addGuess(game.id, guessed_number)

    if game.correctGuess != guessed_number:
        return redirect(url_for('game', game_id = game.id))

    return redirect(url_for('correctGuess', game_id = game.id))

@app.route('/gg')
def correctGuess():
    game_id = request.args.get('game_id', None, int)

    if game_id is None:
        return new_game()

    game = db.getGameById(game_id)
    if game is None:
        return new_game()

    if not game.is_won():
        return redirect(url_for('game', **request.args))

    return render_template(
        'CorrectGuess.html',
        game = game,
        leaderboard = db.getHighestScores(10)
    )

def new_game():
    return redirect(url_for('requestName'))

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 80)
