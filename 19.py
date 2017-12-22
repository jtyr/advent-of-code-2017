#!/usr/bin/python2

"""
--- Day 19: A Series of Tubes ---

Somehow, a network packet got lost and ended up here. It's trying to
follow a routing diagram (your puzzle input), but it's confused about
where to go.

Its starting point is just off the top of the diagram. Lines (drawn with
|, -, and +) show the path it needs to take, starting by going down onto
the only line connected to the top of the diagram. It needs to follow
this path until it reaches the end (located somewhere within the diagram)
and stop there.

Sometimes, the lines cross over each other; in these cases, it needs to
continue going the same direction, and only turn left or right when
there's no other option. In addition, someone has left letters on the
line; these also don't change its direction, but it can use them to keep
track of where it's been. For example:

     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+

Given this diagram, the packet needs to take the following path:

- Starting at the only line touching the top of the diagram, it must go
  down, pass through A, and continue onward to the first +.
- Travel right, up, and right, passing through B in the process.
- Continue down (collecting C), right, and up (collecting D).
- Finally, go all the way left through E and stopping at F.

Following the path to the end, the letters it sees on its path are
ABCDEF.

The little packet looks up at you, hoping you can help it find the way.
What letters will it see (in the order it would see them) if it follows
the path? (The routing diagram is very wide; make sure you view it
without line wrapping.)

--- Part Two ---

The packet is curious how many steps it needs to go.

For example, using the same routing diagram from the example above...

     |
     |  +--+
     A  |  C
 F---|--|-E---+
     |  |  |  D
     +B-+  +--+

...the packet would go:

- 6 steps down (including the first line at the top of the diagram).
- 3 steps right.
- 4 steps up.
- 3 steps right.
- 4 steps down.
- 3 steps right.
- 2 steps up.
- 13 steps left (including the F it stops on).

This would result in a total of 38 steps.

How many steps does the packet need to go?
"""


import sys


def get_data(name):
    f = open(name, 'r')

    return f.readlines()


def find_next(data, x, y, direction, path):
    ch = data[y][x]
    row_len = len(data[0])
    col_len = len(data)
    letters = map(chr, range(65, 91))
    mix = letters + ['|', '-']

    if ch == '|':
        if direction == 'down' and y + 1 < col_len:
            y += 1
        elif direction == 'up' and y - 1 >= 0:
            y -= 1
        elif direction == 'right':
            x += 1
        elif direction == 'left':
            x -= 1
    elif ch == '-':
        if direction == 'up':
            y -= 1
        elif direction == 'down':
            y += 1
        elif direction == 'right' and x + 1 < row_len:
            x += 1
        elif direction == 'left' and x - 1 >= 0:
            x -= 1
    elif ch in letters:
        path.append(ch)

        if direction == 'down' and y + 1 < col_len:
            y += 1
        elif direction == 'up' and y - 1 >= 0:
            y -= 1
        elif direction == 'right' and x + 1 < row_len:
            x += 1
        elif direction == 'left' and x - 1 >= 0:
            x -= 1
    elif ch == '+':
        if (
                direction not in ['up', 'down'] and
                y + 1 < col_len and
                data[y+1][x] in mix):
            y += 1
            direction = 'down'
        elif (
                direction not in ['up', 'down'] and
                y - 1 >= 0 and
                data[y-1][x] in mix):
            y -= 1
            direction = 'up'
        elif (
                direction not in ['left', 'right'] and
                x + 1 < row_len and
                data[y][x+1] in mix):
            x += 1
            direction = 'right'
        elif (
                direction not in ['left', 'right'] and
                x - 1 >= 0 and
                data[y][x-1] in mix):
            x -= 1
            direction = 'left'

    return x, y, direction


def main():
    if len(sys.argv) < 2:
        print("Usage: %s <input_file>" % sys.argv[0])

        sys.exit(1)

    data = get_data(sys.argv[1])

    x = data[0].index('|')
    y = 0
    direction = 'down'
    path = []
    cnt = 0

    while True:
        x_next, y_next, direction = find_next(data, x, y, direction, path)

        if x == x_next and y == y_next:
            break

        x = x_next
        y = y_next
        cnt += 1

    print("[Star 1] Path: %s" % ''.join(path))
    print("[Star 2] Steps: %d" % cnt)


if __name__ == '__main__':
    main()
