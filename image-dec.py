def decrypt(byte_array:bytes, key_factor:int):
    decrypt = []
    for byte in byte_array:
        temp = byte ^ key_factor
        decrypt.append(temp)
    decrypt.reverse()
    return bytes(decrypt)

def main():
    file_name            = 'C:/Users/matheus.rambo/Pictures/Celtinha.rencrypted'
    with open(file=file_name, mode='rb') as file:
        buffer = file.read(10)
        extension = buffer.decode('ascii').strip('\0') 
        with open('C:/Users/matheus.rambo/Pictures/Celtinha2{}'.format(extension), 'wb') as write_file:
            while True:
                buffer = file.read(100)
                if buffer != b"":
                    write_file.write(decrypt(buffer, 2))            
                else:
                    break

if __name__ == "__main__":
    main()