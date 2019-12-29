from ssl import create_default_context
from smtplib import SMTP_SSL
from json import loads
from app_util import read_file_content


def send_mail(file_name: str, receiver:[], message:str):
    print("Init send e-mail to {}", receiver)
    config = read_file_content(file_name = '../config/mail-config.json', buffer_size = 2048)
    json_body = loads(config)

    smtp_oject = json_body['smtp']
    email_config = json_body['mail_config']

    # if user wants to send the email with the content as a file
    # TODO
    # send_as_file = json_body['send_as_file']

    with SMTP_SSL(smtp_oject['server'], smtp_oject['port'], context= create_default_context()) as server:
        server.login(email_config['e-mail'], email_config['password'])
        server.sendmail(email_config['e-mail'], '', message)



