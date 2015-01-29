# Michael Zavarella
# CSCI 391
# Frequency Analysis Decryption

# Guess which letters in the cipher text go to which plaintext letters - Nuh uh.$
# Print out guess for plaintext and ask the user if the output is correct - Easy
# If output is correct, kill the program. If output is incorrect try a different$


def freq_analysis(message):
    l_freq = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
              'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for l in message:
        if l in l_freq:
            l_freq[l] += 1
    print(l_freq)


'''
    for i in range(26):
        print(chr(i + 65), ':', l_freq[i])
        i += 1
'''


def on_start():
    c_text = input('Enter the message you would like to decrypt: ')
    freq_analysis(c_text.upper())


on_start()