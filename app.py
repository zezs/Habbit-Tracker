from flask import Flask, render_template
import os

app =Flask(__name__)

@app.route("/")
def hello():
    return "Hello ji!"