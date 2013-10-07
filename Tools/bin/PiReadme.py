#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This file is part of PatchIt!

    PatchIt! - the standard and simple way to package and install mods
    for LEGO Racers

    Created 2013 Triangle717 <http://Triangle717.WordPress.com/>

    PatchIt! is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PatchIt! is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with PatchIt! If not, see <http://www.gnu.org/licenses/>.

-------------------------------------
Download latest PatchIt! Readme from
<https://github.com/le717/PatchIt/tree/gh-pages/>
"""

import os
import sys
import distutils.dir_util
import zipfile
from urllib.error import HTTPError

# Import wget from parent directory since the script is being run standalone
# Since I can't run `from Tools.wget import wget`
try:
    parentdir = "../wget"
    # Not happy with editing sys.path... >:(
    sys.path.insert(0, parentdir)
    import wget

# The script is being run from the main setup.py, so import from different loc
except ImportError:
    from Tools.wget import wget

curDir = os.getcwd()
zip_link = "https://github.com/le717/PatchIt/archive/gh-pages.zip"
# Define proper name of Zip archive, as the download link doesn't provide it
zip_name = "PatchIt-gh-pages.zip"
# Location to save the Readme
save_path = os.path.join("../..", "Documentation", "Readme")


# Download the readme from the gh-pages branch
try:
    wget.download(zip_link)
    halt = False

# We can't download it right now, so end the process
except HTTPError:
    print("\nPatchIt! Readme cannot be downloaded at this time.\n")
    halt = True

if not halt:
    # Remove the directory for a clean slate
    if os.path.exists(save_path):
        distutils.dir_util.remove_tree(save_path)

    # Extract the zip to the proper location
    with zipfile.ZipFile(zip_name, "r") as extract:
        extract.extractall(path=save_path)

    # Delete the zip archive
    os.unlink(zip_name)

    # Copy the files out of the subfolder
    distutils.dir_util.copy_tree(os.path.join(save_path, "PatchIt-gh-pages"),
                                 save_path)

    # Remove all the unneeded files/folders
    distutils.dir_util.remove_tree(os.path.join(save_path, "PatchIt-gh-pages"))
    distutils.dir_util.remove_tree(os.path.join(save_path, "Documentation"))
    distutils.dir_util.remove_tree(os.path.join(save_path, "Site-Project"))
    os.unlink(os.path.join(save_path, ".gitignore"))
    os.unlink(os.path.join(save_path, ".gitattributes"))

    # And we're done!
    print("\n\nPatchIt! Readme has been successfully downloaded.\n")
