import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
from Lab8.prob1 import MainWindow

class MainWindowMenus(MainWindow):
    def __init__(self):
        super(MainWindowMenus, self).__init__()
        self.setWindowTitle("Calculator with menus")
        self._addMenus()
        self._handleMenus()

    def _addMenus(self):
        self._addFileMenu()
        self._addEditMenu()
        self._addConfigMenu()

    def _addFileMenu(self):
        self.openAction = QAction("Open", self)
        self.saveAction = QAction("Save", self)
        self.exitAction = QAction("Exit", self)
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.exitAction)

    def _addConfigMenu(self):
        self.colorAction = QAction("Color", self)
        self.sizeAction = QAction("Size", self)
        self.configMenu.addAction(self.colorAction)
        self.configMenu.addAction(self.sizeAction)

    def _handleMenus(self):
        self.saveAction.triggered.connect(self._handleSaveMenus)
        self.openAction.triggered.connect(self._handleOpenMenus)
        self.exitAction.triggered.connect(self._handleExitMenus)
        self.clearAction.triggered.connect(self._handleClearMenus)

    def _handleSaveMenus(self):
        reply = QMessageBox.information(self, '',
                                     "Writing result to file result.txt",
                                     
                                     QMessageBox.StandardButton.Ok,
                                     QMessageBox.StandardButton.Ok)
        if reply == QMessageBox.StandardButton.Ok:
            with open("result.txt", "w") as f:
                f.write(self.result_edit.toPlainText())

    def _handleOpenMenus(self):
        reply = QMessageBox.information(self, '',
                                     "Reading result from file result.txt",
                                     
                                     QMessageBox.StandardButton.Ok,
                                     QMessageBox.StandardButton.Ok)
        if reply == QMessageBox.StandardButton.Ok:
            with open("result.txt", "r") as f:
                self.result_edit.setText(f.read())

    def _handleExitMenus(self):
        sys.exit()

    def _handleClearMenus(self):
        self.first_number_edit.clear()
        self.second_number_edit.clear()
        self.result_edit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowMenus()
    window.show()
    sys.exit(app.exec())
