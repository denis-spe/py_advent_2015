# Bless be the LORD of host
from src.file_reader import FileReader
from src.types import Input, SAMPLE_INPUT
import os

class InvalidInput(Exception):
    def __init__(self, message: str = "Invalid input") -> None:
        self.message = message
        super().__init__(self, message)


class DayAbs:
    """
    A class represent day interface of advent of code puzzle
    """

    def __init__(self, inputs: Input):
        self.__inputs: Input = inputs
        self.__test_input = None

    def inputs(self) -> str:
        """
        Represents file contents or string content for testing and submission.
        """
        if self.__inputs is not None:
            if os.path.isfile(self.__inputs):
                return FileReader(self.__inputs).data
            else:
                if len(self.__inputs) == 0:
                    raise InvalidInput("String should not be empty")
                return self.__inputs
        raise InvalidInput("Input should be either str or file path")

    def part_one(self):
        ...

    def part_two(self):
        ...