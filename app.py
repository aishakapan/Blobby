from Blobby import blobby
from flask import Flask
import flask
app = Flask(__name__)


blobby1 = blobby.Blobby()

@app.route("/")
@app.route("/inspect")
def inspect():
    inspecting = blobby1.inspect()
    blobby_image = 'static/happy.png'

    hunger = blobby1.inspect_hunger()
    boredom = blobby1.inspect_boredom()
    health_problems = hunger + boredom
    print(health_problems)


    if health_problems < 10:
        blobby_image = 'static/very_happy.png'
    elif 10 < health_problems < 40:
        blobby_image = 'static/happy.png'
    elif 40 < health_problems < 60:
        blobby_image = 'static/neutral.png'
    elif 60 < health_problems < 80:
        blobby_image = 'static/sad.png'
    else:
        blobby_image = 'static/very_sad.png'



    html = flask.render_template('blobby.html',
                                 hunger=inspecting[0],
                                 boredom=inspecting[1],
                                 blobby_image=blobby_image)
    return html

@app.route("/feed")
def feed():
    feeding = blobby1.feed()
    url_for_inspect = flask.url_for('inspect')
    redirect = flask.redirect(url_for_inspect)
    return redirect


@app.route("/play")
def play():
    playing = blobby1.play()
    url_for_inspect = flask.url_for('inspect')
    redirect = flask.redirect(url_for_inspect)
    return redirect