"""
Created on Fri 10 Sep 15:57

@author: Sergeev David Evgenievich
Group: IVT-41-18
"""

"""
Вариант: 13 mod 10 = 3
V = {0,1,2,3,4} (алфавит)
m = 2 (длина блока шифрограммы) 
|V| = 5
|V|^m = 25
"""

from random import choice
from string import ascii_lowercase

ALPHABET = ['0', '1', '2', '3', '4']
ALPHABET_STRAIGHT = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e'}
ALPHABET_REVERSE = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4'}
CIPHER_MSG_BLOCK_SIZE = 2
CIPHER_KEY = ''


def vernam_cipher(message, key, encrypt):
    result = ""
    for i in range(len(message)):
        char = message[i]
        if encrypt:
            result += chr((ord(char) - 97 + ord(key[i]) - 97) % 26 + 97)
        else:
            result += chr((ord(char) - ord(key[i]) + 26) % 26 + 97)
    return result


def vernam_key_generator(msg_len: int):
    letters_choice = ascii_lowercase
    result_str = ''.join(choice(letters_choice) for _ in range(msg_len))
    return result_str


def cheker(msg: str):
    if not set(msg).issubset(set(ALPHABET)):
        raise ValueError('Symbol not in alphabet')


def number_to_new_alphabet(msg: str) -> str:
    result = ''
    for char in msg:
        result += ALPHABET_STRAIGHT[char]
    return result


def new_alphabet_to_number(msg: str) -> str:
    result = ''
    for char in msg:
        result += ALPHABET_REVERSE[char]
    return result


def input_data_handling():
    input_data_handling.message = input("Ввведите сообщение: ")
    message = input_data_handling.message

    space_replacement = '5'
    global ALPHABET, ALPHABET_REVERSE, ALPHABET_STRAIGHT
    ALPHABET.append(space_replacement)  # space -> 5
    ALPHABET_STRAIGHT.update({'5': 'f'})  # 5 -> 'f'
    ALPHABET_REVERSE.update({'f': '_'})
    message.replace(' ', space_replacement)

    global CIPHER_KEY
    CIPHER_KEY = vernam_key_generator(len(message))
    if len(message) % CIPHER_MSG_BLOCK_SIZE != 0:
        CIPHER_KEY = vernam_key_generator(len(message) + CIPHER_MSG_BLOCK_SIZE - len(message) % CIPHER_MSG_BLOCK_SIZE)

    msg_blocks = []
    word = ''
    msg_len = 0
    for idx in range(len(message)):
        if message[idx] != ' ':
            word += message[idx]
        else:
            word += space_replacement
        msg_len += 1

        if idx == len(message) - 1 and len(word) != CIPHER_MSG_BLOCK_SIZE or len(word) == CIPHER_MSG_BLOCK_SIZE:
            len_delta = CIPHER_MSG_BLOCK_SIZE - len(word)
            for x in range(len_delta):
                word += space_replacement
            cheker(word)
            msg_blocks.append(number_to_new_alphabet(word))
            word = ''
            msg_len = 0

    key_blocks = [CIPHER_KEY[idx: idx + CIPHER_MSG_BLOCK_SIZE]
                  for idx in range(0, len(CIPHER_KEY), CIPHER_MSG_BLOCK_SIZE)]

    return msg_blocks, key_blocks


def cipher(msg_blocks: list, key_blocks: list) -> str:
    msg_encrypted = []
    for idx in range(len(msg_blocks)):
        msg = msg_blocks[idx]
        key = key_blocks[idx]

        msg_processed = vernam_cipher(msg, key, True)
        msg_encrypted.append(msg_processed)

    encrypted = ''.join(str(msg) for msg in msg_encrypted)

    return encrypted


def main():
    msg_blocks, key_blocks = input_data_handling()
    encrypted = cipher(msg_blocks, key_blocks)
    decrypted = vernam_cipher(encrypted, CIPHER_KEY, False)
    decrypted_processed = new_alphabet_to_number(decrypted)

    print(f'Ключ шифра Вернама: {CIPHER_KEY}')
    print(f'Зашифрованное сообщение: {encrypted}')
    print(f'Дешифрованное сообщение: {decrypted_processed}')
    print(f'Необработанное дешифрованное сообщение: {decrypted}')

    inp: str = input_data_handling.message
    for _ in range(CIPHER_MSG_BLOCK_SIZE - len(inp) % CIPHER_MSG_BLOCK_SIZE):
        inp += '_'

    if inp != decrypted_processed:
        print(inp)
        print(decrypted_processed)
        raise RuntimeError('Зашифрованное сообщение не совпадает с пользовательским вводом!')


if __name__ == '__main__':
    main()
