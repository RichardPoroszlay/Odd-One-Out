from flask import Flask, redirect, render_template, url_for
from flask import request
from db_functions import *

app = Flask(__name__)


app.config["MYSQL_HOST"] = "sql11.freemysqlhosting.net"
app.config["MYSQL_USER"] = "sql11646848"
app.config["MYSQL_PASSWORD"] = "h27FqgTnlq"
app.config["MYSQL_DB"] = "sql11646848"
db_conn = DbConnections(app)

rounds_to_play = 0
rounds_won = 0
rounds_lost = 0
solution = None

hc_score = 0

tr_score = 0


def get_solution(words):
    global solution
    solution = words[-1]


@app.route("/")
def index():
    global tr_score
    tr_score = 0
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


@app.route("/time-race")
def time_race():
    global tr_score
    word = db_conn.get_random_record()
    get_solution(word)
    return render_template("time-race.html", word=word, tr_score=tr_score)


@app.route("/time-race/<id>")
def show_next_tr(id):
    global tr_score
    if id == solution:
        tr_score += 1
        return redirect(url_for("time_race"))
    else:
        return redirect(url_for("time_race"))


@app.route("/tr-timeout")
def show_tr_lost():
    global tr_score
    temp_score = tr_score
    tr_score = 0
    return render_template("tr-timeout.html", tr_score=temp_score)


@app.route("/input")
def input():
    return render_template("input.html")


@app.route("/input_game", methods=["GET", "POST"])
def input_game():
    global rounds_to_play

    if request.method == "POST":
        rounds = int(request.form.get("rounds"))
        if rounds < 1:
            return render_template("lost.html")
        rounds_to_play = rounds
        word = db_conn.get_random_record()
        get_solution(word)
        return render_template("input_game.html", word=word)
    elif rounds_to_play - 1 > 0:
        rounds_to_play -= 1
        word = db_conn.get_random_record()
        get_solution(word)
        return render_template("input_game.html", word=word)
    return redirect(url_for("game_result"))


@app.route("/input_game/<id>")
def store_result(id):
    global rounds_won
    global rounds_lost

    if id == solution:
        rounds_won += 1
        return redirect(url_for("input_game"))
    else:
        rounds_lost += 1
        return redirect(url_for("input_game"))


@app.route("/game_result")
def game_result():
    global rounds_won
    global rounds_lost
    rounds_won_holder = rounds_won
    rounds_lost_holder = rounds_lost
    rounds_won = 0
    rounds_lost = 0
    return render_template(
        "input_game_result.html", rounds_won=rounds_won_holder, rounds_lost=rounds_lost_holder
    )


@app.route("/hardcore")
def hardcore():
    global hc_score
    word = db_conn.get_random_record()
    get_solution(word)
    return render_template("hardcore.html", word=word, hc_score=hc_score)


@app.route("/hardcore/<id>")
def show_next(id):
    global hc_score
    if id == solution:
        hc_score += 1
        print(hc_score)
        return redirect(url_for("hardcore"))
    else:
        print(hc_score)
        temp_score = hc_score
        hc_score = 0
        return render_template("hc_lost.html", hc_score=temp_score)


if __name__ == "__main__":
    app.run(debug=True)
