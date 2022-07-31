def encoder(message, password):
    cip = []
    print('Working on the chyper...')
    for i, m in enumerate(message):
        order = ord(password[i%len(password)]) - zero_value
        new_char = zero_value + (ord(m) - zero_value + order) % 26
        print('%s -> %s' % (m, chr(new_char)))
        cip.append(chr(new_char))

    return ''.join(cip)

def decoder(new_message, password):
    dec = []
    print('Decoding message...')
    for i, m in enumerate(new_message):
        order = ord(password[i%len(password)]) - zero_value
        new_char = zero_value + (ord(m) - zero_value + (26 - order)) % 26
        print('%s -> %s' % (m, chr(new_char)))
        dec.append(chr(new_char))

    return ''.join(dec)

def test_vigenere(text, key):
    ciphertext = encoder(text, key)
    plaintext = decoder(ciphertext, key)

    assert plaintext == text , "{!r} -> {!r} -> {!r} (a {} = 0)".format(text, ciphertext, plaintext, "!")

password = input('Enter the chose password for the cypher: ')
message = input('Please enter your message: ')
# valor inicial sendo o valor tabela ascii da letra A
# sendo utilizado como 0 para os shifts futuros
zero_value = ord('A')
password = password.upper()
message = message.upper()
print('Using %s as Key' % password)
new_message = encoder(message, password)
decoded_mesasge = decoder(new_message, password)
print('Plan message: %s' % message)
print('Encoded menssage: %s' % new_message)
print('Decoded message: %s' % decoded_mesasge)
print(test_vigenere(message, password))

