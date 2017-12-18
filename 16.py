#!/usr/bin/python2

"""
--- Day 16: Permutation Promenade ---

You come upon a very unusual sight; a group of programs here appear to be
dancing.

There are sixteen programs in total, named a through p. They start by
standing in a line: a stands in position 0, b stands in position 1, and
so on until p, which stands in position 15.

The programs' dance consists of a sequence of dance moves:

- Spin, written sX, makes X programs move from the end to the front, but
  maintain their order otherwise. (For example, s3 on abcde produces
  cdeab).
- Exchange, written xA/B, makes the programs at positions A and B swap
  places.
- Partner, written pA/B, makes the programs named A and B swap places.

For example, with only five programs standing in a line (abcde), they
could do the following dance:

- s1, a spin of size 1: eabcd.
- x3/4, swapping the last two programs: eabdc.
- pe/b, swapping programs e and b: baedc.

After finishing their dance, the programs end up in order baedc.

You watch the dance for a while and record their dance moves (your puzzle
input). In what order are the programs standing after their dance?

--- Part Two ---

Now that you're starting to get a feel for the dance moves, you turn your
attention to the dance as a whole.

Keeping the positions they ended up in from their previous dance, the
programs perform it again and again: including the first dance, a total
of one billion (1000000000) times.

In the example above, their second dance would begin with the order
baedc, and use the same dance moves:

- s1, a spin of size 1: cbaed.
- x3/4, swapping the last two programs: cbade.
- pe/b, swapping programs e and b: ceadb.

In what order are the programs standing after their billion dances?
"""


import sys


def get_data(name):
    f = open(name, 'r')

    return f.read()


def dance(data, s):
    for move in data:
        if move[0] == 's':
            spin = int(move[1:])

            s = s[-spin:] + s[:-spin]
        elif move[0] == 'x':
            pos1, pos2 = map(int, move[1:].split('/'))

            tmp = s[pos1]
            s[pos1] = s[pos2]
            s[pos2] = tmp
        elif move[0] == 'p':
            swap1, swap2 = move[1:].split('/')

            pos1 = s.index(swap1)
            pos2 = s.index(swap2)

            tmp = s[pos1]
            s[pos1] = s[pos2]
            s[pos2] = tmp

    return s


def main():
    if len(sys.argv) < 2:
        print("Usage: %s <input_file>" % sys.argv[0])

        sys.exit(1)

    data = get_data(sys.argv[1]).strip().split(',')

    if 'test' in sys.argv[1]:
        s = list('abcde')
    else:
        s = map(chr, range(ord('a'), ord('q')))

    s_orig = list(s)
    s0 = ''
    n = 0

    while True:
        s = dance(data, s)

        if n == 0:
            s0 = ''.join(s)

        n += 1

        if s_orig == s:
            break

    x = 1000000000 % n

    while x > 0:
        s = dance(data, s)
        x -= 1

    print("[Star 1] Programs after first dance: %s" % s0)
    print("[Star 2] Programs after billion of dances: %s" % ''.join(s))


if __name__ == '__main__':
    main()
