# Michael Zavarella
# CSCI 391
# Block Cipher

from sys import exit


def decrypt(mes, key):
    output = []
    for i in range(len(mes)):
        if mes[i].isalpha():
            p_i = ord(mes[i]) - 65
            k_i = ord(key[i % len(key)]) - 65
            c_i = chr(((p_i - k_i) % 26) + 65)
            output.append(c_i)
    return ''.join(output)


def encrypt(mes, key):
    output = []
    for i in range(len(mes)):
        if mes[i].isalpha():
            p_i = ord(mes[i]) - 65
            k_i = ord(key[i % len(key)]) - 65
            c_i = chr(((p_i + k_i) % 26) + 65)
            output.append(c_i)
    return ''.join(output)


def remove_spaces(str):
    str_ = str.replace(' ', '')
    return str_


def get_input():
    mes = remove_spaces(input('Enter your message: '))
    key = remove_spaces(input('Enter your key word: '))
    return mes, key


def main():
    method = input('Enter 1 to encrypt or 2 to decrypt: ')
    if method == '1':
        p_text, key = get_input()
        print(encrypt(p_text.upper(), key.upper()).lower())
    elif method == '2':
        c_text, key = get_input()
        print(decrypt(c_text, key))
    elif method.lower() in ['break', 'b']:
        exit()
    else:
        print('Invalid command')
        main()

main()