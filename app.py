from Blobby import blobby
from flask import Flask
import flask
app = Flask(__name__)


# try:
#     blobby1 = blobby.load()
# except Exception:
blobby1 = blobby.Blobby(starting_hunger=50)

@app.route("/")
@app.route("/inspect")
def inspect():
    inspecting = blobby1.inspect()
    hunger_image = 'static/happy.png'
    boredom_image = 'static/happy.png'

    if blobby1.hunger > 50:
        hunger_image = 'static/hungry.png'
    elif blobby1.hunger < 10:
        hunger_image = 'static/happy.png'


    if blobby1.boredom > 50:
        boredom_image = 'static/sleepy.png'
    elif blobby1.boredom < 10:
        boredom_image = 'static/happy.png'

    html = flask.render_template('blobby.html',
                                 hunger = inspecting[0],
                                 boredom = inspecting[1],
                                 hunger_image = hunger_image,
                                 boredom_image = boredom_image)
    return html

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
