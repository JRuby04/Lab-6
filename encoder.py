stored_encoded_password = ''


def encode_password(string_data):
    encoded_password = ''
    for digit in string_data:
        encoded_password += str((int(digit) + 3) % 10)

    return encoded_password


if __name__ == '__main__':
    run = True

    while run:
        print('''Menu
        -------------
        1. Encode
        2. Decode
        3. Quit''')
        user_input = int(input('Please enter an option: '))
        if user_input == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode_password(password)
            print('Your password has been encoded and stored!')
        elif user_input == 2:
#decode 'encoded_password'
        elif user_input == 3:
            run = False