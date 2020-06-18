# -*- coding: utf-8 -*-
"""
This is the `Main` window what describes the main logic of this gui.
It describes all input and text fields, buttons and more.
"""

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(446, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 411, 431))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        # First row: Folder path and open folder button
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        # Folder path to Minecraft world
        self.input_world_path = QtWidgets.QLineEdit(self.widget)
        self.input_world_path.setText("Open a Minecraft world folder...")
        self.input_world_path.setReadOnly(True)
        self.horizontalLayout.addWidget(self.input_world_path)
        # Open Minecraft world folder
        self.button_open_world = QtWidgets.QPushButton(self.widget)
        self.horizontalLayout.addWidget(self.button_open_world)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # Second row: Layout with input options like `Entity Limits` and `Process count`
        self.layout_input_options = QtWidgets.QGridLayout()
        # Entity Limits
        self.label_entity_limits = QtWidgets.QLabel(self.widget)
        self.layout_input_options.addWidget(self.label_entity_limits, 0, 0, 1, 1)
        self.spin_box_entity_limits = QtWidgets.QSpinBox(self.widget)
        self.spin_box_entity_limits.setMaximum(5000)
        self.spin_box_entity_limits.setValue(300)
        self.layout_input_options.addWidget(self.spin_box_entity_limits, 0, 1, 1, 1)
        # Processes Count
        self.spin_box_processes = QtWidgets.QSpinBox(self.widget)
        self.spin_box_processes.setValue(1)
        self.layout_input_options.addWidget(self.spin_box_processes, 0, 3, 1, 1)
        self.label_processes = QtWidgets.QLabel(self.widget)
        self.layout_input_options.addWidget(self.label_processes, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.layout_input_options)

        # Third row: Run buttons like `Delete all bad chunks`
        self.layout_run_options = QtWidgets.QGridLayout()
        # Delete all bad chunks
        self.button_delete_bad_chunks = QtWidgets.QPushButton(self.widget)
        self.button_delete_bad_chunks.setEnabled(False)
        self.layout_run_options.addWidget(self.button_delete_bad_chunks, 1, 0, 1, 1)
        # Delete all bad regions
        self.button_delete_bad_regions = QtWidgets.QPushButton(self.widget)
        self.button_delete_bad_regions.setEnabled(False)
        self.layout_run_options.addWidget(self.button_delete_bad_regions, 1, 1, 1, 1)
        # Replace all bad chunks
        self.button_replace_bad_chunks = QtWidgets.QPushButton(self.widget)
        self.button_replace_bad_chunks.setEnabled(False)
        self.layout_run_options.addWidget(self.button_replace_bad_chunks, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.layout_run_options)
        # Replace all bad regions
        self.button_replace_bad_regions = QtWidgets.QPushButton(self.widget)
        self.button_replace_bad_regions.setEnabled(False)
        self.layout_run_options.addWidget(self.button_replace_bad_regions, 2, 1, 1, 1)

        # Everything below
        self.button_start_world_scan = QtWidgets.QPushButton(self.widget)
        self.button_start_world_scan.setEnabled(False)
        self.verticalLayout.addWidget(self.button_start_world_scan)
        # Scan log output
        self.scan_output = QtWidgets.QTextEdit(self.widget)
        self.scan_output.setReadOnly(True)
        self.verticalLayout.addWidget(self.scan_output)
        # Progress bar
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 0)
        self.verticalLayout.addWidget(self.progressBar)

        # Menu bar at the top
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 21))
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        MainWindow.setMenuBar(self.menubar)
        self.menu_quit = QtWidgets.QAction(MainWindow)
        self.menu_about = QtWidgets.QAction(MainWindow)
        self.menu_open_backups = QtWidgets.QAction(MainWindow)
        self.menu_open_world = QtWidgets.QAction(MainWindow)
        self.menuFile.addAction(self.menu_open_world)
        self.menuTools.addAction(self.menu_open_backups)
        self.menuHelp.addAction(self.menu_quit)
        self.menuHelp.addAction(self.menu_about)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Minecraft Region Fixer"))
        self.button_open_world.setText(_translate("MainWindow", "Open"))
        self.label_entity_limits.setText(_translate("MainWindow", "Entity Limits"))
        self.label_processes.setText(_translate("MainWindow", "Processes"))
        self.button_delete_bad_chunks.setText(_translate("MainWindow", "Delete All Bad Chunks"))
        self.button_delete_bad_regions.setText(_translate("MainWindow", "Delete All Bad Regions"))
        self.button_replace_bad_regions.setText(_translate("MainWindow", "Replace All Bad Regions"))
        self.button_replace_bad_chunks.setText(_translate("MainWindow", "Replace All Bad Chunks"))
        self.button_start_world_scan.setText(_translate("MainWindow", "Start Scan"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menu_quit.setText(_translate("MainWindow", "Quit"))
        self.menu_quit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.menu_about.setText(_translate("MainWindow", "About"))
        self.menu_open_backups.setText(_translate("MainWindow", "Backups"))
        self.menu_open_world.setText(_translate("MainWindow", "Open"))
