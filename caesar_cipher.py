import string
import argparse

def encrypt (letter, offset):
    return chr((ord(letter) - 97 + offset)%26 + 97)

def decrypt (letter, offset):
    return chr((ord(letter) - 97 + 26 - offset)%26 + 97)

def encrypt_file(input_file_name, output_file_name, offset):            
    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'w')

    for line in input_file:
        for letter in line:
            if letter in string.ascii_lowercase:
                output_file.write(encrypt(letter, offset))
            else:
                output_file.write(letter)
        output_file.write('\n')


def decrypt_file(input_file_name, output_file_name, offset):            
    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'w')
    for line in input_file:
        for letter in line:
            if letter in string.ascii_lowercase:
                output_file.write(decrypt(letter, offset))
                
            else:
                output_file.write(letter)


parser = argparse.ArgumentParser(description='Caesar Cipher')

parser.add_argument('-i', '--input', help='Input file name')
parser.add_argument('-o', '--output', help='Output file name')

parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt the file mode')
parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the file mode')

parser.add_argument('-k', '--key', type=int, help='Key to encrypt/decrypt the file')

args = parser.parse_args()

if (args.encrypt):
    encrypt_file(args.input, args.output, args.key)
elif(args.decrypt):
    decrypt_file(args.input, args.output, args.key)