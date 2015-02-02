# Guess which letters in the cipher text go to which plaintext letters - Nuh uh.$
# Print out guess for plaintext and ask the user if the output is correct - Easy
# If output is correct, kill the program. If output is incorrect try a different$
import operator
standard_frequencies = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'


# Compares the list of standard letter frequencies to the list of letter
# frequencies from the user's message
def compare_lists(comparison_list):
    print('Still working on this part... Sorry bruh!')


# This function performs the frequency analysis on the user input.
# For every occurrence of a letter in the message, the value of said letter in
# the frequency_list dictionary is advanced by 1.
# After counting the number of occurrences of each letter, the dictionary is
# sorted into a list of ordered pairs ('letter',number_of_occurrences) by the
# number of occurrences.
def freq_analysis(message):
    frequency_list = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
                      'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
                      'Y': 0, 'Z': 0}
    for l in message:
        if l.isalpha():
            frequency_list[l] += 1
    sorted_frequency_list = sorted(frequency_list.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_frequency_list
    # Need to create a string of letters, similar to standard_frequencies, based on the list of pairs.
    # This string will allow for comparison between the two alphabets.


# Main function to get this bitch movin'
def main():
    user_message = input("Enter your message: ")
    compare_lists(freq_analysis(user_message.upper()))
    print(freq_analysis(user_message.upper()))


# Leggo
main()
