from ssl import create_default_context
from smtplib import SMTP
from json import loads
from app_util import read_file_content

config = read_file_content(file_name = '../config/mail-config.json', buffer_size = 2048)
smtp_oject = loads(config)['smtp']
email_config = loads(config)['mail_config']

message = """\
    Subject: Teste envio de e-mail 2

    Hello Friend"""
    
server = SMTP(smtp_oject['server'], smtp_oject['port'])
server.starttls(context = create_default_context())
server.login(email_config['e-mail'], email_config['password'])
server.sendmail(email_config['e-mail'], '', message)
