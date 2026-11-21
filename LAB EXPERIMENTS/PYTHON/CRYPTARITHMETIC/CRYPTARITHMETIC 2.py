
from itertools import permutations

# Cryptarithmetic: ABCD + EBCB = AFGAG

letters = 'ABCDEFG'

for p in permutations(range(10), 7):

    v = dict(zip(letters, p))

    # First digits cannot be zero
    if v['A'] == 0 or v['E'] == 0:
        continue

    ABCD = (v['A']*1000 + v['B']*100 +
            v['C']*10 + v['D'])

    EBCB = (v['E']*1000 + v['B']*100 +
            v['C']*10 + v['B'])

    AFGAG = (v['A']*10000 + v['F']*1000 +
             v['G']*100 + v['A']*10 + v['G'])

    if ABCD + EBCB == AFGAG:

        print("Solution Found:")

        for letter in letters:
            print(letter, "=", v[letter])

        print("\nABCD =", ABCD)
        print("EBCB =", EBCB)
        print("AFGAG =", AFGAG)

        print(ABCD, "+", EBCB, "=", AFGAG)
        break
