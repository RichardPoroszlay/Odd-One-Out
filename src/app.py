from flask import Flask, render_template
from db_functions import *

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'sql11.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql11646848'
app.config['MYSQL_PASSWORD'] = 'h27FqgTnlq'
app.config['MYSQL_DB'] = 'sql11646848'
db_conn = DbConnections(app) 

@app.route('/')
def index():
    return render_template("main-menu.html")


@app.route("/base")
def base():
	return render_template("base.html", word= db_conn.get_random_record())

@app.route("/base/<id>")
def show_word(id):
	return render_template("main-menu.html")

@app.route("/time")
def time():
	return render_template("time.html")

@app.route("/input")
def input():
	return render_template("input.html")

@app.route("/hardcore")
def hardcore():
	return render_template("hardcore.html")

if __name__ == "__main__":
    app.run(debug=True)
