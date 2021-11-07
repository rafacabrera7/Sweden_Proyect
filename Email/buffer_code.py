import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
sys.path.append('../Database/')
from dbSQL import *

def send_Emails(id_customer, subject, id_body, file, id_sector, id_subcategory):
    

# send_Email(1,'Test of py function', 1, 0, 'rafael.enriquec@hotmail.com')
