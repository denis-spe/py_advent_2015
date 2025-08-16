# Praise Ye the LORD

# Import libraries
from functools import reduce
from typing import Any, Callable


class Stream:
    def __init__(self, inputs: Any):
        self.__inputs = inputs

    def map_(self, func: Callable):
        self.__inputs = map(func, self.__inputs)
        return self

    def tolist(self):
        self.__inputs = list(self.__inputs)
        return self

    def reduce_(self, func: Callable):
        self.__inputs = reduce(func, self.__inputs)
        return self

    def sum_(self):
        return sum(self.__inputs)

    def flat_map_(self, func: Callable):
        self.__inputs = func(self.__inputs)
        return self

    def show_result(self):
        return self.__inputs