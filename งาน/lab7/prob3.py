import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QRadioButton, QTextEdit

class FormApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('MyApp')

        main_layout = QVBoxLayout(self)

        first_name_layout = QHBoxLayout() 
        self.first_name_edit = QLineEdit()
        first_name_layout.addWidget(QLabel('First Name:'))
        first_name_layout.addWidget(self.first_name_edit)

        last_name_layout = QHBoxLayout() 
        self.last_name_edit = QLineEdit()
        last_name_layout.addWidget(QLabel('Last Name:'))
        last_name_layout.addWidget(self.last_name_edit)

        main_layout.addLayout(first_name_layout) 
        main_layout.addLayout(last_name_layout)  
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(QLabel('Gender:'))

        self.female_radio = QRadioButton("Female")
        self.male_radio = QRadioButton("Male")
        self.other_radio = QRadioButton("Other")

        gender_layout.addWidget(self.female_radio)
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.other_radio)

        main_layout.addLayout(gender_layout)

        buttons_layout = QHBoxLayout()

        cancel_button = QPushButton("Cancel")
        cancel_button.setStyleSheet("color: red;")
        cancel_button.clicked.connect(self.cancel_pressed)
        buttons_layout.addWidget(cancel_button)

        submit_button = QPushButton("Submit")
        submit_button.setStyleSheet("color: green;")
        submit_button.clicked.connect(self.submit_pressed)
        buttons_layout.addWidget(submit_button)

        main_layout.addLayout(buttons_layout)

        self.result_text_edit = QTextEdit() 
        self.result_text_edit.setReadOnly(True)
        main_layout.addWidget(QLabel('Result:')) 
        main_layout.addWidget(self.result_text_edit)  

        self.setLayout(main_layout)

    def submit_pressed(self):
        first_name = self.first_name_edit.text()
        last_name = self.last_name_edit.text()
        gender = ""
        if self.female_radio.isChecked():
            gender = "Female"
        elif self.male_radio.isChecked():
            gender = "Male"
        elif self.other_radio.isChecked():
            gender = "Other"

        result = f'First Name: {first_name}\nLast Name: {last_name}\nGender: {gender}'
        self.result_text_edit.setPlainText(result)

    def cancel_pressed(self):
        self.first_name_edit.clear()
        self.last_name_edit.clear()
        self.female_radio.setAutoExclusive(False)
        self.male_radio.setAutoExclusive(False)
        self.other_radio.setAutoExclusive(False)
        self.female_radio.setChecked(False)
        self.male_radio.setChecked(False)
        self.other_radio.setChecked(False)
        self.female_radio.setAutoExclusive(True)
        self.male_radio.setAutoExclusive(True)
        self.other_radio.setAutoExclusive(True)
        self.result_text_edit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = FormApp()
    form.show()
    sys.exit(app.exec())
