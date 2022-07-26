# Random Password Generator

# Setup

from random import randint

# Specify requirements

while True:
    try:
        length = int(input("Password length: "))
        upper_chars = int(input("How many uppercase characters: "))
        number_chars = int(input("How many digits: "))
        special_chars = int(input('How many special characters: '))

        temp_input_values_list = [upper_chars, number_chars, special_chars]

        if upper_chars + number_chars + special_chars > length:
            print("Wrong values! Try again with correct length!")
        else:
            break
    except ValueError:
        print("Wrong input! Use only decimal numbers!")

# Password Creation
while True:
    password = ""

    # Character randomizer
    while len(password) < length:
        ascii_number = randint(33, 126)

        if chr(ascii_number).isupper() and upper_chars > 0:
            upper_chars -= 1
            password += chr(ascii_number)
        elif chr(ascii_number).isdigit() and number_chars > 0:
            number_chars -= 1
            password += chr(ascii_number)
        elif special_chars > 0:
            special_chars -= 1
            password += chr(ascii_number)
        elif chr(ascii_number).isalpha() and chr(ascii_number).islower():
            password += chr(ascii_number)

    # Check correctness of the password
    if upper_chars == 0 and number_chars == 0 and special_chars == 0 and len(password) >= length:
        break
    else:
        upper_chars, number_chars, special_chars = temp_input_values_list
        continue

# Return result
print(password)
