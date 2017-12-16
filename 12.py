#!/usr/bin/python2

"""
--- Day 12: Digital Plumber ---

Walking along the memory banks of the stream, you find a small village
that is experiencing a little confusion: some programs can't communicate
with each other.

Programs in this village communicate using a fixed system of pipes.
Messages are passed between programs using these pipes, but most programs
aren't connected to each other directly. Instead, programs pass messages
between each other until the message reaches the intended recipient.

For some reason, though, some of these messages aren't ever reaching
their intended recipient, and the programs suspect that some pipes are
missing. They would like you to investigate.

You walk through the village and record the ID of each program and the
IDs with which it can communicate directly (your puzzle input). Each
program has one or more programs with which it can communicate, and these
pipes are bidirectional; if 8 says it can communicate with 11, then 11
will say it can communicate with 8.

You need to figure out how many programs are in the group that contains
program ID 0.

For example, suppose you go door-to-door like a travelling salesman and
record the following list:

0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5

In this example, the following programs are in the group that contains
program ID 0:

- Program 0 by definition.
- Program 2, directly connected to program 0.
- Program 3 via program 2.
- Program 4 via program 2.
- Program 5 via programs 6, then 4, then 2.
- Program 6 via programs 4, then 2.

Therefore, a total of 6 programs are in this group; all but program 1,
which has a pipe that connects it to itself.

How many programs are in the group that contains program ID 0?

--- Part Two ---

There are more programs than just the ones in the group containing
program ID 0. The rest of them have no way of reaching that group, and
still might have no way of reaching each other.

A group is a collection of programs that can all communicate via pipes
either directly or indirectly. The programs you identified just a moment
ago are all part of the same group. Now, they would like you to determine
the total number of groups.

In the example above, there were 2 groups: one consisting of programs
0,2,3,4,5,6, and the other consisting solely of program 1.

How many groups are there in total?
"""


import sys


def get_data(name):
    f = open(name, 'r')

    return f.readlines()


def find_path(struct, id, search, path, group):
    ret = False

    if search in struct[id]:
        ret = True
    else:
        for c in struct[id]:
            if c != id and c not in path:
                ret = find_path(struct, c, search, [c] + path, group)

                if ret:
                    break

    if ret and id not in group:
        group.append(id)

    return ret


def main():
    if len(sys.argv) < 2:
        print("Usage: %s <input_file>" % sys.argv[0])

        sys.exit(1)

    data = get_data(sys.argv[1])
    struct = {}

    for line in data:
        id, tmp = line.split('<->')
        children = map(int, tmp.split(','))
        id = int(id)

        struct[id] = children

        for c in children:
            if c not in struct:
                struct[c] = []

    search = 0
    groups1 = 0
    groups2 = []

    for search in struct.keys():
        group = [search]

        for id, children in struct.items():
            if id != search and id not in groups2:
                find_path(struct, id, search, [], group)

                if search == 0:
                    groups1 = len(group)

        if sorted(group) not in groups2:
            groups2.append(sorted(group))

    print("[Star 1] Number of groups reaching 0: %s" % groups1)
    print("[Star 2] Number of groups: %s" % len(groups2))


if __name__ == '__main__':
    main()
