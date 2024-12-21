import sys
import docx
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLineEdit, QFileDialog
from layoutWordProccessor1 import Ui_wordProccessor
from docx import Document
import os

class WordProccessor(QMainWindow, Ui_wordProccessor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(800, 600)
        self.current_file_path = None

        self.saveDocument.triggered.connect(self.save_fast)
        self.saveDocumentWhere.triggered.connect(self.save_as_docx)
        self.openDocument.triggered.connect(self.open_document)
        self.addDocument.triggered.connect(self.new_document)
        self.document.setStyleSheet("""
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

    def new_document(self):
        self.current_file_path = None
        self.document.setPlainText("")

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
            text = self.document.toPlainText()

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


                self.document.setPlainText(text)
                self.current_file_path = file_path
                self.statusBar().showMessage(f"Файл открыт: {file_path}", 5000)

            except Exception as e:
                self.QMessageBox.critical(self, "Ошибка", f"Не удалось открыть файл: {e}")

    def apply_margins_to_stylesheet(self, margins_in_pixels):
        # Устанавливаем отступы для QTextEdit, используя styleSheet
        left_margin, right_margin, top_margin, bottom_margin = margins_in_pixels
        print(margins_in_pixels)
        self.document.setStyleSheet(f"""
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
ex = WordProccessor()
ex.show()
sys.exit(app.exec_())