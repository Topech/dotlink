##
# linkmap.py
##

import pathlib
import json
import os
from dotlink.dotfile import Dotfile



class LinkMap:
    """
    Class for abstracting a linkmap file. Can be used to load or save linkmap files.

    A linkmap is a collection of destinations, each of which have a collection of dotfiles. 
    """


    _linkmap_dict  = dict()
        # a dictionary is used to store the map as it provides a convenient way of storing dotfiles
        # by destination and allows for indexing by strings.

    
    _map_loaded = False
        # this boolean flag stops the class entering an erroneous state where it attempts to link
        # dotfiles from a map that has not been loaded. 



    def load_json(self, filename):
        """
        loads the json file into a dictionary. fails if cannot read or json
        is malformed
        """

        # read the file given and store it as a linkmap. catch any exceptions and print more helpful 
        # error messages.
        try:
            with open(filename, 'r') as json_file:
                json_map = json.load(json_file)
        except IOError:
            print('error: json file {} doesn\'t exist or cannot be accessed'.format(filename))
            sys.exit()
        except json.JSONDecodeError:
            print('error: json file {} is malformed'.format(filename))
            sys.exit()


        # convert json_map elements from strings to objects
        for dest in json_map:
            dest_path = pathlib.Path(dest).expanduser()
    
            # check for invalid paths
            if not dest_path.is_dir():
                raise NotADirectoryError("destination path '{}' is not a directory or does not exist.". format(dest))

            # make an empty list for each destination and append dotfile objects to it
            self._linkmap_dict[dest_path] = []

            for filepath in json_map[dest]:
                dotfile = Dotfile(filepath)

                self.add_to_destination(dotfile, dest_path)


        self._map_loaded = True
    


    def save_json(self, filename):
        """
        save the linkmap contained in _linkmap_dict as a json file called `filename`
        """
        pass


    def add_to_destination(self, dotfile, destination):
        """
        add a dotfile to a destination in the linkmap
        """
    
        dest_path = pathlib.Path(destination)
    
        self._linkmap_dict[dest_path].append(dotfile)



                



########### Deprecieated code - needs to be converted to save_json


## 
# adds a dotfile to the json configuration file. This function can
# optionally be given a target directory to force dotlink to link
# 'dotfile' to a specific directory. If no target is specified, 
# dot file will be linked to the current working directory.
#
# TODO: automatically copy contents to repo?
##
def add_dotfile_to_json(dotfile, target=None):

    repo = load_repo_from_json(json_path)
    
    # set target if not specified
    if target == None:
        target = working_dir

    # compress user dir if present (helps with porting between users)
    target = compressuser(str(target))

    if target in repo:
        if dotfile not in repo[target]:
            repo[target].append(dotfile)
            verbose_print('\'' + dotfile + '\' added to repo')
        else:
            verbose_print('\'' + dotfile + '\' is already in repo') 
    else:
        # init a list in target
        repo[target] = [dotfile]
        verbose_print('\'' + dotfile + '\' added to repo at new target dir')

    # TODO: check it actually saved with no errors
    
    # save repo as json in json_path
    with open(json_path, 'w') as fp:
        json.dump(repo, fp, indent=4)   

    return repo
    


def compressuser(string):   
    home = str(pathlib.Path.home())
    r
