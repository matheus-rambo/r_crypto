# Configuration to send e-mails
Follow this file to be able to use a configured file to send e-mails with your content.

## Example

Json exemple of a configuration:

{

    "smtp": {
        "server": "smtp.gmail.com",
        "port": 587
    },
    "mail_config":{
        "e-mail": "rcrypto@gmail.com",
        "password": "mypassword"
    },
    "subject": "r_crypto message",
    "send_as_file": true
}

## SMTP configuration
 - *Server*: The **smtp** server that you are using.
   - *Google* smtp server is: ``smtp.gmail.com``.
   - *Amazon* smtp server is: ``todo``.

The *server* property is a string.


- *Port*: There are 5 default port for smtp protocol. But you cant use others ports too(*Not recommended*).
   - Unencrypted: 25, 587, 2525
   - SSL: 465, 25025

The *port* property is a number.

## e-mail configuration
 - *e-mail*: Your e-mail. Ex: ``matheus.rambo@gmail.com``
 - *password*: Your password. Obs: If your e-mail account has 2FA, consider using an app password.

The *e_mail* and *password* are strings.

## Other
 - *Subject*: Default subject when no one is defined when sending e-mails.
 - *Send as file*: If you want to send the content of the e-mail as a file, otherwise, the content will be sent as plain text.

The *subject* is a string and *send_as_file* is a boolean.

