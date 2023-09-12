import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon, QKeySequence
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
from Lab10.prob1 import ToolbarIcons

class Toolbar(ToolbarIcons):
    def __init__(self):
        super(Toolbar, self).__init__()

        self.setWindowTitle("Calculator with menus and Toolbar")

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Ready")
        self._createshortcuts()


    def _createshortcuts(self):
        self.openAction.setShortcut(QKeySequence("Ctrl+O"))
        self.saveAction.setShortcut(QKeySequence("Ctrl+S"))
        self.clearAction.setShortcut(QKeySequence("Ctrl+R"))
        self.exit_action = QAction("Exit", self)
        self.exit_action.setShortcut(QKeySequence("Ctrl+Q"))
        self.exit_action.triggered.connect(self.close)

        self.openAction.setStatusTip("Open a file")
        self.saveAction.setStatusTip("Save a file")
        self.clearAction.setStatusTip("Clear the result")
        self.exit_action.setStatusTip("Exit the application")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Toolbar() 
    window.show()
    sys.exit(app.exec())