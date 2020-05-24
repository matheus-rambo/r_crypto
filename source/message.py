from json                 import dumps, loads
from getpass              import getuser
from datetime             import datetime
from source.app_constants import VERSION, NULL_BYTES

class Message():

    def __init__(self, content:bytes, user_message:str, file_path:str = None):

        self.content      = content
        self.user_message = user_message
        self.filename     = self._get_filename(file_path) if file_path is not None else None 
        self.created_by   = None
        self.created_date = None
        self.file_path    = file_path
        self.version      = None
    
    def _metadata_to_json(self, charset:str = 'utf-8') -> str:

        metadata = {
            "filename"    : self.filename,
            "created_by"  : self.created_by,
            "created_date": self.created_date,
            "user_message": self.user_message,
            "file_path"   : self.file_path,
            "version"     : self.version
        }  

        json_str = dumps(metadata)
        return json_str

    def compact(self, charset:str) -> bytes:

        self.created_by   = getuser()
        self.created_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.version      = VERSION

        json_bytes = self._metadata_to_json().encode(charset)

        # init the array with 3 null bytes
        array_bytes = bytearray(NULL_BYTES)

        # copy the metadata
        for byte in json_bytes:
            array_bytes.append(byte)
        
        # insert three null bytes
        array_bytes.append(0)
        array_bytes.append(0)
        array_bytes.append(0)

        # copy the content
        for byte in self.content:
            array_bytes.append(byte)

        # creates a new byte array
        return bytes(array_bytes)

    def decompress(self, charset:str) -> None:

        # 3 null bytes to specify that has metadata
        if self.content[0:3] == NULL_BYTES:

            metadata_info_size = None

            for index in range(3, len(self.content)):

                # 3 null consecutive null bytes, it means that is the end of metadata information
                if self.content[index:index + 3] == NULL_BYTES:

                    metadata_info_size = index
                    content_index      = index + 3
                    break

            metadata = self.content[3:metadata_info_size]   
            self.content = self.content[content_index:]
            self._extract_metadata(metadata, charset)
            

    def _extract_metadata(self, metadata:bytes, charset:str) -> None:

        json_string = metadata.decode(charset)
        json_object = loads(json_string)
        
        self.file_path    = json_object['file_path']
        self.created_by   = json_object['created_by']
        self.created_date = json_object['created_date']
        self.filename     = json_object['filename']
        self.user_message = json_object['user_message']
        self.version      = json_object['version']


    def _get_filename(self, path:str):
        if '/' in path:
            return path[path.rindex('/') + 1:] 
        elif '\\' in path:
            return path[path.rindex('\\') + 1:] 
        else:
            return path        