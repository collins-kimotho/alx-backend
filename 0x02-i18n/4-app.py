#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# Configuration class for supported languages and default settings
class Config:
    LANGUAGES = ['en', 'fr']  # Supported languages
    BABEL_DEFAULT_LOCALE = 'en'  # Default language
    BABEL_DEFAULT_TIMEZONE = 'UTC'  # Default timezone

app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)

# Locale selection function
@babel.localeselector
def get_locale():
    # Check if 'locale' query parameter is present in the request
    locale = request.args.get('locale')
    # If the 'locale' is valid (in the supported languages), return it
    if locale in app.config['LANGUAGES']:
        return locale
    # Otherwise, return the default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Define a route for the root URL
@app.route('/')
def index():
    # Pass the locale to the template
    current_locale = get_locale()
    return render_template('4-index.html', locale=current_locale)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
