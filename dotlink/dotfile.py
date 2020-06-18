##
# dotfile.py
##


##
# Class that represents a single dotfile
##
class dotfile:
    desired_path = ""
    repo = ""

    ## set path to dotfile 
    def __init__(self, path, repo):
        self.desired_path = path
        self.repo = repo 


