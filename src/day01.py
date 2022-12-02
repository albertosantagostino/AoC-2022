#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

from common.meta_utils import get_puzzle_input


def part1(calories_list):
    elf_calories = list(map(sum, calories_list))
    return max(elf_calories)


def part2(calories_list):
    elf_calories = list(map(sum, calories_list))
    elf_calories.sort()
    return sum(elf_calories[-3:])


def parse_input(puzzle_input):
    puzzle_input = [int(el) if el.isnumeric() else 'X' for el in puzzle_input]
    return [list(y) for x, y in itertools.groupby(puzzle_input, lambda val: val == 'X') if not x]


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    calories_list = parse_input(puzzle_input)
    print(f"Part 1 solution: {part1(calories_list)}")
    print(f"Part 2 solution: {part2(calories_list)}")
