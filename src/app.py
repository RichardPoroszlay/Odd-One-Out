from flask import Flask, redirect, render_template, url_for
from flask import request
from db_functions import *

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'sql11.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql11646848'
app.config['MYSQL_PASSWORD'] = 'h27FqgTnlq'
app.config['MYSQL_DB'] = 'sql11646848'
db_conn = DbConnections(app)

rounds_to_play = 0
rounds_won = 0
rounds_lost = 0
solution = None

def get_solution(words):
	global solution
	solution = words[-1]

@app.route('/')
def index():
    return render_template("main-menu.html")


@app.route("/base")
def base():
	word = db_conn.get_random_record()
	get_solution(word)
	return render_template("base.html", word=word)

@app.route("/base/<id>")
def show_word(id):
	if id == solution:
		return render_template("won.html")
	else:
		return render_template("lost.html")

@app.route("/time")
def time():
	return render_template("time.html")

@app.route("/input")
def input():
	return render_template("input.html")

@app.route('/input_game', methods=['GET', 'POST'])
def input_game():
    global rounds_to_play  

    if request.method == 'POST':
        rounds = int(request.form.get('rounds'))
        rounds_to_play = rounds
        word = db_conn.get_random_record()
        get_solution(word)
        return render_template('input_game.html', word=word)

    while rounds_to_play-1 > 0:
        word = db_conn.get_random_record()
        get_solution(word)
        rounds_to_play -= 1
        return render_template('input_game.html', word=word)
    return redirect(url_for('game_result'))

@app.route('/store_result', methods=['POST'])
def store_result():
	result = request.form.get('result')
	global rounds_lost
	global rounds_won

	if result == solution:
		rounds_won += 1
	else:
		rounds_lost += 1

@app.route('/game_result')
def game_result():
    return render_template('input_game_result.html')

@app.route("/hardcore")
def hardcore():
	return render_template("hardcore.html")

if __name__ == "__main__":
    app.run(debug=True)
