from PyQt5.QtWidgets import (QMainWindow, QApplication, QPlainTextEdit, QAction, QFileDialog)
from PyQt5 import uic
import sys
from jparser import parserf


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("loadui.ui", self)

        # Define Our Widgets
        self.plainTextEdit = self.findChild(QPlainTextEdit, "plainTextEdit")
        self.actionLoad = self.findChild(QAction, "actionLoad")
        self.actionSave = self.findChild(QAction, "actionSave")

        # Do something
        # self.button.clicked.connect(self.clicker)
        # self.clear_button.clicked.connect(self.clearer)
        self.actionLoad.triggered.connect(self.getfile)

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

        self.plainTextEdit.appendPlainText(parserf(fname[0]))



# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
