import unittest

# use context to access dotlink 
from .context import dotlink
from dotlink import LinkMap



class TestLinkMap(unittest.TestCase):
    """Test class that tests functionality of the LinkMap class"""


    def setUp(self):
        self.filename = 'tests/resources/test.linkmap'


    def test_constructor(self):

       with self.assertRaises(FileNotFoundError, msg='invalid linkmap name not detected by LinkMap constructor'):
            linkmap = LinkMap("fake-linkmap-filename")
        

    def test_load(self):

        # asserts
        # - load == preset map object
        # - dotfiles == all in mapfile were detected and initted
        # - targets == correct targets
        pass


    def test_save(self):

        # asserts
        # - saved file = new mapfile created
        # - saved file = matches map (saved new)
        # - no file = new file made
        pass


