##
# cli.py
##

import argparse



##
def process_args():
    """process cli options and return object holding the status for each object"""

    #TODO: -l --link [FILE] 
    #TODO: -d --dir 
    #TODO: ADD
    #TODO: REMOVE
    #TODO: LIST

    # App description
    desc = '''Dotlink allows the automation of deploying dotfiles to their desired 
            locations on linux systems. It takes advantage of file symlinks to easily keep
            track of changes to files in your dotfiles repository.
            '''
    # help messages: 
    verbose_help     = 'Print more verbose statements'
    force_help       = 'Force overriding existing files'
    interactive_help = 'Ask before removing files'
    repo_help        = 'Specify a path to the repo holding the dotfiles'
    add_help         = 'Add FILE(s) to dotlink'

    # init parser and add arg opts
    parser = argparse.ArgumentParser(description = desc)
    parser.add_argument("-v", "--verbose", help=verbose_help, action='store_true')
    parser.add_argument("-f", "--force", help=force_help, action='store_true')
    parser.add_argument("-i", "--interactive", help=interactive_help, action='store_true')
    parser.add_argument("-r", "--repo", help=repo_help, nargs=1, metavar='DIR')
    #parser.add_argument("-l", "--link", metavar="FILE", nargs='?', help="link the given file to the correct position")
    parser.add_argument("-a", "--add", help=add_help, nargs='+', metavar='FILE')
    args = parser.parse_args()

    return args

#    # set repo path
#    if args.repo != None:
#        new_repo = G_args.repo[0]
#        verbose_print('changing repo dir to \'' + str(new_repo) + '\'')
#        repo_dir = Path(new_repo)
#        json_path = repo_dir / Path('lm.json')



def ask(message):
    """ask a question through the command line, return true for yes or false for no."""
    yes = ['y', 'yes', 'Y', 'YES']
    no = ['n', 'no', 'No', 'NO', 'N']
    resp = input(message)

    if resp in yes:
        return True    
    elif resp in no:
        return False
    else:
        print('error: invalid response')
        return ask(message)
