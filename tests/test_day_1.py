# Praise Ye The LORD.

# Import libraries.
import unittest
from src.day1.day import DayOne


class TestDayOne(unittest.TestCase):
    def setUp(self):
        INPUT_PATH = "../src/day1/input.txt"
        self.day1 = DayOne(inputs=INPUT_PATH)

    def test_if_part_one_exists(self):
        self.assertTrue(hasattr(self.day1, "part_one"))

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


if __name__ == "__main__":
    unittest.main()
