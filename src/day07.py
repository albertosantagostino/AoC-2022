#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.fsnode import FSNode, FSMode, traverse_tree, populate_dir_size
from common.meta_utils import get_puzzle_input


def part1(tree, threshold):
    total_size = 0
    for node in traverse_tree(tree):
        if node.isdir() and node.size < threshold:
            total_size += node.size
    return total_size


def part2(tree, needed_space, total_disk_size):
    dirs = []
    for node in traverse_tree(tree):
        if node.isdir():
            dirs.append(node.size)
    dirs.sort()
    space_to_free = needed_space - (total_disk_size - dirs[-1])
    return [vv for vv in dirs if vv > space_to_free][0]


def create_filesystem_tree(puzzle_input):
    tree = FSNode(name='/', mode=FSMode.DIR)

    for line in puzzle_input:
        line = line.split()
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '/':
                    curr = tree
                elif line[2] == '..':
                    curr = curr.parent
                else:
                    try:
                        curr = next(filter(lambda node: node.name == line[2], curr.children))
                    except StopIteration:
                        curr = curr.add_child(name=line[2], mode=FSMode.DIR)
        else:
            if line[0] == 'dir':
                if not line[1] in curr.children:
                    curr.add_child(name=line[1], mode=FSMode.DIR)
            else:
                child = curr.add_child(name=line[1], mode=FSMode.FILE)
                child.size = line[0]
    return tree


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    tree = create_filesystem_tree(puzzle_input)
    populate_dir_size(tree)
    print(f"Part 1 solution: {part1(tree, threshold= 100000)}")
    print(f"Part 2 solution: {part2(tree, needed_space = 30000000, total_disk_size = 70000000)}")
