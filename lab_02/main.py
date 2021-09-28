"""
Created on Wed 22 Sep 18:00

@author: Sergeev David Evgenievich
Group: IVT-41-18
"""

"""
Вариант: 13 mod 10 = 3
V = {A..Z,a..z} (алфавит)
m = 18 (длина блока шифрограммы)
"""
ALPHABET = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
    'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

ALPHABET_STRAIGHT = {
    0: 17, 1: 16, 2: 15, 3: 14, 4: 13, 5: 12, 6: 11, 7: 10, 8: 9, 9: 8,
    10: 7, 11: 6, 12: 5, 13: 4, 14: 3, 15: 2, 16: 1, 17: 0
}

ALPHABET_REVERSE = {
    17: 0, 16: 1, 15: 2, 14: 3, 13: 4, 12: 5, 11: 6, 10: 7, 9: 8, 8: 9,
    7: 10, 6: 11, 5: 12, 4: 13, 3: 14, 2: 15, 1: 16, 0: 17
}


CIPHER_MSG_BLOCK_SIZE = 18
SPACE_REPLACEMENT = '_'


def checker(msg: str) -> None or ValueError:
    if not set(msg).issubset(set(ALPHABET)):
        difference = set(msg) - set(ALPHABET)
        raise ValueError(f'Symbol not in alphabet: {difference}')


def input_data_handling() -> list:
    input_data_handling.message = input("Введите сообщение: ")
    message = input_data_handling.message

    global ALPHABET, ALPHABET_REVERSE, ALPHABET_STRAIGHT
    ALPHABET.append(SPACE_REPLACEMENT)  # space -> '_'
    message.replace(' ', SPACE_REPLACEMENT)

    msg_blocks = []
    word = ''
    msg_len = 0
    for idx in range(len(message)):
        if message[idx] != ' ':
            word += message[idx]
        else:
            word += SPACE_REPLACEMENT
        msg_len += 1

        if idx == len(message) - 1 and len(word) != CIPHER_MSG_BLOCK_SIZE or len(word) == CIPHER_MSG_BLOCK_SIZE:
            len_delta = CIPHER_MSG_BLOCK_SIZE - len(word)
            for x in range(len_delta):
                word += SPACE_REPLACEMENT
            checker(word)
            msg_blocks.append(word)
            word = ''
            msg_len = 0
    return msg_blocks


def cipher(msg: str, encrypted=True):
    if encrypted:
        return encrypt(msg)
    else:
        return decrypt(msg)


def encrypt(msg: str):
    encrypted = '*' * CIPHER_MSG_BLOCK_SIZE

    for idx in range(len(msg)):
        encryption_idx: int = ALPHABET_STRAIGHT[idx]
        encrypted = encrypted[:encryption_idx] + msg[idx] + encrypted[encryption_idx+1:]
    return encrypted


def decrypt(msg: str):
    decrypted = '*' * CIPHER_MSG_BLOCK_SIZE

    for idx in range(len(msg)):
        decryption_idx = ALPHABET_REVERSE[idx]
        if msg[idx] != '_':
            decrypted = decrypted[:decryption_idx] + msg[idx] + decrypted[decryption_idx+1:]
        else:
            decrypted = decrypted[:decryption_idx] + ' ' + decrypted[decryption_idx + 1:]
    return decrypted


def main():
    msg_blocks = input_data_handling()
    encrypted = [cipher(el, encrypted=True) for el in msg_blocks]
    decrypted = [cipher(el, encrypted=False) for el in encrypted]
    print(f'encrypted: {encrypted}')
    print(f'decrypted: {decrypted}')


if __name__ == '__main__':
    main()