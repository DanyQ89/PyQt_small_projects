import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLineEdit, QLCDNumber


class MiniCalcularor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 150, 400, 150)
        self.setWindowTitle('Шестая программа')

        self.calculate_button = QPushButton('->', self)
        self.calculate_button.resize(self.calculate_button.sizeHint())
        self.calculate_button.move(150, 55)
        self.calculate_button.clicked.connect(self.action)

        self.label_1 = QLabel(self)
        self.label_2 = QLabel(self)
        self.label_sum = QLabel(self)
        self.label_sub = QLabel(self)
        self.label_mul = QLabel(self)
        self.label_div = QLabel(self)
        self.label_1.setText('Первое число(целое):')
        self.label_2.setText('Второе число(целое):')
        self.label_sum.setText('Сумма:')
        self.label_sub.setText('Разность:')
        self.label_mul.setText('Произведение:')
        self.label_div.setText('Частное:')
        self.label_1.move(0, 15)
        self.label_2.move(0, 65)
        self.label_sum.move(275, 20)
        self.label_sub.move(275, 45)
        self.label_mul.move(250, 65)
        self.label_div.move(275, 85)

        self.result_sum = QLCDNumber(self)
        self.result_sub = QLCDNumber(self)
        self.result_mul = QLCDNumber(self)
        self.result_div = QLCDNumber(self)
        self.result_sum.move(335, 15)
        self.result_sub.move(335, 40)
        self.result_mul.move(335, 65)
        self.result_div.move(335, 90)
        self.number_1 = QLineEdit(self)
        self.number_2 = QLineEdit(self)
        self.number_1.move(0, 30)
        self.number_2.move(0, 80)
        self.number_1.resize(self.number_1.sizeHint())
        self.number_2.resize(self.number_1.sizeHint())

    def action(self):
        a = int(self.number_1.text())
        b = int(self.number_2.text())
        if b:
            div = round(float(a / b), 3)
            self.result_div.display(str(div))
        else:
            self.result_div.display('Error')
        self.result_sum.display(a + b)
        self.result_sub.display(a - b)
        self.result_mul.display(a * b)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Evaluator()
    ex.show()
    sys.exit(app.exec())
