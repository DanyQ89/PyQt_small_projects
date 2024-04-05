import sys
from collections import defaultdict
from string import ascii_lowercase

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton


class MorseCode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.d = defaultdict(str)
        self.setGeometry(400, 400, 400, 400)
        val = 1
        for g in ascii_lowercase[:15]:
            g = QPushButton(g, self)
            g.resize(25, 25)
            g.move(val, 0)
            val += 25
            self.d[str(g.text())] = g
            g.clicked[bool].connect(self.func)

        val = 1
        for g in ascii_lowercase[15:]:
            g = QPushButton(g, self)
            g.resize(25, 25)
            g.move(val, 26)
            val += 25
            self.d[str(g.text())] = g
            g.clicked[bool].connect(self.func)

        self.result = QLineEdit(self)
        self.result.move(0, 51)
        self.result.resize(300, 30)

    @property
    def alphabet_buttons(self):
        return self.d

    def func(self):
        self.morze = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
                      'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                      'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
                      'm': '-_', 'n': '-.', 'o': '---', 'p': '.--.',
                      'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
                      'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                      'y': '-.--', 'z': '--..'}
        sender = self.sender().text()
        self.result.setText(self.result.text() + self.morze[sender])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MorseCode()
    form.show()
    sys.exit(app.exec_())
