
from itertools import permutations

# Cryptarithmetic: SEND + MORE = MONEY

letters = 'SENDMORY'

digits = range(10)

for p in permutations(digits, len(letters)):

    values = dict(zip(letters, p))

    # S and M cannot be zero
    if values['S'] == 0 or values['M'] == 0:
        continue

    SEND = (values['S'] * 1000 +
            values['E'] * 100 +
            values['N'] * 10 +
            values['D'])

    MORE = (values['M'] * 1000 +
            values['O'] * 100 +
            values['R'] * 10 +
            values['E'])

    MONEY = (values['M'] * 10000 +
             values['O'] * 1000 +
             values['N'] * 100 +
             values['E'] * 10 +
             values['Y'])

    if SEND + MORE == MONEY:
        print("Solution Found:")
        for letter in letters:
            print(letter, "=", values[letter])

        print("\nSEND =", SEND)
        print("MORE =", MORE)
        print("MONEY =", MONEY)
        print(SEND, "+", MORE, "=", MONEY)
        break
