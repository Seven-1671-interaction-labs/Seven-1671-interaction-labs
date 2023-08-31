import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QGridLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)
        
        names = ['7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        
        positions = [(i, j) for i in range(1, 5) for j in range(4)]
        
        for position, name in zip(positions, names):
            button = QPushButton(name)
            button.clicked.connect(self.set_text)
            button_font = QFont("Arial, 20")
            button.setFont(button_font)
            grid.addWidget(button, *position)

            
        self.output_label = QLineEdit('8')
        self.output_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.output_label.setStyleSheet("background-color: yellow;")
        output_label_font = QFont("Arial", 20) 
        self.output_label.setFont(output_label_font)
        grid.addWidget(self.output_label, 0, 0, 1, 4)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        
    def set_text(self):
        self.output_label.setText(self.sender().text())
            
app = QApplication(sys.argv)
calculator = Calculator()
calculator.show()
sys.exit(app.exec())