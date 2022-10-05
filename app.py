import flask
from Blobby import blobby, blobby_speech
from Blobby import bgraphics
from flask import Flask, request
from wtforms import Form, StringField, SubmitField




app = Flask(__name__)


# TODO: forms should be separate, also it's a CHAT so better use sth different
class MessageForm(Form):
    message = StringField('Tell Blobby what happened today')
    submit = SubmitField('Send')


@app.route('/')
@app.route('/inspect')
def inspect():
    blobby1 = blobby.load()
    inspecting = blobby1.inspect()
    blobby_image = 'static/happy.png'
    blobby1.poop()

    hunger = blobby1.inspect_hunger()
    boredom = blobby1.inspect_boredom()
    dirtiness = blobby1.inspect_dirtiness()
    sleepiness = blobby1.inspect_sleepiness()


    health_problems = max(0, min(hunger + boredom + dirtiness + sleepiness, 400))

    if health_problems <= 40:
        blobby_image = 'static/very_happy.png'
    elif 40 < health_problems <= 160:
        blobby_image = 'static/happy.png'
    elif 160 < health_problems <= 240:
        blobby_image = 'static/neutral.png'
    elif 240 < health_problems <= 320:
        blobby_image = 'static/sad.png'
    elif 320 < health_problems <= 400:
        blobby_image = 'static/very_sad.png'


    if dirtiness:
        blobby_image = bgraphics.add_poop(dirtiness//10, blobby_image)



    html = flask.render_template('blobby.html',
                                 hunger=inspecting[0],
                                 boredom=inspecting[1],
                                 dirtiness=inspecting[2],
                                 sleepiness=inspecting[3],
                                 blobby_image=blobby_image)
    return html

@app.route('/feed')
def feed():
    blobby1 = blobby.load()
    blobby1.feed()
    url_for_inspect = flask.url_for('inspect')
    redirect = flask.redirect(url_for_inspect)
    return redirect


@app.route('/play')
def play():
    blobby1 = blobby.load()
    blobby1.play()
    url_for_inspect = flask.url_for('inspect')
    redirect = flask.redirect(url_for_inspect)
    return redirect

@app.route('/clean')
def clean():
    blobby1 = blobby.load()
    blobby1.clean()
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





if __name__ == '__main__':
    app.run(debug=True)