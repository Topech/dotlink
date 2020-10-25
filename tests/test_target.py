import unittest

# use context to access dotlink 
from .context import dotlink
from dotlink import Target
import pathlib



class TestDotfile(unittest.TestCase):
    """Test class that tests functionality of the dotfile class"""


    def setUp(self):
        self.target_path = pathlib.Path("tests/resources/target_dir")


    def test_constructor(self):
        # run constructor with valid file paths, exception will raise if wrong
        target = Target(self.target_path)

        # ensure invalid directories are caught (assert to catch an expected raise)
        with self.assertRaises(NotADirectoryError, msg='non-existant targer dir was not detected by targer constructor'):
            fake_path = pathlib.Path("FAKE-DOTFILE-PATH")
            target = Target(fake_path)
        
        # ensure non path types raise a type error
        with self.assertRaises(TypeError, msg='non path given to target constructor not detected'):
            Target("not a path type")



if __name__ == '__main__':
    unittest.main()
