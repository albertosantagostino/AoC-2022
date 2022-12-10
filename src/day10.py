#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.meta_utils import get_puzzle_input


def part1(puzzle_input, registers={'x': 1}):
    curr_cycle = 0
    command_queue = {}
    relevant_cycles = [20, 60, 100, 140, 180, 220]
    for instruction in puzzle_input:
        instruction = instruction.split()
        if instruction[0] == 'noop':
            run_queue(curr_cycle, command_queue, registers)
            curr_cycle += 1
            if curr_cycle in relevant_cycles:
                print(curr_cycle * registers['x'])
        elif 'add' in instruction[0]:
            try:
                xy = command_queue[curr_cycle + 2]
            except:
                command_queue[curr_cycle + 2] = []
                xy = command_queue[curr_cycle + 2]
            xy.append((instruction[0][-1], int(instruction[1])))
            run_queue(curr_cycle, command_queue, registers)
            curr_cycle += 1
            if curr_cycle in relevant_cycles:
                print(curr_cycle * registers['x'])
            run_queue(curr_cycle, command_queue, registers)
            curr_cycle += 1
            if curr_cycle in relevant_cycles:
                print(curr_cycle * registers['x'])

    while (command_queue):
        run_queue(curr_cycle, command_queue, registers)
        print(command_queue)
        curr_cycle += 1
        if curr_cycle in relevant_cycles:
            print(curr_cycle * registers['x'])


def run_queue(curr_cycle, command_queue, registers):
    try:
        curr_commands = command_queue[curr_cycle]
        if curr_commands:
            for command_to_run in curr_commands:
                registers[command_to_run[0]] += command_to_run[1]
            del command_queue[curr_cycle]
    except:
        pass


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)

    print(f"Part 1 solution: {part1(puzzle_input)}")
    #print(f"Part 2 solution: {part2(puzzle_input)}")
