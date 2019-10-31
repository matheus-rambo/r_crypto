import r_crypto as r_crypto
import r_file as r_file
import sys

sys_args_length = len(sys.argv)

if( sys_args_length >= 4):
    filename = sys.argv[1]
    option = sys.argv[2]
    save_to_file = sys.argv[3]
    ciphed = ""
    isEncrypt = False

    
    if(option in ( "--encrypt", "--e" ) ):
        file = r_file.open_file(filename)
        content = r_file.read_file_lines(file)
        fernet = r_crypto.generate_custom_key(input("Insert you key password: "))
        ciphed = r_crypto.encrypt(fernet, content)
        print("Content encrypted!\n")
        isEncrypt = True

    elif (option in ( "--decrypt", "--d" ) ):

        file = r_file.open_rcrypted_file(filename)
        content = r_file.read_file_lines(file)
        fernet = r_crypto.generate_key(input("Insert you key password: "), input("Insert the Secret Key: "))
        ciphed = r_crypto.decrypt(fernet, content)
        print("Content decrypted!\n")
        isEncrypt = False
    else:
    
        print("Invalid cryptography option!\nYou should use --encrypt, --e or --decrypt, --d.")
        sys.exit(1)
        
    if(save_to_file in ( "--yes", "--y" ) ):
    
         file_writter = input("Insert the name of the file: ")
         r_file.write_to_file(ciphed, file_writter, isEncrypt)
    
    elif (save_to_file in ( "--no", "--n" ) ):
    
        print("\nYour data decrypted is:\n{}".format(ciphed.decode("utf-8")))
    
    else:
    
        print("Invalid save option!\nYou should use --yes, --y or --no, --n.")

    print("\nSuccesfull\n")
else:
    print("You shoud use command line arguments!\nHint: <filename> --<crypt-option> --<save-option>")