#!/usr/bin/env python3
"""
A Flask application with Babel for language localization and template parametrization.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

class Config:
    """
    Configuration class for setting available languages, default locale, and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale():
    """
    Determines the best match for supported languages based on the request's Accept-Language headers.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def home():
    """
    Renders the home page with localized messages.
    """
    return render_template('3-index.html', home_title=_("home_title"), home_header=_("home_header"))

if __name__ == "__main__":
    app.run(debug=True)

# Import _ from flask_babel: This is used to mark text for translation.
# Using _() in render_template: The _("home_title") and _("home_header") calls mark these strings as message IDs for translation.
