# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 13:20:27 2023

@author: L
"""

from pathlib import Path
import regex as re

probfolder = Path("problems")

scriptname = Path(__file__).name
day_num = int(re.search("\d+", scriptname).group())
filename = f"day{day_num}.txt"


def part1():
    with open(probfolder / filename) as file:
        total = 0
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            number = re.findall("\d", line)
            number = int(number[0] + number[-1])
            total += number

    return total


def part2():
    with open(probfolder / filename) as file:
        total = 0
        lines = file.readlines()

        num_list = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "\d",
        ]
        pattern = str("|").join(num_list)

        letter2num = dict(zip(num_list[:-1], map(str, range(1, 11))))

        for line in lines:
            line = line.strip()
            number = re.findall(pattern, line, overlapped=True)

            numbers = [number[0], number[-1]]

            for ii, number in enumerate(numbers):
                if number.isalpha():
                    numbers[ii] = letter2num[number]

            number = int(str().join(numbers))
            total += number

    return total


print("Answer to part 1:", part1())
print("Answer to part 2:", part2())
