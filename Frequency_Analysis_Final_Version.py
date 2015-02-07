# Michael Zavarella
# CSCI 391
# Frequency Analysis Program

'''
The first c_text is encrypted with A = 21 and B = 1
The second c_text is encrypted with A = 11 and B = 4
The third c_text is encrypted with A = 3 and B = 19
The fourth c_text is encrypted with A = 23 and B = 14
'''

from operator import itemgetter  # Need this for the frequency analysis, not sure what it does...
from fractions import gcd  # Need this for the gcd function
from sys import exit  # To kill the program
########################################################################################################################


# Flips the c1 and c2 values
def flip_c1_c2(c1, c2):
    c1_f = c2  # The f stands for flipped!
    c2_f = c1
    return c1_f, c2_f


# Decrypts the message
def decrypt(a, b, mes):
    output = []
    inv_a = inverse(a)
    for l in mes:
        if l.isalpha():
            p = chr(((inv_a * ((ord(l) - 65) - b)) % 26) + 65)
            output.append(p.lower())
    return ''.join(output)


# This uses the c1 and c2 values to calculate the a and b values
def calc_a_b(c1, c2,p1, p2, inv_d):
    a = int((inv_d * (c1 - c2)) % 26)
    b = int((inv_d * ((p1*c2) - (p2*c1))) % 26)
    return a, b


# Grabs the ciphertext characters to be used in the decryption process
def find_c1_c2(comparison_list, i, j):
    c1 = ord(comparison_list[i].upper()) - 65
    c2 = ord(comparison_list[j].upper()) - 65
    return c1, c2


# Performs the frequency analysis on the user input.
def freq_analysis(message):
    frequency_dictionary = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
                            'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
                            'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for l in message:
        if l.isalpha():
            frequency_dictionary[l] += 1
    sorted_frequency_tuples = sorted(frequency_dictionary.items(), key=itemgetter(1), reverse=True)

    sorted_frequency_list = [i[0] for i in sorted_frequency_tuples]  # Build the sorted alphabet from the list of tuples

    sorted_alphabet = "".join(sorted_frequency_list)  # Return the sorted alphabet as a string for comparison
    return sorted_alphabet


# Calculates the multiplicative inverse of a number mod 26
def inverse(x):
    for i in range(1, 26):
        if (i * x) % 26 == 1:
            return i


def main():
    p1 = ord('E') - 65  # The minus 65 aligns the alphabet so that the index of A is 0 and Z is 26
    p2 = ord('T') - 65
    inv_d = 19  # Based in p1 and p2 being E and T

    # Get the cipher text from the user
    c_text = input('Enter the cipher text: ').upper()

    # Create the string of the most frequently used characters
    c_text_frequency_alphabet = freq_analysis(c_text)
    while True:
        for i in range(0, 26, 1):
            for j in range(1, 26, 1):
                c1, c2 = find_c1_c2(c_text_frequency_alphabet, i, j)  # Find the first two most common c_text characters

                a, b = calc_a_b(c1, c2, p1, p2, inv_d)  # Calculate the Affine keys, A and B

                if gcd(a, 26) == 1:
                    print(decrypt(a, b, c_text))  # Attempt decryption using the A and B from above
                    ask = input('Is this the correct plaintext? ')
                    if ask.lower() in ['y', 'yes']:
                        print('A is', a, 'and B is', b)
                        exit()
                    else:  # flip c1 and c2, try again
                        c1, c2 = flip_c1_c2(c1, c2)
                        a, b = calc_a_b(c1, c2, p1, p2, inv_d)  # Calculate the Affine keys, A and B

                        print(decrypt(a, b, c_text))  # Attempt decryption using the A and B from above
                        ask = input('Is this the correct plaintext? ')
                        if ask.lower() in ['y', 'yes']:
                            print('A is', a, 'and B is', b)
                            exit()
                else:
                    print('Invalid key A')


main()