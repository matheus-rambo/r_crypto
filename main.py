import r_crypto as r_crypto
import r_file as r_file
import sys

if(len(sys.argv) >= 4):
    filename = sys.argv[1]
    option = sys.argv[2]
    saveToFile = sys.argv[3]
    file = r_file.openFile(filename)
    content = r_file.readFileLines(file)
    ciphed = ""
    if(option == "--encrypt" or option == "--e"):
        fernet = r_crypto.generateCustomKey(input("Insert you key password: "))
        ciphed = r_crypto.encrypt(fernet, content)
    elif (option == "--decrypt" or option == "--d") :
        fernet = r_crypto.generateKey(input("Insert you key password: "), input("Insert the salt key: "))
        ciphed = r_crypto.decrypt(fernet, content)
    else:
        print("Invalid cryptography option.\nYou should use --encrypt, --e or --decrypt, --d.")
        sys.exit(1)
        


    if(saveToFile == "--yes" or saveToFile == "--y"):
         file_writter = input("Insert the name of the file: ")
         r_file.writeToFile(ciphed, file_writter)
    elif (saveToFile == "--no" or saveToFile == "--n"):
        print(ciphed)
    else:
        print("Invalid save option!\nYou should use --yes, --y or --no, --n.")

    print("\nSuccesfull\n")



else:
    print("You shoud use command line arguments!\nHint: <filename> --<crypt-option> --<save-option>")


"""
password =  input("Your password: ")

fernet = r_crypto.generateCustomKey(password)

matehs = r_crypto.encrypt(fernet, "matheus, felipe rambo blume")
r_file.writeToFile(matehs, "txte.txt")
file = r_file.openFile("txte.txt")
con = r_file.readFileLines(file)
print(r_crypto.decrypt(fernet, con.encode()))"""




