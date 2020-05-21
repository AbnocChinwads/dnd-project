import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "some_secret"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/beginning")
def beginning():
    return render_template("beginning.html")


@app.route("/charactercreation")
def charactercreation():
    return render_template("charactercreation.html")


@app.route("/combat")
def combat():
    return render_template("combat.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
