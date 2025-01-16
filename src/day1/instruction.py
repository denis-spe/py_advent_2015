from enum import Enum

class Instruction(Enum):
    OPEN = 1
    CLOSE = 1

    def __getitem__(cls, name: str):
        match name:
            case '(':
                return OPEN
            case ')':
                return CLOSE