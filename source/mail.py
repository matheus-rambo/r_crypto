import ssl
from smtplib import SMTP

smtp_server = 'smtp.gmail.com'
port = 587
sender_email = ""
password = ""
receiver_email = ""
message = """\
    Subject: Teste envio de e-mail

    Ola."""
    
server = SMTP(smtp_server, port)
server.starttls(context = ssl.create_default_context())
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
