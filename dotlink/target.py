import pathlib
from dotlink import dotfile

class Target:

    string = None
    path = None
    dotfiles = dict()
    

    def __init__(self, path_str):

        # detect incorrect path_str type
        if not isinstance(path_str, pathlib.Path):
            raise TypeError("the given path is not a path type.")

        # check if given directory is valid
        if not path_str.is_dir():
            raise NotADirectoryError("the target directory could not be found")
        else:
            self.string = path_str
            self.path = pathlib.Path(path_str)

        
        
