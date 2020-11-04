import unittest

# use context to access dotlink 
from .context import dotlink
from dotlink import Dotfile
from pathlib import Path
import hashlib
import os




class TestLinker(unittest.TestCase):

    # design good test
    def test__link_dotfile(self):
        
        dotfile = self.expected_dotfiles[0]
        dest = self.expected_destinations[0]

        self.linkmap._link_dotfile(dotfile, dest)

        ## check that link has been made
        self.assertTrue(self.expected_link.is_symlink())

        ## delete linked file to avoid clutter
        if self.expected_link.is_symlink():
            os.system('rm {}'.format(self.expected_link.as_posix()))

