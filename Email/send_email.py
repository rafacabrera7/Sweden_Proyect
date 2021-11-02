import os
import smtplib
import imghdr
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Testing Email Sender'
msg['From'] = 'rafaelcabrerajimenez7@gmail.com'
msg['To'] = 'rafaelcabrerajimenez7@hotmail.com'
msg.set_content('This is a text')


with open('CV_Rafael_Cabrera_Jimenez.pdf', 'rb') as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('email-smtp.us-east-2.amazonaws.com', 587) as smtp:
    smtp.login('rafaelcabrerajimenez7@gmail.com', 'cabrera05')
    smtp.send_message(msg)
