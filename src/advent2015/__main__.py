# Bless be the LORD of hosts

"""
-- Advent of code 2015 submission point --
"""

from typing import Callable, List

# Import Libraries
from src.advent2015.day1.day import DayOne
from src.advent2015.day2.day import DayTwo
from src.advent2015.day3.day import DayThree


def submission(days: List[Callable]) -> None:
    for idx in range(1, len(days) + 1):
        # Subtract one since list starts from zero
        day = days[idx - 1](inputs=f"day{idx}/input.txt")
        day_name = f"Day{idx}"

        print(f"{day_name} part One: ", day.part_one())
        print(f"{day_name} part Two: ", day.part_two())

        print()


submission([
    DayOne,
    DayTwo,
    DayThree
])
