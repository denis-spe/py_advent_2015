# Praise Ye The LORD.

# Import libraries.


class PartTwo:
    """
    The class deals on finding the position of the character 
    that causes Santa to first enter the basement?
    """
    def __init__(self, string_instruction: str):
        self.__string_instruction = string_instruction
        
    @property
    def get_position(self):
        from day1.part1 import PartOne
        
        # Instantiate the PartOne class.
        part_one = PartOne(self.__string_instruction)
        
        # santa position
        position = 0
        
        # Number of floors
        total_floor = 0
        
        # Loop over the instructions.
        for instruction in part_one.parse_string_to_instructions:
            position += 1
            total_floor += instruction.value
            
            if total_floor < 0:
                break
            
        return position
        
        
    