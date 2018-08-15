'''
    Multiple controllers:
        https://stackoverflow.com/questions/15231359/split-python-flask-app-into-multiple-files
'''

from flask import Flask
from rest_api import *

app = Flask(__name__)

app.register_blueprint(api)

'''
@app.route("/")
def hello():
    return "Hello World!"
'''

if __name__ == "__main__":
    app.run()