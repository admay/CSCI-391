# Michael Zavarella
# Project 1 for CSCI 391
# Affine Cypher... Whatever THAT is

# Encrypts the user's message based on their a, b, and message inputs
def encrypt(a, b, mes):
    output = []                               
    for l in mes:
        if l.isalpha():             
            c = chr((((a * (ord(l.upper()) - 65)) + b) % 26) + 65)
            output.append(c)            
        else:
            output.append(l)
    print(''.join(output))


# Calculates the multiplicative inverse of a number mod 26
def inverse(a):
    for i in range(1, 26):
        if (i * a) % 26 == 1:
            return i


# Decrypts the user's message based on their a, b, and message inputs
def decrypt(a, b, mes):
    output = []
    for l in mes:
        if l.isalpha():
            p = chr(((inverse(a) * ((ord(l.upper()) - 65) - b)) % 26) + 65)
            output.append(p.lower())
        else:
            output.append(l)
    print(''.join(output))


# Decrypts an encrypted message by trying all possible combinations of a and b
def brute_force(mes):
    for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        for b in range(26):
            decrypt(a, b, mes)
            print(a, b)
            outcome = input("Is this message correct? ")
            if outcome.lower() in ['y', 'yes']:
                return 'Shibby'


def get_key_values():
    check = -1
    while check == -1:
        user_a = int(input("Enter first key: "))
        user_b = int(input("Enter second key: "))
        if user_a != 13 and user_a % 2 != 0:
            if 0 < user_b < 26:
                check = 0
    return user_a, user_b


# Grabs the user inputs like a boss
def input_function(method):
    user_a, user_b = get_key_values()
    if method == '1':
        user_mes = input('What would you like to encrypt? ')
        encrypt(user_a, user_b, user_mes)
    elif method == '2':
        user_mes = input('What would you like to decrypt? ')
        decrypt(user_a, user_b, user_mes)


# Start up function to get the ball rolling
def init():
    x = input("Enter 1 for encrypt, 2 for decrypt, or 3 for a brute force decryption: ")
    if x == '1':
        input_function('1')
    elif x == '2':
        input_function('2')
    elif x == '3':
        user_mes = input('What would you like to force decrypt: ')
        brute_force(user_mes)
        

# Leggo
init()
