# Bless be the name of LORD of host.

"""
--- Day 1: Not Quite Lisp ---
Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and
he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.

Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar;
the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
"""

from typing import List

from src.dayAbs import DayAbs
from src.helper import Stream
from src.types import Input


class DayOne(DayAbs):
    def __init__(self, inputs: Input = None):
        super().__init__(inputs)
        self.instruction = {
            "(": 1,
            ")": -1
        }

    def part_one(self):
        """
        --- Part Two ---
        Santa is trying to deliver presents in a large apartment building, but he can't find the right floor -
        the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows
        the instructions one character at a time. An opening parenthesis, (, means he should go up one floor,
        and a closing parenthesis, ), means he should go down one floor.
        The apartment building is very tall, and the basement is very deep;
        he will never find the top or bottom floors.
        """

        return (
            Stream(self.inputs)
            .tolist()
            .map_(lambda x: self.instruction[x])
            .sum_()
        )

    @staticmethod
    def santa_position(instructions: List[int]):
        pos = 0
        instruction_pos = 0

        for instruction in instructions:
            instruction_pos = instruction_pos + instruction
            pos = pos + 1

            if instruction_pos < 0:
                break

        return pos


    def part_two(self):
        """
        --- Part Two ---
        Now, given the same instructions, find the position of the first character that causes him to enter
        the basement (floor -1). The first character in the instructions has position 1, the second character
        has position 2, and so on.
        """

        return (
            Stream(self.inputs)
            .tolist()
            .map_(lambda x: self.instruction[x])
            .flat_map_(self.santa_position)
            .show_result()
        )
