# Michael Zavarella
# Project 1 for CSCI 391
# Affine Cypher... Whatever THAT is


def encrypt(a, b, mes):
    output = []                               
    for l in mes:
        if l.isalpha():             
            c = chr((((a * (ord(l.upper()) - 65)) + b) % 26) + 65)
            output.append(c)            
        else:
            output.append(l)
    print(''.join(output))


def inverse(a):
    for i in range(1, 26):
        if (i * a) % 26 == 1:
            return i


def decrypt(a, b, mes):
    output = []
    for l in mes:
        if l.isalpha():
            p = chr(((inverse(a) * ((ord(l.upper()) - 65) - b)) % 26) + 65)
            output.append(p.lower())
        else:
            output.append(l)
    print(''.join(output))


def brute_force(mes):
    for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        for b in range(26):
            decrypt(a, b, mes)
            print(a, b)
            outcome = input("Is this message correct? ")
            if outcome.lower() in ['y', 'yes']:
                return 'Shibby'



def input_function(method):
    user_a = int(input('Please enter the first key, A, that is coprime to 26: '))
    user_b = int(input('Please enter the second key, B, between 0 and 25: '))
    if method == '1':
        user_mes = input('What would you like to encrypt? ')
        encrypt(user_a, user_b, user_mes)
    elif method == '2':
        user_mes = input('What would you like to decrypt? ')
        decrypt(user_a, user_b, user_mes)


def init():
    x = input("Enter 1 for encrypt, 2 for decrypt, or 3 for a brute force decryption: ")
    if x == '1':
        input_function('1')
    elif x == '2':
        input_function('2')
    elif x == '3':
        user_mes = input('What would you like to force decrypt: ')
        brute_force(user_mes)
        
<<<<<<< HEAD
init()
=======
init_function()
>>>>>>> origin/master
