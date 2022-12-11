#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import re

from collections import OrderedDict
from common.meta_utils import get_puzzle_input


class Monkey:
    def __init__(self, starting_items, operation, test_condition, test_true_target, test_false_target):
        self.starting_items = starting_items
        self.operation = operation
        self.test_condition = test_condition
        self.test_true_target = test_true_target
        self.test_false_target = test_false_target
        self.inspected_items = 0

    def print_items(self):
        print(f"Starting items: {[item for item in self.starting_items]}")

    def __gt__(self, other):
        return self.inspected_items > other.inspected_items

    def __eq__(self, other):
        return self.inspected_items == other.inspected_items


def solve(monkeys, rounds, worry_divider):
    for _ in range(0, rounds):
        for id in range(len(monkeys)):
            monkey = monkeys[id]
            while (monkey.starting_items):
                item = monkey.starting_items.pop(0)
                monkey.inspected_items += 1
                exec(monkey.operation.replace('old', str(item)))
                if worry_divider != 1:
                    worry_level = math.floor(locals()['new'] / worry_divider)
                if monkey.test_condition[0] == '/':
                    res = worry_level % int(monkey.test_condition[1:])
                if res:
                    monkeys[monkey.test_false_target].starting_items.append(worry_level)
                else:
                    monkeys[monkey.test_true_target].starting_items.append(worry_level)
    monkeys_list = [vv for vv in monkeys.values()]
    monkeys_list.sort()
    return monkeys_list[-2].inspected_items * monkeys_list[-1].inspected_items


def print_all_items(monkeys):
    for kk, vv in monkeys.items():
        print(f"Monkey {kk}")
        vv.print_items()


def parse_input(puzzle_input):
    monkeys = OrderedDict()
    chunked_list = [puzzle_input[i:i + 7] for i in range(0, len(puzzle_input), 7)]
    for monkey_chunk in chunked_list:
        monkey_id = int(re.search(r'\d+', monkey_chunk[0]).group())
        starting_items = re.findall(r'\d+', monkey_chunk[1])
        operation = monkey_chunk[2].split(':')[-1].strip()
        test_condition = monkey_chunk[3].split(':')[-1].strip().replace('divisible by ', '/')
        test_true_target = int(re.search(r'\d+', monkey_chunk[4]).group())
        test_false_target = int(re.search(r'\d+', monkey_chunk[5]).group())
        monkeys[monkey_id] = Monkey(starting_items, operation, test_condition, test_true_target, test_false_target)
    return monkeys


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    monkeys = parse_input(puzzle_input)
    print(f"Part 1 solution: {solve(monkeys, rounds=20, worry_divider=3)}")
    #print(f"Part 2 solution: {solve(monkeys, rounds=10000, worry_divider=1)}")
