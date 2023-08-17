import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QCheckBox, QComboBox, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class DrinkApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        
        self.combo = QComboBox()
        self.combo.addItem("Manee")
        self.combo.currentIndexChanged.connect(self.update_label)
        layout.addWidget(self.combo)

        self.EN842300_check = QCheckBox("EN842300")
        self.EN842314_check = QCheckBox("EN842314")
        self.EN842315_check = QCheckBox("EN842315")
        
        self.EN842300_check.stateChanged.connect(self.update_label)
        self.EN842314_check.stateChanged.connect(self.update_label)
        self.EN842315_check.stateChanged.connect(self.update_label)
        
        layout.addWidget(self.EN842300_check)
        layout.addWidget(self.EN842314_check)
        layout.addWidget(self.EN842315_check)
        
        self.label = QLabel("Pengpan")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("background-color: yellow;")
        layout.addWidget(self.label)
        
        central_widget.setLayout(layout)
        self.update_label()
        
    def update_label(self):
        id_choices = []
        if self.EN842300_check.isChecked():
            id_choices.append("EN842300")
        if self.EN842314_check.isChecked():
            id_choices.append("EN842314")
        if self.EN842315_check.isChecked():
            id_choices.append("EN842315")
        
        study_choice = self.combo.currentText() if self.combo.currentIndex() != -1 else "a program"
        
        if id_choices:
            self.label.setText(f"Hello Manee! and you have studied in  {', '.join(id_choices)}.")
        else:
            self.label.setText(f"You are interested in these courses {study_choice}.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrinkApp()
    window.show()
    sys.exit(app.exec())