import unittest

# use context to access dotlink 
from .context import dotlink
from dotlink import LinkMap
from dotlink import Dotfile
from pathlib import Path
import hashlib
import os




class TestLinkMap(unittest.TestCase):
    """Test class that tests functionality of the LinkMap class"""


    def setUp(self):

        ## Get Linkmap for testing
        
        self.linkmap_path = Path('tests/resources/test.linkmap')

        # get hash of file before calling the load method to ensure the file is not changed by the method. 
        # TODO get working
        self.expected_hash = 1 #hashlib.md5(self.linkmap_path)

        # extract linkmap from file 
        self.linkmap = LinkMap()
        self.linkmap.load_json(self.linkmap_path)

        # expected values to be extracted from the linkmap
        self.expected_dotfiles = [ Dotfile('tests/resources/' + s) for s in ['linkmap_test_a', 'linkmap_test_b', 'linkmap_test_c'] ]
        self.expected_destinations = [Path('~').expanduser()]


        ## calculate links that should be made given dotfiles and destinations

        self.expected_link = Path(self.expected_destinations[0]).joinpath(self.expected_dotfiles[0].name)



    def test_load_json(self):
          
        ## check hashes before and after are same (check for changed mapfile, unlikely)
        # TODO get working
        actual_hash = 1 #hashlib.md5(self.linkmap_path)
        self.assertEqual(self.expected_hash, actual_hash)

        ## check file not deleted or no longer accessible (unlikely)
        file_still_exists = self.linkmap_path.exists()
        self.assertTrue(file_still_exists, msg='linkmap deleted after using the load method.')

        ## Check dotfiles extracted are correct
        actual_dotfiles = self.linkmap._linkmap_dict[self.expected_destinations[0].expanduser()]
        self.assertEqual(self.expected_dotfiles, actual_dotfiles, msg='some or all dotfiles were not extracted or parsed properly.')

        ## Check all destinations detected (linkmap only has 1)
        actual_destinations = list(self.linkmap._linkmap_dict.keys())
        self.assertEqual(self.expected_destinations, actual_destinations, msg='some or all destinations not extracted or parsed properly.')
    
        # FUTURE asserts
        # - dotfiles same name in same dest (repeating)
        # - no dotfiles in dest == empty list for dofile collection

        # - empty file == empty dest collection
        # - multiple dest detected
        # - 2 dest same name == some error



    def test__link_dotfile(self):
        
        dotfile = self.expected_dotfiles[0]
        dest = self.expected_destinations[0]

        self.linkmap._link_dotfile(dotfile, dest)

        ## check that link has been made
        self.assertTrue(self.expected_link.is_symlink())

        ## delete linked file to avoid clutter
        if self.expected_link.is_symlink():
            os.system('rm {}'.format(self.expected_link.as_posix()))

        


    def test_save(self):

        # asserts
        # - saved file = new mapfile created
        # - saved file = matches map (saved new)
        # - no file = new file made
        pass
