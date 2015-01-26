# Michael Zavarella
# Project 1 for CSCI 391
# This program implements an Affine cypher encryption or decryption
output = []


# Encrypts the user's plaintext message received in the get_input function.
# The a and b values are taken from the get_key_values function and are used as
# parameters used in the encryption algorithm. As each individual character is
# encrypted, it is added to the end of the output array which is then printed as a
# string of uppercase characters
def encrypt(a, b, mes):
    for l in mes:
        if l.isalpha():             
            c = chr((((a * (ord(l.upper()) - 65)) + b) % 26) + 65)
            output.append(c)            
        else:
            output.append(l)


# Calculates the multiplicative inverse of a number mod 26
def inverse(a):
    for i in range(1, 26):
        if (i * a) % 26 == 1:
            return i


# Decrypts the user's ciphertext that is received from the get_input function.
# The inverse of a is calculated via the inverse function and used to convert the
# ciphertext back into plaintext. The output is created in the same way as in the
# encrypt function.
def decrypt(a, b, mes):
    for l in mes:
        if l.isalpha():
            p = chr(((inverse(a) * ((ord(l.upper()) - 65) - b)) % 26) + 65)
            output.append(p.lower())
        else:
            output.append(l)


# Decrypts an encrypted message by trying all possible combinations of a and b values.
# After every attempt, the a and b values are printed along with the plaintext that was
# calculated. The user is then asked if the output is correct, if it is then the inputs
# y or yes will end the program, else hit enter and keep trying.
def brute_force(mes):
    for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        for b in range(26):
            decrypt(a, b, mes)
            print(a, b)
            outcome = input("Is this message correct? Press enter to continue decrypting.")
            if outcome.lower() in ['y', 'yes']:
                return 'Shibby'


def get_key_values():
    check = -1
    while check == -1:
        user_a = int(input("Enter first key: "))
        user_b = int(input("Enter second key: "))
        if user_a != 13 and user_a % 2 != 0:
            if 0 <= user_b < 26:
                check = 0
            else:
                print("Invalid B.")
        else:
            print("Invalid A.")
    return user_a, user_b


# Grabs the user's inputs for the keys a and b by calling the get_key_values function.
# Grabs the user's message via a raw input.
# Takes the method as a parameter to determine whether the user wants to encrypt or decrypt
# their message. Then, based on the method, it calls either the encrypt or decrypt function.
def get_input(method):
    user_a, user_b = get_key_values()
    user_mes = input('Enter your message: ')
    if method == '1':
        encrypt(user_a, user_b, user_mes)
    elif method == '2':
        decrypt(user_a, user_b, user_mes)
    print(''.join(output))


# Start-up function that begins by asking the user if they want to encrypt, decrypt, or brute
# force decrypt a message.
def on_start():
    x = input("Enter 1 for encrypt, 2 for decrypt, or 3 for a brute force decryption: ")
    if x == '1':
        get_input('1')
    elif x == '2':
        get_input('2')
    elif x == '3':
        user_mes = input('What would you like to force decrypt: ')
        brute_force(user_mes)
        

on_start()