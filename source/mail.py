from ssl import create_default_context
from smtplib import SMTP
from json import loads
from .app_util import read_file_content

import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def send_message_mail(receiver:[], body:str, info:str, subject: str = None):
    print("\n\tInit send {} e-mail to {}".format(info, receiver))
    config = read_file_content(file_name = './config/mail-config.json', buffer_size = 2048)
    json_body = loads(config)

    smtp_object  = json_body['smtp']
    email_config = json_body['mail_config']
    smtp_server  = smtp_object['server']
    smtp_port    = smtp_object['port']
    subject      = json_body['subject'] if subject is None  else subject
    e_mail       = email_config['e-mail']

    print('\n\tSMTP configuration: SERVER: {}, PORT: {}'.format(smtp_server, smtp_port))
    print('\te-mail that is sending mail: {}\n'.format(e_mail))


    mail = MIMEMultipart()
    mail['From']    = e_mail
    mail['To']      = receiver  
    mail['Subject'] = subject
    
    mail.attach(MIMEText(body, "plain"))

    message = mail.as_string()

    with SMTP(smtp_server, smtp_port) as server:
        server.starttls(context = create_default_context())
        server.login(e_mail, email_config['password'])
        server.sendmail(e_mail, receiver, message)
        print("\n\tE-mail was sent to {}".format(receiver))
        server.close()


