# Decoder created by Kaiden Joy
def decode_password(string_data):
    decoded_password = ''

    for character in string_data:
        if int(character) < 3:
            decoded_password += str(7 + int(character))
        else:
            decoded_password += str(int(character) - 3)

    return decoded_password

# Essentially just a decoder
