#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq as hp
import numpy as np

from common.meta_utils import get_puzzle_input


def solve(heightmap, start, end, part):
    paths_graph = create_graph(heightmap)
    paths_lengths = compute_paths_lengths(paths_graph, end)
    if part == 1:
        return paths_lengths[start]
    else:
        return min(pl for (xx, yy), pl in paths_lengths.items() if heightmap[xx, yy] in 'aS')


def compute_paths_lengths(paths_graph, end):
    # Create a min priority queue
    pq = [(0, end)]
    paths_lengths = {end: 0}
    while pq:
        cost, current = hp.heappop(pq)
        for point in paths_graph[current]:
            if point not in paths_lengths or cost + 1 < paths_lengths[point]:
                paths_lengths[point] = cost + 1
                hp.heappush(pq, (cost + 1, point))
    return paths_lengths


def create_graph(heightmap):
    # Create a dict representing a graph (key is current tile, value are the possible previous tiles)
    graph = {}
    for (xx, yy), tile in np.ndenumerate(heightmap):
        graph[(xx, yy)] = []
        tiles = get_adjecent_tiles(heightmap, [xx, yy])
        tiles = list(
            filter(lambda x, xx=xx, yy=yy: ord(heightmap[(x[0], x[1])]) - ord(heightmap[(xx, yy)]) >= -1, tiles))
        for tile in tiles:
            graph[(xx, yy)].append((tile[0], tile[1]))
    return graph


def parse_input(puzzle_input):
    heightmap = np.matrix([[ch for ch in xx] for xx in puzzle_input])
    xstart, ystart = np.where(heightmap == 'S')
    xend, yend = np.where(heightmap == 'E')
    start, end = (int(xstart), int(ystart)), (int(xend), int(yend))
    heightmap[heightmap == 'S'] = 'a'
    heightmap[heightmap == 'E'] = 'z'
    return heightmap, start, end


def get_adjecent_tiles(heightmap, curr_coordinate, diagonal=False):
    ret = []
    xcurr, ycurr = curr_coordinate
    for xx, yy in [(xcurr + ii, ycurr + jj) for ii in (-1, 0, 1) for jj in (-1, 0, 1) if ii != 0 or jj != 0]:
        if not diagonal and (xx == xcurr or yy == ycurr) and (xx >= 0 and yy >= 0 and xx < heightmap.shape[0]
                                                              and yy < heightmap.shape[1]):
            ret.append([xx, yy, heightmap[xx, yy]])
    return ret


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    heightmap, start, end = parse_input(puzzle_input)
    print(f"Part 1 solution: {solve(heightmap, start, end, part=1)}")
    print(f"Part 2 solution: {solve(heightmap, start, end, part=2)}")
