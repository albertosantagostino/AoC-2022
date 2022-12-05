#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import deepcopy
from operator import itemgetter

from common.meta_utils import get_puzzle_input


def solve(crates_stacks, rearrangement_procedure, crane_model):
    for instruction in rearrangement_procedure:
        batch_size, origin, destination = itemgetter(1, 3, 5)(instruction.split())
        batch_size, origin, destination = int(batch_size), int(origin), int(destination)
        if crane_model == 9000:
            for i in range(0, batch_size):
                crate = crates_stacks[origin].pop()
                crates_stacks[destination].append(crate)
        else:
            crates = crates_stacks[origin][-batch_size:]
            crates_stacks[origin] = crates_stacks[origin][:-batch_size]
            crates_stacks[destination] += crates
    return ''.join([vv[-1] for vv in crates_stacks.values()])


def parse_input(puzzle_input):
    # Locate indexes of interest
    idx_sep = puzzle_input.index('')
    idx_crates_end = idx_sep - 1
    idx_procedure_start = idx_sep + 1
    # Map character index target stack and init stacks
    crates_stacks = {}
    map_str_idx_stack = {}
    for idx, ch in enumerate(puzzle_input[idx_crates_end]):
        if ch.isnumeric():
            crates_stacks[int(ch)] = []
            map_str_idx_stack[idx] = int(ch)
    # Fill stacks directly from bottom to top
    for idx in range(idx_crates_end - 1, -1, -1):
        for idx, ch in enumerate(puzzle_input[idx]):
            if ch.isalpha():
                crates_stacks[map_str_idx_stack[idx]].append(ch)
    return crates_stacks, puzzle_input[idx_procedure_start:]


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    crates_stacks, rearrangement_procedure = parse_input(puzzle_input)
    print(f"Part 1 solution: {solve(deepcopy(crates_stacks), rearrangement_procedure, 9000)}")
    print(f"Part 2 solution: {solve(deepcopy(crates_stacks), rearrangement_procedure, 9001)}")
