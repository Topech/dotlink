##
# linkmap.py
##

import pathlib
import json
import os
from dotlink.dotfile import Dotfile
from dotlink.target import Target



def load_from_json(filename):
    """
    loads the json file into a dictionary. fails if cannot read or json
    is malformed
    """

    # read the file given and store it as a linkmap
    json_map = None
    with open(filename, 'r') as json_file:
        json_map = json.load(json_file)
            # raises IOError for unaccessible or non-existant files
            # raises json.JSONDecodeError for malformed json files
        return json_map



def convert_from_json(json_map):
    """
    check that all given target paths are valid, and check that all dotfiles
    can be found/exist in relevant directory.
    """

    dotfiles = dict()
    targets = dict()

    # convert json_map elements from strings to objects
    for target in json_map:
        target_path = pathlib.Path(target).expanduser()

        # check for invalid target paths
        if not target_path.is_dir():
            raise NotADirectoryError("target path '{}' is not a directory or does not exist.". format(target))
        else:
            targets[target_path] = Target(target_path)
            
        # check for invalid dotfiles
        for filepath in json_map[target]:
            dotfile_path = pathlib.Path(filepath)
            if not dotfile_path.exists():
                raise FileNotFoundError("could not find dotfile '{}'.".format(dotfile_path))
            else:
                dotfiles[filepath] = Dotfile(dotfile_path)

    return dotfiles, targets
        


    



def save_json(filename):
    """
    save the linkmap contained in _linkmap_dict as a json file called `filename`
    """
    pass




                



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
