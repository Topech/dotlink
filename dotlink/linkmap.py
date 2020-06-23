##
# linkmap.py
##

import pathlib
import json



class LinkMap:
    """
    Class for abstracting a linkmap file. Can be used to load or save linkmap files.

    A linkmap is a collection of desitinations, each of which have a collection of dotfiles. 
    """


    linkmap_dict  = dict()



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

        self.linkmap_dict = json_map 
        
    

    def save_json(self, filename):
        """
        save the linkmap contained in linkmap_dict as a json file called `filename`
        """
        pass






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
    home = str(Path.home())
    r
