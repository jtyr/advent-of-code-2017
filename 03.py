#!/usr/bin/python2

"""
--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an infinite
two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a
location marked 1 and then counting up while spiraling outward. For
example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

While this is very space-efficient (no squares are skipped), requested
data must be carried back to square 1 (the location of the only access
port for this memory system) by programs that can only move up, down,
left, or right. They always take the shortest path: the Manhattan
Distance between the location of the data and square 1.

For example:

- Data from square 1 is carried 0 steps, since it's at the access port.
- Data from square 12 is carried 3 steps, such as: down, left, left.
- Data from square 23 is carried only 2 steps: up twice.
- Data from square 1024 must be carried 31 steps.

How many steps are required to carry the data from the square identified
in your puzzle input all the way to the access port?

--- Part Two ---

As a stress test on the system, the programs here clear the grid and then
store the value 1 in square 1. Then, in the same allocation order as
shown above, they store the sum of the values in all adjacent squares,
including diagonals.

So, the first few squares' values are chosen as follows:

- Square 1 starts with the value 1.
- Square 2 has only one adjacent filled square (with value 1), so it also
  stores 1.
- Square 3 has both of the above squares as neighbors and stores the sum of
  their values, 2.
- Square 4 has all three of the aforementioned squares as neighbors and
  stores the sum of their values, 4.
- Square 5 only has the first and fourth squares as neighbors, so it gets
  the value 5.

Once a square is written, its value does not change. Therefore, the first
few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...

What is the first value written that is larger than your puzzle input?
"""


import math
import sys


def get_data(name):
    f = open(name, 'r')

    return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: %s <input_file>" % sys.argv[0])

        sys.exit(1)

    data = int(get_data(sys.argv[1]).rstrip())
    size = int(math.ceil(math.sqrt(data)))

    if size % 2 == 0:
        size += 1

    matrix = [[0 for i in range(size)] for j in range(size)]
    matrix2 = [[0 for i in range(size)] for j in range(size)]

    x0 = int(size/2)
    y0 = int(size/2)

    x = x0
    y = y0

    x_inc = 1
    y_inc = 0

    steps = 0
    first_sum = 0

    for n in range(data):
        matrix[x][y] = n + 1

        if n == 0:
            matrix2[x][y] = n+1
        elif first_sum == 0:
            s = 0

            if x+1 < size:
                s += matrix2[x+1][y]
            if x+1 < size and y+1 < size:
                s += matrix2[x+1][y+1]
            if y+1 < size:
                s += matrix2[x][y+1]
            if x-1 >= 0 and y+1 < size:
                s += matrix2[x-1][y+1]
            if x-1 >= 0:
                s += matrix2[x-1][y]
            if x-1 >= 0 and y-1 >= 0:
                s += matrix2[x-1][y-1]
            if y-1 >= 0:
                s += matrix2[x][y-1]
            if x+1 < size and y-1 >= 0:
                s += matrix2[x+1][y-1]

            matrix2[x][y] = s

            if s > data:
                first_sum = s

        steps = (x - x0 if x > x0 else x0 - x) + (y - y0 if y > y0 else y0 - y)

        x += 1 * x_inc
        y += 1 * y_inc

        if x < 0 or x >= size or y < 0 or y >= size:
            continue

        if x_inc == 1 and y+1 < size and matrix[x][y+1] == 0:
            x_inc = 0
            y_inc = 1
        elif y_inc == 1 and x-1 >= 0 and matrix[x-1][y] == 0:
            x_inc = -1
            y_inc = 0
        elif x_inc == -1 and y-1 >= 0 and matrix[x][y-1] == 0:
            x_inc = 0
            y_inc = -1
        elif y_inc == -1 and x+1 < size and matrix[x+1][y] == 0:
            x_inc = 1
            y_inc = 0

    print("[Star 1] Steps: %d" % steps)
    print("[Star 2] Sum: %d" % first_sum)


if __name__ == '__main__':
    main()
