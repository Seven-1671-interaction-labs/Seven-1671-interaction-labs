import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
from Lab8.prob2 import MainWindowMenus

class ToolbarIcons(MainWindowMenus):
    def __init__(self):
        super(ToolbarIcons, self).__init__()
        self.setWindowTitle("Calculator with menus and Toolbar")
        self._createActions()
        self._createTooBars()

    def _createActions(self):
        path = os.path.dirname(__file__)
        os.chdir(path)
        self.saveAction.setIcon(QIcon("images/file-save.png"))
        self.openAction.setIcon(QIcon("images/file-open.svg"))
        self.clearAction.setIcon(QIcon("images/edit-clear.png"))    
        
    def _createTooBars(self):
        fileToolBar = self.addToolBar('iconbar')
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)
        fileToolBar.addAction(self.clearAction)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToolbarIcons()
    window.show()
    app.exec()
