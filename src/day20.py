#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.meta_utils import get_puzzle_input
from copy import deepcopy


def solve(puzzle_input, decryption_key=1, mixes=1):
    values = []
    for idx, num in enumerate(puzzle_input):
        values.append((idx, num * decryption_key))
    movement_list = deepcopy(values)
    length = len(values)
    for _ in range(0, mixes):
        for kk, vv in movement_list:
            if not vv:
                continue
            curr_idx = values.index((kk, vv))
            new_idx = (curr_idx+vv) % (length-1)
            if new_idx == 0:
                new_idx = length - 1
            del values[curr_idx]
            values.insert(new_idx, (kk, vv))
        tup_val = [el[1] for el in values]
    tup_val = [el[1] for el in values]
    idx_zero = tup_val.index(0)
    return tup_val[(idx_zero+1000) % length] + tup_val[(idx_zero+2000) % length] + tup_val[(idx_zero+3000) % length]


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__, cast=int)
    print(f"Part 1 solution: {solve(deepcopy(puzzle_input))}")
    print(f"Part 2 solution: {solve(deepcopy(puzzle_input),decryption_key=811589153, mixes=10)}")
