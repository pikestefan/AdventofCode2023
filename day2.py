# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 13:20:27 2023

@author: L
"""

from pathlib import Path
import re
from math import prod

probfolder = Path("problems")

scriptname = Path(__file__).name
day_num = int(re.search("\d+", scriptname).group())
filename = f"day{day_num}.txt"


def part1():
    colors = ["red", "green", "blue"]
    smartint = lambda string: int(string or 0)
    
    
    with open(probfolder / filename) as file:
        lines = file.readlines()
        
        possible_rounds = 0
        for line in lines:
            round_dict = dict(zip(colors, [0,0,0]))
            round_id = int(re.match("Game (\d+)", line).group(1))
            for color in colors:
                result = re.findall(f"(\d+) {color}", line)
                result = max(map(smartint, result))

                round_dict[color] = result
                
            if (round_dict["red"] <= 12 and 
                round_dict["green"] <= 13 and 
                round_dict["blue"] <= 14):
                possible_rounds += round_id
    return possible_rounds


def part2():
    colors = ["red", "green", "blue"]
    smartint = lambda string: int(string or 0)
    
    with open(probfolder / filename) as file:
        lines = file.readlines()
        tot_power = 0
        for line in lines:
            round_dict = dict(zip(colors, [0,0,0]))
            # round_id = int(re.match("Game (\d+)", line).group(1))
            for color in colors:
                result = re.findall(f"(\d+) {color}", line)
                result = max(map(smartint, result))

                round_dict[color] = result
            power = prod(round_dict.values())
            tot_power += power
            
    return tot_power


print("Answer to part 1:", part1())
print("Answer to part 2:", part2())
