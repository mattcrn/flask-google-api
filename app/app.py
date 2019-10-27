from flask import Flask, request, jsonify, escape, render_template
from google_sheet import addSong
from mail import Mail
import pprint

app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Hello from the other side!'

@app.route('/send-mail')
def send_mail():

    data = {'name': 'Matthias', 'name1': 'Nadine', 'name2': 'Khaleesi'}

    rsvp = Mail(['another@mail.com'], data['name'] + ' hat zugesagt!')
    rsvp.body = render_template('rsvp.txt', data=data)
    rsvp.reply_to = 'some@mail.com'
    return rsvp.send()


@app.route('/suggest-song', methods=['POST'])
def handle_song():
    artist = escape(request.form['artist'])
    song = escape(request.form['song'])

    if(artist != "" and song != ""):
        addSong([artist, song])
        return 'succ'
    else: 
        return 'Provide artist and song', 400


    # try:
    #     addSong(['Bilderbuch', 'Bungalow'])

    # except OSError as e:
    #     print(e)
    # return 'Song added'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
