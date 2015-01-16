# Michael Zavarella
# Project 1 for CSCI 391
# Affine Cypher... Whatever THAT is


from fractions import gcd


# ''The encryption function takes in the values for a, b, and the user's message and encrypts it
def encrypt(a, b, mes):
    output = []                           # ''Empty list to store values in later
    for l in mes:
        if l.isalpha():                   # ''Check to see if each character is a letter
            p = ord(l.upper()) - 65       # ''Char to int
            y = ((a * p) + b) % 26        # ''Encipher int
            c = chr(y + 65)               # ''Int to char
            output.append(c)              # ''Append character to list o
        else:
            output.append(l)              # ''Appends special characters to o
    print(''.join(output))

# ''Code for the decryption process. Need a function to calculate the multiplicative inverse of A and then a function
# ''to decrypt the actual message.


def find_coprime(a):
    for i in range(26):
        if ((i * a) % 26) == 1:
            return i


def decrypt(a, b, mes):
    output = []
    inv_a = find_inv(a)
    for l in mes:
        if l.isalpha():
            c = ord(l.upper()) - 65
            y = (inv_a * (c - b)) % 26
            p = chr(y + 65)
            output.append(c)
        else:
            output.append(l)
    print(''.join(output))


def initialize_encryption():
    method = input("Enter 1 for encrypt or 2 for decrypt: ")
    if method == '1':
        print('Encrypt')
        user_a = int(input('Please enter the first key, A, that is coprime to 26: '))
        user_b = int(input('Please enter the second key, B, between 0 and 26: '))
        message = input("What message would you like to encrypt? ")
        encrypt(user_a, user_b, message)
    elif method == '2':
        print('Decrypt')
        message = input("What message would you like to decrypt? ")
        return message.lower()
    else:
        print('Error in your input')
        try_again = input('Would you like to try again? (Yes or No) ')
        if try_again.lower() in {'y', 'yes'}:
            initialize_encryption()
        elif try_again.lower() in {'no', 'n'}:
            print('Have a nice day')
        else:
            print('Error in your input, closing program')


'''
def get_message():
    user_message = str(input("What message would you like to encrypt? "))
    print(user_message)
    return user_message


def get_b_value():
    user_b = int(input('Please enter the second key, B, between 0 and 26: '))
    if 0 <= user_b <= 26:
        print('First', user_b)
        return user_b
    else:
        get_b_value()


def get_value_a():
    user_a = int(input('Please enter the first key, A, that is coprime to 26: '))
    if gcd(user_a, 26) == 1:
        print('First', user_a)
        return user_a
    else:
        get_value_a()


def encrypt_or_decrypt():
    x = int(input("Enter 1 for encrypt or 2 for decrypt: "))
    if x == 1:
        user_a = 0
        user_b = 0
        user_message = 'hello'
        get_value_a()
        print('Second', user_a)
        get_b_value()
        print('Second', user_b)
        get_message()
        encrypt(user_a, user_b, str(user_message))
'''

# '' encrypt_or_decrypt()

initialize_encryption()