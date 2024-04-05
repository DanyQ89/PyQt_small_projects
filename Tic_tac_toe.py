import sys
from collections import defaultdict

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QLabel
from numpy import array_split


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.val = 'X'
        self.counter = 0

    def initUI(self):
        self.d = defaultdict(str)
        self.setGeometry(400, 400, 400, 400)

        self.x = QRadioButton('X', self)
        self.o = QRadioButton('O', self)
        self.x.move(100, 25)
        self.o.move(150, 25)
        self.x.click()
        self.x.clicked.connect(self.func)
        self.o.clicked.connect(self.func)
        self.arr = []

        val_x = 100
        val_y = 100
        for i in range(1, 10):
            num = i
            if i in [4, 7]:
                val_y += 51
                val_x = 100
            i = QPushButton('', self)
            i.resize(50, 50)
            i.move(val_x, val_y)
            self.arr.append(i)
            val_x += 51
            i.clicked.connect(self.func)

        self.result = QLabel('', self)
        self.result.move(120, 260)
        self.result.resize(100, 20)
        self.new_game = QPushButton('Новая игра', self)
        self.new_game.move(120, 300)
        self.new_game.clicked.connect(self.func)

    @property
    def button_grid(self):
        need = [i for i in array_split(self.arr, 3)]
        # print(need)
        return need

    def func(self):
        sender = self.sender()
        if sender.text() == 'Новая игра':
            for i in self.arr:
                i.setEnabled(True)
                i.setText('')
            self.result.setText('')
            self.counter = 0
            if self.x.isChecked():
                self.val = 'X'
            else:
                self.val = 'O'
        elif sender.text() in ['O', 'X']:
            if sender.text() == 'O':
                self.val = 'O'
            else:
                self.val = 'X'
            for i in self.arr:
                i.setText('')
            self.result.setText('')
            self.counter = 0
        else:
            self.mark = self.val
            sender.setText(self.val)
            if self.val == 'X':
                self.val = 'O'
            else:
                self.val = 'X'

        a = list(map(lambda x: '' if not x.text() else x.text(), self.arr))

        if a[0] == a[1] == a[2] != '' or a[3] == a[4] == a[5] != '' or a[6] == a[7] == a[8] != '':
            print(a[3])
            self.result.setText(f'Выиграл {self.mark}!')
            for i in self.arr:
                i.setEnabled(False)
        elif a[0] == a[4] == a[8] != '' or a[2] == a[4] == a[6] != '':
            self.result.setText(f'Выиграл {self.mark}!')
            for i in self.arr:
                i.setEnabled(False)
        elif a[0] == a[3] == a[6] != '' or a[1] == a[4] == a[7] != '' or a[2] == a[5] == a[8] != '':
            self.result.setText(f'Выиграл {self.mark}!')
            for i in self.arr:
                i.setEnabled(False)
        self.counter += 1
        if self.counter == 9 and self.result.text() == '':
            self.result.setText('Ничья!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = TicTacToe()
    form.show()
    sys.exit(app.exec_())
