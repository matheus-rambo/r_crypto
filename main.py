import r_crypto as r_crypto
import r_file as r_file
import sys

if(len(sys.argv) >= 4):
    filename = sys.argv[1]
    option = sys.argv[2]
    save_to_file = sys.argv[3]
    file = r_file.open_file(filename)
    content = r_file.read_file_lines(file)
    ciphed = ""
    if(option == "--encrypt" or option == "--e"):
        fernet = r_crypto.generate_custom_key(input("Insert you key password: "))
        ciphed = r_crypto.encrypt(fernet, content)
    elif (option == "--decrypt" or option == "--d") :
        fernet = r_crypto.generate_key(input("Insert you key password: "), input("Insert the salt key: "))
        ciphed = r_crypto.decrypt(fernet, content)
    else:
        print("Invalid cryptography option!\nYou should use --encrypt, --e or --decrypt, --d.")
        sys.exit(1)
        
    if(save_to_file == "--yes" or save_to_file == "--y"):
         file_writter = input("Insert the name of the file: ")
         r_file.write_to_file(ciphed, file_writter)
    elif (save_to_file == "--no" or save_to_file == "--n"):
        print("\nYour data decrypted is:\n{}".format(ciphed.decode("utf-8")))
    else:
        print("Invalid save option!\nYou should use --yes, --y or --no, --n.")

    print("\nSuccesfull\n")
else:
    print("You shoud use command line arguments!\nHint: <filename> --<crypt-option> --<save-option>")