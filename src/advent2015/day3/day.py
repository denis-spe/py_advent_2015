# Praise Ye the LORD

"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and
then an elf at the North Pole calls him via radio and tells him where to move next.
Moves are always exactly one house to the north (^), south (v), east (>), or west (<).
After each move, he delivers another present to the house at his new location.
"""
from src.dayAbs import DayAbs
from src.helper import Stream


class DayThree(DayAbs):
    def part_one(self):
        """
        --- Part One ---
        However, the elf back at the North Pole has had a little too much eggnog,
        and so his directions are a little off, and Santa ends up visiting some houses more than once.
        How many houses receive at least one present?
        """
        return (
            Stream(list(self.inputs))
            .flat_map_(set)
            .flat_map_(lambda x: x if len(x) > 1 else list(x) * 2)
            .flat_map_(len)
            .show_result()
        )

    def part_two(self):
        pass
