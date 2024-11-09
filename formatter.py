def standard_format_text(plain_text):
    for char in plain_text:
        if char.isalpha() == False:
            plain_text = plain_text.replace(char, '')
    plain_text = plain_text.upper()
    return plain_text

def standard_reformat_text(original_text, new_text):
    j = 0
    reformatted_text = ''
    for i in range(len(new_text)):
        while True:
            if original_text[j].isalpha() == False:
                reformatted_text += original_text[j]
                j += 1
            else:
                reformatted_text += new_text[i]
                j += 1
                break
    return reformatted_text

if __name__ == '__main__':
    plain_text = input()
    plain_text = standard_format_text(plain_text)
    print(len(plain_text))
    print(plain_text)