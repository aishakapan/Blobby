from Blobby import blobby
from flask import Flask
import flask
app = Flask(__name__)

# if __name__ == '__main__':
#     try:
#         blobby1 = blobby.load()
#     except Exception:
blobby1 = blobby.Blobby(starting_hunger=50)


@app.route("/inspect")
def inspect():
    inspecting = blobby1.inspect()
    return inspecting


@app.route("/feed")
def feed():
    feeding = blobby1.feed()
    feeding = blobby1.inspect()
    return feeding


@app.route("/play")
def play():
    playing = blobby1.play()
    playing = blobby1.inspect()
    return playing
