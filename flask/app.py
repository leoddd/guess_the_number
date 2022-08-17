from flask import Flask, render_template, request
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/')
def initialize():
    arguments = request.args;
    try:
        game = db.get_game(arguments['game'])
    except:
        return render_template('newGame.html')

    return render_template(
        'main.html',
        args = request.args
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
