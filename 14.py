#!/usr/bin/python2

"""
--- Day 14: Disk Defragmentation ---

Suddenly, a scheduled job activates the system's disk defragmenter. Were
the situation different, you might sit and watch it for a while, but
today, you just don't have that kind of time. It's soaking up valuable
system resources that are needed elsewhere, and so the only option is to
help it finish its task as soon as possible.

The disk in question consists of a 128x128 grid; each square of the grid
is either free or used. On this disk, the state of the grid is tracked by
the bits in a sequence of knot hashes.

A total of 128 knot hashes are calculated, each corresponding to a single
row in the grid; each hash contains 128 bits which correspond to
individual grid squares. Each bit of a hash indicates whether that square
is free (0) or used (1).

The hash inputs are a key string (your puzzle input), a dash, and a
number from 0 to 127 corresponding to the row. For example, if your key
string were flqrgnkx, then the first row would be given by the bits of
the knot hash of flqrgnkx-0, the second row from the bits of the knot
hash of flqrgnkx-1, and so on until the last row, flqrgnkx-127.

The output of a knot hash is traditionally represented by 32 hexadecimal
digits; each of these digits correspond to 4 bits, for a total of 4 * 32
= 128 bits. To convert to bits, turn each hexadecimal digit to its
equivalent binary value, high-bit first: 0 becomes 0000, 1 becomes 0001,
e becomes 1110, f becomes 1111, and so on; a hash that begins with
a0c2017... in hexadecimal would begin with
10100000110000100000000101110000... in binary.

Continuing this process, the first 8 rows and columns for key flqrgnkx
appear as follows, using # to denote used squares, and . to denote free
ones:

##.#.#..-->
.#.#.#.#
....#.#.
#.#.##.#
.##.#...
##..#..#
.#...#..
##.#.##.-->
|      |
V      V

In this example, 8108 squares are used across the entire 128x128 grid.

Given your actual key string, how many squares are used?

--- Part Two ---

Now, all the defragmenter needs to know is the number of regions. A
region is a group of used squares that are all adjacent, not including
diagonals. Every used square is in exactly one region: lone used squares
form their own isolated regions, while several adjacent squares all count
as a single region.

In the example above, the following nine regions are visible, each marked
with a distinct digit:

11.2.3..-->
.1.2.3.4
....5.6.
7.8.55.9
.88.5...
88..5..8
.8...8..
88.8.88.-->
|      |
V      V

Of particular interest is the region marked 8; while it does not appear
contiguous in this small view, all of the squares marked 8 are connected
when considering the whole 128x128 grid. In total, in this example, 1242
regions are present.

How many regions are present given your key string?
"""


import sys


def get_data(name):
    f = open(name, 'r')

    return f.read()


def knot_hash(data):
    lengths = map(ord, data) + [17, 31, 73, 47, 23]
    num_length = 256
    nums = range(num_length)
    pos = 0
    skip = 0
    dense_hash = ''

    for n in range(64):
        for l in lengths:
            if pos + l > num_length - 1:
                selection = nums[pos:] + nums[:pos + l - num_length]
            else:
                selection = nums[pos:pos + l]

            for i in range(pos, pos + l):
                nums[i % num_length] = selection.pop()

            pos = (pos + l + skip) % num_length
            skip += 1

    for n in range(num_length / 16):
        xor = reduce(lambda i, j: int(i) ^ int(j), nums[n*16:n*16+16])
        dense_hash += ("%x" % xor).zfill(2)

    return dense_hash


def search_grid(rows, x, y, checked, reg, level):
    reg.append((x, y))

    if (
            x > 0 and
            (x-1, y) not in reg and
            (x-1, y) not in checked and
            rows[x-1][y] == '1'):
        search_grid(rows, x-1, y, checked, reg, level+1)

    if (
            x < 127 and
            (x+1, y) not in reg and
            (x+1, y) not in checked and
            rows[x+1][y] == '1'):
        search_grid(rows, x+1, y, checked, reg, level+1)

    if (
            y > 0 and
            (x, y-1) not in reg and
            (x, y-1) not in checked and
            rows[x][y-1] == '1'):
        search_grid(rows, x, y-1, checked, reg, level+1)

    if (
            y < 127 and
            (x, y+1) not in reg and
            (x, y+1) not in checked and
            rows[x][y+1] == '1'):
        search_grid(rows, x, y+1, checked, reg, level+1)


def main():
    if len(sys.argv) < 2:
        print("Usage: %s <input_file>" % sys.argv[0])

        sys.exit(1)

    data = get_data(sys.argv[1]).rstrip()
    size = 128
    used = 0
    rows = []
    checked = []
    regs = 0

    for n in range(size):
        s = "%s-%d" % (data, n)
        kh = knot_hash(s)
        b = bin(int(kh, 16))[2:].zfill(128)
        rows.append(b)

        used += len(b.replace('0', ''))

    for x in range(size):
        for y in range(size):
            if rows[x][y] == '1' and (x, y) not in checked:
                reg = []
                search_grid(rows, x, y, checked, reg, 0)
                checked += reg
                regs += 1

    print("[Star 1] Used squares: %d" % used)
    print("[Star 2] Regions: %s" % regs)


if __name__ == '__main__':
    main()
