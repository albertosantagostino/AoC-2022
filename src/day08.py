#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

from common.meta_utils import get_puzzle_input


class WoodenTree():
    """A real 🌳 (or maybe a 🌲, but most likely a 🎄, who knows?)"""
    def __init__(self, height: int, visible: bool = False):
        self.height = height
        self.visible = visible

    def __repr__(self):
        return f"{self.height}{'V' if self.visible else 'H'}"


def part1(grid):
    for xx in [0, len(grid) - 1]:
        for yy in range(0, len(grid)):
            if not (xx):
                look_from_boundary(grid, xx, yy, direction=[1, 0])
            else:
                look_from_boundary(grid, xx, yy, direction=[-1, 0])
    for yy in [0, len(grid) - 1]:
        for xx in range(0, len(grid)):
            if not (yy):
                look_from_boundary(grid, xx, yy, direction=[0, 1])
            else:
                look_from_boundary(grid, xx, yy, direction=[0, -1])

    return sum(1 for el in grid.flat if el.visible)


def look_from_boundary(grid, x, y, direction):
    max_height = -1
    while True:
        tree = grid[x, y]
        if tree.height > max_height:
            max_height = tree.height
            grid[x, y].visible = True
        x += direction[0]
        y += direction[1]
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid):
            break


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    grid = np.vectorize(WoodenTree)(np.matrix([list(row) for row in puzzle_input], dtype=int))
    print(f"Part 1 solution: {part1(grid)}")
    print(f"Part 2 solution: {part2(grid)}")
