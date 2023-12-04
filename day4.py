# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 10:46:03 2023

@author: L
"""

from pathlib import Path
import re

probfolder = Path("problems")

scriptname = Path(__file__).name
day_num = int(re.search("\d+", scriptname).group())
filename = f"day{day_num}.txt"


class CardCollection:
    """
    Class to tidy up the processing in part 2.
    """

    def __init__(self, winning_list, own_list):
        self.winlist = winning_list
        self.ownlist = own_list

        self.stack_tracker = [1 for _ in self.ownlist]
        self.queue = [ii for ii in range(len(self.ownlist))]

    def process_card(self):
        cardidx = self.queue.pop(0)
        card_multiplier = self.stack_tracker[cardidx]

        win_nums, own_nums = self.winlist[cardidx], self.ownlist[cardidx]

        occurrences = 0
        for number in own_nums:
            if number in win_nums:
                occurrences += 1

        if occurrences > 0:
            for ii in range(occurrences):
                woncard_idx = cardidx + 1 + ii
                if woncard_idx not in self.queue:
                    self.queue.append(woncard_idx)
                self.stack_tracker[woncard_idx] += card_multiplier

    def process_stack(self):
        while self.queue:
            self.process_card()

        card_total = sum(self.stack_tracker)
        return card_total


with open(probfolder / filename) as file:
    lines = file.read().splitlines()


def part1(lines):
    numpatt = re.compile("(\d+)(?!:)")
    points_total = 0

    for line in lines:
        line = line.split(":")[1]
        winning, own = line.split("|")

        winning, own = numpatt.findall(winning), numpatt.findall(own)
        winning, own = (list(map(int, winning)), list(map(int, own)))
        occurrences = 0
        for number in own:
            if number in winning:
                occurrences += 1

        points = 2 ** (occurrences - 1) if occurrences > 0 else 0
        points_total += points
    return points_total


def part2(lines):
    numpatt = re.compile("(\d+)(?!:)")

    winlist, ownlist = [], []
    for line in lines:
        line = line.split(":")[1]
        winning, own = line.split("|")

        winning, own = numpatt.findall(winning), numpatt.findall(own)
        winning, own = (list(map(int, winning)), list(map(int, own)))
        winlist.append(winning)
        ownlist.append(own)

    cardcoll = CardCollection(winlist, ownlist)
    output = cardcoll.process_stack()
    return output


print("Answer to part 1:", part1(lines))
print("Answer to part 2:", part2(lines))
