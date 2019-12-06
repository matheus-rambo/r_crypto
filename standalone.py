#!/usr/bin/python3.7

# -*- coding: utf-8 -*-

import source.r_crypto as r_crypto
from cryptography.fernet import Fernet
from source.RCrypto import InvalidKeyException


class Standalone():
    def __init__(self):
        self.key = None
        self.secret_key = None
        self.fernet = None
        self.generate_default_keys()

    # Will generate the default keys to the user
    def generate_default_keys(self):
        print("Generating default keys . . . ")
        self.key = "K3RN31_p2n1C_matheus*%61"
        self.secret_key = r_crypto.generate_secret_key(self.key)
        self.fernet = r_crypto.generate_fernet_from_key_and_secret_key(self.key, self.secret_key)
        print("Done . . .\tDefault keys were generated!")

    # will encrypt and return
    def encrypt_message(self, message:str):
        return r_crypto.encrypt(self.fernet, message)

    # will decrypt and return
    def decrypt_message(self, message: str):
        return r_crypto.decrypt(self.fernet, message)

    # Will update the keys
    def update_keys(self):
        self.key = input("Insert your key: ")
        opt = input("Do you want to use a secret key already computed? Remeber, the secret key must be generated with the key! [Yes,No] ")
        
        if opt.lower() in ("yes", "y"):
             self.secret_key = input("Insert your secret key") 
        else:
            self.secret_key = r_crypto.generate_secret_key(self.key)

        self.fernet = r_crypto.generate_fernet_from_key_and_secret_key(self.key, self.secret_key)
        print("Keys were updated!")
    
    def show_keys(self):
        print("\nYour key is: {}".format(self.key))
        print("Your secret key is: {}\n".format(self.secret_key))
        print("Now, you can share this keys with your friends...")



def main():
    # Create the object to help us work with some defined methods
    standalone = Standalone()


    while True:
        print("\n1 - Encrypt messages")
        print("2 - Decrypt messages")
        print("3 - Update key and generate a new secret key")
        print("4 - Show my keys")
        print("5 - Exit\n")


        option = input("What do you want to do? ")
        if option == "1":
            print("Press Ctrl + C(Keyboard Interrupt) to stop encrypt")
            
            while True:
            
                try:
                    message = input("Type:\t")
                    print(standalone.encrypt_message(message).decode('utf-8'))

                # When user want to stop
                except KeyboardInterrupt:
                    print("Stop encryption...")
                    break

        elif option == "2":
            print("Press Ctrl + C(Keyboard Interrupt) to stop encrypt")
            
            while True:
            
                try:
                    message = input("Type:\t")
                    print(standalone.decrypt_message(message).decode('utf-8'))

                # When user want to stop
                except KeyboardInterrupt:
                    print("Stop decryption...")
                    break
                except InvalidKeyException:
                    print("\nYou are not using the correct keys!\tStopping decryption . . . ")
                    break

        elif option == "3":
            standalone.update_keys()
        
        elif option == "4":
            standalone.show_keys()

        elif option == "5":
            break
        else:
            print("Sorry, this option is not available.")

    print("Bye . . . \tHave a nice day!")

# calls the main method
if __name__ == '__main__':
    main()