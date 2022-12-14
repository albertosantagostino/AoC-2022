#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.iter_utils import slide
from common.meta_utils import get_puzzle_input


def solve(puzzle_input, marker_length):
    for group, idx in slide(puzzle_input, marker_length):
        if len(set(group)) == marker_length:
            return marker_length + idx


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)[0]
    print(f"Part 1 solution: {solve(puzzle_input, marker_length=4)}")
    print(f"Part 2 solution: {solve(puzzle_input, marker_length=14)}")
