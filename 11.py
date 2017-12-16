#!/usr/bin/python2

"""
--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream
when a program comes up to you, clearly in distress. "It's my child
process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes
can be found to the north, northeast, southeast, south, southwest, and
northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \

You have the path the child process took. Starting where he started, you
need to determine the fewest number of steps required to reach him. (A
"step" means to move from the hex you are in to any adjacent hex.)

For example:

- ne,ne,ne is 3 steps away.
- ne,ne,sw,sw is 0 steps away (back where you started).
- ne,ne,s,s is 2 steps away (se,se).
- se,sw,se,sw,sw is 3 steps away (s,s,sw).

--- Part Two ---

How many steps away is the furthest he ever got from his starting
position?
"""


import sys


def get_data(name):
    f = open(name, 'r')

    return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: %s <input_file>" % sys.argv[0])

        sys.exit(1)

    data = get_data(sys.argv[1]).rstrip()

    dirs = data.split(',')
    x = 0
    y = 0
    cur_dist = 0
    max_dist = 0

    for d in dirs:
        if d == 'n':
            y += 1
        elif d == 'ne':
            x += 1
        elif d == 'se':
            x += 1
            y -= 1
        elif d == 's':
            y -= 1
        elif d == 'sw':
            x -= 1
        elif d == 'nw':
            x -= 1
            y += 1

        cur_dist = max([x, y, (x+y) * -1])

        if cur_dist > max_dist:
            max_dist = cur_dist

    print("[Star 1] Distance: %s" % cur_dist)
    print("[Star 2] Max distance: %s" % max_dist)


if __name__ == '__main__':
    main()
