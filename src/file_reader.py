# Praise Ye The LORD.

# Import libraries
import os

class FileReader:
    def __init__(self, path: str):
        self.__path = path 

    @property
    def data(self):
        current_dir = os.path.dirname(__file__)
        input_file = os.path.join(current_dir, self.__path)
        
        contents = ''
        with open(input_file, 'r') as file:
            contents += file.read()
        return contents.strip()

