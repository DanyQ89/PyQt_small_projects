import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QPlainTextEdit, QLineEdit


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.checkboxes = []
        self.inputs = []
        self.setGeometry(400, 400, 400, 400)

        val = 0
        for i in ['Чизбургер', 'Гамбургер', 'Кока-кола', 'Наггетсы']:
            smth = QCheckBox(i, self)
            smth_text = QLineEdit(None, self)
            smth_text.setPlaceholderText('0')
            self.checkboxes.append(smth)
            self.inputs.append(smth_text)
            smth.resize(80, 40)
            smth.move(0, val)
            smth_text.move(100, val + 10)
            val += 30
            smth.clicked[bool].connect(self.help_func)

        self.orderButton = QPushButton('Заказать', self)
        self.orderButton.move(15, 150)
        self.orderButton.clicked.connect(self.func)
        self.order = QPlainTextEdit('', self)
        self.order.resize(200, 200)
        self.order.move(0, 180)

    def help_func(self, click):
        sender = self.sender()
        if click:
            if not self.inputs[self.checkboxes.index(sender)].text():
                self.inputs[self.checkboxes.index(sender)].setText('1')
        else:
            self.inputs[self.checkboxes.index(sender)].setText(None)
            self.inputs[self.checkboxes.index(sender)].setPlaceholderText('0')

    def func(self):
        d = {"Чизбургер": 10, 'Гамбургер': 20, 'Кока-кола': 15, 'Наггетсы': 30}
        sum = 0
        self.order.setPlainText('Ваш заказ\n')
        for k, z in zip(self.checkboxes, self.inputs):
            if k.isChecked() or (z.text() != '' and not k.isChecked()):
                self.order.appendPlainText(f'{k.text()}-----{int(z.text())}-----{int(z.text()) * d[k.text()]}')
                sum += int(z.text()) * d[k.text()]

        self.order.appendPlainText(f'\nИтого: {sum}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.exit(app.exec_())
