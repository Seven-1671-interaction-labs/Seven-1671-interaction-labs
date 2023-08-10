import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self, name, student_id):
        super().__init__()
        self.setWindowTitle(name)
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton('Click me', self)
        self.button.setGeometry(100, 80, 100, 40)
        self.button.clicked.connect(self.on_button_clicked)

        self.name = name
        self.student_id = student_id

    def on_button_clicked(self):
        self.button.setText(self.student_id)
        self.button.setEnabled(False)
        self.setWindowTitle(self.student_id)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    student = {'name': 'Manee Jaidee', 'id': '653040167-1'}
     
    window = MainWindow(student['name'], student['id'])
    window.show()

    app.exec()             
    