import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit, QSpinBox, QLCDNumber, QListWidget, QLabel


class Pseudonym(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setFixedSize(300, 300)
        self.setWindowTitle('Записная книжка')

        self.remainLcd = QLCDNumber(self)
        self.remainLcd.move(70, 250)
        self.remainLcd.resize(100, 40)

        self.stones = QSpinBox(self)
        self.count = self.stones.text()
        self.stones.move(10, 250)

        self.takeInput = QLineEdit(self)
        self.takeInput.move(250, 270)

        self.startButton = QPushButton("Задать", self)
        self.startButton.move(200, 250)
        self.startButton.clicked.connect(self.new_game)

        self.takeButton = QPushButton("Взять", self)
        self.takeButton.move(200, 200)
        self.takeButton.setEnabled(False)
        self.takeButton.clicked.connect(self.take)

        self.listWidget = QListWidget(self)

        self.resultLabel = QLabel(self)
        self.resultLabel.move(10, 200)
        self.resultLabel.show()
        self.resultLabel.resize(150, 40)

    def new_game(self):
        self.listWidget.clear()
        self.remainLcd.display(int(self.stones.text()))
        self.takeButton.setEnabled(True)
        self.resultLabel.clear()
        self.count = int(self.stones.text())

    def II(self, count):
        if count < 4:
            return count
        else:
            return count % 3 + 1

    def take(self):
        if 0 < int(self.takeInput.text()) and int(self.takeInput.text()) < 4:
            self.count -= int(self.takeInput.text())
            self.listWidget.addItem(f"Игрок взял - {self.takeInput.text()}")
            if self.count < 1:
                self.count = 0
                self.resultLabel.setText("Победа пользователя!")
                self.takeButton.setEnabled(False)
            else:
                self.turnII = self.II(self.count)
                self.count -= self.turnII
                self.listWidget.addItem(f"Компьютер взял - {self.turnII}")
                if self.count < 1:
                    self.count = 0
                    self.resultLabel.setText("Победа компьютера!")
                    self.takeButton.setEnabled(False)
        self.remainLcd.display(self.count)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pseudonym()
    ex.show()
    sys.exit(app.exec())
