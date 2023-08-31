import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QGridLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QKeyEvent

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)

        self.expression = ""
        self.result_shown = False
        
        names = ['7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(1, 5) for j in range(4)]

        for position, name in zip(positions, names):
            button = QPushButton(name)
            if name == '=':
                button.clicked.connect(self.calculate)
            else:
                button.clicked.connect(self.append_text)
            button_font = QFont("Arial", 20)
            button.setFont(button_font)
            grid.addWidget(button, *position)

        self.output_label = QLineEdit('0')
        self.output_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.output_label.setStyleSheet("background-color: yellow;")
        output_label_font = QFont("Arial", 20)
        self.output_label.setFont(output_label_font)
        grid.addWidget(self.output_label, 0, 0, 1, 4)

        self.move(300, 150)
        self.setWindowTitle('Calculator')

    def append_text(self):
        if self.result_shown:
            self.expression = ""
            self.result_shown = False

        self.expression += self.sender().text()
        self.output_label.setText(self.expression)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.output_label.setText(str(result))
            self.result_shown = True
        except Exception as e:
            self.output_label.setText("Error")
            self.result_shown = True

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            self.calculate()
        elif event.key() == Qt.Key.Key_Escape:
            self.expression = ""
            self.output_label.setText("0")
        else:
            super().keyPressEvent(event)

app = QApplication(sys.argv)
calculator = Calculator()
calculator.show()
sys.exit(app.exec())
