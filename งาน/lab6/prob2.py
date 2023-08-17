import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, name_ids):
        super().__init__()
        self.setWindowTitle("My App")
        self.label = QLabel("Hello, Chakkapat 1671")
       
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.name_ids = name_ids

app = QApplication(sys.argv)

name_ids = {"name": "Manee", "id": "5829"}

window = MainWindow(name_ids)
window.show()

app.exec()