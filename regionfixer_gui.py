#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets
from gui.gui import MainWindow

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()
