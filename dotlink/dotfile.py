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
    

    def __init__(self, path):
        """
        set path to dotfile 
        """

        self.path = pathlib.Path(path)
        self.name = self.path.name

        # check if given files are valid
        if not self.path.is_file():
            raise FileNotFoundError("the dotfile could not be found")



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
