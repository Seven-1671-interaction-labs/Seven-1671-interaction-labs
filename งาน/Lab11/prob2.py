import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QSize, QRect, QPoint
from PyQt6.QtGui import QPainter, QPen, QColor, QFont, QPixmap, QBrush
from functools import partial
import math

class Text(QLabel):
    def __init__(self):
        super().__init__()
        font = QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(40)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFont(font)
    def set_pen_color(self,c):
        moo = {'red': 'Sunday', 'yellow': 'Monday','pink': 'Tuesday', 'green':'Wednesday', 'orange':'Thursday', 'blue':'Friday', 'purple':'Saturday'}
        mii = {'red':'white', 'yellow': 'black', 'pink': 'black', 'green':'white', 'orange':'black', 'blue':'white', 'purple':'white'}
        self.setText(moo[c])
        self.setStyleSheet(f'background-color:{c}; color:{mii[c]}')
        
class Canvas(QLabel):
    def __init__(self):
        super().__init__()
        pixmap = QPixmap(300, 300)
        pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(pixmap)


    def set_pen_color(self, c):
        pixmap = QPixmap(500, 500)
        pixmap.fill(Qt.GlobalColor.white)

        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        pen = QPen()
        pen.setWidth(1)
        

        pen.setColor(QColor(c))
        
        brush = QBrush()
        brush.setColor(QColor(c))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)
        painter.setPen(pen)
        painter.drawEllipse(100, 100, 300, 300)
        pen.setStyle(Qt.PenStyle.DashLine)
        painter.end()

        self.setPixmap(pixmap)



COLORS = ['red', 'yellow', 'pink', 'green', 'orange', 'blue', 'purple']


class QPaletteButton(QPushButton):
    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QSize(24, 24))
        self.color = color
        self.setStyleSheet(f"background-color: {color};")


class DrawingMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas()
        self.Text = Text()
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        layout.addWidget(self.Text)
        layout.addWidget(self.canvas)
        palette = QHBoxLayout()
        self.add_palette_buttons(palette)
        layout.addLayout(palette)
        self.setCentralWidget(widget)

    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(partial(self.canvas.set_pen_color, c))
            
            b.pressed.connect(partial(self.Text.set_pen_color, c))
            layout.addWidget(b)
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrawingMainWindow()
    window.show()
    sys.exit(app.exec())
