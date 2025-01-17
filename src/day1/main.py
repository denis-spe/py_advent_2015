# Praise Ye The LORD.

# Import libraries.
import sys
sys.path.append(sys.path[0].removesuffix('day1'))

from day1.part1 import PartOne
from day1.part2 import PartTwo
from file_reader import FileReader

# Read the txt file
file_reader = FileReader("day1/input.txt")

# Instantiate the part one class.
part_one = PartOne(file_reader.data)
print(part_one.get_final_floor)

# Instantiate the part one class.
part_two = PartTwo(file_reader.data)
print(part_two.get_position)