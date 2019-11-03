# A simple terminal tool to encrypt/decrypt files/text.

***Note*** This project uses *symmetric cryptography*.


# Undestanding Cryptography

 If you want to know more about Symmetric Cryptography, there is a good link of python implementation of **symmetric**: [Symmetric Cryptography](https://docs.python-guide.org/scenarios/crypto/), and this is a link for basic understanding of **symmetric** and **asymmetric** ***encryption/decryption***: [Symmetric vs Asymmetric](https://www.ssl2buy.com/wiki/symmetric-vs-asymmetric-encryption-what-are-differences)
 
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

 ***This is not available yet***.


# Release notes

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
 - [*v1.3*](https://github.com/punishercoder/r_crypto/releases/tag/v1.3) **Stable version**
 - [*v1.2.2*](https://github.com/punishercoder/r_crypto/releases/tag/v1.2.2) 
 - [*v1.1*](https://github.com/punishercoder/r_crypto/releases/tag/v1.1) 
 - [*v1.0*](https://github.com/punishercoder/r_crypto/releases/tag/v1.0)

# Docs
 - ***Version 1.0***: [v1.0](https://github.com/punishercoder/r_crypto/wiki/Documentation-r_crypto-release-v1.0)
 - ***Version 1.1***: [v1.1](https://github.com/punishercoder/r_crypto/wiki/Documentation-r_crypto-release-v1.1)
 - ***Version 1.2***: [v1.2](https://github.com/punishercoder/r_crypto/wiki/Documentation-r_crypto-release-v1.2)
 - ***Version 1.3***: [v1.3](https://github.com/punishercoder/r_crypto/wiki/Documentation-r_crypto-release-v1.3)


# Author

- **Matheus Rambo**
  - [GitHub](https://github.com/punishercoder)
  - [Protonmail](matheusrambo@protonmail.ch)
