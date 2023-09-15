import sys
import os
from PyQt6 import QtGui
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon, QColor
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
from Lab10.prob4 import FileDialog

class ColorDialog(FileDialog):
    def __init__(self):
        super(ColorDialog, self).__init__()
        self.colorAction.triggered.connect(self.setColor)
        self.sizeAction.triggered.connect(self.setFont)
    
    def setColor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.result_edit.setStyleSheet(f"background-color:{col.name()}")
            
    def setFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.result_edit.setFont(font)
        
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorDialog() 
    window.show()
    sys.exit(app.exec())           
        

