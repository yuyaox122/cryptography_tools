import formatter
import math
import random

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

def permutation_decipher(cipher_text, key):
    plain_text = ''
    for i in range(len(cipher_text) // len(key)):
        block = cipher_text[i * len(key):(i + 1) * len(key)]
        for j in range(len(key)):
            plain_text += block[key[j]]
    return plain_text
        
def permutation_hill_climb(cipher_text, key, quadgram_score, N):
    best_fitness = quadgram_fitness(cipher_text, quadgram_score, N)
    parent_key = key.copy()
    counter = 0
    while counter < 500 * len(key):
        child_key = parent_key.copy()
        if random.random() < 0.5:
            idx1 = random.randint(0, len(child_key) - 1)
            idx2 = random.randint(0, len(child_key) - 1)
            child_key[idx1], child_key[idx2] = child_key[idx2], child_key[idx1]
        else:
            cut = random.randint(1, len(child_key) - 1)
            child_key = child_key[cut:] + child_key[:cut]

        plain_text = permutation_decipher(cipher_text, child_key)
        new_fitness = quadgram_fitness(plain_text, quadgram_score, N)
        print(new_fitness)
        if new_fitness > best_fitness or (new_fitness > best_fitness * 0.9 and random.randint(1, 20) == 1):
            parent_key = child_key
            best_fitness = new_fitness
            print("New best: " + str(best_fitness))
            counter = 0
        else:
            counter += 1
    print(parent_key)
    print(best_fitness)
    return permutation_decipher(cipher_text, parent_key)

if __name__ == '__main__':
    cipher_text = input()
    quadgram_score, N = english_quadgram()
    key = list(range(6))
    plain_text = permutation_hill_climb(formatter.standard_format_text(cipher_text), key, quadgram_score, N)
    print("\n" + formatter.standard_reformat_text(cipher_text, plain_text))
    