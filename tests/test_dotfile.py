import unittest

# use context to access dotlink 
from .context import dotlink
from dotlink import Dotfile



class TestDotfile(unittest.TestCase):
    """Test class that tests functionality of the dotfile class"""


    def setUp(self):
        self.test_repo = "tests/resources"
        self.test_linkmap = "tests/resources/test.linkmap"
        self.dotfile_path = "tests/resources/dotfile"



    def test_constructor(self):

        # run constructor with valid file paths, exception will raise if wrong
        Dotfile(self.dotfile_path, self.test_repo)        


        # ensure invalid dotfiles are caught
        with self.assertRaises(FileNotFoundError, msg='non-existant dotfile path not detected by Dotfile constructor'):
           Dotfile("FAKE-DOTFILE-PATH", self.test_repo)
        

        # ensure invalid repos are caught
        with self.assertRaises(NotADirectoryError, msg='non-existant repo not detected by Dotfile constructor'):
           Dotfile(self.dotfile_path, "FAKE-REPO")

        # asserts:
        # - file does exist == true
        # - file does not exist == false
    


    def test_is_linked(self):

        dotfile = Dotfile(self.dotfile_path, self.test_repo)        
                

        # asserts
        # - file is link (not broken) == true
        # - file is link (broken) == true
        # - file is not link == false
        pass






if __name__ == '__main__':
    unittest.main()
