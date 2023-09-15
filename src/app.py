from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
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
