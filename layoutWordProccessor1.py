# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layoutWordProccessor1.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WordProcessor(object):
    def setup_ui(self, WordProccessor):
        WordProccessor.setObjectName("WordProccessor")
        WordProccessor.resize(1086, 767)
        WordProccessor.setStyleSheet("background-color: rgb(175, 236, 184);")
        self.central_widget = QtWidgets.QWidget(WordProccessor)
        self.central_widget.setObjectName("central_widget")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.vertical_layout.setObjectName("verticalLayout")
        self.menu_layout = QtWidgets.QGridLayout()
        self.menu_layout.setObjectName("menu_layout")
        spacer_item = QtWidgets.QSpacerItem(33, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.menu_layout.addItem(spacer_item, 0, 6, 1, 1)
        spacer_item1 = QtWidgets.QSpacerItem(33, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.menu_layout.addItem(spacer_item1, 0, 14, 1, 1)
        spacer_item2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.menu_layout.addItem(spacer_item2, 0, 0, 1, 1)
        self.copy_button = QtWidgets.QPushButton(self.central_widget)
        self.copy_button.setMinimumSize(QtCore.QSize(35, 35))
        self.copy_button.setMaximumSize(QtCore.QSize(35, 35))
        self.copy_button.setText("")
        self.copy_button.setIconSize(QtCore.QSize(30, 30))
        self.copy_button.setObjectName("copy_button")
        self.menu_layout.addWidget(self.copy_button, 0, 3, 1, 1)
        spacer_item3 = QtWidgets.QSpacerItem(33, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.menu_layout.addItem(spacer_item3, 0, 10, 1, 1)
        self.underline_text_button = QtWidgets.QPushButton(self.central_widget)
        self.underline_text_button.setMinimumSize(QtCore.QSize(35, 35))
        self.underline_text_button.setMaximumSize(QtCore.QSize(35, 35))
        self.underline_text_button.setText("П")
        self.underline_text_button.setIconSize(QtCore.QSize(30, 30))
        self.underline_text_button.setObjectName("underline_text_button")
        self.menu_layout.addWidget(self.underline_text_button, 0, 13, 1, 1)
        spacer_item4 = QtWidgets.QSpacerItem(33, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.menu_layout.addItem(spacer_item4, 0, 4, 1, 1)
        spacer_item5 = QtWidgets.QSpacerItem(33, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.menu_layout.addItem(spacer_item5, 0, 12, 1, 1)
        spacer_item6 = QtWidgets.QSpacerItem(33, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.menu_layout.addItem(spacer_item6, 0, 16, 1, 1)
        self.back_button = QtWidgets.QPushButton(self.central_widget)
        self.back_button.setMinimumSize(QtCore.QSize(35, 35))
        self.back_button.setMaximumSize(QtCore.QSize(35, 35))
        self.back_button.setText("")
        self.back_button.setIconSize(QtCore.QSize(30, 30))
        self.back_button.setObjectName("back_button")
        self.menu_layout.addWidget(self.back_button, 0, 1, 1, 1)
        spacer_item7 = QtWidgets.QSpacerItem(33, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.menu_layout.addItem(spacer_item7, 0, 8, 1, 1)
        self.bold_text_button = QtWidgets.QPushButton(self.central_widget)
        self.bold_text_button.setMinimumSize(QtCore.QSize(35, 35))
        self.bold_text_button.setMaximumSize(QtCore.QSize(35, 35))
        self.bold_text_button.setText("Ж")
        self.bold_text_button.setIconSize(QtCore.QSize(30, 30))
        self.bold_text_button.setObjectName("bold_text_button")
        self.menu_layout.addWidget(self.bold_text_button, 0, 11, 1, 1)
        self.paragraph_button = QtWidgets.QPushButton(self.central_widget)
        self.paragraph_button.setMinimumSize(QtCore.QSize(35, 35))
        self.paragraph_button.setMaximumSize(QtCore.QSize(35, 35))
        self.paragraph_button.setText("")
        self.paragraph_button.setIconSize(QtCore.QSize(30, 30))
        self.paragraph_button.setObjectName("paragraph_button")
        self.menu_layout.addWidget(self.paragraph_button, 0, 17, 1, 1)
        self.fonts = QtWidgets.QFontComboBox(self.central_widget)
        self.fonts.setMinimumSize(QtCore.QSize(120, 0))
        self.fonts.setMaximumSize(QtCore.QSize(120, 16777215))
        self.fonts.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fonts.setObjectName("fonts")
        self.fonts.setEditable(False)


        self.fonts.setItemText(5, "")
        self.menu_layout.addWidget(self.fonts, 0, 5, 1, 1)
        self.font_color = QtWidgets.QComboBox(self.central_widget)
        self.font_color.setMinimumSize(QtCore.QSize(120, 0))
        self.font_color.setMaximumSize(QtCore.QSize(120, 16777215))
        self.font_color.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.font_color.setObjectName("font_color")
        self.font_color.addItem("")
        self.font_color.addItem("")
        self.font_color.addItem("")
        self.font_color.addItem("")
        self.font_color.addItem("")
        self.font_color.addItem("")
        self.font_color.addItem("")
        self.menu_layout.addWidget(self.font_color, 0, 15, 1, 1)
        self.font_size = QtWidgets.QComboBox(self.central_widget)
        self.font_size.setMinimumSize(QtCore.QSize(50, 0))
        self.font_size.setMaximumSize(QtCore.QSize(50, 16777215))
        self.font_size.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.font_size.setObjectName("font_size")
        self.font_size.addItem("")
        self.font_size.addItem("")
        self.font_size.addItem("")
        self.font_size.addItem("")
        self.font_size.addItem("")
        self.font_size.addItem("")
        self.font_size.addItem("")
        self.font_size.addItem("")
        self.font_size.addItem("")
        self.font_size.addItem("")
        self.font_size.addItem("")
        self.font_size.addItem("")
        self.font_size.addItem("")
        self.font_size.addItem("")
        self.font_size.addItem("")
        self.menu_layout.addWidget(self.font_size, 0, 7, 1, 1)
        spacer_item8 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.menu_layout.addItem(spacer_item8, 0, 18, 1, 1)
        self.italic_text_button = QtWidgets.QPushButton(self.central_widget)
        self.italic_text_button.setMinimumSize(QtCore.QSize(35, 35))
        self.italic_text_button.setMaximumSize(QtCore.QSize(35, 35))
        self.italic_text_button.setText("К")
        self.italic_text_button.setIconSize(QtCore.QSize(30, 30))
        self.italic_text_button.setObjectName("italic_text_button")
        self.menu_layout.addWidget(self.italic_text_button, 0, 9, 1, 1)
        spacer_item9 = QtWidgets.QSpacerItem(33, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.menu_layout.addItem(spacer_item9, 0, 2, 1, 1)
        self.vertical_layout.addLayout(self.menu_layout)
        self.word_search_field_layout = QtWidgets.QHBoxLayout()
        self.word_search_field_layout.setObjectName("word_search_field_layout")
        spacer_item10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.word_search_field_layout.addItem(spacer_item10)
        self.word_search_field = QtWidgets.QLineEdit(self.central_widget)
        self.word_search_field.setMinimumSize(QtCore.QSize(0, 0))
        self.word_search_field.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.word_search_field.setObjectName("word_search_field")
        self.word_search_field_layout.addWidget(self.word_search_field)
        spacer_item11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.word_search_field_layout.addItem(spacer_item11)
        self.vertical_layout.addLayout(self.word_search_field_layout)
        self.word_proccessor_layout = QtWidgets.QHBoxLayout()
        self.word_proccessor_layout.setSpacing(0)
        self.word_proccessor_layout.setObjectName("word_proccessor_layout")
        spacer_item12 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.word_proccessor_layout.addItem(spacer_item12)
        self.document_layout = QtWidgets.QHBoxLayout()
        self.document_layout.setObjectName("document_layout")
        self.scroll_area = QtWidgets.QScrollArea(self.central_widget)
        self.scroll_area.setMinimumSize(QtCore.QSize(1030, 300))
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.sheets_scroll_area = QtWidgets.QWidget()
        self.sheets_scroll_area.setGeometry(QtCore.QRect(0, 0, 1028, 638))
        self.sheets_scroll_area.setObjectName("sheets_scroll_area")
        self.sheets_layout = QtWidgets.QVBoxLayout(self.sheets_scroll_area)
        self.sheets_layout.setContentsMargins(0, 0, 0, 0)
        self.sheets_layout.setSpacing(30)
        self.sheets_layout.setObjectName("verticalLayout_3")
        self.scroll_area.setWidget(self.sheets_scroll_area)
        self.document_layout.addWidget(self.scroll_area)
        self.word_proccessor_layout.addLayout(self.document_layout)
        spacer_item13 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.word_proccessor_layout.addItem(spacer_item13)
        self.vertical_layout.addLayout(self.word_proccessor_layout)
        WordProccessor.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(WordProccessor)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 1086, 26))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(175, 236, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 236, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 236, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 236, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 236, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 236, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 236, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 236, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 236, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.menu_bar.setPalette(palette)
        self.menu_bar.setObjectName("menu_bar")
        self.menu = QtWidgets.QMenu(self.menu_bar)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(175, 236, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 236, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 236, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 236, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 236, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 236, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 236, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 236, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 236, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.menu.setPalette(palette)
        self.menu.setObjectName("menu")
        WordProccessor.setMenuBar(self.menu_bar)
        self.add_document_action = QtWidgets.QAction(WordProccessor)
        self.add_document_action.setObjectName("add_document_action")
        self.open_document_action = QtWidgets.QAction(WordProccessor)
        self.open_document_action.setObjectName("open_document_action")
        self.save_document_action = QtWidgets.QAction(WordProccessor)
        self.save_document_action.setObjectName("save_document_action")
        self.save_document_where_action = QtWidgets.QAction(WordProccessor)
        self.save_document_where_action.setObjectName("save_document_where_action")
        self.menu.addAction(self.add_document_action)
        self.menu.addAction(self.open_document_action)
        self.menu.addAction(self.save_document_action)
        self.menu.addAction(self.save_document_where_action)
        self.menu_bar.addAction(self.menu.menuAction())

        self.retranslateUi(WordProccessor)
        QtCore.QMetaObject.connectSlotsByName(WordProccessor)

    def retranslateUi(self, WordProccessor):
        _translate = QtCore.QCoreApplication.translate
        WordProccessor.setWindowTitle(_translate("WordProccessor", "Word Proccessor"))

        self.font_color.setItemText(0, _translate("WordProccessor", "Black"))
        self.font_color.setItemText(1, _translate("WordProccessor", "Red"))
        self.font_color.setItemText(2, _translate("WordProccessor", "Yellow"))
        self.font_color.setItemText(3, _translate("WordProccessor", "Green"))
        self.font_color.setItemText(4, _translate("WordProccessor", "Orange"))
        self.font_color.setItemText(5, _translate("WordProccessor", "Blue"))
        self.font_color.setItemText(6, _translate("WordProccessor", "Purple"))
        self.font_size.setItemText(0, _translate("WordProccessor", "8"))
        self.font_size.setItemText(1, _translate("WordProccessor", "9"))
        self.font_size.setItemText(2, _translate("WordProccessor", "10"))
        self.font_size.setItemText(3, _translate("WordProccessor", "11"))
        self.font_size.setItemText(4, _translate("WordProccessor", "12"))
        self.font_size.setItemText(5, _translate("WordProccessor", "14"))
        self.font_size.setItemText(6, _translate("WordProccessor", "16"))
        self.font_size.setItemText(7, _translate("WordProccessor", "18"))
        self.font_size.setItemText(8, _translate("WordProccessor", "20"))
        self.font_size.setItemText(9, _translate("WordProccessor", "24"))
        self.font_size.setItemText(10, _translate("WordProccessor", "26"))
        self.font_size.setItemText(11, _translate("WordProccessor", "28"))
        self.font_size.setItemText(12, _translate("WordProccessor", "36"))
        self.font_size.setItemText(13, _translate("WordProccessor", "48"))
        self.font_size.setItemText(14, _translate("WordProccessor", "72"))
        self.menu.setTitle(_translate("WordProccessor", "Файл"))
        self.add_document_action.setText(_translate("WordProccessor", "Создать"))
        self.open_document_action.setText(_translate("WordProccessor", "Открыть..."))
        self.save_document_action.setText(_translate("WordProccessor", "Сохранить"))
        self.save_document_where_action.setText(_translate("WordProccessor", "Сохранить как..."))
