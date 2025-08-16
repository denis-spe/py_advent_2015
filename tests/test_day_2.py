# Great is the LORD GOD

"""
=========== Testing day two =========
"""

# Import libraries
import unittest

from src.advent2015.day2.day import DayTwo, SquareFeetSlack
from tests.day_test_abs import DayTestAbs


class TestDayTwo(DayTestAbs):

    def test_shortest_distance(self):
        self.assertEqual(SquareFeetSlack([2, 3, 5]).final_result, 6)
        self.assertEqual(SquareFeetSlack([1, 1, 10]).final_result, 1)
        self.assertEqual(SquareFeetSlack([8, 1, 10]).final_result, 8)
        self.assertEqual(SquareFeetSlack([8, 14, 10]).final_result, 80)

    def test_part_one_sample_input(self):
        # Test case
        testCase1 = DayTwo(inputs="2x3x4").part_one()
        testCase2 = DayTwo(inputs="1x1x10").part_one()

        self.assertEqual(testCase1, 58)
        self.assertEqual(testCase2, 43)

    def test_part_two_sample_input(self):
        # Test case
        testCase1 = DayTwo(inputs="2x3x4").part_two()
        testCase2 = DayTwo(inputs="1x1x10").part_two()

        self.assertEqual(testCase1, 34)
        self.assertEqual(testCase2, 14)


if __name__ == "__main__":
    unittest.main()
