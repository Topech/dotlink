##
# dotfile.py
##

import pathlib


##
# Class that represents a single dotfile
##
class Dotfile:
    desired_path = ""

    ## set path to dotfile 
    def __init__(self, path):

        self.desired_path = pathlib.Path(path)

        # check if given files are valid
        if not self.desired_path.is_file():
            raise FileNotFoundError("the dotfile could not be found")
