##
# dotfile.py
##

import pathlib


##
# Class that represents a single dotfile
##
class Dotfile:

    # TODO: name variable better
    name = None
    path = None
    targets = {}
    

    def __init__(self, file_path):
        """
        set path to dotfile 
        """
        
        # detect incorrect file_path type
        if not isinstance(file_path, pathlib.Path):
            raise TypeError("the given file_path is not a path type.")

        # check if given dotfile path is valid (there is a file there)
        if not file_path.is_file():
            raise FileNotFoundError("the dotfile could not be found")
        else:
            self.name = file_path.name
            self.path = pathlib.Path(file_path)



    def add_target(self, target):
        """
        adds a target to the dotfile. This will be used to get all targets
        related to a dotfile.
        """
        from dotlink import Target

        # detect any incorrect target by type
        if not isinstance(target, Target):
            error_msg = "{} is not of type Target"
            raise TypeError(error_msg)

        # add target to dotfile
        if not target.string in self.targets:
            self.targets[target.string] = target
        else:
            # it is expected that a target is only added to a dotlink if it is not already there.
            error_msg = "a duplicate target {} is attempted to be added to {}".format(target, self) 
            raise ValueError(error_msg)
        
        


    def __eq__(self, obj):
        """
        override the equals operator so dotfiles can be compared
        """

        # equality requires the dotfiles have the same name and both
        # objects are dotfile objects
        if isinstance(obj, Dotfile) and self.name == obj.name:
            return True
        else:
            return False



    def __ne__(self, obj):
        """
        override the not equals operator. the not of equals
        """

        return not __eq__(self, obj)


    
    def __str__(self):
        """
        override the string cnversion for dorfile
        """
    
        return "Dotfile({})".format(self.name)
