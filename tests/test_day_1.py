# Praise Ye The LORD.

# Import libraries.
import unittest
import sys
sys.path.append(sys.path[0].replace("tests", ""))

from src.day1.part1 import PartOne
from src.day1.part2 import PartTwo
from src.day1.instruction import Instruction
from src.file_reader import FileReader


class TestDayOne(unittest.TestCase):
    def setUp(self):
        # Part One
        # =========
        
        test_case_1 = "(())"
        test_case_2 = "()()"
        test_case_3 = ")())())"
        test_case_4 = "())"

        # Initialize the Part one object.
        self.part_one_1 = PartOne(test_case_1)
        self.part_one_2 = PartOne(test_case_2)
        self.part_one_3 = PartOne(test_case_3)
        self.part_one_4 = PartOne(test_case_4)

        # Final submission
        file_reader = FileReader("day1/input.txt")
        self.part_one = PartOne(file_reader.data)
        
        # Part Two
        # ==========
        test_case_1 = ')'
        test_case_2 = '()())'
        
        self.part_two_1 = PartTwo(test_case_1)
        self.part_two_2 = PartTwo(test_case_2)
        
        # Final submission
        file_reader = FileReader("day1/input.txt")
        self.part_two = PartTwo(file_reader.data)
        

    def test_parse_string_to_instructions(self):
        self.assertEqual(
            self.part_one_1.parse_string_to_instructions,
            [Instruction.OPEN, Instruction.OPEN, Instruction.CLOSE, Instruction.CLOSE],
        )

    def test_get_final_floor(self):
        self.assertEqual(self.part_one_1.get_final_floor, 0)
        self.assertEqual(self.part_one_2.get_final_floor, 0)
        self.assertEqual(self.part_one_3.get_final_floor, -3)
        self.assertEqual(self.part_one_4.get_final_floor, -1)

        # Final submission test
        self.assertEqual(self.part_one.get_final_floor, 232)
        
    def test_get_position(self):
        self.assertEqual(self.part_two_1.get_position, 1)
        self.assertEqual(self.part_two_2.get_position, 5)
        
        # Final submission test
        self.assertEqual(self.part_two.get_position, 1783)


if __name__ == "__main__":
    unittest.main()
