import itertools
import string
from time import sleep
from itertools import islice

ENGLISH_FREQUENCY_WORNG = (0.0749, 0.0129, 0.0354, 0.0362, 0.1400, 0.0218, 0.0174, 0.0422, 0.0665, 0.0027, 0.0047,
                0.0357, 0.0339, 0.0674, 0.0737, 0.0243, 0.0026, 0.0614, 0.0695, 0.0985, 0.0300, 0.0116,
                0.0169, 0.0028, 0.0164, 0.0004)

ENGLISH_FREQUENCY = (0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025,
                0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074)

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

def cypher_vigenere(message, password, a_is_zero=True):
    message = message.lower()
    count = itertools.cycle(map(ord, password))
    return "".join(
        chr(ord('a') + (
            (next(count) - ord('a') + ord(letter) - ord('a'))
            + (0 if a_is_zero else 2)
            ) % 26) if letter in string.ascii_lowercase
        else letter
        for letter in message.lower()
    )

def decoder_vigenere(new_message, password, a_is_zero=True):
    inverse = "".join(chr(ord('a') +
        ((26 if a_is_zero else 22) - 
            (ord(x) - ord('a'))
        ) % 26) for x in password)
    
    return cypher_vigenere(new_message, inverse, a_is_zero)


def test_vigenere(text, key, a_is_zero=True):
    ciphertext = cypher_vigenere(text, key,a_is_zero)
    plaintext = decoder_vigenere(ciphertext, key,a_is_zero)

    assert plaintext == text
    return "{!r} -> {!r} -> {!r}".format(text, ciphertext, plaintext, "" if a_is_zero else "!")

def compare_frequency(text):

    text = [t for t in text.lower()]
    freq = [0] * 26
    total = float(len(text))
    for letter in text:
        freq[ord(letter) - ord('a')] +=1
    return sum(abs(foo / total - E) for foo, E in zip(freq, ENGLISH_FREQUENCY))


def cracking_vigenere(text, password_min_size=None, password_max_size=None):
    best_passwords = []
    password_min_size = password_min_size or 1
    password_max_size = password_max_size or len(text) +1

    text_letters = [t for t in text.lower()]

    for password_length in range(password_min_size, password_max_size):
        password = [None] * password_length
        for password_index in range(password_length):
            #letters = "".join(islice(text_letters, password_index, password_length+password_index))
            letters = "".join(text_letters[slice(0, password_index+1)])
            rotator = []
            for password_char in string.ascii_lowercase:
                rotator.append(
                    (compare_frequency(decoder_vigenere(letters, password_char, True)), password_char)
                )
            print(letters)
            password[password_index] = min(rotator, key=lambda x: x[0])[1]
        best_passwords.append("".join(password))
    best_passwords.sort(key=lambda password: compare_frequency(decoder_vigenere(text,password, True)))
    return best_passwords[:2]


message = input('Please enter your message: ')
cypherkey = input('Please input chyper key: ')
# valor inicial sendo o valor tabela ascii da letra A
# sendo utilizado como 0 para os shifts futuros

print(test_vigenere(message, cypherkey, True))
print(test_vigenere(message, cypherkey, False))
new_message = cypher_vigenere(message, cypherkey, True)
for password in reversed(cracking_vigenere(new_message)):
    print("Found password: {!r}".format(password))
    print("*" * 80) 
    print('Solution: ')
    print(decoder_vigenere(new_message, password))
    print("*" * 80) 

sleep(500)

