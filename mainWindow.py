import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QSizePolicy, QMenu, QAction
from bs4 import BeautifulSoup
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QFont, QTextCharFormat
from layoutWordProccessor1 import Ui_WordProcessor
from docx import Document
import docx
from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn


class Sheet(QTextEdit):

    def __init__(self, sheets_layout, previous_sheet=None):
        super().__init__()
        self.previous_sheet = previous_sheet
        self.sheets_layout = sheets_layout
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
        self.f = -1
        self.sheet1 = None
        self.textChanged.connect(self.check_and_delete_if_empty)
        self.textChanged.connect(lambda: self.check_text_height(sheets_layout))
        self.cursorPositionChanged.connect(self.apply_styles_to_current_sheet)

    def check_text_height(self, sheets_layout):
        check = self.cursorRect(self.textCursor()).y() + self.cursorRect().height() * 2
        check2 = self.document().size().height()
        
        if check2 > 1208 and self.sheet1 is None:
            self.sheet1 = Sheet(sheets_layout, previous_sheet=self)
            self.text = self.toPlainText().split("\n")
            self.sheet1.insertPlainText(self.text.pop())
            
        elif check2 > 1208:
            if check > 1208:
                self.f -= 1
            self.text = self.toPlainText().split("\n")

            self.sheet1.insertPlainText("\n" + self.text[len(self.text) + self.f])

        if check > 1208 and self.sheet1 is None:
            self.sheet1 = Sheet(sheets_layout, previous_sheet=self)
            self.apply_styles_to_sheet(self.sheet1)
            self.move_cursor(self.sheet1)

        elif check > 1208:
            self.apply_styles_to_sheet(self.sheet1)
            self.move_cursor(self.sheet1)

    def check_and_delete_if_empty(self):
        text = self.toPlainText().strip()
        cursor = self.textCursor()
        if not text and not cursor.hasSelection():
            self.remove_sheet()

    def remove_sheet(self):
        if self.previous_sheet is None:
            print(2)
            return
        self.sheets_layout.removeWidget(self)

        if self.previous_sheet is not None:
            self.previous_sheet.sheet1 = None

        self.deleteLater()

    def apply_styles_to_current_sheet(self):
        self.set_font()
        self.set_size()
        self.set_color()
        self.set_underline(self.fontUnderline())
        self.set_bold(self.fontWeight())
        self.set_italic(self.fontItalic())

    def apply_styles_to_sheet(self, sheet):
        sheet.set_font(self.current_font)
        sheet.set_size(self.current_size)
        sheet.set_color(self.current_color)
        sheet.set_underline(self.fontUnderline())
        sheet.set_bold(self.fontWeight())
        sheet.set_italic(self.fontItalic())

    def move_cursor(self, sheet):
        self.cursor = sheet.textCursor()
        self.cursor.setPosition(0)
        sheet.setFocus()
        sheet.setTextCursor(self.cursor)

    def set_font(self, font="mS Shell Dlg 2"):

        if self.textCursor().selectionEnd() == self.textCursor().selectionStart():
            if font != "mS Shell Dlg 2":
                self.current_font = font

            self.setFontFamily(self.current_font)
            if self.sheet1 is not None:
                self.sheet1.set_font(self.current_font)

        elif font != "mS Shell Dlg 2":# условие для форматирования выделенного текста
            self.current_font = font
            self.setFontFamily(self.current_font)
            if self.sheet1 is not None:
                self.sheet1.set_font(self.current_font)

    def set_size(self, font_size="7"):
        if self.textCursor().selectionEnd() == self.textCursor().selectionStart():
            if font_size != "7":
                self.current_size = font_size

            self.setFontPointSize(int(self.current_size))
            if self.sheet1 is not None:
                self.sheet1.set_size(self.current_size)

        elif font_size != "7":
            self.current_size = font_size
            self.setFontPointSize(int(self.current_size))
            if self.sheet1 is not None:
                self.sheet1.set_size(self.current_size)

    def set_color(self, font_color="black"):
        if self.textCursor().selectionEnd() == self.textCursor().selectionStart():
            if font_color != "black":
                self.current_color = font_color

                self.setTextColor(QColor(self.current_color))
                if self.sheet1 is not None:
                    self.sheet1.set_color(self.current_color)

        elif font_color != "black":
            self.current_color = font_color
            self.setTextColor(QColor(self.current_color))
            if self.sheet1 is not None:
                self.sheet1.set_color(self.current_color)

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
        if self.sheet1 is not None:
            self.sheet1.set_underline(c)

    def set_bold(self, c):
        self.setFontWeight(c)
        if self.sheet1 is not None:
            self.sheet1.set_bold(c)

    def set_italic(self, c):
        self.setFontItalic(c)
        if self.sheet1 is not None:
            self.sheet1.set_italic(c)

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)
        copy_action = QAction("Копировать", self)
        insert_action = QAction("Вставить", self)

        context_menu.addAction(copy_action)
        context_menu.addAction(insert_action)

        copy_action.triggered.connect(self.copy)
        insert_action.triggered.connect(self.paste)

        context_menu.exec(event.globalPos())

    def iterate_sheets(self):
        current_sheet = self
        while current_sheet:
            yield current_sheet
            current_sheet = current_sheet.sheet1


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

            doc.styles['Normal'].font.name = 'Calibri'
            doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')

            html_content = ""
            for sheet in self.sheet.iterate_sheets():
                html_content += sheet.toHtml()

            soup = BeautifulSoup(html_content, "html.parser")

            for line in soup.find_all("p"):
                paragraph = doc.add_paragraph()
                for span in line.find_all("span"):
                    run = paragraph.add_run(span.text)
                    style = span.attrs.get("style", "")
                    if "font-size" in style:
                        size = int(style.split("font-size:")[1].split("pt")[0])
                        run.font.size = Pt(size)
                    if "font-family" in style:
                        font_name = style.split("font-family:")[1].split(";")[0].replace("'", "")
                        run.font.name = font_name
                    if "font-weight" in style and "bold" in style.lower():
                        run.bold = True
                    if "font-style" in style and "italic" in style.lower():
                        run.italic = True
                    if "text-decoration" in style and "underline" in style.lower():
                        run.underline = True
                    if "color" in style:
                        color_value = style.split("color:")[1].split(";")[0].strip()
                        run.font.color.rgb = RGBColor(int(color_value[1:3], 16), int(color_value[3:5], 16), int(color_value[5:7], 16))

            doc.save(file_path)
            self.statusBar().showMessage(f"Файл сохранен: {file_path}", 5000)
        except Exception as e:
            self.statusBar().showMessage(f"Ошибка сохранения: {e}", 5000)

    def open_document(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Открыть документ...", "", "Документ Word (*.docx)")
        if file_path:
            try:
                doc = docx.Document(file_path)
                html_content = ""
                sheet_count = len(doc.paragraphs)

                for paragraph in doc.paragraphs:
                    html_content += "<p>"
                    for run in paragraph.runs:
                        style = ""
                        if run.font.size:
                            size = run.font.size.pt
                            style += f"font-size: {size}pt; "
                        if run.font.name:
                            style += f"font-family: {run.font.name}; "
                        if run.font.bold:
                            style += "font-weight: bold; "
                        if run.font.italic:
                            style += "font-style: italic; "
                        if run.font.underline:
                            style += "text-decoration: underline; "
                        if run.font.color.rgb:
                            rgb = run.font.color.rgb
                            style += f"color: #{rgb}; "
                        html_content += f"<span style='{style}'>{run.text}</span>"
                    html_content += "</p>"

                for sheet in self.sheet.iterate_sheets():
                    sheet.setPlainText("")

                for i in range(sheet_count):
                    new_sheet = Sheet(self.sheets_layout)
                    self.apply_margins_to_stylesheet([0, 0, 0, 0])
                    new_sheet.setHtml(html_content)

                self.current_file_path = file_path
                self.statusBar().showMessage(f"Файл открыт: {file_path}", 5000)
            except Exception as e:
                self.statusBar().showMessage(f"Ошибка открытия: {e}", 5000)

    def apply_margins_to_stylesheet(self, margins_in_pixels):
        left_margin, right_margin, top_margin, bottom_margin = margins_in_pixels
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
