import random
import sys

from PyQt5.Qt import QMainWindow
from PyQt5.QtWidgets import QApplication, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.y = None
        self.x = None
        self.button = QPushButton('Нажми меня', self)
        self.button.resize(70, 50)
        self.button.move(100, 100)
        self.initUI()

    def rasst(self, xa, xb, ya, yb):
        return ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        if self.rasst(self.button.x(), self.x, self.button.y(), self.y) <= 100:
            x = random.randint(0, self.size().width() - self.button.size().width())
            y = random.randint(0, self.size().height() - self.button.size().height())
            self.button.move(x, y)

    def initUI(self):
        self.setWindowTitle('Убегающая кнопка')
        self.setMouseTracking(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
