def chyper(password, menssage):
    cip = []
    print('Working on the chyper...')
    for i, m in enumerate(menssage):
        order = ord(password[i%len(password)]) - zero_value
        new_char = zero_value + (ord(m) - zero_value + order) % 26
        print('%s -> %s' % (m, chr(new_char)))
        cip.append(chr(new_char))

    return ''.join(cip)

def decoder(new_massage, password):
    cip = []
    print('Decoding message...')
    for i, m in enumerate(new_massage):
        order = ord(password[i%len(password)]) - zero_value
        new_char = zero_value + (ord(m) - zero_value + (26 - order)) % 26
        print('%s -> %s' % (m, chr(new_char)))
        cip.append(chr(new_char))

    return ''.join(cip)

password = input('Enter the chose password for the cypher: ')
menssage = input('Please enter your menssage: ')
# valor inicial sendo o valor tabela ascii da letra A
# sendo utilizado como 0 para os shifts futuros
zero_value = ord('A')
password = password.upper()
menssage = menssage.upper()
print('Using %s as Key' % password)
new_massage = chyper(password, menssage)
decoded_mesasge = decoder(new_massage, password)
print('Plan menssage: %s' % menssage)
print('Encoded menssage: %s' % new_massage)
print('Decoded message: %s' % decoded_mesasge)

