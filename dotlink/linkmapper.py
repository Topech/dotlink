##
# linkmap.py
##



##
# Class that abstracts a linkmap that can be used to link dotfiles throughout a system.
class linkmap:
    repo = ""
    dotfile_list = ""
    linkmap_file = ""

    def __init__(self, linkmap_file):
        self.linkmap_file = linkmap_file


    def load()
        print('load file stub!')






##
# loads the json file into a dictionary. fails if cannot read or json
#  is malformed 
##
def load_repo_from_json(filename):
    try:
        with open(filename, 'r') as json_file:
            repo = json.load(json_file)
    except IOError:
        print('error: json file {} doesn\'t exist'.format(filename))
        sys.exit()
    except json.JSONDecodeError:
        print('error: json file {} is malformed'.format(filename))
        sys.exit()
    return repo
    


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
    return string.replace(home, '~')
