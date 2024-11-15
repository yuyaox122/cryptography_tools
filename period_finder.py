import index_of_coincidence as ioc
import formatter

def rough_ioc_period(cipher_text):
    ioc_value = ioc.get_index_of_coincidence(cipher_text)
    m = (ioc_value - 1) / 0.75
    # 1.75 1 (monoalphabetic)
    # 1.38 2 (polyalphabetic)
    # 1.25 3 (polyalphabetic)
    # 1.19 4 (polyalphabetic)
    # 1.15 5 (polyalphabetic)
    # 1.13 6 (polyalphabetic)
    return m

def slice_ioc_period(cipher_text):
    period = 0
    while True:
        period += 1
        slices = ['' for i in range(period)]
        for i in range(len(cipher_text)):
            slices[i % period] += cipher_text[i]
        sum_ioc = 0
        for i in range(period):
            sum_ioc += ioc.get_index_of_coincidence(slices[i])
        average_ioc = sum_ioc / period * 26
        if average_ioc > 1.6:
            break
    return period

if __name__ == '__main__':
    cipher_text = input()
    cipher_text = formatter.standard_format_text(cipher_text)
    print(rough_ioc_period(cipher_text))
    print(slice_ioc_period(cipher_text))