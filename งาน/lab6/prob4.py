import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QCheckBox, QComboBox, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class DrinkApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Information of 653040167-1")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        self.name_label = QLabel("Chakkapat Waenmook")
        font = QFont("Arial", 16, QFont.Weight.Bold)
        self.name_label.setFont(font)
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.name_label)

        self.orange_check = QCheckBox("Orange Juice")
        self.green_check = QCheckBox("Green Tea")
        
        self.orange_check.stateChanged.connect(self.update_label)
        self.green_check.stateChanged.connect(self.update_label)
        
        layout.addWidget(self.orange_check)
        layout.addWidget(self.green_check)
        
        self.combo = QComboBox()
        self.combo.addItem("COE")
        self.combo.addItem("DME")
        self.combo.currentIndexChanged.connect(self.update_label)
        layout.addWidget(self.combo)
        
        self.label = QLabel("Pengpan")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("background-color: green;")
        layout.addWidget(self.label)
        
        quit_button = QPushButton("Quit")
        quit_button.clicked.connect(self.close)
        layout.addWidget(quit_button)
        
        central_widget.setLayout(layout)
        self.update_label()
        
    def update_label(self):
        drink_choices = []
        if self.orange_check.isChecked():
            drink_choices.append("Orange Juice")
        if self.green_check.isChecked():
            drink_choices.append("Green Tea")
        
        study_choice = self.combo.currentText() if self.combo.currentIndex() != -1 else "a program"
        
        if drink_choices:
            self.label.setText(f"You want to drink {', '.join(drink_choices)} and you have studied in {study_choice}.")
        else:
            self.label.setText(f"You do not want to drink anything and you have studied in {study_choice}.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrinkApp()
    window.show()
    sys.exit(app.exec())