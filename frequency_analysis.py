import matplotlib.pyplot as plt

def plot_frequencies(letters, frequencies):
    english_frequencies = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]

    fig, axs = plt.subplots(1, 2, figsize=(14, 7))

    axs[0].bar(letters, frequencies)
    axs[0].set_title('Cipher Text Letter Frequencies')

    axs[1].bar(letters, english_frequencies)
    axs[1].set_title('Common English Letter Frequencies')
    plt.show()
    return 

def get_frequencies(cipher_text):
    letters = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']
    frequencies = [0 for i in range(26)]
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            frequencies[ord(cipher_text[i]) - ord('A')] += 1
    
    # for i in range(26):
        # print(letters[i], frequencies[i])
    
    frequencies = [i / len(cipher_text) * 100 for i in frequencies]
    
    return letters, frequencies    

if __name__ == '__main__':
    cipher_text = input()
    letters, frequencies = get_frequencies(cipher_text)
    plot_frequencies(letters, frequencies)
