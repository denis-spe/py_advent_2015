# Holy, holy, holy is the LORD of hosts

"""
=========== Testing day three =========
"""
from src.advent2015.day3.day import DayThree
from tests.day_test_abs import DayTestAbs


class TestDayTwo(DayTestAbs):

    def setUp(self):
        INPUT_PATH = "day3/input.txt"
        self.day3 = DayThree(inputs=INPUT_PATH)

    def test_part_one_sample_input(self):
        test_case1 = DayThree(inputs=">")
        test_case2 = DayThree(inputs="^>v<")
        test_case3 = DayThree(inputs="^v^v^v^v^v")

        self.assertEqual(test_case1.part_one(), 2)
        self.assertEqual(test_case2.part_one(), 4)
        self.assertEqual(test_case3.part_one(), 2)

    def test_part_two_sample_input(self):
        pass
