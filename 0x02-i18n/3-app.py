#!/usr/bin/env python3
""" A simple flask app that serves an html page """


from flask import Flask, render_template, request
from flask_babel import Babel

class Config(object):
    """languages"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """gets the locale of
    user
    """

    return request.accept_languages.best_match(app.config(['LANGUAGES']))


@app.route('/')
def home():
    """ Home route that serves the
    landing page """

    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
