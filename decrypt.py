import sys

with open(sys.argv[1], 'r+') as fi, open(sys.argv[2], 'w') as fo:
    input_string = fi.read()

    input_list = input_string.splitlines()
    # print('Letter\tASCII\tDecrypted\tDecryptedCharacter')

    for line in input_list:
        for character in range(len(line)):
            if character % 2 == 0:
                decrypted_ascii_value = ord(line[character]) - 7
            else:
                decrypted_ascii_value = ord(line[character]) + 9        

            # print(line[character], '\t', ord(line[character]), '\t', decrypted_ascii_value, '\t\t', chr(decrypted_ascii_value))
            fo.write(chr(decrypted_ascii_value))