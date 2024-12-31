import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QSizePolicy, QMenu, QAction
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from layoutWordProccessor1 import Ui_WordProcessor
from docx import Document
import docx


class Sheet(QTextEdit):
    __instance = None

    def __init__(self, sheets_layout):
        super().__init__()
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setMinimumSize(QtCore.QSize(990, 1400))
        self.setMaximumSize(QtCore.QSize(990, 1400))
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                           "QMenuBar::item:selected {\n"
                           "background-color: #AAAAAA;\n"
                           " }")

        sheets_layout.addWidget(self)
        self.setStyleSheet("""
                    QTextEdit {
                        background-color: #FFFFFF;
                        font-family: 'Calibri', sans-serif;  /* Шрифт, как в Word */
                        font-size: 11pt;  /* Размер шрифта */
                        padding-left: 144px;     /* Отступ слева (1.27 см) */
                        padding-right: 72px;    /* Отступ справа (1.27 см) */
                        padding-top: 96px;      /* Отступ сверху (1.27 см) */
                        padding-bottom: 96px;   /* Отступ снизу (1.27 см) */
                        
                    }
                """)

        self.textChanged.connect(lambda: self.check_text_height(sheets_layout))

    def check_text_height(self, sheets_layout):
        check = self.cursorRect(self.textCursor()).y() + self.cursorRect().height()

        if check > 1208 and self.__instance is None:
            self.__instance = Sheet(sheets_layout)
            self.move_cursor(self.__instance)

        elif check > 1208:
            self.move_cursor(self.__instance)

    def move_cursor(self, sheet):
        self.cursor = sheet.textCursor()
        self.cursor.setPosition(0)
        sheet.setFocus()
        sheet.setTextCursor(self.cursor)

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)
        add_page_higher_action = QAction("Добавить страниу выше", self)
        add_page_lower_action = QAction("Добавить страницу ниже", self)
        delite_page_action = QAction("Удалить страницу", self)
        context_menu.addAction(add_page_higher_action)
        context_menu.addAction(add_page_lower_action)
        context_menu.addAction(delite_page_action)
        context_menu.exec(event.globalPos())


class WordProcessor(QMainWindow, Ui_WordProcessor):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)
        self.resize(800, 600)
        self.current_file_path = None

        self.sheet = Sheet(self.sheets_layout)


        self.save_document_action.triggered.connect(self.save_fast)
        self.save_document_where_action.triggered.connect(self.save_as_docx)
        self.open_document_action.triggered.connect(self.open_document)
        self.add_document_action.triggered.connect(self.add_new_document)

    def add_new_document(self):
        self.current_file_path = None
        self.sheet.setPlainText("")

    def save_fast(self):
        if self.current_file_path:
            self.save_to_path(self.current_file_path)
        else:
            self.save_as_docx()

    def save_as_docx(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл как...", "", "Документ Word (*.docx)")
        if file_path:
            self.current_file_path = file_path
            self.save_to_path(file_path)

    def save_to_path(self, file_path):
        try:
            doc = Document()
            text = self.sheet.toPlainText()

            for line in text.splitlines():
                doc.add_paragraph(line)

            doc.save(file_path)
            self.statusBar().showMessage(f"Файл сохранен: {file_path}", 5000)
        except Exception as e:
            self.statusBar().showMessage(f"Ошибка сохранения: {e}", 5000)

    def open_document(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Открыть документ...", "", "Документ Word (*.docx)")
        if file_path:
            try:
                doc = docx.Document(file_path)

                section = doc.sections[0]
                margins = section.left_margin, section.right_margin, section.top_margin, section.bottom_margin
                margins_in_pixels = [(margin // 360000) * 48 for margin in margins]
                self.apply_margins_to_stylesheet(margins_in_pixels)

                text = ""
                for paragraph in doc.paragraphs:
                    text += paragraph.text + "\n"

                self.sheet.setPlainText(text)
                self.current_file_path = file_path
                self.statusBar().showMessage(f"Файл открыт: {file_path}", 5000)

            except Exception as e:
                self.QMessageBox.critical(self, "Ошибка", f"Не удалось открыть файл: {e}")

    def apply_margins_to_stylesheet(self, margins_in_pixels):
        # Устанавливаем отступы для QTextEdit, используя styleSheet
        left_margin, right_margin, top_margin, bottom_margin = margins_in_pixels
        print(margins_in_pixels)
        self.sheet.setStyleSheet(f"""
            QTextEdit {{
                background-color: #FFFFFF;
                font-family: 'Calibri', sans-serif;
                font-size: 11pt;
                padding-left: {left_margin}px;
                padding-right: {right_margin}px;
                padding-top: {top_margin}px;
                padding-bottom: {bottom_margin}px;
            }}
        """)



app = QApplication(sys.argv)
ex = WordProcessor()
ex.show()
sys.exit(app.exec_())
