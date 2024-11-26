import random
from data import alphabets, numbers, symbols
import os
os.system('clear')

NUM_LETTERS = random.randint(8, 10)
NUM_NUMBERS = random.randint(2,4)
NUM_SYMBOLS = random.randint(2, 4)


def password_generator():
    password = []
    char_password = ''

    password.extend([random.choice(alphabets) for x in range(NUM_LETTERS)])
    password.extend([random.choice(numbers) for y in range(NUM_NUMBERS)])
    password.extend([random.choice(symbols) for z in range(NUM_SYMBOLS)])

    random.shuffle(password)
    char_password = ''.join(password)

    return char_password
