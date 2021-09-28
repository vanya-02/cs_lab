from PyQt5.QtWidgets import (QMainWindow, QApplication, QTableView, QPlainTextEdit, QAction, QFileDialog)
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtCore import Qt
import sys
from jparser import parserf


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        # Load the ui file
        uic.loadUi("loadui.ui", self)

        # Instance variables
        self.parsed = None

        # Define Our Widgets
        self.tableView = self.findChild(QTableView, "tableView")
        self.plainTextEdit = self.findChild(QPlainTextEdit, "plainTextEdit")
        self.actionLoad = self.findChild(QAction, "actionLoad")
        self.actionSave = self.findChild(QAction, "actionSave")

        # Do something
        # self.clear_button.clicked.connect(self.clearer)
        self.actionLoad.triggered.connect(self.getfile)
        self.actionSave.triggered.connect(self.savefile)

        # Show The App
        self.show()

    def table(self, data):
        self.tableView.setModel(TableModel([[i] for i in data]))

    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "C:\\", "Audit Files (*.audit)")
        # print(fname)
        self.parsed = parserf(fname[0])
        self.plainTextEdit.appendPlainText(self.parsed[0])
        self.table(self.parsed[1])

    def savefile(self):
        if self.parsed:
            fname = QFileDialog.getSaveFileName(self, "Save as", "C:\\", "JSON File (*.json)")
            with open(fname[0], 'w') as file:
                file.write(self.parsed[0])


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
