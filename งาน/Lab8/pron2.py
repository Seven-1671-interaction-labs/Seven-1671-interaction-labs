import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QFrame, QSizePolicy, QWidget
import tkinter as tk
from tkinter import Menu

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator with Menus")
        self.setGeometry(100, 100, 400, 300)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        edit_menu = menubar.addMenu("Edit")
        config_menu = menubar.addMenu("Config")

        def new_file():
            print("New File")

        def open_file():
            print("Open File")

        def save_file():
            print("Save File")

        def exit_app():
            self.close()

        file_menu.addAction("Open", open_file)
        file_menu.addAction("Save", save_file)
        file_menu.addAction("Exit", exit_app)

        edit_menu.addAction("Clear")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Cut")

        config_menu.addAction("Color")
        config_menu.addAction("Size")

        self.label1 = QLabel("Enter the first number:")
        self.line_edit1 = QLineEdit()
        self.label2 = QLabel("Enter the second number:")
        self.line_edit2 = QLineEdit()
        self.line_edit1.setStyleSheet("background-color: yellow;")
        self.line_edit2.setStyleSheet("background-color: yellow;")

        self.operators_layout = QHBoxLayout()
        self.add_button = QPushButton("+")
        self.subtract_button = QPushButton("-")
        self.multiply_button = QPushButton("*")
        self.divide_button = QPushButton("/")

        self.operators_layout.addWidget(self.add_button)
        self.operators_layout.addWidget(self.subtract_button)
        self.operators_layout.addWidget(self.multiply_button)
        self.operators_layout.addWidget(self.divide_button)

        self.result_box = QFrame()
        self.result_box.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.result_layout = QHBoxLayout(self.result_box)
        self.result_label = QLabel("Result:")
        self.result_text = QTextEdit()
        self.result_layout.addWidget(self.result_label)
        self.result_layout.addWidget(self.result_text)
        self.result_text.setStyleSheet("background-color: green;")

        main_layout = QVBoxLayout()
        entry_layout1 = QHBoxLayout()
        entry_layout1.addWidget(self.label1)
        entry_layout1.addWidget(self.line_edit1)

        entry_layout2 = QHBoxLayout()
        entry_layout2.addWidget(self.label2)
        entry_layout2.addWidget(self.line_edit2)

        main_layout.addLayout(entry_layout1)
        main_layout.addLayout(entry_layout2)
        main_layout.addLayout(self.operators_layout)
        main_layout.addWidget(self.result_box)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.add_button.clicked.connect(self.add)
        self.subtract_button.clicked.connect(self.subtract)
        self.multiply_button.clicked.connect(self.multiply)
        self.divide_button.clicked.connect(self.divide)

    def add(self):
        num1 = float(self.line_edit1.text())
        num2 = float(self.line_edit2.text())
        result = num1 + num2
        self.result_text.setPlainText(str(result))

    def subtract(self):
        num1 = float(self.line_edit1.text())
        num2 = float(self.line_edit2.text())
        result = num1 - num2
        self.result_text.setPlainText(str(result))

    def multiply(self):
        num1 = float(self.line_edit1.text())
        num2 = float(self.line_edit2.text())
        result = num1 * num2
        self.result_text.setPlainText(str(result))

    def divide(self):
        num1 = float(self.line_edit1.text())
        num2 = float(self.line_edit2.text())
        if num2 != 0:
            result = num1 / num2
            self.result_text.setPlainText(str(result))
        else:
            self.result_text.setPlainText("Cannot divide by zero")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())
