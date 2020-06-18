# -*- coding: utf-8 -*-
"""
This window is only a placeholder for the upcoming 'Backups' window.
"""

from PyQt5 import QtCore, QtWidgets


class Ui_Backups(object):
    def setupUi(self, Backups):
        Backups.setObjectName("Backups")
        Backups.resize(300, 90)
        self.verticalLayout = QtWidgets.QVBoxLayout(Backups)
        self.verticalLayout.setObjectName("verticalLayout")
        self.not_finished_text = QtWidgets.QPlainTextEdit(Backups)
        self.not_finished_text.setObjectName("not_finished_text")
        self.verticalLayout.addWidget(self.not_finished_text)

        self.retranslateUi(Backups)
        QtCore.QMetaObject.connectSlotsByName(Backups)

    def retranslateUi(self, Backups):
        _translate = QtCore.QCoreApplication.translate
        Backups.setWindowTitle(_translate("Backups", "Backups"))
        self.not_finished_text.setPlainText(_translate("Backups", "The implementation is not yet completely finished."))
