from flask import Flask
# from flask_wtf.csrf import CSRFProtect
from views import tsm_view
from settings import DevelopmentConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())
    app.register_blueprint(tsm_view.bp)
    return app


app = create_app()
