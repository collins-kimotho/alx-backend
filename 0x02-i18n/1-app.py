#!/usr/bin/env python3
"""
A Flask application with Babel for language localization
"""

from flask import Flask, render_template
from flask_babel import Babel

class Config:
    """
    Config class for setting available languages,
    default locale, and timezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_tIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@app.route('/')
def home():
    """
    Renders the home page with a welcome message
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(debug=True)