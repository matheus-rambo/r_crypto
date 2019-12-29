from ssl import create_default_context
from smtplib import SMTP
from json import loads
from .app_util import read_file_content
from .classes import EmailInfo, SMTPServer

import email
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


default_mail_config_path = './config/mail-config.json'



def request_email_information():
    from getpass import getpass
    smtp_server = input('SMTP server: ')
    port        = input('SMTP port: ')
    email       = input('Your e-mail: ')
    password    = getpass('Your password: ')
    e_mail_info = EmailInfo(email, password, SMTPServer(smtp_server, port))
    return e_mail_info


def send_message_mail(receiver:[], body:str, filename:str, subject: str = None):
    print("\n\tInit send e-mail to {}".format(receiver))
    
    smtp = email_info = subject = send_as_file = None    

    if input('Read mail configuration file from default path: {} ? [Yes, No]:  '.format(default_mail_config_path)).lower()[0] == 'y':
        
        config       = read_file_content(file_name = default_mail_config_path , buffer_size = 2048)
        json_body    = loads(config)
        smtp_object  = json_body['smtp']
        email_config = json_body['mail_config']
        
        smtp_server  = smtp_object['server']
        smtp_port    = smtp_object['port']
        e_mail       = email_config['e-mail']
        password     = email_config['password']

        smtp         = SMTPServer(smtp_server, smtp_port)
        email_info   = EmailInfo(e_mail, password, smtp)
        subject      = json_body['subject'] if subject is None  else subject
        send_as_file = json_body['send_as_file']
    
    else:
        email_info   = request_email_information()
        smtp         = email_info.smtp
        subject      = 'r_crypto message' if subject is None else subject
        send_as_file = input('Do you want to send the content as a file? [Yes, No] ').lower()[0] == 'y'


    print("""
            \n\tSMTP configuration: SERVER: {}, PORT: {}
         """.format(
                    smtp.server, 
                    smtp.port
                    )
        )

    mail = MIMEMultipart()
    mail['From']    = email_info.e_mail
    mail['To']      = receiver  
    mail['Subject'] = subject

    print("""\tFrom e-mail: {}
            \n\tTo: {}
            \n\tSubject: {}
            \n\tThe e-mail will be sent as a: {}
        """.format(
                   email_info.e_mail,
                   receiver,
                   subject, 
                   'text file' if send_as_file else 'text'
                   )
        )


    if send_as_file:
        part = MIMEBase("text", "plain")
        part.set_payload(body.encode('utf-8'))
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {filename}")
        mail.attach(part)
    else:
        mail.attach(MIMEText(body, "plain"))

    message = mail.as_string()

    with SMTP(smtp.server, smtp.port) as server:
        server.starttls(context = create_default_context())
        server.login(email_info.e_mail, email_info.password)
        server.sendmail(email_info.e_mail, receiver, message)
        print("\n\tE-mail was sent to {}\n".format(receiver))
        server.close()


