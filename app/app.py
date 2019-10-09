from flask import Flask, request, jsonify
from google_sheet import addSong
import pprint

app = Flask(__name__)

@app.route('/suggest-song', methods=['POST'])
def handle_song():
    artist = request.form['artist']
    song = request.form['song']

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