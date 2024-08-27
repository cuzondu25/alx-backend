#!/usr/bin/env python3
"""
Flask app
"""
from flask import (
    Flask,
    render_template,
    request
)
from flask_babel import Babel


class Config(object):
    """
    Babel configuration
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
    To select and return best language match based on supported languages
    """
    loacl = request.args.get('locale')
    if loacl in app.config['LANGUAGES']:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles root / route
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    """
    Run flask app
    """
    app.run(port="5000", host="0.0.0.0", debug=True)
