# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('jotty')

from jotty_lib import Window
from jotty.AboutJottyDialog import AboutJottyDialog
from jotty.PreferencesJottyDialog import PreferencesJottyDialog

# See jotty_lib.Window.py for more details about how this class works
class JottyWindow(Window):
    __gtype_name__ = "JottyWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(JottyWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutJottyDialog
        self.PreferencesDialog = PreferencesJottyDialog

        # Code for other initialization actions should be added here.

