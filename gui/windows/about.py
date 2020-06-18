# -*- coding: utf-8 -*-
"""
Small window for `About` with general project/program information,
such as the github or minecraftforum link for support and more.
"""
import webbrowser
from functools import partial

from PyQt5 import QtCore, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(450, 250)
        self.verticalLayout = QtWidgets.QVBoxLayout(About)
        self.verticalLayout.setObjectName("verticalLayout")

        # Text field (with project information)
        self.text_field = QtWidgets.QPlainTextEdit(About)
        self.text_field.setReadOnly(True)
        self.text_field.setObjectName("text_field")
        self.verticalLayout.addWidget(self.text_field)

        # Minecraft Forum button
        self.minecraftforum_button = QtWidgets.QPushButton(About)
        self.minecraftforum_button.setObjectName("minecraftforum_button")
        self.verticalLayout.addWidget(self.minecraftforum_button)
        self.minecraftforum_button.clicked.connect(partial(self.open_url, "http://www.minecraftforum.net/topic/302380-minecraft-region-fixer"))

        # Github button
        self.github_button = QtWidgets.QPushButton(About)
        self.github_button.setObjectName("github_button")
        self.verticalLayout.addWidget(self.github_button)
        self.github_button.clicked.connect(partial(self.open_url, "https://github.com/Fenixin/Minecraft-Region-Fixer"))

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))
        self.text_field.setPlainText(_translate("About",
                                                "Minecraft Region Fixer\n"
                                                "\n"
                                                "Program to check the integrity of Minecraft worlds and fix them when possible.\n"
                                                "It uses NBT by twoolie. Author: Alejandro Aguilera (Fenixin)\n"))
        self.minecraftforum_button.setText(_translate("About", "Minecraft Forum"))
        self.github_button.setText(_translate("About", "Github"))

    @staticmethod
    def open_url(url):
        webbrowser.open(url)
