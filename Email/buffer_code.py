import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
sys.path.append('../Database/')
from dbSQL import *
from send_emails import *

def send_Emails(id_customer, subject, id_body, file, n_jobs, id_sector, id_subcategory=None):
    job_list = get_jobs(id_customer, n_jobs, id_sector, id_subcategory)
    c = 0
    print("Emails will be be sent: ")
    for j in job_list:
        print(j[3])
        t = send_Email(id_customer, subject, id_body, file, j[3], j[0],j[2], j[4])
        c+=t
    print(c,"emails sent")
send_Emails(1,'Test of py function', 1, 0, 3, 5)
