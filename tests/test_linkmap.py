import unittest

# use context to access dotlink 
from .context import dotlink
from dotlink import LinkMap
import hashlib
from pathlib import Path



class TestLinkMap(unittest.TestCase):
    """Test class that tests functionality of the LinkMap class"""


    def setUp(self):
        self.filepath = Path('tests/resources/test.linkmap')



    def test_constructor(self):

        # ensure invalid filepaths for Linkmaps raise FileNotFoundError
        with self.assertRaises(FileNotFoundError, msg='invalid linkmap name not detected by LinkMap constructor'):
            linkmap = LinkMap("fake-linkmap-filename")
        


    def test_load(self):

          
        linkmap = LinkMap(self.filepath)

        # get hash of file befor calling the load method to ensure the file is not changed by the method. 
        hash_before = hashlib.md5(self.filepath)

        # call the load method
        linkmap.load()

        # post-conditions to test.
        file_still_exists = self.filepath.exists()
        hash_after = hashlib.md5(self.filepath)

        # ensure that the linkmap file is not deleted after calling load (unlikely)
        self.assertTrue(file_still_exists, msg='linkmap deleted after using the load method.')

        # ensure the linkmap file is not changed after calling load (unlikely)
        self.assertEquals(hash_before, hash_after)

        # asserts
        # - dotfiles == all in mapfile were detected and initted
        # - targets == correct targets
        pass



    def test_save(self):

        # asserts
        # - saved file = new mapfile created
        # - saved file = matches map (saved new)
        # - no file = new file made
        pass


