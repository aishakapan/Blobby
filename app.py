from Blobby import blobby, blobby_speech
from flask import Flask, request
from wtforms import Form, StringField, SubmitField
import requests
import flask


app = Flask(__name__)


blobby1 = blobby.Blobby()

class MessageForm(Form):
    message = StringField('Tell Blobby what happened today')
    submit = SubmitField('Send')


@app.route('/')
@app.route('/inspect')
def inspect():
    inspecting = blobby1.inspect()
    blobby_image = 'static/happy.png'

    hunger = blobby1.inspect_hunger()
    boredom = blobby1.inspect_boredom()
    health_problems = hunger + boredom



    if health_problems <= 10:
        blobby_image = 'static/very_happy.png'
    elif 10 < health_problems <= 40:
        blobby_image = 'static/happy.png'
    elif 40 < health_problems <= 60:
        blobby_image = 'static/neutral.png'
    elif 60 < health_problems <= 80:
        blobby_image = 'static/sad.png'
    elif 80 < health_problems <= 100:
        blobby_image = 'static/very_sad.png'



    html = flask.render_template('blobby.html',
                                 hunger=inspecting[0],
                                 boredom=inspecting[1],
                                 blobby_image=blobby_image)
    return html

@app.route('/feed')
def feed():
    feeding = blobby1.feed()
    url_for_inspect = flask.url_for('inspect')
    redirect = flask.redirect(url_for_inspect)
    return redirect


@app.route('/play')
def play():
    playing = blobby1.play()
    url_for_inspect = flask.url_for('inspect')
    redirect = flask.redirect(url_for_inspect)
    return redirect


@app.route('/respond', methods=['GET', 'POST'])
def respond():
    message = MessageForm(request.form)
    if message.validate():
        print("MESSAGE DATA RECEIVED", message.data)
        response = blobby_speech.process_sentiment(message.data.get("message", ""))
        html = flask.render_template('response.html',
                                 response=response,
                                 )
        return html


@app.route('/chat', methods=['GET'])
def chat():
    message = MessageForm(request.form)
    print("MESSAGE DATA SENT", message.data)
    html = flask.render_template('chat.html',
                                 form=message
                                 )
    return html





