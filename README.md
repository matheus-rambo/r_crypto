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

# Getting Starded
Please, read this [wiki](https://github.com/matheus-rambo/r_crypto/wiki/Getting-Started).

# Release notes
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
 - [*v1.5.1*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.5.1) **Stable version** [*Docker Tag*](https://hub.docker.com/layers/matheusrambo/r_crypto/v1.5/images/sha256-01d205e2f17a6fe8e19f5b7f4baed5fb00cd0ef8d6fcade94bc21d89f761e959)
 - [*v1.5*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.5)
 - [*v1.4.1*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.4.1) [*Docker Tag*](https://hub.docker.com/layers/matheusrambo/r_crypto/v1.4/images/sha256-1492892d04b139fea9455edb95e67b66164c80accb343b3b18c4909b2d3abf61)
 - [*v1.4*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.4)
 - [*v1.4-steganography*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.4-steganography)
 - [*v1.3*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.3) [*Docker Tag*](https://hub.docker.com/layers/matheusrambo/r_crypto/v1.3/images/sha256-d8f8b8feeb001dfe4491befeb62cdb659afbdfa1b3ff23c1f3fae41f243fef60)
 - [*v1.3-beta*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.3-beta)
 - [*v1.2.2*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.2.2) [*Docker Tag*](https://hub.docker.com/layers/matheusrambo/r_crypto/v1.2/images/sha256-16e95224bd39359fba72c38209a1f9a7ec1cf2ae173936d868961d39d1261e75)
 - [*v1.2.1*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.2.1)
 - [*v1.1*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.1) [*Docker Tag*](https://hub.docker.com/layers/matheusrambo/r_crypto/v1.1/images/sha256-f898469acc6b5f2f418d2dc4cea365eb929292ca44c2188593b39745d4fab120) 
 - [*v1.0*](https://github.com/matheus-rambo/r_crypto/releases/tag/v1.0) [*Docker Tag*](https://hub.docker.com/layers/matheusrambo/r_crypto/v1.0/images/sha256-c0421b81bd580a8ea54e60ff0f2d7a5dc7ca45ef095cfa35a61736906a0a9085)

# Docs
 - ***Version 1.0***: [v1.0](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v1.0)
 - ***Version 1.1***: [v1.1](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v1.1)
 - ***Version 1.2***: [v1.2](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v1.2)
 - ***Version 1.3***: [v1.3](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v1.3)
 - ***Version 1.4***: [v1.4](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v1.4)
 - ***Version 1.5***: [v1.5](https://github.com/matheus-rambo/r_crypto/wiki/Documentation-r_crypto-release-v1.5)


# Author

- **Matheus Rambo**
  - [*GitHub*](https://github.com/matheus-rambo)
  - *e-mail* matheusrambo@protonmail.ch
