#!/usr/bin/python2

"""
--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to
use a passphrase instead of simply a password. A passphrase consists of a
series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

- aa bb cc dd ee is valid.
- aa bb cc dd aa is not valid - the word aa appears more than once.
- aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How
many passphrases are valid?

--- Part Two ---

For added security, yet another system policy has been put in place. Now,
a valid passphrase must contain no two words that are anagrams of each
other - that is, a passphrase is invalid if any word's letters can be
rearranged to form any other word in the passphrase.

For example:

- abcde fghij is a valid passphrase.
- abcde xyz ecdab is not valid - the letters from the third word can be
  rearranged to form the first word.
- a ab abc abd abf abj is a valid passphrase, because all letters need to
  be used when forming another word.
- iiii oiii ooii oooi oooo is valid.
- oiii ioii iioi iiio is not valid - any of these words can be rearranged
  to form any other word.

Under this new system policy, how many passphrases are valid?
"""


import sys


def get_data(name):
    f = open(name, 'r')

    return f.readlines()


def main():
    if len(sys.argv) < 2:
        print("Usage: %s <input_file>" % sys.argv[0])

        sys.exit(1)

    data = get_data(sys.argv[1])
    num_valid1 = 0
    num_valid2 = 0

    for line in data:
        line = line.rstrip()

        words = line.split(' ')
        valid1 = True
        valid2 = True

        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if i != j and w1 == w2:
                    valid1 = False

                if i != j and ''.join(sorted(w1)) == ''.join(sorted(w2)):
                    valid2 = False

        if valid1:
            num_valid1 += 1

        if valid2:
            num_valid2 += 1

    print("[Star 1] Num valid: %d" % num_valid1)
    print("[Star 2] Num valid: %d" % num_valid2)


if __name__ == '__main__':
    main()
