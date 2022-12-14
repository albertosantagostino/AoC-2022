#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import re

from copy import deepcopy

from common.iter_utils import slide
from common.meta_utils import get_puzzle_input


def part1(cave_map, starting_coord):
    idx = 0
    while True:
        grainx, grainy = starting_coord
        while True:
            try:
                newx, newy = drop(cave_map, grainx, grainy)
            except:
                return idx
            if (newx, newy) == (grainx, grainy):
                break
            grainx, grainy = newx, newy
        cave_map[grainx, grainy] = 'O'
        idx += 1


def part2(cave_map, starting_coord):
    # Not so nice but it works: pick padding using trial and error (until solution no longer changes)
    pad_sides = 150
    # Pad matrix and fill floor
    cave_map = np.pad(cave_map, pad_width=((0, 2), (pad_sides, pad_sides)), constant_values='.')
    cave_map[-1] = '#'

    startx, starty = np.where(cave_map == 'O')
    starting_coord = (int(startx), int(starty))
    sdd, sld, srd = (starting_coord[0] + 1, starting_coord[1]), (starting_coord[0] + 1,
                                                                 starting_coord[1] - 1), (starting_coord[0] + 1,
                                                                                          starting_coord[1] + 1)
    idx = 0
    while True:
        grainx, grainy = starting_coord
        while True:
            try:
                newx, newy = drop(cave_map, grainx, grainy)
            except:
                break
            if cave_map[sdd] == 'O' and cave_map[sld] == 'O' and cave_map[srd] == 'O':
                return idx + 1
            if (newx, newy) == (grainx, grainy):
                break
            grainx, grainy = newx, newy
        cave_map[grainx, grainy] = 'O'
        idx += 1


def drop(cave_map, grainx, grainy):
    dd, ld, rd = (grainx + 1, grainy), (grainx + 1, grainy - 1), (grainx + 1, grainy + 1)
    if cave_map[dd] == '.':
        return dd
    elif cave_map[ld] == '.':
        return ld
    elif cave_map[rd] == '.':
        return rd
    else:
        return grainx, grainy


def parse_input(puzzle_input, starting_point=(500, 0)):
    match_y = re.compile(r'(\d+)(?:,(\d+))')
    lines = []
    xmax, ymax, xmin, ymin = 0, 0, 1000, 1000
    for line in puzzle_input:
        coords = [(int(el[0]), int(el[1])) for el in re.findall(match_y, line)]
        xs, ys = list(zip(*coords))
        xmax = max(xs) if max(xs) > xmax else xmax
        ymax = max(ys) if max(ys) > ymax else ymax
        xmin = min(xs) if min(xs) < xmin else xmin
        ymin = min(ys) if min(ys) < ymin else ymin
        lines.append(coords)
    width = xmax - xmin
    height = ymax - ymin

    cave_map = np.full(shape=(height + 1, width + 1), fill_value='.')
    for coords in lines:
        for coord, _ in slide(coords, 2):
            y1, x1, y2, x2 = coord[0][0] - xmin, coord[0][1] - ymin, coord[1][0] - xmin, coord[1][1] - ymin
            if x1 == x2:
                y1, y2 = min(y1, y2), max(y1, y2)
                cave_map[x1, y1:y2 + 1] = '#'
            else:
                x1, x2 = min(x1, x2), max(x1, x2)
                cave_map[x1:x2 + 1, y1] = '#'

    if ymin > starting_point[1]:
        top_pad = ymin - starting_point[1]
        ymin = starting_point[1]
    cave_map = np.pad(cave_map, pad_width=((top_pad, 0), (0, 0)), constant_values='.')
    cave_map[starting_point[1] - ymin, starting_point[0] - xmin] = 'O'
    starting_coord = (starting_point[1] - ymin, starting_point[0] - xmin)
    return cave_map, starting_coord


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    cave_map, starting_coord = parse_input(puzzle_input)

    print(f"Part 1 solution: {part1(deepcopy(cave_map), starting_coord)}")
    print(f"Part 2 solution: {part2(deepcopy(cave_map), starting_coord)}")
