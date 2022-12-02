#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.meta_utils import get_puzzle_input

hand_map = {'X': 'A', 'Y': 'B', 'Z': 'C'}
hand_values = {'A': 1, 'B': 2, 'C': 3}
key_beats_value = {'A': 'C', 'B': 'A', 'C': 'B'}
value_beats_key = {vv: kk for kk, vv in key_beats_value.items()}


def part1(puzzle_input):
    total_score = 0
    for round in puzzle_input:
        opponent_move, my_move = round[0], hand_map[round[2]]
        score = hand_values[my_move]
        if opponent_move == my_move:
            score += 3
        elif key_beats_value[my_move] == opponent_move:
            score += 6
        total_score += score
    return total_score


def part2(puzzle_input):
    total_score = 0
    for round in puzzle_input:
        opponent_move, desired_outcome = round[0], round[2]
        if desired_outcome == 'X':
            my_move = key_beats_value[opponent_move]
            total_score += hand_values[my_move]
        elif desired_outcome == 'Y':
            my_move = opponent_move
            total_score += hand_values[my_move] + 3
        else:
            my_move = value_beats_key[opponent_move]
            total_score += hand_values[my_move] + 6
    return total_score


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    print(f"Part 1 solution: {part1(puzzle_input)}")
    print(f"Part 2 solution: {part2(puzzle_input)}")
