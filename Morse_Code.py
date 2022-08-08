# Morse Code App

# Setup
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# App


def morse_code_encrypt(text):
    result = ""
    for elem in text:
        if elem == " ":
            result += " / "
            continue
        result += MORSE_CODE_DICT[elem.upper()] + " "

    return result.strip()



def morse_code_decrypt(text):
    result = ""
    for elem in text.split():
        if elem == "/":
            result += " "
        for key, value in MORSE_CODE_DICT.items():
            if value == elem:
                result += key

    return result


text = "Hello World"

print(morse_code_encrypt(text))

text = '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'

print(morse_code_decrypt(text))
