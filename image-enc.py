def encrypt(byte_array:bytes, key_factor:int):
    encrypted = []
    for byte in byte_array:
        temp = byte ^ key_factor
        encrypted.append(temp)
    encrypted.reverse()
    return bytes(encrypted)


def main():
    file_name            = 'C:/Users/matheus.rambo/Pictures/Celtinha.jpg'
    extension            = file_name[file_name.rindex('.'):]
    extension_max_length = 10
    key_factor           = int(input('Choose a number for the key factor: ')) 

    with open(file=file_name, mode='rb') as file:
        buffer = None
        with open('C:/Users/matheus.rambo/Pictures/Celtinha.rencrypted', 'wb') as write_file:
            for index in range(extension_max_length - len(extension)):
                write_file.write(b'\0')
            write_file.write(bytes(extension, 'ascii'))
            while True:
                buffer = file.read(100)
                if buffer != b"":
                    write_file.write(encrypt(buffer, key_factor))
                else:
                    break


if __name__ == "__main__":
    main()