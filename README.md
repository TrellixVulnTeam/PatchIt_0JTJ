HEADS UP!
=========

If anyone has any remotes or links to this project, this is for you:

This repo will be renamed very soon to refelect the project's new name, and at that time, you will no longer be able to connect to it or reach it via any links. If you are unable to find this, please go back to [profile](https://github.com/le717), and get the new link from there. If you cannot contrib anymore, you'll need to reconnect to it.

PatchIt! Readme
===============

This is the readme to *PatchIt!*, a [Python 3](http://www.python.org) application written by le717 to provide a standard way of 
installing mods for the 1999 High Voltage Software PC game *LEGO Racers*.

The Plan
--------

Although *LEGO Racers* modding is still in it's early stages, many mods are already being developed, and there 
needs to be a standard way to install them. Heavily influenced and based on *Patchman*, a mod installer for 
the 1999 Data Design Interactive PC game *LEGO Rock Raiders*, *PatchIt!* aims to be a standard yet simple way 
to install *LEGO Racers* mods.

How It Works
------------

The three main goals for *PatchIt!* are as follows:

* Ask for *LEGO Racers* installation path, ensure it exists, and store it in a plain text file in the same folder as itself to be used for mod installation, and 
to create a completely portable application.
* Create  *PatchIt!* patches by entering the mod's name, version, and creator, and pointing it to the modded files. *PatchIt!* will automatically compress the 
files into a normal ZIP archive, and write the details to a plain text file ( * .PiP) using the mod's name and version as the filename.
* Install *PatchIt!* patches by selecting the * .PiP file, confirming the installation, and automatically decompressing the ZIP archive directly into the *LEGO 
Racers* installation.

Contribute
----------

If you would like to contribute to the development of *PatchIt!*, please be sure to read these few guidelines.

* As already stated, *PatchIt!* is written in Python 3, 3.3.0 to be exact. You will need to have a complete installation of Python 3.3.0 to commit to this repo. I will not be back-porting the to 2.7.

* Coming soon.

*PatchIt!* is copyright 2013 le717, and released under the GNU General Public License Version 3.