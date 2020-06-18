import unittest

# use context to access dotlink 
from .context import dotlink



class TestDotlink(unittest.TestCase):
    
    def test_test(self):
        self.assertEqual(1,1);

    
    #TODO: figure out what to test amd how to layout test classes/files




class TestDotfile(unittest.TestCase):
    """Test class that tests functionality of th dotfile class"""

    def setUp(self):
        self.repo = "~/tests/resources"


    def test_constructor(self):
        dotfile_path = ".test_dotfile"
        dotfile = dotlink.dotfile.dotfile(dotfile_path, self.repo)
        
        #TODO: test erroneous dotfiles for exeptions
        self.assertIsNotNone(dotfile, msg="constructer creates valid object")


    def test_exists(self):
        dotfile_path = ".test_dotfile"

        # asserts:
        # - file does exist == true
        # - file does not exist == false
    

    def test_already_linked(self):
        
        # asserts
        # - file is link (not broken) == true
        # - file is link (broken) == true
        # - file is not link == false


if __name__ == '__main__':
    unittest.main()
