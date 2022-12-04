#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.meta_utils import get_puzzle_input


def solve(puzzle_input, part):
    overlapping_pairs = 0
    for pair in puzzle_input:
        elves = pair.split(',')
        elves = [xx.split('-') for xx in elves]
        elfA, elfB = [int(elves[0][0]), int(elves[0][1])], [int(elves[1][0]), int(elves[1][1])]
        lenA, lenB = elfA[1] - elfA[0], elfB[1] - elfB[0]
        if lenA < lenB:
            elfA, elfB = elfB, elfA
        if part == 1 and (elfB[0] >= elfA[0] and elfB[1] <= elfA[1]):
            overlapping_pairs += 1
        if part == 2 and ((elfB[0] <= elfA[1] and elfB[0] >= elfA[0]) or (elfB[1] >= elfA[0] and elfB[1] <= elfA[1])):
            overlapping_pairs += 1
    return overlapping_pairs


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    print(f"Part 1 solution: {solve(puzzle_input, part=1)}")
    print(f"Part 2 solution: {solve(puzzle_input, part=2)}")
