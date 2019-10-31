## A symmetric Cryptography to encrypt/decrypt files/text.

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

# Version 1.1.
 - Setting extension for encrypted files.
 - Setting extension for decrypted files.

# What you can do

#### Encrypt

 **Encrypting** files:
 ``python main.py <your-file-name> --e --<save-option>``
 
 It will prompt a input to you use choose your **own key**.
 Then, it will generate the **salt key** used to create the ***Secret Key*** for encryption.
 **Attention** You must store the key that you choosed, and the salt key generate, if you lost some, you will not be able to decrypt anymore.
  
 Save to a file: ``python main.py <your-file-name> --e --y``
 
 ***Note*** *This will ask you to define the filename for the file encrypted.*
 
 Print to console:``python main.py <your-file-name> --e --n``
 
### Decrypt
 
  **Decrypting** files:
  ``python main.py <your-file-name>.rencrypted --d --<save-option>``
  
  It will prompt you to you input your key that you choosed when you encrypted, after, it will ask you to input the *Secret Key* that was generated*. 
  ***Note*** If the **key** or the **secret key** is not identical, the *decrypt* operation will ***fail***!

Save to a file: ``python main.py <file>.rencrypted --d --y``

***Note*** *This will ask you to define the filename for the file decrypted.*

Print to console:``python main.py <file>.rencrypted --d --n``
 
 
# Author

**Matheus Rambo** (*punishercoder*)

