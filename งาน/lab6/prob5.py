import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QListWidget, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPalette, QColor

class CourseSelectionApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 400, 300)

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your name")
        main_layout.addWidget(self.name_input)

        self.course_list = QListWidget()
        self.course_list.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        courses = ["EN842300", "EN842314", "EN842315"]
        self.course_list.addItems(courses)
        main_layout.addWidget(self.course_list)

        self.display_label = QLabel()
        self.display_label.setAutoFillBackground(True)
        
        palette = self.display_label.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("yellow"))
        self.display_label.setPalette(palette)
        main_layout.addWidget(self.display_label)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.course_list.itemSelectionChanged.connect(self.display_selection)

    def display_selection(self):
        name = self.name_input.text()
        selected_courses = [item.text() for item in self.course_list.selectedItems()]
        selected_courses_text = ", ".join(selected_courses)

        greeting = f"Hello Manee! You have studied in: {selected_courses_text}"
        self.display_label.setText(greeting)
        

def main():
    app = QApplication(sys.argv)
    window = CourseSelectionApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
