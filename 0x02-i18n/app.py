#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz
from datetime import datetime

app = Flask(__name__)

# Configuration class for supported languages and default settings
class Config:
    LANGUAGES = ['en', 'fr']  # Supported languages
    BABEL_DEFAULT_LOCALE = 'en'  # Default locale
    BABEL_DEFAULT_TIMEZONE = 'UTC'  # Default timezone

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

# Function to get a user from the mock user table
def get_user():
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None

# before_request function to set the user
@app.before_request
def before_request():
    g.user = get_user()

# Locale selection function with the specified priority order
@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Timezone selection function with the specified priority order
@babel.timezoneselector
def get_timezone():
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user and g.user.get('timezone'):
        try:
            return pytz.timezone(g.user.get('timezone')).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']

# Define a route for the root URL
@app.route('/')
def index():
    current_locale = get_locale()
    current_timezone = get_timezone()
    
    # Get the current time in the user's timezone
    now = datetime.now(pytz.timezone(current_timezone))
    
    return render_template('7-index.html', locale=current_locale, timezone=current_timezone, current_time=now)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
