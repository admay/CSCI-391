# Michael Zavarella
# CSCI 391
# Frequency Analysis Program

import operator


# This uses the c1 and c2 values to calculate the a and b values
def calculate_a_and_b(c1, c2, p1, p2, inv_d):
    a = (inv_d * (c1 - c2)) % 26
    b = (inv_d * ((p1*c2) - (p2*c1))) % 26
    return a, b


# This function grabs the ciphertext characters to be used in the decryption process
def get_c1_and_c2(comparison_list):
    i = 0
    j = i + 1
    c1 = ord(comparison_list[i].upper()) - 65
    c2 = ord(comparison_list[j].upper()) - 65
    return c1, c2


# This function performs the frequency analysis on the user input.
# For every occurrence of a letter in the message, the value of said letter in
# the frequency_list dictionary is advanced by 1.
# After counting the number of occurrences of each letter, the dictionary is
# sorted into a list of ordered pairs ('letter',number_of_occurrences) by the
# number of occurrences. This bitch works!
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


def decrypt(a, b, mes):
    output = []
    inv_a = inverse(a)
    print('a inverse is: ', inv_a)
    for l in mes:
        if l.isalpha():
            p = chr(((inv_a * ((ord(l) - 65) - b)) % 26) + 65)
            output.append(p.lower())
    print('The multiplicative inverse of A is', inverse(a))
    print(''.join(output))


# Main function to get this bitch movin'
def main():
    p1 = ord('E') - 65
    p2 = ord('T') - 65

    # Get the cipher text
    c_text = input('Enter your ciphertext: ').upper()

    # Perform frequency analysis and return the alphabet as a string sorted by most commonly occurring characters
    alphabet = freq_analysis(c_text)
    print(alphabet)

    # Get the c1 and c2 values
    c1, c2 = get_c1_and_c2(alphabet)
    print('c1 :', c1, 'c2: ', c2)

    # Calculate a and b based on c1, c2, and the letters E and T
    a_val, b_val = calculate_a_and_b(c1, c2, p1, p2)
    print('a: ', a_val, 'b: ', b_val)

    # Decrypt the ciphertext based on a and b
    decrypt(int(a_val), int(b_val), c_text)

    # Ask the user if it is correct
    # If correct kill the program
    # If not correct, reverse c1 and c2 and try again
    # If still not correct, try a different combination of letters (650 total combinations of 2 letters)
    # Do this until the output is correct

# Leggo
main()
