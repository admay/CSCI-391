# Michael Zavarella
# CSCI 391
# Block Cipher Cryptanalysis
'''
WSPGM HHEHM CMTGP NROVX WISCQ TXHKR VESQT IMMKW BMTKW CSTVL TGOPZ XGTKS CXHCX HSMGX WMNIA XPLVY GROWX LILNF JXTJI RIRVE XRTAX WETUS BITJM CKMCO TWSGR HIRGK PVDNI HWOHL DAIVX JVNUS JX
'''
#######################################################################################################################

from operator import itemgetter  # Need this for the frequency analysis, not sure what it does...
from sys import exit  # To kill the program
p_comp = 'ETNORIAS'

l_0 = []
l_1 = []
l_2 = []
l_3 = []
l_4 = []


def decrypt(mes, key):
    out = []
    for i in range(len(mes)):
        c = ord(mes[i]) - 65
        j = i % 5
        k = ord(key[j].upper()) - 65
        x = chr(((c - k) % 26) + 65)
        out.append(x)
        i += 1
    return ''.join(out)


# Loads the dictionary file that is used to find the valid key words in the list of all possible key words
def load_dictionary():
    dictionary_file = open('dictionary.txt')
    words = []
    for e in dictionary_file:
        e = e.replace('\n', '')
        words.append(e)
    dictionary_file.close()
    return words


# Checks the list of possible key words and removes all of those that are not English words
def check_dictionary_value(lst_in):
    lst_out = []
    dictionary = load_dictionary()
    for e in lst_in:
        if e in dictionary:
            lst_out.append(e)
    return lst_out


# Creates all possible key words
def make_key_combinations(str_0, str_1, str_2, str_3, str_4):
    output = []
    key_guess = []
    for i in range(len(str_0)):
        for j in range(len(str_1)):
            for k in range(len(str_2)):
                for l in range(len(str_3)):
                    for m in range(len(str_4)):
                        key_guess.append(str_0[i])
                        key_guess.append(str_1[j])
                        key_guess.append(str_2[k])
                        key_guess.append(str_3[l])
                        key_guess.append(str_4[m])
                        output.append(''.join(key_guess))
                        key_guess = []
                        m += 1
                    l += 1
                k += 1
            j += 1
        i += 1
    return output


def find_p_text_chars(c, p_text):
    out = []
    for i in range(len(p_text)):
        k = (ord(p_comp[i]) - 65) % 26
        x = (ord(c) - 65) % 26
        p = chr(((x - k) % 26) + 65)
        out.append(p)
        i += 1
    str_out = ''.join(out)
    return str_out


# Performs the frequency analysis on the ciphertext
def freq_analysis(message):
    frequency_dictionary = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
                            'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
                            'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for l in message.upper():
        if l.isalpha():
            frequency_dictionary[l] += 1
    sorted_frequency_tuples = sorted(frequency_dictionary.items(), key=itemgetter(1), reverse=True)

    sorted_frequency_list = [i[0] for i in sorted_frequency_tuples]  # Build the sorted alphabet from the list of tuples

    sorted_alphabet = "".join(sorted_frequency_list)  # Return the sorted alphabet as a string for comparison
    return sorted_alphabet


# Splits the user input into 5 strings
def parse_string_to_lists(string):
    for i in range(len(string)):
        if i % 5 == 0:
            l_0.append(string[i])
        elif i % 5 == 1:
            l_1.append(string[i])
        elif i % 5 == 2:
            l_2.append(string[i])
        elif i % 5 == 3:
            l_3.append(string[i])
        else:
            l_4.append(string[i])
        i += 1
    return l_0, l_1, l_2, l_3, l_4


# Removes any non-alphabetical characters and then returns a string of uppercase letters
def fix_input(txt):
    output = []
    for l in txt:
        if l.isalpha():
            output.append(l.upper())
    return output


# Yeah
def main():
    mes = fix_input(input('Enter your message: '))

    parse_string_to_lists(mes)

    comp_0 = find_p_text_chars(freq_analysis(''.join(l_0))[0], p_comp)
    comp_1 = find_p_text_chars(freq_analysis(''.join(l_1))[0], p_comp)
    comp_2 = find_p_text_chars(freq_analysis(''.join(l_2))[0], p_comp)
    comp_3 = find_p_text_chars(freq_analysis(''.join(l_3))[0], p_comp)
    comp_4 = find_p_text_chars(freq_analysis(''.join(l_4))[0], p_comp)

    print(comp_0)

    pos_keys = make_key_combinations(comp_0, comp_1, comp_2, comp_3, comp_4)
    # print(comp_0, comp_1, comp_2, comp_3, comp_4)

    legal_keys = check_dictionary_value(pos_keys)

    while True:
        for e in legal_keys:
            print(decrypt(mes, e).lower())
            check = input('Is this correct? ')
            if check.lower() in ['yes', 'y']:
                print('The keyword is', e)
                exit()

main()
