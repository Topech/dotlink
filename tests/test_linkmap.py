import unittest

# use context to access dotlink 
from .context import dotlink
import dotlink.linkmap as linkmap
from dotlink import Dotfile, Target
from pathlib import Path
import hashlib
import os
import json




class TestLinkMap(unittest.TestCase):
    """Test class that tests functionality of the LinkMap class"""


    def setUp(self):

        ## Get Linkmap for testing
        
        self.linkmap_path = Path('tests/resources/test.linkmap')

        # get hash of file before calling the load method to ensure the file is not changed by the method. 
        # TODO get working
        #self.expected_hash = hashlib.md5(self.linkmap_path)

        # expected values to be extracted from the linkmap
        self.expected_dotfiles = [ 'tests/resources/' + s for s in ['linkmap_test_a', 'linkmap_test_b', 'linkmap_test_c'] ]
        self.expected_targets = ['~']

      

    def test_load_from_json(self):

        # try a non-existant linkmap file 
        with self.assertRaises(IOError, msg='load_from_json does not raise a FileNotFoundError for non-existant files'):
            linkmap.load_from_json("fake-file-name.linkmap")

        # todo: try a file without read permissions

        
        # try a malformed linkmap file
        with self.assertRaises(json.JSONDecodeError, msg='a malformed linkmap was not detected'):
            linkmap.load_from_json('tests/resources/malformed.linkmap')


        # run load_from_json on a correct linkmap file
        json_in = linkmap.load_from_json(self.linkmap_path)
        # todo: catch unexpected raises? (ie, should i try catch when i am not
        # testing for it?)
        self.assertIsNotNone(json_in, msg='load_from_json does not return a correct linkmap when called')

        # Check dotfiles extracted are correct
        actual_dotfiles = json_in[self.expected_targets[0]]
        self.assertEqual(self.expected_dotfiles, actual_dotfiles, msg='some or all dotfiles were not extracted or parsed properly.')

        # Check all targets detected (case of only 1 target)
        actual_targets = list(json_in.keys())
        self.assertEqual(self.expected_targets, actual_targets, msg='some or all destinations not extracted or parsed properly.')

        ## check hashes before and after are same (check for changed mapfile, unlikely)
        # TODO get working
        #actual_hash = hashlib.md5(self.linkmap_path)
        #self.assertEqual(self.expected_hash, actual_hash)

           
        # FUTURE asserts
        # - dotfiles same name in same target (repeating)
        # - no dotfiles in dest == empty list for dofile collection

        # - empty file == empty dest collection
        # - multiple dest detected
        # - 2 dest same name == some error



    
    def test_convert_from_json(self):
        """
        tests if converting to dotfiles and targets works. 
        """

        # load in json
        json_in = linkmap.load_from_json(self.linkmap_path)

        # get a list of expected dotfiles
        dotfile_list = [ Dotfile(Path(df_str)) for df_str in self.expected_dotfiles ] 
        target_list = [ Target(Path(target_str)) for target_str in self.expected_targets ] 

        # call convert_from_json and populate the dict storages
        dotfiles, targets = linkmap.convert_from_json(json_in)

        extracted_dotfiles = list(dotfiles.values())
        extracted_targets = list(targets.values())

        # check all expected dotfiles are found
        error_msg = 'the extracted dotfiles are not as expected (either incorrectly converted or missing dotfiles)'
        self.assertEqual(extracted_dotfiles, dotfile_list, msg=error_msg)
        
        error_msg = 'the extracted targets are not as expected (either incorrectly converted or missing targets)'
        self.assertEqual(extracted_targets, target_list, msg=error_msg)



    def test_save(self):

        # asserts
        # - saved file = new mapfile created
        # - saved file = matches map (saved new)
        # - no file = new file made
        pass
