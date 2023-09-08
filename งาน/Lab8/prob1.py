import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Simple Calculator")
        self.mainLayout = QVBoxLayout()


        self._createMenuBar()
        self._createNumbersLayout()
        self._createButtonsLayout()
        self._createResultLayout()
        
        self.mainLayout.addLayout(self.numbersLayout)
        self.mainLayout.addLayout(self.buttonsLayout)
        self.mainLayout.addLayout(self.resultLayout)

        self.container = QWidget()
        self.container.setLayout(self.mainLayout)
        self.setCentralWidget(self.container)

    def _createMenuBar(self):
        self.menuBar = self.menuBar()
        self.menuBar.setNativeMenuBar(False)
        self.fileMenu = self.menuBar.addMenu("File")
        self.editMenu = self.menuBar.addMenu("Edit")
        self.configMenu = self.menuBar.addMenu("Config")

    def _createNumbersLayout(self):
        self.numbersLayout = QGridLayout()
        self.first_number_label = QLabel("Enter the first number:")
        self.first_number_edit = QLineEdit()
        self.first_number_edit.setStyleSheet("background-color: yellow;") 
        self.second_number_label = QLabel("Enter the second number:")
        self.second_number_edit = QLineEdit()
        self.second_number_edit.setStyleSheet("background-color: yellow;")
        self.first_number_edit.setAlignment(Qt.AlignmentFlag.AlignRight)  
        self.second_number_edit.setAlignment(Qt.AlignmentFlag.AlignRight)  

        self.numbersLayout.addWidget(self.first_number_label,0,0)
        self.numbersLayout.addWidget(self.first_number_edit,0,1)
        self.numbersLayout.addWidget(self.second_number_label,1,0)
        self.numbersLayout.addWidget(self.second_number_edit,1,1)   
    
    def _createButtonsLayout(self):
        self.buttonsLayout = QGridLayout()
        names = ['+','-','*','/']

        positions = [(i, j) for i in range(1,6) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            button.clicked.connect(self.cal)
            self.buttonsLayout.addWidget(button, *position)          
    
    
    def _createResultLayout(self):
        self.resultLayout= QGridLayout()
        self.result_label = QLabel("Result:")
        self.result_edit = QTextEdit()
        self.result_edit.setStyleSheet("background-color: lightgreen;") 

        self.resultLayout.addWidget(self.result_label,3,0)
        self.resultLayout.addWidget(self.result_edit,3,1)

    def cal(self):
        op = self.sender().text()
        ans = 0
        try:
            n1 = float(self.first_number_edit.text())
            n2 = float(self.second_number_edit.text())
            if op == '+':
                ans = n1 + n2
            elif op == '-':
                ans = n1 - n2
            elif op == '*':
                ans = n1 * n2
            elif op == '/':
                ans = n1 / n2
            self.result_edit.append(f'{n1} {op} {n2} = {ans}')
        except ZeroDivisionError:
            self.result_edit.append('Error: Division by zero')
        except ValueError:
            self.result_edit.append('Enter number plsssssss')
        
    def _addEditMenu(self):
        self.clearAction = QAction("Clear", self)
        self.copyAction = QAction("Copy", self)
        self.pasteAction = QAction("Paste", self)
        self.cutAction = QAction("Cut", self)
        self.editMenu.addAction(self.clearAction)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addAction(self.cutAction)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

