from flask import Flask
import os

from jadg.api.game_communication import Messenger

def create_app(test_config=None) -> Flask:
    """https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/"""
    app: Flask = Flask(__name__, instance_relative_config=True)
    messsenger = Messenger()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/helloWorld')
    def helloWorld() -> str:
        return messsenger.hello_world()

    return app
