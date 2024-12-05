import os

from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from . import bp_home
    app.register_blueprint(bp_home.bp)

    return app