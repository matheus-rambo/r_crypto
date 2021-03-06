# A simple *Cryptography* terminal tool.

![eagle](https://user-images.githubusercontent.com/33197461/69020567-b03f4380-0993-11ea-8aca-92d965de279b.png)

***Note*** This project uses *symmetric cryptography*, and uses *SHA-256* to generate the Fernet key. [Fernet Documentation](https://cryptography.io/en/latest/fernet/)

# Undestanding Cryptography

 If you want to know more about Symmetric Cryptography, there is a good link of python implementation of **symmetric**: [Symmetric Cryptography](https://docs.python-guide.org/scenarios/crypto/), and this is a link for basic understanding of **symmetric** and **asymmetric** ***encryption/decryption***: [Symmetric vs Asymmetric](https://www.ssl2buy.com/wiki/symmetric-vs-asymmetric-encryption-what-are-differences)
 

# Projects that helped and are helping me to build this:
- Cryptography module: https://github.com/pyca/cryptography

# Getting Starded
Please, read this [wiki](https://github.com/matheus-rambo/r_crypto/wiki/Getting-Started).

# Release notes

- ***Version 4.2***
   - *Implemented*: https://github.com/matheus-rambo/r_crypto/issues/57
   - *Implemented*: https://github.com/matheus-rambo/r_crypto/issues/71 

- ***Version 4.1 ( June 7, 2020 )***
   - *Implemented*: https://github.com/matheus-rambo/r_crypto/issues/64
   - *Implemented*: https://github.com/matheus-rambo/r_crypto/issues/55

- ***Version 4.0.1 ( May 24, 2020 )***
   - *Fixed*: https://github.com/matheus-rambo/r_crypto/issues/60
   
- ***Version 4.0***
   - Refactored to a more readable code. 
   - The Steganography module was removed(It might will be back in future releases).
   - The e-mail feature was removed(But it will be back in future releases).
   - The file r_cryptography was renamed to r_crypto.
   - The optional parameters were renamed, and some were deleted.
   - The user can not choose the name of a encrypted file(will use *.enc* extension), and a keys file(will use *.keys* extension).

- ***Version 3.2***
   - *Enhancement*: https://github.com/matheus-rambo/r_crypto/issues/5. Now, we can encrypt/decrypt directories.

- ***Version 3.1.1***
   - *Fixed*: https://github.com/matheus-rambo/r_crypto/issues/52. Not showing decrypted content.

- ***Version 3.1***
   - Now, we add metadata inside an encrypted content( it can be a file, text, image whatever), and when the content is decrypted we show the metadata to the user.
   - *Enhancement*: https://github.com/matheus-rambo/r_crypto/issues/43. When a file is encrypted, we store its extension, so when it is decrypted, we may(if the user wants to) save the file with its original extension back.
   - *Enhancement*: https://github.com/matheus-rambo/r_crypto/issues/42. Storing metadata inside the content.
   - Removed rkeys extension for file with keys to decrypt. 
   - Removed rencrypted extension when a file is encrypted.
   
- ***Version 3.0.2***
   - *Fixed*: https://github.com/matheus-rambo/r_crypto/issues/51. Error when running r_steganography.

- ***Version 3.0.1***
   - *Fixed*: https://github.com/matheus-rambo/r_crypto/issues/47. Was not possible to send e-mails with the 3.0 version.
   - We encode the *bytes* with **base64** before send the e-mail. So, before decrypt it, you will need to decode the **base64** to get the *bytes*.

- ***Version 3.0***
   - *Fixed*: https://github.com/matheus-rambo/r_crypto/issues/20
   - What was encryted with a version lower than *3*, can not be decrypted with this version.
   - Optional argument ``buffer-size`` on steganography and cryptography was renamed to ``chunk-size``.   
   - Now, files are written and read in binary format, with this, we can encrypt images too. 
   - We can encrypt images, videos and much more. At lower versions, we could only encrypt text files, now we can do anything.

- ***Version 2.1.1***
   - *Fixed*: https://github.com/matheus-rambo/r_crypto/issues/41
    
- ***Version 2.1***
    - *Enhancement*: https://github.com/matheus-rambo/r_crypto/issues/2. Now, the user can send e-mails with his content.
    - Mail.py file to help with the send of e-mails.
    - A config file to user configure the e-mail account, and smtp.    
    - *r_cryptography.py* now has an option to send the *encrypted*/*decrypted* and the *keys* over an e-mail. And allows multiple receivers too.
    - Sending unique e-mail to destinantions list, so then can not see who else received the same e-mail.
    - User can decide if he wants to send the decryption keys, and may send the keys to other e-mail.

- ***Version 2.0***
   - Update how secret key is generate. Now, we use the ***secrets*** module. We are not using anymore the secret key as a hexadecimal string.

- ***Version 1.5.1*** 
   - *Fixed*: https://github.com/matheus-rambo/r_crypto/issues/31

- ***Version 1.5***
   - Implemented argparse.
   - Refactor of files, that were too hard to maintain and read.
   - Deleted 6 files. They are: encrypt-file, encrypt-text, decrypt-file, decrypt-text, behind-image and reveal-image.
   - Loading keys from a file. 
   - Created 2 files. r_cryptography and r_steganography.
   - *Saving keys as a json file*. **Enhancement**: https://github.com/matheus-rambo/r_crypto/issues/30
   - Refactor of *main-app* file.

- ***Version 1.4.1***
   - Implemented standalone file that can do almost every operation of *r_crypt*.

- ***Version 1.4***
   - Implemented support for *Steganography*, at this moment we can hide a text or file text inside an image.
   - We can hide and reveal a message inside an image.
   - *Enhancement*: https://github.com/matheus-rambo/r_crypto/issues/24
   - User can not choose the name of the files anymore when encrypt/decrypt a file.    
   - *Fixed security issue when allowing user to pass his keys as command line arguments*.

 - ***Version 1.3***
    - *Enhancement*: https://github.com/matheus-rambo/r_crypto/issues/8
    - *Enhancement*: https://github.com/matheus-rambo/r_crypto/issues/14
    - The file r_encrypt-text.py was renamed to encrypt-text.py.
    - The file r_encrypt-file.py was renamed to encrypt-file.py.
    - The file r_decrypt-text.py was renamed to decrypt-text.py.
    - The file r_decrypt-file.py was renamed to decrypt-file.py.
    - The files r_file.py, r_crypto.py and RCrypto.py were moved to source folder.
    - Custom messages when user is using wrong keys to decrypt conntent.
    - Dockerfile to build images ( Images can be created with *release tags* and the *master* branch ).
    
 - ***Version 1.2.2***
    - *Fixed*: https://github.com/matheus-rambo/r_crypto/issues/13

 - ***Version 1.2.1***
     - *Fixed*: https://github.com/matheus-rambo/r_crypto/issues/11
     - *Fixed*: https://github.com/matheus-rambo/r_crypto/issues/10
     - *Fixed*: https://github.com/matheus-rambo/r_crypto/issues/9

 - ***Version 1.2***
    - main.py and InvalidFileExtensionException.py were deleted.
    - Saving information of encryption on file. The user that encrypted, data and the original extension of the file before encryption and more.
    - When a file is decrypted, it backs to its original file extension.
    - Removed the *.rdecrypted* extension from files that were decrypted by rcrypt.
    - *Fixed*: https://github.com/matheus-rambo/r_crypto/issues/4

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
 - [*v4.2*](https://github.com/matheus-rambo/r_crypto/releases/tag/v4.2) **Stable Version**
 - [*v4.1*](https://github.com/matheus-rambo/r_crypto/releases/tag/v4.1)
 - [*v4.0*](https://github.com/matheus-rambo/r_crypto/releases/tag/v4.0)
 - [*v3.2*](https://github.com/matheus-rambo/r_crypto/releases/tag/v3.2)
 - [*v3.1.1*](https://github.com/matheus-rambo/r_crypto/releases/tag/v3.1.1)
 - [*v3.1*](https://github.com/matheus-rambo/r_crypto/releases/tag/v3.1)
 - [*v3.0.2*](https://github.com/matheus-rambo/r_crypto/releases/tag/v3.0.2)
 - [*v3.0.1*](https://github.com/matheus-rambo/r_crypto/releases/tag/v3.0.1)
 - [*v3.0*](https://github.com/matheus-rambo/r_crypto/releases/tag/v3.0)
 - [*v2.1.1*](https://github.com/matheus-rambo/r_crypto/releases/tag/v2.1.1)   
 - [*v2.1*](https://github.com/matheus-rambo/r_crypto/releases/tag/v2.1)   
 - [*v2.0*](https://github.com/matheus-rambo/r_crypto/releases/tag/v2.0)  
 - [*v1.5.1*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.5.1) 
 - [*v1.5*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.5)
 - [*v1.4.1*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.4.1) 
 - [*v1.4*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.4)
 - [*v1.4-steganography*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.4-steganography)
 - [*v1.3*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.3)
 - [*v1.3-beta*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.3-beta)
 - [*v1.2.2*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.2.2)
 - [*v1.2.1*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.2.1)
 - [*v1.1*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.1) 
 - [*v1.0*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.0)

# Docs
 - ***Version 4.2***: [v4.2](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v4.2)
 - ***Version 4.1***: [v4.1](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v4.1)
 - ***Version 4.0***: [v4.0](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v4.0)
 - ***Version 3.2***: [v3.2](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v3.2)
 - ***Version 3.1***: [v3.1](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v3.1)
 - ***Version 3.0***: [v3.0](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v3.0)
 - ***Version 2.1***: [v2.1](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v2.1)
 - ***Version 2.0***: [v2.0](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v2.0)
 - ***Version 1.5***: [v1.5](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v1.5)
 - ***Version 1.4***: [v1.4](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v1.4)
 - ***Version 1.3***: [v1.3](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v1.3)
 - ***Version 1.2***: [v1.2](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v1.2)
 - ***Version 1.1***: [v1.1](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v1.1)
 - ***Version 1.0***: [v1.0](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v1.0)

# Authors

- **Matheus Rambo**
  - [*GitHub*](https://github.com/matheus-rambo)
  - *e-mail* matheusrambo@protonmail.ch
  
- **Arthur Bottcher**
  - [*GitHub*](https://github.com/ArthurBottcher)
  - *e-mail* arthurbottcher@gmail.com
