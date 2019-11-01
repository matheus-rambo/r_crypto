## A simple terminal tool to encrypt/decrypt files/text in a terminal console.

***Note*** This project uses *symmetric cryptography*.

**Make sure that you have Python >= 3.7 and pip installed!**

### Undestanding Cryptography

 If you want to know more about Symmetric Cryptography, there is a good link of python implementation of **symmetric**: [Symmetric Cryptography](https://docs.python-guide.org/scenarios/crypto/), and this is a link for basic understanding of **symmetric** and **asymmetric** ***encryption/decryption***: [Symmetric vs Asymmetric](https://www.ssl2buy.com/wiki/symmetric-vs-asymmetric-encryption-what-are-differences)
 
# Installing r_crypto
``git clone https://github.com/punishercoder/r_crypto.git``

``cd r_crypto``

``pip install -r requirements.txt``


# Version 1.0
 - Encrypt and Decrypt files.
 - Save files encrypted and decrypted.

# Version 1.1
 - Setting extension for encrypted files.
 - Setting extension for decrypted files.
 - Script to read data from file and encrypt it.
 - Script to read data from console and encrypt it.
 - Script to read encrypted data from file and decrypt it.
 - Script to read encrypted data from console and decrypt it.
 
 # Version 1.2
 - main.py and InvalidFileExtensionException.py were deleted.
 - Saving information of encryption on file. The user that encrypted, data and the original extension of the file before encryption and more.
  - When a file is decrypted, it backs to its original file extension.
  - Removed *.rdecrypted* from files that were decrypted by rcrypt.
 
# Usage of r_crypto

#### Encrypt
 
**Attention!** You must store the **key** that you choosed, and the ***Secret Key*** that was generated in a ***safe place***, if you lost some of these keys, you will not be able to decrypt anymore!
  
*If you want to encrypt a file, use:* 

``python r_encrypt-file.py <your-file-name> <your-key>``

``python r_encrypt-file.py <your-file-name>`` *This will ask you to input the key name.*

``python r_encrypt-file.py`` *This will ask you to input the file and the key.*

*If you want to encrypt a text from terminal, use:*

``python r_encrypt-text.py <your-text> <your-key>``

``python r_encrypt-text.py <your-text>`` *This will ask you to input the key name.*

``python r_encrypt-text.py`` *This will ask you to input the text and the key.*


### Decrypt
   
***Note*** If the **key** or the **secret key** is not identical, the *decrypt* operation will ***fail***!

*If you want to decrypt a file, use:*

``python r_decrypt-file.py <your-file-name>.rencrypted <your-key> <your-secret-key>``

``python r_decrypt-file.py <your-file-name>.rencrypted <your-key>`` *This will ask you to input the secret key.*

``python r_decrypt-file.py <your-file-name>.rencrypted`` *This will ask you to input the key and the secret key.*

``python r_decrypt-file.py`` *This will ask you to input the file, key and the secret key.*

 *If you want to decrypt a text from terminal, use:*

``python r_decrypt-text.py <your-text> <your-key> <your-secret-key>``

``python r_decrypt-text.py <your-text> <your-key>`` *This will ask you to input the secret key.*

``python r_decrypt-text.py <your-text>`` *This will ask you to input the key and the secret key.*

``python r_decrypt-text.py`` *This will ask you to input the text, key and the secret key.*

# Author

**Matheus Rambo** (*punishercoder*)

