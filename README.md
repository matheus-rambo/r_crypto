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
 
# What you can do

#### Encrypt

 **Encrypting** files:
 ``python main.py <your-file-name> --e --<save-option>``
 
 It will ask you to input your **own key**. Then, with your **key**, we will create the ***Secret key***. We will show you the *Secret Key that was generated*.
 
 **Attention!** You must store the **key** that you choosed, and the ***Secret Key*** that was generated in a ***safe place***, if you lost some of these keys, you will not be able to decrypt anymore!
 
 Save to a file: ``python main.py <your-file-name> --e --y``
 
 ***Note*** *This will ask you to define the filename for the file encrypted.*
 
 Print to console:``python main.py <your-file-name> --e --n``
 
*If you want to encrypt a file, use:* 

``python r_encrypt-file.py <your-file-name> <your-key>``

``python r_encrypt-file.py <your-file-name>`` *This will ask you to input the key name.*

``python r_encrypt-file.py`` *This will ask you to input the file and the key.*

*If you want to encrypt a text from terminal, use:*

``python r_encrypt-text.py <your-text> <your-key>``

``python r_encrypt-text.py <your-text>`` *This will ask you to input the key name.*

``python r_encrypt-text.py`` *This will ask you to input the text and the key.*


### Decrypt
 
  **Decrypting** files:
  ``python main.py <your-file-name>.rencrypted --d --<save-option>``
  
  It will prompt you to you input your key that you choosed when you encrypted, after, it will ask you to input the *Secret Key* that was generated*. 
  ***Note*** If the **key** or the **secret key** is not identical, the *decrypt* operation will ***fail***!

Save to a file: ``python main.py <your-file-name>.rencrypted --d --y``

***Note*** *This will ask you to define the filename for the file decrypted.*

Print to console:``python main.py <your-file-name>.rencrypted --d --n``
 
*If you want to decrypt a file, use:*

``python r_decrypt-file.py <your-file-name>.rdecrypt <your-key> <your-secret-key>``

``python r_decrypt-file.py <your-file-name>.rdecrypt <your-key>`` *This will ask tou to input the secret key.*

``python r_decrypt-file.py <your-file-name>.rdecrypt`` *This will ask tou to input the key and the secret key.*

``python r_decrypt-file.py`` *This will ask tou to input the file, key and the secret key.*

 *If you want to decrypt a text from terminal, use:*

``python r_decrypt-text.py <your-text> <your-key> <your-secret-key>``

``python r_decrypt-text.py <your-text> <your-key>`` *This will ask tou to input the secret key.*

``python r_decrypt-text.py <your-text>`` *This will ask tou to input the key and the secret key.*

``python r_decrypt-text.py`` *This will ask tou to input the text, key and the secret key.*

# Author

**Matheus Rambo** (*punishercoder*)

