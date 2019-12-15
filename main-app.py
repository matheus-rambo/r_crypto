from source.classes import Cryptor, Keys, InvalidKeyException

def generate_key(base_key : str = None):
    if base_key is None:
        base_key = 'rcryto_tool*(matheus)'
        import random
        size = len(base_key)
        key = ""
        for x in range(0, 15):
            key = key + base_key[random.randint(0, size - 1)] 
        return key
    return base_key


def main():
    print("Welcome . . .\n\tGenerating default keys . . .")
    key = generate_key()
    cryptor = Cryptor(key) 

    while True:
        print('\n1 - Encrypt messages.')
        print('\n2 - Decrypt messages.')
        print('\n3 - Update key and secret key.')
        print('\n4 - Show key and secret key.')
        print('\n5 - Exit.')

        option = input("\nWhat do you want to do? ")
        if option == "1":
            while True:
                try:
                    message = input("Insert you message: \t")
                    encrypted = cryptor.encrypt(message)
                    print('Your encrypted message:\t{}'.format(encrypted))

                except KeyboardInterrupt:
                    print('\nKeyboard interrupt. Stopping encryption . . .')
                    break
                

        elif option == "2":
            while True:
                try:
                    encrypted = input('Insert your encrypted message:\t')
                    message = cryptor.decrypt(encrypted)
                    print('Your message:\t{}'.format(message))
                except KeyboardInterrupt:
                    print('\nKeyboard interrupt. Stopping decryption . . .')
                    break
                except InvalidKeyException:
                    print("\nYou are not using the correct keys!\tStopping decryption . . . ")
                    break

        elif option == "3":
            key = input("Insert your key.\nTip: Leave it blank if you want to use a auto generated key:")
            key = generate_key() if key is None or key.strip() == "" else key
            secret_key = None
            if key is not None:
                secret_key = input("Insert your secret key.\nTip: Leave it blank if you want to use a auto generated key:")
                secret_key = None if secret_key is None or secret_key.strip() == "" else secret_key
            cryptor.update_keys(key, secret_key)
            print('\nKeys were updated!')

        elif option == "4":
            keys = cryptor.keys.get_keys()
            print(keys)

        elif option == "5":
            break

        else:
            print('\nInvalid option!')


if __name__ == "__main__":
    main()
    print('\n\tDone\n\t\tHave a nice day.')
    
