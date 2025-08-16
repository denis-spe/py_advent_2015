# Glory be to the LORD our GOD

"""
--- Day 2: I Was Told There Would Be No Math ---
The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the
dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.
"""
from functools import reduce
from typing import Tuple

# Import libraries
from src.dayAbs import DayAbs
from src.helper import Stream
from src.types import DIM


def shortest_distance(dimensions: DIM) -> Tuple[int, int]:
    first_val, second_val, third_val = dimensions
    lst = [
        (first_val, second_val),
        (first_val, third_val),
        (second_val, third_val),
    ]

    return min(lst, key=sum)


class SquareFeetSlack:
    def __init__(self, dimensions: DIM):
        distances = shortest_distance(dimensions)
        self.final_result = reduce(lambda x, y: x * y, distances)

    def __add__(self, other) -> int:
        return self.final_result + other.final_result


class SquareFeetWrappingPaper:
    def __init__(self, dimensions: DIM):
        width, height, length = dimensions
        surface_area = (2 * length * width) + (2 * width * height) + (2 * height * length)
        self.final_result = surface_area

    def __add__(self, other) -> int:
        return self.final_result + other.final_result


class RibbonFeetToWrapPresent:
    def __init__(self, dimensions: DIM):
        dim_1, dim_2 = shortest_distance(dimensions)
        self.final_result = dim_1 + dim_1 + dim_2 + dim_2

    def __add__(self, other) -> int:
        return self.final_result + other.final_result


class RibbonFeetForTheBow:
    def __init__(self, dimensions: DIM):
        self.final_result = reduce(lambda x, y: x * y, dimensions)

    def __add__(self, other) -> int:
        return self.final_result + other.final_result


class DayTwo(DayAbs):

    def part_one(self):
        """
        --- Part One ---
        Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required
        wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.
        The elves also need a little extra paper for each present: the area of the smallest side.
        """
        return (
            Stream(self.inputs.split("\n"))
            .map_(lambda x: x.strip().split('x'))
            .map_(lambda x: tuple(int(value) for value in x))
            .map_(lambda x: SquareFeetWrappingPaper(x) + SquareFeetSlack(x))
            .sum_()
        )

    def part_two(self):
        """
        --- Part Two ---
        The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the
        length they need to order, which they would again like to be exact.

        The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of
        any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the
        perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though;
        they'll never tell.
        """
        return (
            Stream(self.inputs.split("\n"))
            .map_(lambda x: x.strip().split('x'))
            .map_(lambda x: tuple(int(value) for value in x))
            .map_(lambda x: RibbonFeetToWrapPresent(x) + RibbonFeetForTheBow(x))
            .sum_()
        )
