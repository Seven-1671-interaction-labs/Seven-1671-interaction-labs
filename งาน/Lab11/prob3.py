import sys 
import os 
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
os.pardir)))
from Lab11.prob2 import DrawingMainWindow


class AnimationWindow(DrawingMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color of the Day with Animation")
        self._createMenuBar()
        self._createToolBars()
        self._setStatusBar()
        self.sizeAction.triggered.connect(self.doanima)

    def _createMenuBar(self):
        path = os.path.dirname(__file__)
        os.chdir(path)
        self.menuBar = self.menuBar()
        self.animaMenu = self.menuBar.addMenu("Animation")
        self.menuBar.setNativeMenuBar(False)
        self.sizeAction = QAction('Size', self)
        self.sizeAction.setIcon(QIcon("icon-size.png"))
        self.sizeAction.setShortcut(QKeySequence("Ctrl+Shift+s"))
        self.animaMenu.addAction(self.sizeAction)

    def _createToolBars(self):
        self.animaMenu = self.addToolBar("Animation")
        self.animaMenu.addAction(self.sizeAction)

    def _setStatusBar(self):
        self.statusBar = self.statusBar()
        self.sizeAction.setStatusTip('Animate the size of the label')
        self.statusBar.showMessage('Ready')

    def doanima(self):
        self.ani = QPropertyAnimation(self.Text, b"geometry")
        self.ani.setDuration(3000)
        self.ani.setStartValue(QRect(10,10,100,30))
        self.ani.setEndValue(QRect(100, 20, 150, 40))
        self.ani.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnimationWindow()
    window.show()
    app.exec()