def frequencies(ciphertext):
    freq = [0]*26
    for i in ciphertext:
        freq[ord(i) - ord('a')] += 1
    return freq


def modify_input(mes):
    output = []
    for i in mes:
        if i.isalpha():
            output.append(i.lower())
    return ''.join(output)


def index(freq, cipher_length):
    sum = 0
    i = 0
    while i < 26:
        sum += freq[i] * (freq[i] - 1)
    denominator = cipher_length * (cipher_length - 1)
    num = sum / denominator
    return num


def key_length(cipher_index, cipher_length):
    k = (0.0265 * cipher_length) / ((0.065 - cipher_index) + cipher_length*(cipher_index - 0.0385))
    return k


def main():
    text_input = input('Enter your message: ')
    c_text = modify_input(text_input)
    print('After removing all spaces, special characters, and making everything lowercase', c_text)

    c_len = len(c_text)
    print('The length of the cipher text is', c_len)
    c_freq = frequencies(c_text)
    c_index = index(c_freq, c_len)
    print(c_index)

main()
















