# Michael Zavarella
# CSCI 391
# Frequency Analysis Decryption

# Guess which letters in the cipher text go to which plaintext letters - Nuh uh.$
# Print out guess for plaintext and ask the user if the output is correct - Easy
# If output is correct, kill the program. If output is incorrect try a different$
import operator


def compare_lists(base, comparison):
    print('Still working on this part... Sorry bruh!')


def freq_analysis(message):
    frequency_list = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
                      'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
                      'Y': 0, 'Z': 0}
    for l in message:
        if l.isalpha():
            frequency_list[l] += 1
    print(frequency_list)
    sorted_frequency_list = sorted(frequency_list.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_frequency_list


def main():
    user_message = input("Enter your message: ")
    print(freq_analysis(user_message.upper()))


main()