# Michael Zavarella
# CSCI 391
# Frequency Analysis Program

# Global Variables

p1 = ord('E') - 65  # The minus 65 aligns the alphabet so that the index of A is 0 and Z is 26
p2 = ord('T') - 65  # E and T are the two most frequently occurring letters in the english alphabet, so we'll use them
'''
# These will be used to index the c1 and c2 values that will appear later. I'm using the index as a global variable
# because I can't think of an easier way to do it yet
i_counter = 0
j_counter = 1
'''
# Need this for the frequency analysis, not sure what it does...
import operator

# Need this for the gcd function
from fractions import gcd
########################################################################################################################


def flip_c1_c2(C1, C2):
    c1_f = C2  # The f stands for flipped!
    c2_f = C1
    return c1_f, c2_f


def decrypt(a, b, mes):
    output = []
    inv_a = inverse(a)
    print('a inverse is: ', inv_a)
    for l in mes:
        if l.isalpha():
            p = chr(((inv_a * ((ord(l) - 65) - b)) % 26) + 65)
            output.append(p.lower())
    return ''.join(output)


# This uses the c1 and c2 values to calculate the a and b values
def calc_a_b(C1, C2, P1, P2, inv_d):
    a = int((inv_d * (C1 - C2)) % 26)
    b = int((inv_d * ((P1*C2) - (P2*C1))) % 26)
    return a, b


# This function grabs the ciphertext characters to be used in the decryption process
def find_c1_c2(comparison_list, i, j):
    c1 = ord(comparison_list[i].upper()) - 65
    c2 = ord(comparison_list[j].upper()) - 65
    return c1, c2


# This function performs the frequency analysis on the user input.
def freq_analysis(message):
    frequency_dictionary = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
                            'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
                            'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for l in message:
        if l.isalpha():
            frequency_dictionary[l] += 1

    sorted_frequency_tuples = sorted(frequency_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    # print(sorted_frequency_tuples)

    # Create a list of the sorted alphabet from the list of tuples
    sorted_frequency_list = [i[0] for i in sorted_frequency_tuples]

    # Return the sorted alphabet as a string for comparison
    sorted_alphabet = "".join(sorted_frequency_list)
    return sorted_alphabet


# Calculates the multiplicative inverse of a number mod 26
def inverse(x):
    for i in range(1, 26):
        if (i * x) % 26 == 1:
            return i


def main():
    i = 0
    j = 1

    # This is for when the program asks the user if the output is correct. While the check is false, the program will
    # keep trying. When the check goes to true, the program will shut down. Dope.
    output_check = False

    # Calculate d and inv_d initially so you only have to do it once!
    d = (p1 - p2) % 26
    inv_d = inverse(d)
    print('The inverse of d is', inv_d)

    # Get the cipher text from the user
    c_text = input('Enter the cipher text: ').upper()

    # Create the string of the most frequently used characters
    c_text_frequency_alphabet = freq_analysis(c_text)
    print('The cipher text alphabet sorted by frequency is', c_text_frequency_alphabet, 'and its length is',
          len(c_text_frequency_alphabet))
    while output_check is False:
        for i in range(0, 26, 1):
            for j in range(1, 26, 1):

                # Find the first two most common c_text characters
                c1, c2 = find_c1_c2(c_text_frequency_alphabet, i, j)
                print('C1 is', c1, 'and C2 is', c2)

                # Calculate the Affine keys, A and B
                a, b = calc_a_b(c1, c2, p1, p2, inv_d)
                print('A is', a, 'and B is', b)
                print('The inverse of a is', inverse(a))

                # Attempt decryption using the A and B from above
                print(decrypt(a, b, c_text))
                ask = input('Is this the correct plaintext? ')
                if ask.lower() in ['y', 'yes']:
                    output_check = True
                    print('Shibby')
                    break
                else:  # flip c1 and c2, try again
                    c1, c2 = flip_c1_c2(c1, c2)
                    print('C1 is', c1, 'and C2 is', c2)

                    # Calculate the Affine keys, A and B
                    a, b = calc_a_b(c1, c2, p1, p2, inv_d)
                    print('A is', a, 'and B is', b)
                    print('The inverse of a is', inverse(a))

                    # Attempt decryption using the A and B from above
                    print(decrypt(a, b, c_text))
                    ask = input('Is this the correct plaintext? ')
                    if ask.lower() in ['y', 'yes']:
                        output_check = True
                        print('Shibby')
                        break
                    else:
                        print('Sorry')  # Need to add 1 to j


main()