import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QVBoxLayout, QWidget
from googletrans import Translator

class TranslationApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("翻訳アプリ")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.label = QLabel("テキストを入力して翻訳ボタンをクリックしてください", self)
        layout.addWidget(self.label)

        self.text_edit_input = QTextEdit(self)
        layout.addWidget(self.text_edit_input)

        self.translate_button = QPushButton("翻訳", self)
        self.translate_button.clicked.connect(self.translate_text)
        layout.addWidget(self.translate_button)

        self.text_edit_output = QTextEdit(self)
        self.text_edit_output.setReadOnly(True)
        layout.addWidget(self.text_edit_output)

        self.central_widget.setLayout(layout)

    def translate_text(self):
        text = self.text_edit_input.toPlainText()
        translator = Translator()
        result = translator.translate(text, dest='en')
        self.text_edit_output.setPlainText(result.text)

def main():
    app = QApplication(sys.argv)
    window = TranslationApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()