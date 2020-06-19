import unittest

# use context to access dotlink 
from .context import dotlink
from dotlink import LinkMap



class TestLinkMap(unittest.TestCase):
    """Test class that tests functionality of the LinkMap class"""


    def setUp(self):
        pass


    def test_load(self):

        # asserts
        # - load == preset map object
        # - dotfiles == all in mapfile were detected and inited
        # - targets == correct targets
        pass


    def test_save(self):

        # asserts
        # - saved file = new mapfile created
        # - saved file = matches map (saved new)
        # - no file = new file made
        pass


