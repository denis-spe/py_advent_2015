# Praise Ye The LORD.

# Import libraries.
import unittest
import os, sys
sys.path.append(sys.path[0].replace('tests', ''))

from src.file_reader import FileReader

class TestFileReader(unittest.TestCase):
    def setUp(self):
        self.file_reader = FileReader(
            '/data/data/com.termux/files/home/Py/py_advent_2015/src/day1/input.text'
            )

    def test_data(self):
        self.assertIn('()', self.file_reader.data())

if __name__ == '__main__':
    unittest.main()
