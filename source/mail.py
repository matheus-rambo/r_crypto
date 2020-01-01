from ssl import create_default_context
from smtplib import SMTP
from json import loads
from .app_util import read_file_content, read_ask_answear

import email
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


default_mail_config_path = './config/mail-config.json'

class Mail():

    # constructor
    def __init__(self):
        self.email_info       = None
        self.smtp             = None
        self.send_as_file     = None

    
    # destructor
    def __del__(self):
        del self.smtp
        del self.email_info


    def send_email(self, destination:str, body:str, filename:str, subject: str):       

        # when send 2 emails, we only need to load the e-mail info for the first e-mail, at 
        # the second, we can reuse the same info
        if self.email_info is None or self.smtp is None:
            
            if read_ask_answear('Read mail configuration file from default path: {} ? [Yes, No]:  '.format(default_mail_config_path), True):
                self.read_from_config_file(default_mail_config_path)
            elif read_ask_answear('Do you want to use your own mail config file? [Yes, No]: ', True):    
                self.read_from_config_file(input('Mail configuration file path: '))
            else:
                self.request_email_information()
                self.send_as_file = read_ask_answear('Do you want to send the content as a file? [Yes, No]: ', True)
        else:
            print("\n\tUsing stored e-mail info . . . ")


        print("""
                \n\tSMTP configuration: SERVER: {}, PORT: {}
            """.format(
                        self.smtp.server, 
                        self.smtp.port
                        )
            )

        mail = MIMEMultipart()
        mail['From']    = self.email_info.e_mail
        mail['Subject'] = subject

        print("""\tFrom e-mail: {}
                \tTo: {}
                \tSubject: {}
                \tThe e-mail will be sent as a: {}
            """.format(
                    self.email_info.e_mail,
                    destination,
                    subject, 
                    'text file' if self.send_as_file else 'text'
                    )
            )

        if self.send_as_file:
            part = MIMEBase("text", "plain")
            part.set_payload(body.encode('utf-8'))
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {filename}")
            mail.attach(part)
        else:
            mail.attach(MIMEText(body, "plain"))


        with SMTP(self.smtp.server, self.smtp.port) as server:
            server.starttls(context = create_default_context())
            server.login(self.email_info.e_mail, self.email_info.password)

            for receiver in destination.split(','):
                # TODO
                # We can implement PGP later
                mail['To'] = receiver
                message    = mail.as_string()
                print('\n\tSending e-mail to: {}'.format(receiver))
                server.sendmail(self.email_info.e_mail, receiver, message)
                print('\n\tE-mail sent!')
            server.close()


    def send_email_with_images(self, destination:str, images:[], subject : str):
        if read_ask_answear('Read mail configuration file from default path: {} ? [Yes, No]:  '.format(default_mail_config_path), True):
            self.read_from_config_file(default_mail_config_path)
        elif read_ask_answear('Do you want to use your own mail config file? [Yes, No]: ', True):    
            self.read_from_config_file(input('Mail configuration file path: '))
        else:
            self.request_email_information()
        
        print("""
                \n\tSMTP configuration: SERVER: {}, PORT: {}
            """.format(
                        self.smtp.server, 
                        self.smtp.port
                        )
            )

        mail = MIMEMultipart()
        mail['From']    = self.email_info.e_mail
        mail['Subject'] = subject


        print("""\tFrom e-mail: {}
                \tTo: {}
                \tSubject: {}
               """.format(
                    self.email_info.e_mail,
                    destination,
                    subject
                    )
            )

        for image in images:
            # when sending an attachment as an image, we need to specify the type
            image_type = 'jpeg' if ( image[image.rindex('.'): len(image)] in ('jpeg', 'jpg')) else 'png'

            temp_name = image if '/' not in image else image[image.rindex('/'): len(image)]

            # Opening the image file and reading it's bytes
            part = MIMEBase("image", image_type)
            with open( file = image, mode = 'rb') as file:
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {temp_name}")
                mail.attach(part)


        with SMTP(self.smtp.server, self.smtp.port) as server:
            server.starttls(context = create_default_context())
            server.login(self.email_info.e_mail, self.email_info.password)

            for receiver in destination.split(','):
                mail['To'] = receiver
                message = mail.as_string()
                print('\n\tSending e-mail to: {}'.format(receiver))
                server.sendmail(self.email_info.e_mail, receiver, message)
                print('\n\tE-mail sent!')
            server.close()
            

    def read_from_config_file(self, config_file_path:str):
        config                 = read_file_content(file_name = config_file_path , buffer_size = 2048)
        json_body              = loads(config)
        smtp_object            = json_body['smtp']
        email_config           = json_body['mail_config']
                
        smtp_server            = smtp_object['server']
        smtp_port              = smtp_object['port']
        e_mail                 = email_config['e-mail']
        password               = email_config['password']

        self.smtp              = SMTPServer(smtp_server, smtp_port)
        self.email_info        = EmailInfo(e_mail, password)
        self.send_as_file      = json_body['send_as_file']


    def request_email_information(self):
        from getpass import getpass
        smtp_server      = input('SMTP server: ')
        port             = input('SMTP port: ')
        email            = input('Your e-mail: ')
        password         = getpass('Your password: ')
        self.smtp        = SMTPServer(smtp_server, port)
        self.email_info  = EmailInfo(email, password)


class SMTPServer():

    # constructor
    def __init__(self, server: str, port: int):
        self.server = server
        self.port   = port

    # destructor
    def __del__(self):
        pass


class EmailInfo():

    # constructor
    def __init__(self, e_mail: str, password: str ):
        self.e_mail   = e_mail
        self.password = password

    # destructor
    def __del__(self):
        pass