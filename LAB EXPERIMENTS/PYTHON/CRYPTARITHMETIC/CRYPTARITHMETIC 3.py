
from itertools import permutations

# Cryptarithmetic: ONE + ONE + ONE + ONE = TEN

letters = 'ONET'

for p in permutations(range(10), 4):

    v = dict(zip(letters, p))

    # O and T cannot be zero
    if v['O'] == 0 or v['T'] == 0:
        continue

    ONE = (v['O'] * 100 +
           v['N'] * 10 +
           v['E'])

    TEN = (v['T'] * 100 +
           v['E'] * 10 +
           v['N'])

    if ONE + ONE + ONE + ONE == TEN:

        print("Solution Found:")

        for letter in letters:
            print(letter, "=", v[letter])

        print("\nONE =", ONE)
        print("TEN =", TEN)

        print(ONE, "+", ONE, "+",
              ONE, "+", ONE, "=", TEN)
        break
