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
    for i in range(26):
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


def input_function(method):
    user_a = int(input('Please enter the first key, A, that is coprime to 26: '))
    user_b = int(input('Please enter the second key, B, between 0 and 26: '))
    if method == '1':
        user_mes = input('What would you like to encrypt? ')
        encrypt(user_a, user_b, user_mes)
    elif method == '2':
        user_mes = input('What would you like to decrypt? ')
        decrypt(user_a, user_b, user_mes)


def init_function():
    x = input("Enter 1 for encrypt or 2 for decrypt: ")
    if x == '1':
        input_function('1')
    elif x == '2':
        input_function('2')
        
init_function()