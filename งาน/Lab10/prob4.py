import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
from Lab10.prob3 import MessageBox

class FileDialog(MessageBox):
    def __init__(self):
        super(FileDialog, self).__init__()
        self.setWindowTitle("Calculator with Message Box")
        self.path = os.path.dirname(__file__)
        os.chdir(self.path)
        
    def _handleOpenMenus(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', self.path)
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.result_edit.setText(data)
                
    def _handleSaveMenus(self):
        fname = QFileDialog.getSaveFileName(self, 'Save File', self.path)
        if fname[0]:
            with open(fname[0], "w") as file:
                file.write(self.result_edit.toPlainText())            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileDialog() 
    window.show()
    sys.exit(app.exec())