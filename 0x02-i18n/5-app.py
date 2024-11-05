#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import babel

app = Flask(__name__)

# Configuration class for supported languages and default settings
class Config:
    LANGUAGES = ['en', 'fr'] # Supported languages
    BABEL_DEFAULT_LOCALE = 'en' # Default language
    BABEL_DEFAULT_TIMEZONE = 'UTC' # Default timezone

app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Function to get user from mock user table
def get_user():
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return user.get(int(user_id))
    return None

# before_request function to set the user
@app.before_request
def before_request():
    g.user = get_user()

# Locale selection function with priority order
@babel.localeselector
def get_locale():
    # Check if 'locale' query parameter is present in the request
    if locale and locale in app.config['LANGUAGES']:
        return locale
    
    #  Check the user's preferred locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    
    # otherwise return the best match from the request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Define a route for the root URL
@app.route('/')
def index():
    current_locale = get_locale()
    return render_template('5-index.html', locale=current_locale)

# run the flask app
if __name__ == '__main__':
    app.run(debug=True)