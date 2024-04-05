import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber, QLineEdit


class WordTrick(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 100, 400, 100)
        self.setWindowTitle('Фокус со словами')

        self.trick_button = QPushButton('->', self)
        self.trick_button.resize(self.trick_button.sizeHint())
        self.trick_button.move(150, 0)
        self.trick_button.clicked.connect(self.hello)

        self.first_value = QLineEdit(self)
        self.first_value.move(0, 0)
        self.second_value = QLineEdit(self)
        self.second_value.move(260, 0)
        self.first_value.resize(self.first_value.sizeHint())
        self.second_value.resize(self.first_value.sizeHint())

        # print(self.name)

        self.count = 0

    def hello(self):
        if self.second_value.text() and self.trick_button.text() == '->':
            self.first_value.setText('')
            self.second_value.setText('')
        if self.trick_button.text() == '->':
            self.trick_button.setText('<-')
        else:
            self.trick_button.setText('->')

        if self.first_value.text() != '':
            name = self.first_value.text()
            self.second_value.setText(name)
            self.first_value.setText('')
        elif self.second_value.text() != '':
            name = self.second_value.text()
            self.first_value.setText(name)
            self.second_value.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WordTrick()
    ex.show()
    sys.exit(app.exec())
