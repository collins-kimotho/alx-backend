#!/usr/bin/env python3
"""
A basic Flask application with a single route.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the home page with a welcome message.
    """
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run(debug=True)
Install the Babel Flask extension:

$ pip3 install flask_babel==2.0.0
Then instantiate the Babel object in your app. Store it in a module-level variable named babel.

In order to configure available languages in our app, you will create a Config class that has a LANGUAGES class attribute equal to ["en", "fr"].

Use Config to set Babel’s default locale ("en") and timezone ("UTC").

Use that class as config for your Flask app.

Repo:

GitHub repository: alx-backend
Directory: 0x02-i18n
File: 1-app.py, templates/1-index.html