import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

gmail_user = os.getenv("GMAIL_ACCOUNT")
gmail_password = os.getenv("GMAIL_PASSWORD")

sent_from = 'Nadine & Matthias <'+ gmail_user + '>'
to = [os.getenv("TEST_MAIL")]
subject = 'OMG Super Important Message'
body = 'Hey, whats up?\n\n- Nadine & Matthias'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')