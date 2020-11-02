
    def _link_dotfile(self, dotfile, destination):
        """
        link a given dotfile to a specified destination in the filesystem.
        """

        if (self._map_loaded == False):
            # TODO: fail if map has not been loaded
            pass    

        # pre conditions:
        # - dotfile is of type Dotfile
        # - destination is of type Path
        # - destination exists and is a directory
        # - destination does not contain file with name of dotfile

        # convert dotfile and destination to a link command
        dotfile_str = dotfile.path.as_posix() 
        dest_str = pathlib.Path(destination).expanduser().as_posix()
        command = "ln -s {} {}". format(dotfile_str, dest_str)

        # run link command
        os.system(command)

        # post condidtions:
        # - dotfile is linked in destination



    def link_all_dotfiles(self):
        """
        links all dotfiles in a linkmap to their respective destinations.
        """

        if (self._map_loaded == False):
            # TODO: fail if map has not been loaded
            pass


        # iterate through each destination and link its respective dotfile
        for dest in self._linkmap_dict:
            for dotfile in self._linkmap_dict[dest]:
                self._link_dotfile(dotfile, dest)
