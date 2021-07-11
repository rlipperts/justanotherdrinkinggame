from flask import Flask
app = Flask(__name__)

class MainApi():
    # app = Flask(__name__)
    def __init__(self):
        pass

    @app.route('/helloWorld')
    def helloWorld(self) -> str:
        return "Hello World!"
