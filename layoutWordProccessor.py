# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layoutWordProccessor.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wordProccessor(object):
    def setupUi(self, wordProccessor):
        wordProccessor.setObjectName("wordProccessor")
        wordProccessor.resize(969, 1318)
        wordProccessor.setStyleSheet("background-color: rgb(175, 236, 184);")
        self.centralwidget = QtWidgets.QWidget(wordProccessor)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(890, 170, 20, 1127))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.wordSearchField = QtWidgets.QLineEdit(self.centralwidget)
        self.wordSearchField.setGeometry(QtCore.QRect(330, 120, 321, 20))
        self.wordSearchField.setObjectName("wordSearchField")
        self.document = QtWidgets.QTextEdit(self.centralwidget)
        self.document.setGeometry(QtCore.QRect(70, 170, 797, 1127))
        self.document.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.document.setObjectName("document")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 170, 801, 1131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.documentLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.documentLayout.setContentsMargins(0, 0, 0, 0)
        self.documentLayout.setObjectName("documentLayout")
        wordProccessor.setCentralWidget(self.centralwidget)

        self.retranslateUi(wordProccessor)
        QtCore.QMetaObject.connectSlotsByName(wordProccessor)

    def retranslateUi(self, wordProccessor):
        _translate = QtCore.QCoreApplication.translate
        wordProccessor.setWindowTitle(_translate("wordProccessor", "Word Proccessor"))