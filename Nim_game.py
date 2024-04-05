import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QLabel


class NimStrikesBack(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.val = 10
        self.checkboxes = []
        self.inputs = []
        self.setGeometry(400, 400, 400, 400)

        self.btnp = QPushButton(f'+{str(randint(1, 20))}', self)
        self.btnm = QPushButton(f'-{str(randint(1, 20))}', self)
        self.btnp.move(50, 30)
        self.btnm.move(150, 30)
        self.btnm.clicked.connect(self.func)
        self.btnp.clicked.connect(self.func)

        self.X = randint(1, 15)

        self.moves_left = QLCDNumber(self)
        self.num = QLCDNumber(self)
        self.moves_left.display(self.val)
        self.num.display(self.X)
        self.moves_left.move(200, 100)
        self.num.move(200, 150)
        self.result_label = QLabel('', self)
        self.result_label.resize(200, 20)

    def func(self):
        sender = self.sender()
        self.moves_left.display(self.val)
        if self.result_label:
            self.result_label.setText('')
        if self.val > 1:
            self.X = eval(f'{self.X}{sender.text()[0]}{sender.text()[1:]}')
            if self.X == 0:
                self.val -= 1
                self.moves_left.display(self.val)
                self.X = 0
                self.num.display(self.X)
                self.result_label.setText('Вы победили, начинаем новую игру')
                self.btnm.setDisabled(True)
                self.btnp.setDisabled(True)
            else:
                self.num.display(self.X)
                self.val -= 1
                self.moves_left.display(self.val)
        else:
            self.X = eval(f'{self.X}{sender.text()[0]}{sender.text()[1:]}')
            if self.X == 0:
                self.result_label.setText('Вы победили, начинаем новую игру')
                self.btnm.setDisabled(True)
                self.btnp.setDisabled(True)
            else:
                self.result_label.setText('Вы проиграли, начинаем новую игру')
                self.Y = randint(1, 20)
                self.Z = randint(1, 20)
                self.btnp.setText(f'+{self.Y}')
                self.btnm.setText(f'-{self.Z}')
                self.X = randint(1, 15)
                self.num.display(self.X)
                self.val = 10
                self.moves_left.display(self.val)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = NimStrikesBack()
    form.show()
    sys.exit(app.exec_())
