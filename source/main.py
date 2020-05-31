#!/usr/bin/python

from source.content_type  import ContentType
from source.io_util       import IOUtil
from source.file          import File
from source.keys          import Keys
from source.message       import Message
from source.cryptor       import Cryptor
from source.app_constants import ENCRYPTED_EXTENSION, KEYS_EXTENSION
from source.style         import Formatter
    
class Main():

    def __init__(self, use:str, encryption:bool, save_content:bool, show_input:bool, 
            save_keys:bool, chunk_size:int, 
            read_keys_file:bool, charset:str, auto_generated_salt:bool):

        # Objects that will be used in the internally objects
        self._content_type = ContentType(use)
        self._encryption   = encryption
        self._save_content = save_content
        self._save_keys    = save_keys     
        self._chunk_size   = chunk_size
        self._charset      = charset
        self._read_keys    = read_keys_file

        # Objects that are used internally
        self._io        = IOUtil(show_input)
        self._formatter = Formatter()
        self._keys     = self._construct_keys(read_keys_file = read_keys_file, auto_generated_salt = auto_generated_salt)
        self._crypto    = None
        self._messages  = None

    def _construct_keys(self, read_keys_file:bool, auto_generated_salt:bool) -> Keys:

        self._io.stdout(self._formatter.yellow_foreground("\n\tStage 1 read user keys initiliazed ...\n"))

        # User passphrase
        secret_key = None

        # The salt that will be used to generate the Fernet Key
        salt       = None

        # The user wants to read the keys from a file
        if read_keys_file:
            formatted = self._formatter.green_foreground("Insert the name of yours keys file:\t")
            filename = self._io.stdin(formatted)
            file_object = File(filename, self._charset, self._chunk_size)   
            json_bytes = file_object.read_content_to_json()
            del file_object
            secret_key   = json_bytes['secret_key']
            salt = json_bytes['salt']
        else:
            secret_key = self._io.stdin("Insert your secret key:\t")
            if ( not self._encryption ) and auto_generated_salt:
                salt = self._io.stdin("Insert the salt\t: ")
            else:
                salt = secret_key if not auto_generated_salt else None

        self._io.stdout(self._formatter.green_foreground("\n\tStage 1 read user keys finished ..."))


        ## Construct the keys object
        return Keys(secret_key=secret_key, salt=salt)

    def _read(self) -> None:

        self._io.stdout(self._formatter.yellow_foreground("\n\tStage 2 read user content initiliazed ...\n"))

        if self._content_type == ContentType.TEXT:

            self._messages = []
            self._messages.append(self._read_text())

        elif self._content_type == ContentType.FILE:
            
            self._messages = self._read_file()

        else:

            self._messages = self._read_directory()

        self._io.stdout(self._formatter.green_foreground("\n\tStage 2 read user content finished ... "))


    def _read_text(self) -> Message:

        message      = None
        user_message = None

        if self._encryption:
            message = self._io.stdin_to_bytes(' Insert the message: \t', self._charset)
            str_ask = ' Do you want to store a message inside the encrypted content?' + self._formatter.orange_foreground(' [Yes, No]:')
            insert_message_inside = self._io.read_ask_answear(str_ask)
            if insert_message_inside:
                user_message = self._io.stdin(" Insert the message to store inside: ")
        else:
            message = self._io.stdin_to_bytes(' Insert the encrypted message: \t', self._charset)

        return Message(content=message, user_message=user_message)
    
    def _read_file(self) -> []:

        messages = []
        self._io.stdout(" For two or more files, type: file;file;file3")
        files = self._io.stdin(" Files: \t ").split(";")

        for filename in files:
            messages.append(self._read_file_content(filename))
        return messages

    def _read_directory(self) -> []:
        
        messages = []

        self._io.stdout(" For two or mode directories, type: directory;directory;directory")
        directories = self._io.stdin("Directories: \t").split(";")
        str_aux = " Do you want to access all files of directories recursively?" + self._formatter.orange_foreground(' [Yes, No]:')
        recursively = self._io.read_ask_answear(str_aux)

        for directory in directories:
            files = self._get_directory_files(directory, recursively)
            for filename in files:
                messages.append(self._read_file_content(filename))
        
        return messages


    def _get_directory_files(self, directory: str, recursively:bool) -> []:

        import os 
        files = []

        if recursively:

            for directory_item in os.listdir(directory):
                path = '{}/{}'.format(directory, directory_item)
                # we will get the files recursively
                if os.path.isdir(path):
                    files = files + self._get_directory_files(path, recursively)
                else:
                    files.append(path)
        else:
            for directory_item in os.listdir(directory):
                path = '{}/{}'.format(directory, directory_item)
                if not os.path.isdir(path):
                    files.append(path)

        return files

    def _read_file_content(self, filename:str) -> Message:
        
        user_message = None

        if self._encryption:
            str_aux = 'Do you want to store a message inside the {} encrypted file?'.format(filename) + self._formatter.orange_foreground(' [Yes, No]:')
            insert_message_inside = self._io.read_ask_answear(str_aux)
          
            if insert_message_inside:
                user_message = self._io.stdin("Insert the message to store inside: ")
        
        file_object = File(filename=filename, charset=self._charset, chunk_size=self._chunk_size)
        message = file_object.read()
        del file_object

        return Message(content=message, user_message=user_message, file_path=filename)

    def _encrypt(self) -> None:
        for message in self._messages:
            to_encrypt = message.compact(self._charset)
            message.content = self._crypto.encrypt(to_encrypt)

    def _decrypt(self) -> None:
        for message in self._messages:
            message.content = self._crypto.decrypt(message.content)
            message.decompress(self._charset)

    def _show_metadata(self, message: Message) -> None:

        if message.file_path and message.filename:

            self._io.stdout("Original file path: {}".format(message.file_path))
            self._io.stdout("Original filename: {}".format(message.filename))

        self._io.stdout("Created at: {} by: {} ".format(message.created_date, message.created_by))

        if message.user_message:
            self._io.stdout("{} left a message to you: {}".format(message.created_by, message.user_message))

        self._io.stdout("Encrypted with r_crypto version: {}".format(message.version))

    def _save_messages(self) -> None:
        if self._encryption:          

            for message in self._messages:
                
                filename = None
                
                if self._content_type == ContentType.TEXT:
                    filename = self._io.stdin("Insert the name for the encrypted file of the text: ")
                else:
                    filename = self._io.stdin("Insert the name for the encrypted file of the file {} :".format(message.filename))

                file_object = File(filename, self._charset)
                file_object.write(message.content, ENCRYPTED_EXTENSION)
                del file_object

        else:

            for message in self._messages:
                filename = None

                if message.filename:
                    filename = message.filename
                else:
                    filename = self._io.stdin("Insert the name for the decrypted file: ")

                file_object = File(filename, self._charset)
                file_object.write(message.content)
                del file_object
                self._show_metadata(message)

    def _show_messages_in_console(self) -> None:
        
        if self._encryption:

            for message in self._messages:
                str_aux = self._formatter.purple_foreground("\n Your encrypted content: ") + '{}'.format(message.content)
                self._io.stdout(str_aux)
                
        else:
            for message in self._messages:
                self._show_metadata(message)
                str_aux = self._formatter.purple_foreground("\n Your decrypted content: ") + '{}'.format(message.content)
                self._io.stdout(str_aux)
                


    def _encrypt_or_decrypt(self) -> None:

        self._crypto = Cryptor(self._keys, self._charset)

        if self._encryption:
            self._encrypt()
        else:
            self._decrypt()

        del self._crypto

    def _save_or_show(self, messages:bool):

        if messages:
            if self._save_content:
                self._io.stdout(self._formatter.yellow_foreground("\n\tStage 3 saving content to file initiliazed ...\n"))
                self._save_messages()
                self._io.stdout(self._formatter.green_foreground("\n\tStage 3 saving content to file finished ...\n"))
            else:
                self._io.stdout(self._formatter.yellow_foreground("\n\tStage 3 showing content in console initiliazed ...\n "))
                self._show_messages_in_console()
                self._io.stdout(self._formatter.green_foreground("\n\tStage 3 showing content in console finished ...\n"))

        elif not self._read_keys:
            
            if self._save_keys:
                self._io.stdout(self._formatter.yellow_foreground("\n\tStage 4 saving keys to file initiliazed ...\n"))
                keys_file_name = self._io.stdin(" Insert the keys file name: ")
                keys_content   = self._keys.get_keys_as_json().encode(self._charset)
                file_object = File(keys_file_name, self._charset)
                file_object.write(keys_content, KEYS_EXTENSION)
                del file_object
                self._io.stdout(self._formatter.green_foreground("\n\tStage 4 saving keys to file finished ...\n"))
            else:
                self._io.stdout(self._formatter.yellow_foreground("\n\tStage 4 showing keys in console initiliazed ...\n "))
                str_aux =  self._formatter.purple_foreground("\n Your secret key: ") + '{key}\t' + self._formatter.purple_foreground(" Your salt: ") + '{secret_key}'
                self._io.stdout(str_aux, self._keys.get_keys())
                self._io.stdout(self._formatter.green_foreground("\n\tStage 4 showing keys in console finished ...\n"))


    def init(self):
        self._read()
        self._encrypt_or_decrypt()
        self._save_or_show(True)
        self._save_or_show(False)
         
