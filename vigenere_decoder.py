import period_finder
import formatter
import math

def english_quadgram():
    f = open(r'C:\\Users\\yuyao\\OneDrive\\Documents\\Cryptography\\cryptography_tools\\data\\english_quadgrams.txt', 'r')
    N = 0
    quadgram_score = {}
    for line in f:
        quadgram_score[line.split(' ')[0]] = int(line.split(' ')[1].strip())
        N += int(line.split(' ')[1].strip())
    return quadgram_score, N

def quadgram_fitness(plain_text, quadgram_score, N):
    fitness = 0
    for i in range(len(plain_text) - 3):
        quadgram = plain_text[i:i + 4]
        if quadgram in quadgram_score:
            fitness += math.log10((quadgram_score[quadgram] / N))
        else:
            fitness += math.log10(0.01 / N)
    return fitness

def vigenere_decrypt(cipher_text, key):
    decrypted_text = ''
    key_repeated = (key * (len(cipher_text) // len(key))) + key[:len(cipher_text) % len(key)]
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            shift = ord(key_repeated[i].upper()) - ord('A')
            if cipher_text[i].isupper():
                decrypted_text += chr((ord(cipher_text[i]) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(cipher_text[i]) - shift - ord('a')) % 26 + ord('a'))
        else:
            decrypted_text += cipher_text[i]
    return decrypted_text

def vigenere_hill_climb(cipher_text, m):
    key = 'A' * m
    quadgram_score, N = english_quadgram()
    current_fitness = quadgram_fitness(cipher_text, quadgram_score, N)
    flag = False
    old_fitness = 0
    maximum_fitness = 0
    while not flag:
        old_fitness = current_fitness
        for i in range(m):
            maximum_fitness = current_fitness
            for x in range(26):
                new_key = key[:i] + chr(x + ord('A')) + key[i + 1:]
                decrypted_text = vigenere_decrypt(cipher_text, new_key)
                new_fitness = quadgram_fitness(decrypted_text, quadgram_score, N)
                if new_fitness > maximum_fitness:
                    maximum_fitness = new_fitness
                    key = new_key
                    print(new_fitness)
                    print(key)
        if current_fitness == old_fitness:
            flag = True
    return key

if __name__ == '__main__':
    cipher_text = input()
    cipher_text = formatter.standard_format_text(cipher_text)
    quadgram_score, N = english_quadgram()
    m = period_finder.slice_ioc_period(cipher_text)
    # m = 4
    print(m)
    key = vigenere_hill_climb(cipher_text, m)
    decrypted_text = vigenere_decrypt(cipher_text, key)
    print("\n" + formatter.standard_reformat_text(cipher_text, decrypted_text))
    print(key)