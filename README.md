# Dotlink
Dotlink allows the automation of deploying dotfiles to their desired locations on linux systems. It takes advantage of file symlinks to easily keep track of changes to files in your dotfiles repository.

You can use dotlink to link whole directories as well (for example `~/.config/i3/`) so that all changes within that directory are present in the dotfile repo. 

## Linkmap
The heart of the program is the linkmap file. This is a repo-specific configuration file that dictates where each dotfile is to be linked (it's target directory). This is to be placed in a traditional dotfile repo. Currently this file must be named lm.json but this should be fixed soon.

## Program Flags
```
optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         be verbose during execution
  -f, --force           force overriding existing files
  -i, --interactive     ask before removing files
  -r DIR, --repo DIR    specify a path to the repo holding the dotfiles
  -a FILE [FILE ...], --add FILE [FILE ...]
                        add FILE(s) to dotlink
```

### Changing Repo Directory
Dotlink assumes that the dotfile repo is at the current working directory. If this is not the case, you can use the `-r` or `--repo` flag to specify the dotfile repo. This is particularly helpful (Currently mandatory) when using the add command. I hope to make a config file for dotlink that can hold this information soon so that this flag is no longer needed.

### Adding To the Repo
You can add a dotfile (or directory) with the `-a` or `--add`flag. This will automatically add it to the linkmap in the dotfile repo. In the future I plan to make this command automatically copy the added dotfile to the repository (and possibly automatically link it in doing so).



