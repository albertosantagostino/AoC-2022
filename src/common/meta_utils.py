#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests

from pathlib import Path

root_path = Path(__file__).parents[2]
config = json.load(root_path.joinpath('config.json').open())


def download_puzzle_data(year, day):
    """Fetch puzzle input data from AoC, using the cookie value stored in config.json"""
    # Download text input for specific puzzle
    print(f"Fetching puzzle input for day {day}")
    res = requests.get(url=f'https://adventofcode.com/{year}/day/{day}/input',
                       cookies={"session": config['aoc_cookie']})
    res.raise_for_status()
    # Store locally under data/
    with open(root_path.joinpath('data', f'day{day:02}_input.txt'), 'w') as fp:
        fp.write(res.text)


def get_puzzle_input(filename=None, day=None, cast=None, oneline=False):
    """Retrieve puzzle input locally (if already downloaded) or invokes download_puzzle_data()"""
    # Get day number from script filename
    if filename:
        day = int(filename.split('/')[-1][3:5])
    if not day:
        raise ValueError("get_puzzle_data() must be called with either filename or day")
    puzzle_data_file = root_path.joinpath('data', f'day{day:02}_input.txt')
    # Download puzzle data (if needed)
    if not puzzle_data_file.exists():
        download_puzzle_data(year=config['year'], day=day)
    puzzle_input = puzzle_data_file.open().read().splitlines()
    # Handle all input on one line
    if oneline:
        puzzle_input = [entry for entry in puzzle_input[0].split(',')]
    # Cast to specific type
    if cast:
        return [cast(entry) for entry in puzzle_input]
    return puzzle_input
