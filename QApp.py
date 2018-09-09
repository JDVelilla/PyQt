# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 19:00:15 2017

@author: TOSHIBA
"""
from PyQt4.QtGui import *
from PyQt4 import QtCore

from GUI.EMainWindow import EMainWindow
import sys

app=QApplication(sys.argv)
ventana=EMainWindow()
ventana.show()

sys.exit(app.exec_())

