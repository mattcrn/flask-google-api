import smtplib
import os
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

class Mail:
    to = []
    subject = ''
    body = ''
    reply_to = []
    cc = []

    def __init__(self, to, subject):
        self.to = to
        self.subject = subject

    def get_plain(self):
        plain= re.compile('<.*?>')
        return re.sub(plain, '', self.body)

    def send(self):
        load_dotenv()
        gmail_user = os.getenv("GMAIL_ACCOUNT")
        gmail_password = os.getenv("GMAIL_PASSWORD")
        sent_from = 'Nadine & Matthias <' + gmail_user + '>'

        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = sent_from
        message["To"] = ', '.join(self.to)
        if(self.cc != ''):
            message["CC"] = ', '.join(self.cc)
        html = MIMEText(self.body, 'html')
        plain = MIMEText(self.get_plain(), 'plain')

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(html)
        message.attach(plain)

        if len(self.reply_to) :
                message.add_header('reply-to', self.reply_to)
                

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, self.to+self.cc, message.as_string())
            server.close()

            return True
        except:
            return False