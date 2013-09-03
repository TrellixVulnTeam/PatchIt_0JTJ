# -*- coding: utf-8 -*-
# <pep8-80 compliant>
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
"""
# PatchIt! V1.1.2 Unstable RunAsAdmin Intergration

import os
import subprocess

# Tkinter GUI library
from tkinter import Tk
from tkinter.messagebox import (showerror, askyesno)

# App Logging
import logging

# PatchIt! "Constants"
import constants


class AdminRun(object):
    """Invokes the RunAsAdmin helper utility"""

    def __init__(self):
        """Draw (then withdraw) root Tkinter window"""
        global __root
        __root = Tk()
        __root.withdraw()
        __root.iconbitmap(constants.app_icon)

    def launch(self, message):
        """Relaunch PatchIt! with administrator rights"""

        __admin = askyesno("Relaunch PatchIt?",
    '''{0}
Would you like to relaunch PatchIt! with Administrator rights?'''.format(
    message))

        # User does not want to relaunch PatchIt!
        if not __admin:
            logging.info("User does not want to relaunch PatchIt!")
            __root.destroy()  # lint:ok
            return False

        # If user wants to relaunch
        else:
            logging.info("User wants to relaunch PatchIt!")

            # This is the raw Python script. RunAsAdmin will not work
            if (constants.exe_name.endswith("py") or
                    constants.exe_name.endswith("pyw")):
                logging.warning('''This is the raw PatchIt! Python script ({0})
RunAsAdmin.exe cannot operate!'''.format(constants.exe_name))

                showerror("Running Error!",
    '''You are running the raw PatchIt! Python script ({0}).
RunAsAdmin will not work at all.'''.format(constants.exe_name))
                __root.destroy()  # lint:ok
                return False

            # Launch RunAsAdmin to reload PatchIt!
            else:
                logging.info('''This is the PatchIt! exe ({0}).
Launching RunAsAdmin.exe'''.format(constants.exe_name))

                subprocess.call(
                    [os.path.join(constants.app_folder, "RunAsAdmin.exe"),
                        constants.exe_name])

                # Now we close PatchIt!, and let RunAsAdmin take over
                # (that is, if this is an exe)
                __root.destroy()  # lint:ok
                logging.shutdown()
                raise SystemExit(0)
