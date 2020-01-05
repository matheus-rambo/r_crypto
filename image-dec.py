def main():
    file_name            = 'C:/Users/matheus.rambo/Pictures/Celtinha.rencrypted'
    with open(file=file_name, mode='rb') as file:
        buffer = file.read(10)
        extension = buffer.decode('ascii').strip('\0') 
        with open('C:/Users/matheus.rambo/Pictures/Celtinha2{}'.format(extension), 'wb') as write_file:
            while True:
                buffer = file.read(10)
                if buffer != b"":
                    write_file.write(buffer)            
                else:
                    break

if __name__ == "__main__":
    main()