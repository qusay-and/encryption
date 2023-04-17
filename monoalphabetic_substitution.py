import string
import argparse

def create_encryption_mapping(key):
    key_letters = list(dict.fromkeys(key).keys())
    letters = list(string.ascii_lowercase)
    mapped_letters = list(string.ascii_lowercase)
    mapping = {}

    for letter in key_letters:
        if letter not in string.ascii_lowercase:
            key_letters.remove(letter)

    for letter in key_letters:
        mapping[mapped_letters[0]] = letter
        mapped_letters.remove(mapped_letters[0])
        letters.remove(letter)

    for letter in letters:
        mapping[mapped_letters[0]] = letter
        mapped_letters.remove(mapped_letters[0])

    return mapping

def create_decryption_mapping(key):
    mapping = {}
    key_letters = list(dict.fromkeys(key).keys())

    for letter in key_letters:
        if letter not in string.ascii_lowercase:
            key_letters.remove(letter)


    for letter in string.ascii_lowercase:
        if letter not in key_letters:
            key_letters.append(letter)

    for key, val in zip(key_letters, string.ascii_lowercase):
        mapping[key] = val

    return mapping

def encrypt_file(input_file_name, output_file_name, key):    
    mapping = create_encryption_mapping(key)

    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'w')

    for line in input_file:
        for letter in line:
            if letter in string.ascii_lowercase:
                output_file.write(mapping[letter])
            else:
                output_file.write(letter)
        output_file.write('\n')


def decrypt_file(input_file_name, output_file_name, key):
    mapping = create_decryption_mapping(key)            
    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'w')
    for line in input_file:
        for letter in line:
            if letter in string.ascii_lowercase:
                output_file.write(mapping[letter])
                
            else:
                output_file.write(letter)

parser = argparse.ArgumentParser(description='Monoalphabetic Substitution Cipher')

parser.add_argument('-i', '--input', help='Input file name')
parser.add_argument('-o', '--output', help='Output file name')

parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt the file')
parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the file')

parser.add_argument('-k', '--key', type=str, help='Key to encrypt/decrypt the file')

args = parser.parse_args()

if (args.encrypt):
    encrypt_file(args.input, args.output, args.key)
elif(args.decrypt):
    decrypt_file(args.input, args.output, args.key)