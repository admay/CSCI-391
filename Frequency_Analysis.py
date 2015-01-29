# Michael Zavarella
# CSCI 391
# Frequency Analysis Decryption

# Guess which letters in the cipher text go to which plaintext letters - Nuh uh.$
# Print out guess for plaintext and ask the user if the output is correct - Easy
# If output is correct, kill the program. If output is incorrect try a different$
most_common_letters = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'


def freq_analysis(message):
    l_freq = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
              'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for l in message:
        if l in l_freq:
            l_freq[l] += 1
    return l_freq


def grab_first_item(u_list):
    return u_list[0]


def reorder_freq_list(message):
    let_to_freq = freq_analysis(message)

    freq_to_let = {}
    for l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if l_freq[l] not in ordered_freq_dictionary:
            freq_to_let[let_to_freq[l]] = [l]
        else:
            freq_to_let[let_to_freq[l]].append[l]

    for frequency in ordered_freq_dictionary:
        freq_to_let[frequency].sort(key=most_common_letters.find, reverse=True)
        freq_to_let[frequency] = ''.join(freq_to_let[frequency])

    frequency_pairs = list(freq_to_let.items())
    frequency_pairs.sort(key=grab_first_item, reverse=True)

    orderd_dictionary = []
    for pair in frequency_pairs:
        orderd_dictionary.append(pair[1])

    return ''.join(orderd_dictionary)


def common_match_score(message):
    ordered_dictionary = reorder_freq_list(message)

    match_score = 0

    for com_let in most_common_letters[:6]:
        if com_let in ordered_dictionary[:6]:
            match_score += 1

    for uncom_let in most_common_letters[-6:]:
        if uncom_let in ordered_dictionary[-6:]:
            match_score += 1

    return match_score


def on_start():
    c_text = input('Enter the message you would like to decrypt: ')
    freq_analysis(c_text.upper())


on_start()