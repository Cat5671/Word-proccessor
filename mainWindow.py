import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLineEdit
from layoutWordProccessor1 import Ui_wordProccessor

class WordProccessor(QMainWindow, Ui_wordProccessor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
ex = WordProccessor()
ex.show()
sys.exit(app.exec_())