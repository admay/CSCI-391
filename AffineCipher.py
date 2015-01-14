# Michael Zavarella
# Project 1 for CSCI 391
# Affine Cypher... Whatever THAT is


# ''The encryption function takes in the values for a, b, and the user's message and encrypts da motha' fuckers
def encrypt(a, b, mes):
    output = []                                # ''Empty list to store values in later
    for l in mes:
        if l.isalpha():                   # ''Check to see if each character is a letter
            x = ord(l.upper()) - 65       # ''Char to int             
            y = ((a * x) + b) % 26        # ''Encipher int
            c = chr((y) + 65)             # ''Int to char
            output.append(c)              # ''Append character to list o
        else:
            output.append(l)              # ''Appends special characters to o
    print(''.join(output))


def decrypt(a, b, mes):
    o = []
    for l in mes:
        if l.isalpha():
            x = ord(l.upper()) - 65                    
            y = ((a * x) + b) % 26
            p = chr((y) + 65)
            o.append(p.lower())
        else:
            o.append(l)
    print(o)


def get_user_inputs():
    x = input("Enter 1 for encrypt or 2 for decrypt: ")
    if x == '1':
        print('Encrypt')
        user_a = int(input('Please enter the first key, A, that is coprime to 26: '))
        user_b = int(input('Please enter the second key, B, between 0 and 26: '))
        message = input("What message would you like to encrypt? ")
        encrypt(user_a, user_b, message)
    elif x == '2':
        print('Decrypt')
        message = input("What message would you like to encrypt? ")
        return message.lower()
    else:
        print('Error in your input')
        try_again = input('Would you like to try again? (Yes or No) ')
        if try_again.lower() == 'yes' or try_again.lower() == 'y':
            encrypt_or_decrypt()
        elif try_again.lower() == 'no' or try_again.lower() == 'n':
            print('Have a nice day')
        else:
            print('Error in your input, closing program')

get_user_inputs()