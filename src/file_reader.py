# Praise Ye The LORD.

# Import libraries


class FileReader:
    def __init__(self, path: str):
        self.__path = path 

    def data(self):
        contents = ''
        with open(self.__path, 'r') as file:
            contents += file.read()
        return contents

