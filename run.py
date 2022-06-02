from crypt import methods

from flask import Flask, appcontext_popped

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_word():
    return 'Jesus eu te amo!'
