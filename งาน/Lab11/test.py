import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Simple Calculator")
        self.mainLayout = QVBoxLayout()

        self._createMenuBar()
       
        self.container = QWidget()
        self.container.setLayout(self.mainLayout)
        self.setCentralWidget(self.container)

    def _createMenuBar(self):
        self.menuBar = self.menuBar()
        self.menuBar.setNativeMenuBar(False)
        self.fileMenu = self.menuBar.addMenu("Animation")
class MainWindowMenus(MainWindow):
    def __init__(self):
        super(MainWindowMenus, self).__init__()
        self.setWindowTitle("Calculator with menus")
        self._addMenus()


    def _addMenus(self):
        self._addFileMenu()

    def _addFileMenu(self):
        self.openAction = QAction("Start", self)
        self.fileMenu.addAction(self.openAction)


   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowMenus()
    window.show()
    sys.exit(app.exec())
