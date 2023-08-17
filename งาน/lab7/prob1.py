import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QLabel, QLineEdit

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle('Login Form')
        
        layout = QGridLayout(self)
        
        layout.addWidget(QLabel('First Name:'), 0, 0)
        layout.addWidget(QLineEdit(), 0, 1)
        
        layout.addWidget(QLabel('Last Name:'), 1, 0)
        layout.addWidget(QLineEdit(), 1, 1)
        
        quit_button = QPushButton("Cancel")
        quit_button.clicked.connect(self.close)
        quit_button.setStyleSheet("background-color: red; color: white;")
        layout.addWidget(quit_button)
        
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.close)
        submit_button.setStyleSheet("background-color: green; color: white;")
        layout.addWidget(submit_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())