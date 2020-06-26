import unittest

# use context to access dotlink 
from .context import dotlink
from dotlink import LinkMap
from dotlink import Dotfile
import hashlib
from pathlib import Path



class TestLinkMap(unittest.TestCase):
    """Test class that tests functionality of the LinkMap class"""


    def setUp(self):
        self.filepath = Path('tests/resources/test.linkmap')
        self.dest_path = Path('~')
        


    def test_load_json(self):
          
        linkmap = LinkMap()

        # get hash of file before calling the load method to ensure the file is not changed by the method. 
        # TODO get working
        hash_before = 1 #hashlib.md5(self.filepath)


        # run the load_json method and test post-conditions
        linkmap.load_json(self.filepath)


        # check file not deleted or no longer accessible (unlikely)
        file_still_exists = self.filepath.exists()
        self.assertTrue(file_still_exists, msg='linkmap deleted after using the load method.')

        # check hashes before and after are same (check for changed mapfile, unlikely)
        # TODO get working
        hash_after = 1 #hashlib.md5(self.filepath)
        self.assertEqual(hash_before, hash_after)

        # all dotfiles in mapfile were captured (non-repeating)
        # TODO: make more accurate
        testfile_dotfiles = [ Dotfile('tests/resources/' + s) for s in ['linkmap_test_a', 'linkmap_test_b', 'linkmap_test_c'] ]
            # attempt to make a list of dotfile objects the same as that in the linkmap file

        self.assertEqual(testfile_dotfiles, linkmap._linkmap_dict[self.dest_path], msg='incorrect dotfiles extracted from mapfile')


        # all destinations detected (only 1)
        testfile_destinations = [self.dest_path]
        linkmap_destinations = list(linkmap._linkmap_dict.keys())
        self.assertEqual(linkmap_destinations, testfile_destinations)
    


        # FUTURE asserts
        # - dotfiles same name in same dest (repeating)
        # - no dotfiles in dest == empty list for dofile collection

        # - empty file == empty dest collection
        # - multiple dest detected
        # - 2 dest same name == some error



    def test_save(self):

        # asserts
        # - saved file = new mapfile created
        # - saved file = matches map (saved new)
        # - no file = new file made
        pass
