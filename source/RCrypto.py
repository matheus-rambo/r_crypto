class Info():
    def __init__(self):
        self.content = None
        self._generated_by = None
        self._data_generated = None
        self._original_file_extension = None
        self._rcrypt_version = None
    
    def get_original_file_extension(self):
        if self._original_file_extension is None:
            return ".txt"
        return self._original_file_extension
        
    def set_information(self, info_content:str):
        info = info_content.split(";")
        self._generated_by = info[1]
        self._data_generated = info[2]
        self._original_file_extension = info[3]
        self._rcrypt_version = info[4]

    def print_info(self):
        if self._generated_by is not None:
            print("\n*** Information of the file, when it was encrypted! ***")
            print("The file was encrypted by: {}".format(self._generated_by))
            print("In: {}".format(self._data_generated))
            print("The original file extension is: {}".format(self._original_file_extension))
            print("Encrypted with rcrypt version: {}".format(self._rcrypt_version))
        else:
            pass

    def print_all(self):
        print("\n{}".format(self.content))
        self.print_info()

class UserFile():
    def __init__(self, file:str):
        self.file_name = None
        self.extension = None
        self._set_file_properties(file)
    
    def _set_file_properties(self, file:str):
        if "." in file:
            dot_index = file.rindex(".")
            self.extension = file[dot_index:]
            self.file_name = file[:dot_index]
        else:
            self.file_name = file
            self.extension = ""

class InvalidFileExtensionException(Exception):
    def __init__(self, message: str):
        self.message = message
