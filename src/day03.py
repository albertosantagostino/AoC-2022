#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.meta_utils import get_puzzle_input

priority_map = {chr(val): val - 96 for val in range(97, 123)} | ({chr(val): val - 38 for val in range(65, 91)})


def part1(puzzle_input):
    total_score = 0
    for rucksack in puzzle_input:
        first, second = set(rucksack[:len(rucksack) // 2]), set(rucksack[len(rucksack) // 2:])
        for item in first:
            if item in second:
                total_score += priority_map[item]
                break
    return total_score


def part2(puzzle_input):
    total_score = 0
    groups = list(divide_groups(puzzle_input, 3))
    for group in groups:
        badge = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
        total_score += priority_map[badge]
    return total_score


def divide_groups(groups, nn):
    for idx in range(0, len(groups), nn):
        yield groups[idx:idx + nn]


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    print(f"Part 1 solution: {part1(puzzle_input)}")
    print(f"Part 2 solution: {part2(puzzle_input)}")
