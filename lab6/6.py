import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, name, student_id):
        super().__init__()
        self.setWindowTitle("My App")
        label = QLabel("Chakkapat")
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.setCentralWidget(label)

        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton('Quit', self)
        self.button.setGeometry(100, 80, 100, 40)
        self.button.clicked.connect(self.quit_clicked)

        self.name = name
        self.student_id = student_id

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                     QMessageBox.StandardButton.Yes | 
                                     QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def quit_clicked(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow("Main Window", "Your Student ID")
    window.show()
    sys.exit(app.exec())