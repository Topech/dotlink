import pathlib
from dotlink.dotfile import Dotfile

class Target:

    string = None
    path = None
    dotfiles = {}
    

    def __init__(self, path_str):
        """
        create a new target instance, with a path to the target directory.
        """
        # detect incorrect path_str type
        if not isinstance(path_str, pathlib.Path):
            raise TypeError("the given path is not a path type.")

        # check if given directory is valid
        if not path_str.is_dir():
            raise NotADirectoryError("the target directory could not be found")
        else:
            self.string = path_str
            self.path = pathlib.Path(path_str)

        
    def add_dotfile(self, dotfile):
        """
        add a relationship to a set of dotfiles, this will fail if there is
        already a dotfile with the name in it.
        """
        if not isinstance(dotfile, Dotfile):
            error_msg = "{} is not a dotfile".format(dotfile)
            raise TypeError(error_msg)

        if not dotfile.name in self.dotfiles:
            self.dotfiles[dotfile.name] = dotfile
        else:
            error_msg = "a duplicate dotfile {} is attempted to be added to {}".format(dotfile, self) 
            raise ValueError(error_msg)
        
