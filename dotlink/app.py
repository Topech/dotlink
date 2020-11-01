##
# app.py
## 

import dotlink.cli as cli
import load_json from dotlink.linkmap


def run():
    args = cli.process_args();

    dotfiles = dict()
    targets = dict()


