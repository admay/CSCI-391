# Michael Zavarella
# CSCI 391
# Hill Cipher


import fractions


def int_to_char(lst):
    out = []
    for i in lst:
        l = chr(i)
        out.append(l)
    return ''.join(out)


def char_to_int(string):
    out = []
    for i in string:
        l = ord(i) - 65
        out.append(l)
    return out


def decrypt(msg, key):
    out = []
    mes = char_to_int(msg)
    for i in range(int(len(mes)/2)):
        print(i, 2*i, 2*i + 1)
        x = ((key[0][0] * mes[2*i]) + (key[0][1] * mes[2*i + 1])) % 26
        y = ((key[1][0] * mes[2*i]) + (key[1][1] * mes[2*i + 1])) % 26
        out.append(x + 65)
        out.append(y + 65)
        i += 1
    print('Decrypt', mes, 'using', key)
    print(out)
    return int_to_char(out)


def encrypt(msg, key):
    out = []
    mes = char_to_int(msg)
    print(key[0][0], key[0][1], key[1][0], key[1][1])
    for i in range(int(len(mes)/2)):
        x = ((key[0][0] * mes[2*i]) + (key[0][1] * mes[2*i + 1])) % 26
        y = ((key[1][0] * mes[2*i]) + (key[1][1] * mes[2*i + 1])) % 26
        out.append(x + 65)
        out.append(y + 65)
        i += 1
    print('Encrypt', mes, 'using ', key)
    return int_to_char(out)


def inverse(a):
    for i in range(1, 26):
        if (i * a) % 26 == 1:
            return i


def get_det(mx):
    det = mx[0][0]*mx[1][1] - mx[0][1]*mx[1][0]
    return det


def mx_inverse(mx_input):
    mx_inv = [[0, 0], [0, 0]]
    det_inv = inverse(get_det(mx_input))
    mx_inv[0][0] = det_inv * mx_input[1][1] % 26
    mx_inv[0][1] = (det_inv * mx_input[0][1] * -1) % 26
    mx_inv[1][0] = (det_inv * mx_input[1][0] * -1) % 26
    mx_inv[1][1] = det_inv * mx_input[0][0] % 26
    return mx_inv


def get_key():
    key = [[0, 0], [0, 0]]
    key[0][0] = int(input('Enter key matrix value 1 - '))
    key[0][1] = int(input('Enter key matrix value 2 - '))
    key[1][0] = int(input('Enter key matrix value 3 - '))
    key[1][1] = int(input('Enter key matrix value 4 - '))
    return key


def encrypt_or_decrypt(choice, mes, key):
    if choice == '1':
        out_put = encrypt(mes, key)
        return out_put
    elif choice == '2':
        out_put = decrypt(mes, mx_inverse(key))
        return out_put
    else:
        print('Invalid command.')
        ask_command()


def check_mes(mes):
    if fractions.gcd(len(mes), 2) != 2:
        mes.append('A')
        return mes
    else:
        return mes


def fix_input(mes):
    out = []
    for i in mes:
        if i.isalpha():
            out.append(i.upper())
    return check_mes(out)


def get_mes():
    mes = input('Enter your message - ')
    return fix_input(mes)


def ask_command():
    choice = input('Enter 1 to encrypt or 2 to decrypt - ')
    return choice


def main():
    out_put = encrypt_or_decrypt(ask_command(), get_mes(), get_key())
    print(out_put)

main()