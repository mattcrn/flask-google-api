from flask import Flask, request, jsonify, escape
from google_sheet import addSong
import pprint

app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Hello from the other side!'

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
