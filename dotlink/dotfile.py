##
# dotfile.py
##

import pathlib


##
# Class that represents a single dotfile
##
class Dotfile:
    desired_path = ""
    repo = ""

    ## set path to dotfile 
    def __init__(self, path, repo):

        self.desired_path = pathlib.Path(path)
        self.repo = pathlib.Path(repo)

        # check if given files are valid
        if not self.desired_path.is_file():
            raise FileNotFoundError("the dotfile could not be found")

        if not self.repo.is_dir():
            raise NotADirectoryError("the repo given does not exist or is not a directory")
