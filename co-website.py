from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/covid")
def covid():
    return render_template("covid.html")


@app.route("/symptoms")
def symptoms():
    return render_template("symptoms.html")


@app.route("/prevention")
def prevention():
    return render_template("prevention.html")


if __name__ == "__main__":
    app.run()
