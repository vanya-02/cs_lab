from PyQt5.QtWidgets import (QMainWindow, QApplication, QPlainTextEdit, QAction, QFileDialog)
from PyQt5 import uic
import sys
from jparser import parserf


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        self.parsed = None

        # Load the ui file
        uic.loadUi("loadui.ui", self)

        # Define Our Widgets
        self.plainTextEdit = self.findChild(QPlainTextEdit, "plainTextEdit")
        self.actionLoad = self.findChild(QAction, "actionLoad")
        self.actionSave = self.findChild(QAction, "actionSave")

        # Do something
        # self.clear_button.clicked.connect(self.clearer)
        self.actionLoad.triggered.connect(self.getfile)
        self.actionSave.triggered.connect(self.savefile)

        # Show The App
        self.show()

    # def clearer(self):
    # 	self.textedit.setPlainText("")
    # 	self.label.setText("Enter Your Name...")

    # def clicker(self):
    # 	self.label.setText(f'Hello There {self.textedit.toPlainText()}')
    # 	self.textedit.setPlainText("")
    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "C:\\", "Audit Files (*.audit)")
        # print(fname)
        self.parsed = parserf(fname[0])
        self.plainTextEdit.appendPlainText(self.parsed)

    def savefile(self):
        if self.parsed:
            fname = QFileDialog.getSaveFileName(self, "Save as", "C:\\", "JSON File (*.json)")
            with open(fname[0], 'w') as file:
                file.write(self.parsed)


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
