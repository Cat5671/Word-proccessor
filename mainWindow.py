import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QSizePolicy, QMenu, QAction
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QFont
from layoutWordProccessor1 import Ui_WordProcessor
from docx import Document
import docx


class Sheet(QTextEdit):

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
        self.current_font = "MS Shell Dlg 2"
        self.current_color = "Black"
        self.current_size = "8"
        self.setStyleSheet("""
                    QTextEdit {
                        background-color: #FFFFFF;
                        padding-left: 144px;     /* Отступ слева (1.27 см) */
                        padding-right: 72px;    /* Отступ справа (1.27 см) */
                        padding-top: 96px;      /* Отступ сверху (1.27 см) */
                        padding-bottom: 96px;   /* Отступ снизу (1.27 см) */
                        
                        
                    }
                """)

        self.textChanged.connect(lambda: self.check_text_height(sheets_layout))
        self.sheet1 = None

    def check_text_height(self, sheets_layout):
        check = self.cursorRect(self.textCursor()).y() + self.cursorRect().height()

        if check > 1208 and self.sheet1 is None:
            self.sheet1 = Sheet(sheets_layout)
            self.sheet1.current_font = self.current_font
            self.sheet1.current_color = self.current_color
            self.sheet1.current_size = self.current_size
            self.sheet1.setFontFamily(self.sheet1.current_font)
            print(self.sheet1.fontFamily())

            self.move_cursor(self.sheet1)

        elif check > 1208:
            self.move_cursor(self.sheet1)

        self.set_font("mS Shell Dlg 2")
        self.set_color("black")
        self.set_size("7")
        self.set_underline(self.fontUnderline())
        self.set_bold(self.fontWeight())
        self.set_italic(self.fontItalic())
    def move_cursor(self, sheet):
        self.cursor = sheet.textCursor()
        self.cursor.setPosition(0)
        sheet.setFocus()
        sheet.setTextCursor(self.cursor)

    def set_font(self, font="mS Shell Dlg 2"):
        if font != "mS Shell Dlg 2":
            self.current_font = font

        self.setFontFamily(self.current_font)
        if self.sheet1 is None:
            pass
        else:
            self.sheet1.set_font(self.current_font)

    def set_size(self, font_size="7"):
        if font_size != "7":
            self.current_size = font_size

        self.setFontPointSize(int(self.current_size))
        if self.sheet1 is None:
            pass
        else:
            self.sheet1.set_font(self.current_size)

    def set_color(self, font_color="Black"):
        if font_color != "black":
            self.current_color = font_color

        self.setTextColor(QColor(self.current_color))
        if self.sheet1 is None:
            pass
        else:
            self.sheet1.set_color(font_color)

    def count_u(self):
        if self.fontUnderline():
            self.set_underline(False)
        else:
            self.set_underline(True)

    def count_b(self):
        if self.fontWeight():
            self.set_bold(False)
        else:
            self.set_bold(QFont.Bold)

    def count_i(self):
        if self.fontItalic():
            self.set_italic(False)
        else:
            self.set_italic(True)

    def set_underline(self, c):
        self.setFontUnderline(c)
        if self.sheet1 is None:
            pass
        else:
            self.sheet1.set_underline(c)

    def set_bold(self, c):
        self.setFontWeight(c)
        if self.sheet1 is None:
            pass
        else:
            self.sheet1.set_bold(c)

    def set_italic(self, c):
        self.setFontItalic(c)
        if self.sheet1 is None:
            pass
        else:
            self.sheet1.set_italic(c)

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)
        copy_action = QAction("Копировать", self)
        insert_action = QAction("Вставить", self)

        context_menu.addAction(copy_action)
        context_menu.addAction(insert_action)


        context_menu.exec(event.globalPos())



class WordProcessor(QMainWindow, Ui_WordProcessor):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)
        self.resize(800, 600)
        self.current_file_path = None

        self.sheet = Sheet(self.sheets_layout)
        self.fonts.currentTextChanged.connect(self.sheet.set_font)
        self.font_size.currentTextChanged.connect(self.sheet.set_size)
        self.font_color.currentTextChanged.connect(self.sheet.set_color)
        self.underline_text_button.clicked.connect(self.sheet.count_u)
        self.italic_text_button.clicked.connect(self.sheet.count_i)
        self.bold_text_button.clicked.connect(self.sheet.count_b)


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
