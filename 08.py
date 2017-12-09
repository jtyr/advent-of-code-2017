#!/usr/bin/python2

"""
--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent
assistance with jump instructions, it would like you to compute the
result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify,
whether to increase or decrease that register's value, the amount by
which to increase or decrease it, and a condition. If the condition
fails, skip the instruction without modifying the register. The registers
all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10

These instructions would be processed as follows:

- Because a starts at 0, it is not greater than 1, and so b is not
  modified.
- a is increased by 1 (to 1) because b is less than 5 (it is 0).
- c is decreased by -10 (to 10) because a is now greater than or equal to
  1 (it is 1).
- c is increased by -20 (to -10) because c is equal to 10.

After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to).
However, the CPU doesn't have the bandwidth to tell you what all the
registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the
instructions in your puzzle input?

--- Part Two ---

To be safe, the CPU also needs to know the highest value held in any
register during this process so that it can decide how much memory to
allocate to these operations. For example, in the above instructions, the
highest value ever held was 10 (in register c after the third instruction
was evaluated).
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
    reg = {}
    prog = []
    max_end_value = 0
    max_value = -9999999999

    # Parse data and initiate registers
    for line in data:
        line = line.rstrip()

        inc_reg, inc_instr, inc_val, _, cond_reg, cond_op, cond_val = line.split(' ')

        if inc_reg not in reg:
            reg[inc_reg] = 0

        if cond_reg not in reg:
            reg[cond_reg] = 0

        prog.append({
            'inc_reg': inc_reg,
            'inc_instr': inc_instr,
            'inc_val': int(inc_val),
            'cond_reg': cond_reg,
            'cond_op': cond_op,
            'cond_val': int(cond_val)
        })

    # Process the program
    for line in prog:
        cond = False

        # Evaluate the condition
        if line['cond_op'] == '>':
            cond = reg[line['cond_reg']] > line['cond_val']
        elif line['cond_op'] == '<':
            cond = reg[line['cond_reg']] < line['cond_val']
        elif line['cond_op'] == '>=':
            cond = reg[line['cond_reg']] >= line['cond_val']
        elif line['cond_op'] == '<=':
            cond = reg[line['cond_reg']] <= line['cond_val']
        elif line['cond_op'] == '==':
            cond = reg[line['cond_reg']] == line['cond_val']
        elif line['cond_op'] == '!=':
            cond = reg[line['cond_reg']] != line['cond_val']

        # Increment/decrement register if the condition is True
        if cond:
            if line['inc_instr'] == 'inc':
                reg[line['inc_reg']] += line['inc_val']
            else:
                reg[line['inc_reg']] -= line['inc_val']

            if reg[line['inc_reg']] > max_value:
                max_value = reg[line['inc_reg']]

    max_end_value = max(reg.values())

    print("[Star 1] Largest end value: %s" % max_end_value)
    print("[Star 2] Largest register value: %d" % max_value)


if __name__ == '__main__':
    main()
