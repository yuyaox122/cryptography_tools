import frequency_analysis

def get_difference(frequency):
    english_frequencies = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]
    difference = 0
    for i in range(26):
        difference += abs(frequency[i] - english_frequencies[i])
    return difference
    

def affine_decoder(cipher_text):
    difference = 100000000
    best_text = ''
    best_a = 0
    best_b = 0
    for a in range(26):
        for b in range(26):
            new_text = ''
            for i in range(len(cipher_text)):
                if cipher_text[i].isalpha():
                    new_text += chr((a * (ord(cipher_text[i]) - ord('A')) + b) % 26 + ord('A'))
                else:
                    new_text += cipher_text[i]
            letters, frequency = frequency_analysis.get_frequencies(new_text)
            if get_difference(frequency) < difference:
                difference = get_difference(frequency)
                best_a = a
                best_b = b
                best_text = new_text
    print(best_text)
    return best_a, best_b    
    
if __name__ == '__main__':
    cipher_text = input()
    a, b = affine_decoder(cipher_text)
