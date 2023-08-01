#!/usr/bin/env python3
from flask import Flask, render_template

""" A simple flask app that serves an html page """


app = Flask(__name__)

@app.route('/')
def home():
    """ Home route that serves the 
    landing page """

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
