# Praise Ye The LORD.

# Import libraries
from typing import List
import sys
sys.path.append(sys.path[0].removesuffix('src/day1'))

from src.day1.instruction import Instruction

class PartOne:
    """
    The class represents what floor do the instructions take Santa.
    """
    def __init__(self, string_instruct: str):
        self.string_instruct = string_instruct
    
    @property
    def parse_string_to_instructions(self) -> List[Instruction]:
        instruct_lst = list(self.string_instruct.strip(' '))

        # Map the instructs like ( to OPEN and ) to CLOSE
        map_instructs = list(map(lambda x: Instruction.parse_instructions(x), instruct_lst))
        
        return map_instructs
    
    @property
    def get_final_floor(self) -> int:
        parsed_instructions = self.parse_string_to_instructions
        
        return sum(map(lambda x: x.value, parsed_instructions))
