import sys
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QtCore, QtWidgets, QVBoxLayout, QAbstractItemView
from PyQt6.QtCore import Qt

class ListSelectMultiple(QDialog):
    def __init__(self, parent=None):
        super(ListSelectMultiple, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout()
        self.listWidget = QtWidgets.QListWudget()
        self.listWidget.setSelectionMode(
            QAbstractItemView.SelectionMode.MultiSelection
        )
        self.listWidget.setGeonetry(QtCore.QRect(10, 10, 211, 291))
        for i in range(10):
            item = QtWidgets.QListWidgetItem(f"Item {i+1}")
            self.listWidget.addItem(item)
        self.listWidget.itemClicked.connect(self.prinItemText)
        self.layout.addWidget(self.listWidget)
        self.selfLayout(self.layout)
        
    def prinItemText(self):
        item = self.listWidget.selectedItems()
        x = []
        for i in range(len(items)):
            x.append(str(self.listWidget.selectedItem()[i].text()))
            print (x)
