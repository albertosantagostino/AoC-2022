#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

from common.meta_utils import get_puzzle_input


def solve(grid):
    count = 0
    air_count = 0
    for (xx, yy, zz), el in np.ndenumerate(grid):
        try:
            # yapf: disable
            nearby = [
                grid[xx - 1, yy - 1:yy + 2, zz - 1:zz + 2],
                grid[xx,     yy - 1:yy + 2, zz - 1:zz + 2],
                grid[xx + 1, yy - 1:yy + 2, zz - 1:zz + 2]
            ]
            # yapf: enable
            adj = [nearby[0][1, 1], nearby[1][1, 0], nearby[1][0, 1], nearby[1][1, 2], nearby[1][2, 1], nearby[2][1, 1]]
            if (el == 1):
                count += (6 - sum([1 for el in adj if el == 1]))
        except IndexError:
            pass

    return count


def parse_input(puzzle_input):
    xmax, ymax, zmax = 0, 0, 0
    cubes = []
    for cube in puzzle_input:
        xx, yy, zz = [int(el) for el in cube.split(',')]
        cubes.append([xx, yy, zz])
        xmax = xx if xx > xmax else xmax
        ymax = yy if yy > ymax else ymax
        zmax = zz if zz > zmax else zmax

    grid = np.zeros((xmax + 1, ymax + 1, zmax + 1), dtype=int)
    for xx, yy, zz in cubes:
        grid[xx, yy, zz] = True

    grid = np.pad(grid, [(1, 1), (1, 1), (1, 1)], mode='constant', constant_values=2)
    return grid


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    grid = parse_input(puzzle_input)
    print(f"Part 1 solution: {solve(grid)}")
