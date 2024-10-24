import formatter

def get_index_of_coincidence(plain_text):
    ic = 0
    for i in range(26):
        n = plain_text.count(chr(i + ord('A')))
        ic += n * (n - 1) / (len(plain_text) * (len(plain_text) - 1))
    return ic
        
if __name__ == '__main__':
    cipher_text = input()
    cipher_text = formatter.standard_format_text(cipher_text)
    print("\n" + str(get_index_of_coincidence(plain_text)) + "\n")
    print("If the index of coincidence is close to 0.070: \nIt is likely to have been encrypted using a transposition cipher or a monoalphabetic substitution cipher. \n")
    print("If the index of coincidence is close to 0.0385: \nIt is likely to have been encrypted using a polyalphabetic substitution cipher. \n")