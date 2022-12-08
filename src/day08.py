#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

from common.meta_utils import get_puzzle_input


class WoodenTree():
    """A real 🌳 (or maybe a 🌲, but most likely a 🎄, who knows?)"""
    def __init__(self, height: int, visible: bool = False, score: int = 0):
        self.height = height
        self.visible = visible
        self.score = score

    def __repr__(self):
        return f"{self.height}:{'V' if self.visible else 'H'}:{self.score}"


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


def part2(grid):
    for (xx, yy), tree in np.ndenumerate(grid):
        if xx != 0 and yy != 0 and xx != len(grid) - 1 and yy != len(grid) - 1:
            grid[xx, yy].score = 1
            for direction in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                grid[xx, yy].score *= look_from_tree(grid, xx, yy, direction)
    return max(el.score for el in grid.flat)


def look_from_tree(grid, xx, yy, direction):
    visible_trees = 0
    this_height = grid[xx, yy].height
    xx += direction[0]
    yy += direction[1]
    while True:
        visible_trees += 1
        if grid[xx, yy].height >= this_height:
            break
        xx += direction[0]
        yy += direction[1]
        if xx < 0 or yy < 0 or xx >= len(grid) or yy >= len(grid):
            break
    return visible_trees


def look_from_boundary(grid, x, y, direction):
    max_height = -1
    while True:
        if grid[x, y].height > max_height:
            max_height = grid[x, y].height
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
