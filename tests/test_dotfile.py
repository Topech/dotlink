import unittest

# use context to access dotlink 
from .context import dotlink
from dotlink import Dotfile
import pathlib



class TestDotfile(unittest.TestCase):
    """Test class that tests functionality of the dotfile class"""


    def setUp(self):
        self.dotfile_path = pathlib.Path("tests/resources/dotfile")


    def test_constructor(self):
        # run constructor with valid file paths, exception will raise if wrong
        dotfile = Dotfile(self.dotfile_path)

        # ensure invalid dotfiles are caught (assert to catch an expected raise
        with self.assertRaises(FileNotFoundError, msg='non-existant dotfile path not detected by Dotfile constructor'):
            fake_path = pathlib.Path("FAKE-DOTFILE-PATH")
            Dotfile(fake_path)
        
        # ensure non path types raise a type error
        with self.assertRaises(TypeError, msg='non path given to dotfile not detected'):
            Dotfile("not a path type")
    


if __name__ == '__main__':
    unittest.main()
