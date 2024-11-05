from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale():
    """
    Determines the best match for supported languages
    based on the request's Accept-Language headers
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def home():
    """
    Render the home page with a welcome message
    """
    return render_template('2-index.html')

if __name__ == "__main__":
    app.run(debug=True)