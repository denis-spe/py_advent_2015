# Praise Ye The LORD.

# Import libraries
import os

class FileReader:
    def __init__(self, path: str):
        self.__path = path 

    @property
    def data(self):

        contents = ''
        with open(self.__path, 'r') as file:
            contents += file.read()
        return contents.strip()

