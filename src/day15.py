#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ipdb
import re

from collections import defaultdict

from common.iter_utils import slide
from common.meta_utils import get_puzzle_input


def part1(tunnels_map, beacons, sensors, row):
    forbidden_areas = []
    for beacon, sensor in zip(beacons, sensors):
        dis = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])
        # area: [(xup, yup), (xright, yright), (xdown, ydown), (xleft, yleft)]
        area = [(sensor[0], sensor[1] - dis), (sensor[0] + dis, sensor[1]), (sensor[0], sensor[1] + dis),
                (sensor[0] - dis, sensor[1])]
        forbidden_areas.append(area)

    xmin = float('inf')
    xmax = 0
    xmin, xmax = min(tunnels_map), max(tunnels_map)
    #ymin, ymax = min([min(el) for el in tunnels_map.values()]), max ([max(el) for el in tunnels_map.values()])

    count = 0
    for xx in range(xmin, xmax - 1):
        is_in_area = False
        for area in forbidden_areas:
            is_inside_forbidden_area = []
            for points, _ in slide(area + [area[0]], 2):
                is_inside_forbidden_area.append(check_point_side_left(points[0], points[1], (xx, row)))
            if all(is_inside_forbidden_area):
                is_in_area = True
                break
        if is_in_area:
            count += 1
    return count + 1


def check_point_side_left(linepoint1, linepoint2, point):
    return ((linepoint2[0] - linepoint1[0]) * (point[1] - linepoint1[1]) - (linepoint2[1] - linepoint1[1]) *
            (point[0] - linepoint1[0])) >= 0


def part2(puzzle_input):
    ipdb.set_trace()


def parse_input(puzzle_input):
    match_coords = re.compile(r'-?\d+')
    tunnels_map = defaultdict(set)
    beacons = []
    sensors = []
    for line in puzzle_input:
        coords = [int(el) for el in re.findall(match_coords, line)]
        sensor = (coords[0], coords[1])
        beacon = (coords[2], coords[3])
        tunnels_map[sensor[0]].add(sensor[1])
        tunnels_map[beacon[0]].add(beacon[1])
        beacons.append((beacon[0], beacon[1]))
        sensors.append((sensor[0], sensor[1]))
    return tunnels_map, beacons, sensors


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    tunnels_map, beacons, sensors = parse_input(puzzle_input)
    print(f"Part 1 solution: {part1(tunnels_map, beacons, sensors, row=2000000)}")
    #print(f"Part 2 solution: {part2(tunnels_map)}")
