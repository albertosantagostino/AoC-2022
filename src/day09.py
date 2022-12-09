#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import add

from common.meta_utils import get_puzzle_input

direction_lookup = {'R': [1, 0], 'U': [0, 1], 'L': [-1, 0], 'D': [0, -1]}


def solve(puzzle_input, knots):
    knots_positions = [[0, 0] for _ in range(0, knots)]
    visited = set()
    visited.add((0, 0))
    for move in puzzle_input:
        direction, steps = move.split()
        for _ in range(int(steps)):
            knots_positions[0] = list(map(add, knots_positions[0], direction_lookup[direction]))
            for idx in range(1, len(knots_positions)):
                knots_positions[idx] = update_knot(knots_positions[idx - 1], knots_positions[idx])
            visited.add((tuple(knots_positions[knots - 1])))
    return len(visited)


def update_knot(front_knot_pos, rear_knot_pos):
    xh, yh = front_knot_pos
    xt, yt = rear_knot_pos
    if (yt == yh):
        delta = xt - xh
        if (delta <= -2):
            xt += 1
        elif (delta >= 2):
            xt -= 1
    elif (xt == xh):
        delta = yt - yh
        if (delta <= -2):
            yt += 1
        elif (delta >= 2):
            yt -= 1
    else:
        # Assume taxicab geometry for diagonal
        if ((abs(xt - xh) + abs(yt - yh)) > 2):
            if (xh > xt):
                movex = 1
            else:
                movex = -1
            if (yh > yt):
                movey = 1
            else:
                movey = -1
            xt += movex
            yt += movey
    return [xt, yt]


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    print(f"Part 1 solution: {solve(puzzle_input ,knots=2)}")
    print(f"Part 2 solution: {solve(puzzle_input, knots=10)}")
