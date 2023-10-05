import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(1000, 1000)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()
    def draw_something(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)        
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor("#FF0000"))
        painter.setPen(pen)
        painter.drawRect(300, 300, 400, 400) #square 
        pen.setColor(QtGui.QColor("#000000"))
        pen.setStyle(Qt.PenStyle.DashLine)  
        painter.setPen(pen)
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor("#AFE58E"))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawEllipse (350, 350, 300, 300)#circle
        font = QtGui.QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(17)
        painter.setFont(font)

        painter.drawText(375, 515, 'Chakkapat Waenmook')
        painter.end()
        self.label.setPixmap(canvas)
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()