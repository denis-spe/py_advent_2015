from enum import Enum

class Instruction(Enum):
    OPEN = 1
    CLOSE = -1
    
    @classmethod
    def parse_instructions(cls, name: str):
        match name:
            case '(':
                return cls.OPEN
            case ')':
                return cls.CLOSE
            case _:
                raise ValueError(f'Unknown name {name}')