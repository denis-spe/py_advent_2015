# Bless be the LORD of host
from src.file_reader import FileReader
from src.types import Input
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

    @property
    def inputs(self) -> str:
        """
        Represents file contents or string content for testing and submission.
        """
        if self.__inputs is not None:
            if self.__inputs.startswith("day"):
                self.__inputs = os.path.join(os.path.dirname(__file__), self.__inputs)

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