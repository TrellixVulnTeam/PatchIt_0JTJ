"""
    PatchIt! -  the standard yet simple way to packaging and install mods for LEGO Racers
    Copyright 2013 Triangle717 <http://triangle717.wordpress.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
# PatchIt! V1.1.0 Unstable Modern Patch Creation code

import PatchIt, os, shutil, time
# Colored shell text
import color, color.colors as colors
# File/Folder Dialog Boxes
from tkinter import (filedialog, Tk)
# App Logging modules
import logging

# ------------ Begin Thumbs.db Check And Delete Code ------------ #

def delThumbs(inputfiles):
    '''Checks for and Deletes Thumbs.db'''

    # Traversing the files in each subfolder..
    logging.info("Walking through {0}...".format(inputfiles))
    for root, dir, files in os.walk(inputfiles):
        for item in files:

            # I've heard of a ethumbs.db file once before...
            if item.lower().endswith(".db"):
                logging.warning("Thumbs.db has been found!")

                '''Uncomment this to target just thumbs.db'''
                #if item.lower() == "thumbs.db":

                '''This will print upon every instance of thumbs.db. Not good. TODO: Fix it!'''
                #print('''\nI found Thumbs.db in your files. I will delete it for you in a few seconds.
#Don't worry, Windows will recreate it.\n''')

                '''Actually delete the file(s)'''
                logging.info("Deleting Thumbs.db (don't worry, Windows will recreate it. ;))")
                os.unlink(os.path.join(root, item))

# ------------ End Thumbs.db Check And Delete Code ------------ #


# ------------ Begin PatchIt! Patch Creation ------------ #

def patchDesc():
    '''Mod Description input and length check'''

    # Because I can't see how to do it any other way
    global desc
    logging.info("Ask for mod description")
    desc = input("Description: ")

    # 162 characters will mess up PatchIt! entirely
    if len(desc) > 161:
            logging.warning("The description is too longer - longer than 161 characters!")
            colors.pc("\nYour description is too long! Please write it a bit shorter.\n", color.FG_LIGHT_RED)
            # Loop back through the input if it is longer
            logging.info("Loop back through for shorter description (patchDesc())")
            patchDesc()
    else:
        logging.info("Your description fits into the 161 character limit")
        logging.info("Proceed back to writePatch()")
        # It fits into the limit, send it back to writepatch()
        return desc

def PatchInfo():
    '''Asks for PatchIt! Patch details'''

    logging.info("Create a PatchIt! Patch")
    colors.pc("\nCreate a {0} Patch\n".format(PatchIt.app), color.FG_LIGHT_YELLOW)

    # Tells the user how to cancel the process
    logging.info('Type "exit" in the "Name:" field to cancel the Patch Creation process.')
    print('Type "exit" in the "Name:" field to cancel.', end="\n")

    name = input("\nName: ")

    # I want to quit the process
    if name.lower() == "exit":
        logging.warning("User canceled PatchIt! Patch Creation!")
        colors.pc("\nCanceling creation of {0} Patch\n".format(PatchIt.app), color.FG_LIGHT_RED)
        time.sleep(0.5)
        logging.info("Proceeding to main menu")
        PatchIt.main()

    # I want to continue on
    logging.info("Ask for mod version")
    ver = input("Version: ")

    logging.info("Ask for mod author")
    author = input("Author: ")

    logging.info("Switching to patchDesc().")
    # See def patchDesc() above.
    patchDesc()

    # Draw (then withdraw) the root Tk window
    logging.info("Drawing root Tk window")
    root = Tk()
    logging.info("Withdrawing root Tk window")
    root.withdraw()

    # Overwrite root display settings
    logging.info("Overwrite root settings to (basically) completely hide it")
    root.overrideredirect(True)
    root.geometry('0x0+0+0')

    # Show window again, lift it so it can recieve the focus
    # Otherwise, it is behind the console window
    root.deiconify()
    root.lift()
    root.focus_force()

    # The files to be compressed
    # TODO: Make dialog active window automatically and do the same to main window when closed.
    inputfiles = filedialog.askdirectory(
    parent=root,
    title="Select the files you wish to compress"
    )

    # The user clicked the cancel button
    if len(inputfiles) == 0:

        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        logging.warning("User did not select any files to compress!")
        colors.pc("\nCannot find any files to compress!\n", color.FG_LIGHT_RED)
        time.sleep(1)
        logging.info("Proceeding to main menu")
        PatchIt.main()

    # The user selected files for Patch creation
    else:
        writePatch()


def writePatch():
    '''Writes and compresses PatchIt! Patch'''

    # The user selected a folder to compress
    # Give focus back to console window
    logging.info("Give focus back to console window")
    root.destroy()
    try:
        logging.info("User selected files at {0} for Patch compression".format(inputfiles))
        # Check for and delete thumbs.db
        logging.info("Switching to delThumbs(inputfiles)")
        delThumbs(inputfiles)

        # Write PiP file format, as defined in Documentation/PiP Format.md
        logging.info("Write {0}{1}.PiP using UTF-8 encoding with mod details".format(createname, createver))
        with open("{0}{1}.PiP".format(createname, createver), 'wt', encoding='utf-8') as createpatch:
            print("// PatchIt! Patch format, created by le717 and rioforce.", file=createpatch)
            print("[General]", file=createpatch)
            print(createname, file=createpatch)
            print("Version: {0}".format(createver), file=createpatch)
            print("Author: {0}".format(createauthor), file=createpatch)
            print("[Description]", file=createpatch)
            print("{0}".format(createdesc), file=createpatch)
            print("[ZIP]", file=createpatch)
            print("{0}{1}.zip".format(createname, createver), file=createpatch, end="")
            logging.info('''

                    // PatchIt! Patch format, created by le717 and rioforce.
                    [General]
                    {0}
                    Version: {1}
                    Author: {2}
                    [Description]
                    {3}
                    [ZIP]
                    {4}{5}.zip
                        '''.format(createname, createver, createauthor, createdesc, createname, createver))

        # Compress the files
        logging.info("Compress files located at {0} into a ZIP archive".format(inputfiles))
        zipfile = shutil.make_archive(inputfiles, format="zip", root_dir=inputfiles)

        # Rename the ZIP archive to createnamecreationver.zip, as defined in Documentation/PiP Format V1.1.md
        logging.info("Rename ZIP archive to {0}{1}.zip, as defined in {2}".format(createname, createver, "Documentation/PiP Format.md"))
        newzipfile = os.replace(zipfile, createname + createver + ".zip")

        # Declare the Patch and ZIP filenames
        patchfile = "{0}{1}.PiP".format(createname, createver)
        newzipfile = "{0}{1}.zip".format(createname, createver)
        logging.info("The final file names are {0} and {1}".format(patchfile, newzipfile))

        # Move the Patch and ZIP to the folder the compressed files came from
        logging.info("Moving {0} from {1} to {2}".format(patchfile, os.getcwd(), inputfiles))
        movepatch = shutil.move(patchfile, inputfiles)
        logging.info("Moving {0} from {1} to {2}".format(newzipfile, os.getcwd(), inputfiles))
        movezip = shutil.move(newzipfile, inputfiles)
        time.sleep(0.5)

        # The Patch was created sucessfully!
        logging.info("Exit code '0'")
        logging.info("{0} Version: {1} created and saved to {2}".format(createname, createver, inputfiles))
        print("\n{0} patch for {1} Version: {2} created and saved to\n{3}!\n".format(PatchIt.app, createname, createver, inputfiles))

    # The user does not have the rights to write a PiP in that location
    except PermissionError:
        logging.info("Error number '13'")
        logging.warning("{0} does not have the rights to save {1} {2}".format(PatchIt.app, createname, createver))
        colors.pc("\n{0} does not have the rights to create {1} {2}!\n".format(PatchIt.app, createname, createver), color.FG_LIGHT_RED)
        # TODO: Delete incomplete .PiP file here?

    # Python itself had some I/O error / any exceptions not handled
    except Exception:
        logging.info("Unknown error number")
        logging.warning("{0} ran into an unknown error while trying to create {1} {2}!".format(PatchIt.app, createname, createver))
        colors.pc("\n{0} ran into an unknown error while trying to create {1} {2}!\n".format(PatchIt.app, createname, createver), color.FG_LIGHT_RED)

    finally:
        # Sleep for 2 seconds after displaying creation result before kicking back to the PatchIt! menu.
        time.sleep(2)
        logging.info("Proceeding to main menu")
        PatchIt.main()

# ------------ End PatchIt! Patch Creation ------------ #