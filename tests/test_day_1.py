# Praise Ye The LORD.

"""
=========== Testing day one =========
"""

# Import libraries.
import unittest

from src.advent2015.day1.day import DayOne
from tests.day_test_abs import DayTestAbs


class TestDayOne(DayTestAbs):
    def test_part_one_sample_input(self):

        # Test case
        testCase1 = DayOne(inputs="(())").part_one()
        testCase2 = DayOne(inputs="()()").part_one()
        testCase3 = DayOne(inputs="(((").part_one()
        testCase4 = DayOne(inputs="(()(()(").part_one()
        testCase5 = DayOne(inputs="))(((((").part_one()
        testCase6 = DayOne(inputs="())").part_one()
        testCase7 = DayOne(inputs="))(").part_one()
        testCase8 = DayOne(inputs=")))").part_one()
        testCase9 = DayOne(inputs=")())())").part_one()

        self.assertEqual(testCase1, 0)
        self.assertEqual(testCase2, 0)
        self.assertEqual(testCase3, 3)
        self.assertEqual(testCase4, 3)
        self.assertEqual(testCase5, 3)
        self.assertEqual(testCase6, -1)
        self.assertEqual(testCase7, -1)
        self.assertEqual(testCase8, -3)
        self.assertEqual(testCase9, -3)

    def test_part_two_sample_input(self):

        # Test case
        testCase1 = DayOne(inputs=")").part_two()
        testCase2 = DayOne(inputs="()())").part_two()

        self.assertEqual(testCase1, 1)
        self.assertEqual(testCase2, 5)


if __name__ == "__main__":
    unittest.main()
