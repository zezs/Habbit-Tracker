from flask import Flask, render_template
import os

app =Flask(__name__)
habits = ["Test habit"]

@app.route("/")
def index():
    return render_template("index.html", title="Habit Tracker - Home", habits=habits)

@app.route("/add", methods=["GET", "POST"])
def add_habit():
    return render_template("add_habit.html", title="Habit Tracker - Add Habit")