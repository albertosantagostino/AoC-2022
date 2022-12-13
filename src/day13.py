#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import cmp_to_key

from common.meta_utils import get_puzzle_input


def part1(puzzle_input):
    total = 0
    for idx, (packet1, packet2) in enumerate(zip(*[iter(puzzle_input)] * 2)):
        if compare_elements(packet1, packet2) == 1:
            total += idx + 1
    return total


def part2(puzzle_input):
    puzzle_input += [[[2]], [[6]]]
    puzzle_input = sorted(puzzle_input, key=cmp_to_key(compare_elements), reverse=True)
    return (puzzle_input.index([[2]]) + 1) * (puzzle_input.index([[6]]) + 1)


def compare_elements(packet1, packet2):
    # Check types
    if isinstance(packet1, int) and isinstance(packet2, int):
        return 1 if packet1 <= packet2 else -1
    elif isinstance(packet1, int):
        packet1 = [packet1]
    elif isinstance(packet2, int):
        packet2 = [packet2]
    # Handle case in which the packets are identical
    if packet1 == packet2:
        return 0
    # Iterate over packets as lists
    for idx in range(0, max(len(packet1), len(packet2))):
        try:
            p1_el = packet1[idx]
        except IndexError:
            return 1
        try:
            p2_el = packet2[idx]
        except IndexError:
            return -1
        if p1_el != p2_el:
            return compare_elements(p1_el, p2_el)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    puzzle_input = [eval(line) for line in puzzle_input if line]
    print(f"Part 1 solution: {part1(puzzle_input)}")
    print(f"Part 2 solution: {part2(puzzle_input)}")
