"""
Created on Wed 23 Sep 20:43

@author: Sergeev David Evgenievich
Group: IVT-41-18
"""

"""
Вариант: 13 mod 10 = 3
A    =  13
B    = 161
C    =  43
T(0) =  37
"""

A = 13
B = 161
C = 43
T_0 = 37

STD_INPUT = 'Эту глупую улыбку он не мог простить себе. Увидав эту улыбку, Долли вздрогнула, как от ' \
            'физической боли, разразилась, со свойственною ей горячностью, потоком жестоких слов и ' \
            'выбежала из комнаты. С тех пор она не хотела видеть мужа.'  # Анна Каренина
ALPHABET = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c',
    'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П',
    'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г',
    'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
    'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+',
    ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}',
    '~'
]
ALPHABET_LEN = len(ALPHABET)


def alphabet_msg_sequence(msg: str) -> list:
    # msg -> list of char positions in alphabet
    alphabet_pos_sequence = []
    for char in msg:
        alphabet_pos_sequence.append(ALPHABET.index(char))
    return alphabet_pos_sequence


def pseudorandom_number_generator(msg_len: int) -> list:
    # pseudorandom number generator for gamma
    gamma = [T_0]
    for idx in range(1, msg_len):
        # t(i+1) = (A * t(i) + C) mod B
        num = (A * gamma[idx - 1] + C) % B
        gamma.append(num)
    return gamma


def gamma_to_str(gamma: list) -> str:
    gamma_ = ''
    for idx in gamma:
        gamma_ += ALPHABET[idx]
    return gamma_


def encode(msg_pos_sequence: list, gamma: list):
    encoded_str = ''
    encoded_list = []
    for idx in range(len(gamma)):
        value = (msg_pos_sequence[idx] + gamma[idx]) % ALPHABET_LEN
        encoded_list.append(value)
    for idx in encoded_list:
        encoded_str += ALPHABET[idx]

    return [encoded_str, encoded_list]


def decode(encoded_str: str, gamma: list):
    decoded_str = ''
    decoded_list = []
    for idx in range(len(gamma)):
        value = ALPHABET.index(encoded_str[idx]) - gamma[idx]
        if value < 0:
            value += ALPHABET_LEN
        decoded_list.append(value)
    for idx in decoded_list:
        decoded_str += ALPHABET[idx]

    return [decoded_str, decoded_list]


def main():
    msg = input()
    print(f'\n\nMessage: {msg}')
    # Перевод сообщения в список позиций символов алфавита
    msg_alphabet_pos_sequence = alphabet_msg_sequence(msg)
    print(f'msg_alphabet_pos_sequence: {msg_alphabet_pos_sequence}')
    # Генерация псевдослучайной гаммы длиной сообщения msg
    gamma = pseudorandom_number_generator(len(msg))
    gamma_str = gamma_to_str(gamma)
    print(f'\nGamma: {gamma_str}')
    # Шифрование строки
    encoded_str, encoded_list = encode(msg_alphabet_pos_sequence, gamma)
    print(f'\nencoded: {encoded_str}')
    print(f'encoded: {encoded_list}\n')
    # Дешифрование строки
    decoded_str, decoded_list = decode(encoded_str, gamma)
    print(f'decoded: {decoded_str}')
    print(f'decoded: {decoded_list}\n')

if __name__ == '__main__':
    main()
