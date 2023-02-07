# Cleanparts

This python script reads a *snapcraft.yaml* file in the current folder,
or at *snap/* folder, finds all the parts listed there, and executes
a *snapcraft clean PARTS*.

This is similar to running *snapcraft clean*, but with the diference
that the container (when using LXC) is not destroyed, so the next build
will be faster because it won't need to recreate it, only the project's
parts.

## Installation

Just run *sudo setup.sh*, and you will be able to call *cleanparts.py*
from any snap project folder.

## Author

Sergio Costas  
sergio.costas@canonical.com
