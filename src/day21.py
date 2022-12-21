#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

from copy import deepcopy
from sympy import solve, sympify

from common.meta_utils import get_puzzle_input

words_match = re.compile(r'[^\d\W]+')

def part1(monkeys):
    # Recursively replace monkey names with values until only numbers are present
    while True:
        root_ops = monkeys['root']
        if not any(ch.isalpha() for ch in root_ops):
            break
        words = [el for el in re.findall(words_match, root_ops)]
        for word in words:
            monkeys['root'] = root_ops.replace(word, '(' + monkeys[word] + ')')
    return int(eval(root_ops))


def part2(monkeys):
    root_ops = [el for el in re.findall(words_match, monkeys['root'])]
    # Prepare comparison for sympy.solve(), use the same technique of part1 for the replacement
    root_comparison = f'{root_ops[0]} - {root_ops[1]}, 0'
    monkeys['humn'] = 'humn'
    while True:
        if not any(ch.isalpha() for ch in root_comparison.replace('humn', '')):
            break
        words = [el for el in re.findall(words_match, root_comparison)]
        for word in words:
            if word != 'humn':
                root_comparison = root_comparison.replace(word, '(' + monkeys[word] + ')')
    sympy_res = solve(sympify("Eq(" + root_comparison + ")"))
    return sympy_res[0]


def parse_input(puzzle_input):
    monkeys = {}
    for line in puzzle_input:
        curr, op = line.split(':')
        monkeys[curr.strip()] = op.strip()
    return monkeys


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    monkeys = parse_input(puzzle_input)
    print(f"Part 1 solution: {part1(deepcopy(monkeys))}")
    print(f"Part 2 solution: {part2(deepcopy(monkeys))}")
