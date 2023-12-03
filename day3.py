# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 10:46:03 2023

@author: L
"""

from pathlib import Path
import numpy as np
import re
from math import prod
from collections import defaultdict

probfolder = Path("problems")

scriptname = Path(__file__).name
day_num = int(re.search("\d+", scriptname).group())
filename = f"day{day_num}.txt"

with open(probfolder / filename) as file:
    lines = file.read().splitlines()


def part1(input_lines):
    numpatt = re.compile("\d+")
    sympatt = re.compile("([^a-zA-Z\d\.])")

    number_list = []
    for line in input_lines:
        number_list.append(numpatt.finditer(line))

    total = 0
    for row_ind, nums in enumerate(number_list):
        for number in nums:
            is_part = False
            start, stop = number.start() - 1, number.end() + 1
            for hood in input_lines[max(row_ind - 1, 0) : row_ind + 2]:
                searchline = hood[max(start, 0) : stop]
                match = sympatt.search(searchline)
                if match is not None:
                    is_part = True
            if is_part:
                total += int(number.group())
    return total


def part2(input_lines):
    numpatt = re.compile("\d+")
    gearpatt = re.compile("\*")

    number_list = []
    for line in input_lines:
        number_list.append(numpatt.finditer(line))

    row_tot = len(input_lines)
    col_tot = len(input_lines[0])

    gear_dict = defaultdict(lambda: [])

    for row_ind, nums in enumerate(number_list):
        for number in nums:
            start, stop = max(number.start() - 1, 0), number.end() + 1
            for subrow in range(max(row_ind - 1, 0), min(row_ind + 2, row_tot - 1)):
                hood = input_lines[subrow]
                searchline = hood[start:stop]
                match = gearpatt.search(searchline)
                if match is not None:
                    gear_id = subrow * col_tot + start + match.start()
                    gear_dict[gear_id].append(int(number.group()))

    gear_ratios = 0
    for gearid, gears in gear_dict.items():
        if len(gears) == 2:
            gear_ratios += prod(gears)

    return gear_ratios


print("Answer to part 1:", part1(lines))
print("Answer to part 2:", part2(lines))
