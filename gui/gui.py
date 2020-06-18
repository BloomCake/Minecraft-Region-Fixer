#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Here functionalities are added to the different windows.
The windows are also linked with each other.

Currently it is not yet very nice, but the basic functions work.
"""

from os.path import expanduser
from time import sleep

from PyQt5 import QtWidgets

from .windows.main import Ui_MainWindow
from .windows.about import Ui_About
from .windows.backups import Ui_Backups

from regionfixer_core import world
from regionfixer_core.world import World
from regionfixer_core.scan import (AsyncWorldRegionScanner,
                                   AsyncDataScanner,
                                   ChildProcessException)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # General and region fixer specific variables
        self.world = None

        self.setupUi(self)

        # Menu: Quit Trigger
        self.menu_quit.triggered.connect(self.close)
        # Connect to Open world actions
        self.menu_open_world.triggered.connect(self.open_world)
        self.button_open_world.clicked.connect(self.open_world)

        # Connect to scan actions
        self.button_start_world_scan.clicked.connect(self.start_scan)
        self.button_delete_bad_chunks.clicked.connect(self.start_delete_chunks)
        self.button_delete_bad_regions.clicked.connect(self.start_delete_regions)
        self.button_replace_bad_chunks.clicked.connect(self.start_replace_chunks)
        self.button_replace_bad_regions.clicked.connect(self.start_replace_regions)

        self.menu_about.triggered.connect(self.open_about)
        self.menu_open_backups.triggered.connect(self.open_backups)

    def open_about(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_About()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def open_backups(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_Backups()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def open_world(self):
        """Called with every action to open/choose a Minecraft world folder."""
        world_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Chosse a Minecraft world folder", expanduser("~"))

        world = World(world_path)
        if not world.isworld:
            self.update_button_status(False)
            error_msg = QtWidgets.QMessageBox()
            error_msg.setIcon(QtWidgets.QMessageBox.Warning)
            error_msg.setWindowTitle("Minecraft world folder")
            error_msg.setText("This directory doesn't look like a Minecraft world folder.")
            error_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            error_msg.exec_()
        else:
            self.world = world
            self.input_world_path.setText(self.world.path)
            self.update_button_status(True)

    def update_button_status(self, state):
        self.button_start_world_scan.setEnabled(state)
        self.button_delete_bad_chunks.setEnabled(state)
        self.button_delete_bad_regions.setEnabled(state)
        self.button_replace_bad_regions.setEnabled(state)
        self.button_replace_bad_chunks.setEnabled(state)

    def start_scan(self):
        """Called with every action to start the world scan progress."""
        # Disable buttons
        self.update_button_status(False)
        # Get running variables
        entity_limit = self.spin_box_entity_limits.value()
        process_count = self.spin_box_processes.value()
        delete_entities = False

        scanners = [
            AsyncDataScanner(self.world.players, process_count),
            AsyncDataScanner(self.world.old_players, process_count),
            AsyncDataScanner(self.world.data_files, process_count),
            AsyncWorldRegionScanner(self.world, process_count, entity_limit, delete_entities)
        ]

        try:
            self.scan_output.append("Scanning world... %s" % self.world.get_name())
            self.progressBar.setValue(0)

            for scanner in scanners:
                # Self Update Progress Bar
                self.progressBar.setMinimum(0)
                self.progressBar.setMaximum(len(scanner))

                scanner.scan()
                counter = 0
                while not scanner.finished:
                    sleep(0.001)
                    result = scanner.get_last_result()

                    if result:
                        counter += 1
                    self.progressBar.setValue(counter)

            # The scan finished successfully
            self.scan_output.append("\nFinal scan results... %s" % self.world.generate_report(True))
            self.world.scanned = True
            # Enable buttons again
            self.update_button_status(True)
        except ChildProcessException:
            scanner.terminate()
            self.close

    def start_delete_chunks(self):
        """Called with every action to start delete bad chunks."""
        # Disable buttons
        self.update_button_status(False)
        self.scan_output.append("Removing bad chunks...")

        remove_chunks = self.world.remove_problematic_chunks
        for problem in world.CHUNK_PROBLEMS:
            print(world.CHUNK_STATUS_TEXT[problem])
            remove_chunks(problem)

        self.scan_output.append("Scan again the world for results.")
        # Enable buttons again
        self.update_button_status(True)

    def start_delete_regions(self):
        """Called with every action to start delete bad regions."""
        # Disable buttons
        self.update_button_status(False)
        self.scan_output.append("Removing bad regions...")

        remove_regions = self.world.remove_problematic_regions
        for problem in world.REGION_PROBLEMS:
            remove_regions(problem)

        self.scan_output.append("Scan again the world for results.")
        # Enable buttons again
        self.update_button_status(True)

    def start_replace_chunks(self):
        """Called with every action to start replace bad chunks."""
        self.scan_output.append("Currently this does not work because the backup functionality is not yet implemented.")
        return

        # Disable buttons
        self.update_button_status(False)
        self.scan_output.append("Replcaing bad chunks...")
        # Get running variables
        entity_limit = self.spin_box_entity_limits.value()
        delete_entities = False

        backups = self.backups.world_list
        replace_chunks = self.world.replace_problematic_chunks
        for problem in world.CHUNK_PROBLEMS:
            print(world.CHUNK_STATUS_TEXT[problem])
            replace_chunks(backups, problem, entity_limit, delete_entities)

        self.scan_output.append("Scan again the world for results.")
        # Enable buttons again
        self.update_button_status(True)

    def start_replace_regions(self):
        """Called with every action to start replace bad regions."""
        self.scan_output.append("Currently this does not work because the backup functionality is not yet implemented.")
        return

        # Disable buttons
        self.update_button_status(False)
        self.scan_output.append("Replcaing bad regions...")
        # Get running variables
        entity_limit = self.spin_box_entity_limits.value()
        delete_entities = False

        backups = self.backups.world_list
        replace_regions = self.world.replace_problematic_regions
        for problem in world.REGION_PROBLEMS:
            print(world.REGION_STATUS_TEXT[problem])
            replace_regions(backups, problem, entity_limit, delete_entities)

        self.scan_output.append("Scan again the world for results.")
        # Enable buttons again
        self.update_button_status(True)
