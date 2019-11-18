# A simple *Cryptography/Steganography* terminal tool.

![eagle](https://user-images.githubusercontent.com/33197461/69020567-b03f4380-0993-11ea-8aca-92d965de279b.png)

***Note*** This project uses *symmetric cryptography*.

# Undestanding Cryptography

 If you want to know more about Symmetric Cryptography, there is a good link of python implementation of **symmetric**: [Symmetric Cryptography](https://docs.python-guide.org/scenarios/crypto/), and this is a link for basic understanding of **symmetric** and **asymmetric** ***encryption/decryption***: [Symmetric vs Asymmetric](https://www.ssl2buy.com/wiki/symmetric-vs-asymmetric-encryption-what-are-differences)
 
# Undestanding Steganography
https://www.techopedia.com/definition/4131/steganography


# Projects that helped and are helping me to build this:
- Cryptography module: https://github.com/pyca/cryptography

- Steganography module: https://github.com/cedricbonhomme/Stegano

 
# Installing r_crypto 

## Without Docker
**Make sure that you have Python >= 3.7 and pip3 installed!**

``git clone https://github.com/punishercoder/r_crypto.git``

``cd r_crypto``

``pip install -r requirements.txt``

## With Docker 
 - *Cloning the project*

``git clone https://github.com/punishercoder/r_crypto.git``

``cd r_crypto``

``docker build -t r_crypto:1.3 .``

``docker run -it -rm r_crypto:1.3``

 - Pulling docker image from docker hub

 ``docker pull rambosaiyan3/r_crypto``

 ``docker run -it r_crypto:latest``

# Release notes

- ***Version 1.4***
   - Implemented support for *Steganography*, at this moment we can hide and text or file text inside an image.
   - We can hide and reveal a message inside an image.
   - *Enhancement*: https://github.com/punishercoder/r_crypto/issues/24
   - User can not choose the name of the files anymore.    
   - *Fixed security issue when allowing user to pass his keys as command line arguments*.

 - ***Version 1.3***
    - *Enhancement*: https://github.com/punishercoder/r_crypto/issues/8
    - *Enhancement*: https://github.com/punishercoder/r_crypto/issues/14
    - The file r_encrypt-text.py was renamed to encrypt-text.py.
    - The file r_encrypt-file.py was renamed to encrypt-file.py.
    - The file r_decrypt-text.py was renamed to decrypt-text.py.
    - The file r_decrypt-file.py was renamed to decrypt-file.py.
    - The files r_file.py, r_crypto.py and RCrypto.py were moved to source folder.
    - Custom messages when user is using wrong keys to decrypt conntent.
    - Dockerfile to build images ( Images can be created with *release tags* and the *master* branch ).

    
 - ***Version 1.2.2***
    - *Fixed*: https://github.com/punishercoder/r_crypto/issues/13

 - ***Version 1.2.1***
     - *Fixed*: https://github.com/punishercoder/r_crypto/issues/11
     - *Fixed*: https://github.com/punishercoder/r_crypto/issues/10
     - *Fixed*: https://github.com/punishercoder/r_crypto/issues/9

 - ***Version 1.2***
    - main.py and InvalidFileExtensionException.py were deleted.
    - Saving information of encryption on file. The user that encrypted, data and the original extension of the file before encryption and more.
    - When a file is decrypted, it backs to its original file extension.
    - Removed the *.rdecrypted* extension from files that were decrypted by rcrypt.
    - *Fixed*: https://github.com/punishercoder/r_crypto/issues/4

 - ***Version 1.1***
    - Setting extension for encrypted files.
    - Setting extension for decrypted files.
    - Script to read data from file and encrypt it.
    - Script to read data from console and encrypt it.
    - Script to read encrypted data from file and decrypt it.
    - Script to read encrypted data from console and decrypt it.

- ***Version 1.0***
    - Encrypt and Decrypt files.
    - Save files encrypted and decrypted.

# Releases 
 - [*v1.4*](https://github.com/punishercoder/r_crypto/releases/tag/v1.4)
 - [*v1.4-steganography*](https://github.com/punishercoder/r_crypto/releases/tag/v1.4-steganography)
 - [*v1.3*](https://github.com/punishercoder/r_crypto/releases/tag/v1.3) **Stable version**
 - [*v1.2.2*](https://github.com/punishercoder/r_crypto/releases/tag/v1.2.2) 
 - [*v1.1*](https://github.com/punishercoder/r_crypto/releases/tag/v1.1) 
 - [*v1.0*](https://github.com/punishercoder/r_crypto/releases/tag/v1.0)

# Docs
 - ***Version 1.0***: [v1.0](https://github.com/punishercoder/r_crypto/wiki/Documentation-r_crypto-release-v1.0)
 - ***Version 1.1***: [v1.1](https://github.com/punishercoder/r_crypto/wiki/Documentation-r_crypto-release-v1.1)
 - ***Version 1.2***: [v1.2](https://github.com/punishercoder/r_crypto/wiki/Documentation-r_crypto-release-v1.2)
 - ***Version 1.3***: [v1.3](https://github.com/punishercoder/r_crypto/wiki/Documentation-r_crypto-release-v1.3)
 - ***Version 1.4***: [v1.4](https://github.com/punishercoder/r_crypto/wiki/Documentation-r_crypto-release-v1.4)


# Join us
 - [Slack](https://join.slack.com/t/ramboindustries/shared_invite/enQtODE5MjY0OTgyNzQwLTcyZTBhZTRmNzM2MThhOTAyODNlODg3NTkxNmU0NThjZjUzMDQwYzVkNWYyNDgwMWNmN2UzYTM0Mjk3YzBiNjg)


# Author

- **Matheus Rambo**
  - [*GitHub*](https://github.com/punishercoder)
  - *e-mail* matheusrambo@protonmail.ch
