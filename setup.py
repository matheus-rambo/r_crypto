LINUX   = "linux"
WINDOWS = "windows"

from os import popen
 
def detect_sisop() -> str:

    print("Detecting user operation system ...")
    from platform import system
    sis_op = system().lower()

    if sis_op == WINDOWS:
        print("Windows machine detected!") 
    elif sis_op == LINUX:
        print("Linux machine detected")

    return sis_op

def apply_variables(sisop: str) -> str :
    variable         = "rcrypto"
    if sisop == LINUX:
        # echo -n does not put a new line after the string.
        # So, it is very useful for us now
        directory_path   = popen("echo -n $HOME").read()
        r_crypto_path    = popen("echo -n $(pwd)").read()
        filename = "{}/.bash_aliases".format(directory_path)  
        command       = "\"python {}/r_crypto.py\"".format(r_crypto_path)
        alias_command = "alias {variable}={command} \n".format(variable=variable, command=command) 
        with open(file=filename, mode='wt') as file:
            file.write(alias_command)
    else:
        print("Not supported yet!")

def main():
    print("Running initial setup for r_crypto installation!")  
    sisop = detect_sisop()
    apply_variables(sisop)
    

if __name__ == "__main__":
    main()
    print("Configuration done!")
