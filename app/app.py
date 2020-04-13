from flask import Flask, request, jsonify, escape, render_template
from google_sheet import addSong
from mail import Mail
import pprint
import os
from dotenv import load_dotenv
import logging
from helpers import clean_empty

app = Flask(__name__)


@app.route('/')
def greeting():
    return 'Hello from the other side!'


@app.route('/send-mail', methods=['POST'])
def send_mail():

    logging.basicConfig(level=logging.DEBUG, filename='debug.log')
    data = request.json

    # remove all empty values
    clean_data = clean_empty(data)
    # add sender email
    clean_data.update({'sender_email': os.getenv("GMAIL_ACCOUNT")})

    # send rsvp
    rsvp = Mail([os.getenv("RSVP_MAIL")], '[Foreverstories] Neue Nachricht von ' + clean_data['name'])
    rsvp.body = render_template('personal-message.txt', data=clean_data)
    logging.debug('rendered template: %s', rsvp.body)
    rsvp.reply_to = clean_data['email']
    assert(rsvp.send()), 'Could not send RSVP Mail'

<<<<<<< HEAD
#    if('hotel' in clean_data):
#        # send hotel reservation
#        hotel_booking = Mail([os.getenv("HOTEL_MAIL")], 'Hochzeit 01.05.2020 Nadine Scheitz und Matthias Frank')
#        hotel_booking.body = render_template('hotel-booking.txt', data=clean_data)
#        hotel_booking.cc = [clean_data['guest']['1']['mail']]
#        hotel_booking.reply_to = clean_data['guest']['1']['mail']
#        assert(hotel_booking.send()), 'Could not send Hotel reservation Mail'
=======
    if('hotel' in clean_data):
        # send hotel reservation
        hotel_booking = Mail([os.getenv("HOTEL_MAIL")], 'Hochzeit 01.05.2020 Nadine Scheitz und Matthias Frank')
        hotel_booking.body = render_template('hotel-booking.txt', data=clean_data)
        hotel_booking.cc = [clean_data['guest']['1']['mail']]
        hotel_booking.reply_to = [clean_data['guest']['1']['mail'], os.getenv("GMAIL_ACCOUNT")]
        assert(hotel_booking.send()), 'Could not send Hotel reservation Mail'
>>>>>>> f91105543dd6352711e6bb42e24262461ed550e1

    return jsonify('Email sent!')


@app.route('/suggest-song', methods=['POST'])
def handle_song():
    artist = escape(request.form['artist'])
    song = escape(request.form['song'])

    if(artist != "" and song != ""):
        addSong([artist, song])
        return jsonify('succ')
    else:
        return 'Provide artist and song', 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
