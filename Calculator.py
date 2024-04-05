import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
<class>Form</class>
<widget class="QWidget" name="Form">
 <property name="geometry">
  <rect>
   <x>0</x>
   <y>0</y>
   <width>371</width>
   <height>565</height>
  </rect>
 </property>
 <property name="windowTitle">
  <string>Красивый калькулятор</string>
 </property>
 <widget class="QWidget" name="layoutWidget">
  <property name="geometry">
   <rect>
    <x>20</x>
    <y>20</y>
    <width>345</width>
    <height>481</height>
   </rect>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QLCDNumber" name="table"/>
   </item>
   <item>
    <layout class="QGridLayout" name="gridLayout">
     <item row="2" column="1">
      <widget class="QPushButton" name="btn8">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>8</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_digits</string>
       </attribute>
      </widget>
     </item>
     <item row="0" column="1">
      <widget class="QPushButton" name="btn2">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>2</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_digits</string>
       </attribute>
      </widget>
     </item>
     <item row="0" column="3">
      <widget class="QPushButton" name="btn_plus">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>+</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_binary</string>
       </attribute>
      </widget>
     </item>
     <item row="3" column="2">
      <widget class="QPushButton" name="btn_eq">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>=</string>
       </property>
      </widget>
     </item>
     <item row="3" column="0">
      <widget class="QPushButton" name="btn0">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>0</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_digits</string>
       </attribute>
      </widget>
     </item>
     <item row="3" column="3">
      <widget class="QPushButton" name="btn_div">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>/</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_binary</string>
       </attribute>
      </widget>
     </item>
     <item row="0" column="0">
      <widget class="QPushButton" name="btn1">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>1</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_digits</string>
       </attribute>
      </widget>
     </item>
     <item row="2" column="2">
      <widget class="QPushButton" name="btn9">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>9</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_digits</string>
       </attribute>
      </widget>
     </item>
     <item row="3" column="1">
      <widget class="QPushButton" name="btn_dot">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>.</string>
       </property>
      </widget>
     </item>
     <item row="0" column="2">
      <widget class="QPushButton" name="btn3">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>3</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_digits</string>
       </attribute>
      </widget>
     </item>
     <item row="1" column="0">
      <widget class="QPushButton" name="btn4">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>4</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_digits</string>
       </attribute>
      </widget>
     </item>
     <item row="1" column="1">
      <widget class="QPushButton" name="btn5">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>5</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_digits</string>
       </attribute>
      </widget>
     </item>
     <item row="2" column="0">
      <widget class="QPushButton" name="btn7">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>7</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_digits</string>
       </attribute>
      </widget>
     </item>
     <item row="1" column="2">
      <widget class="QPushButton" name="btn6">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>6</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_digits</string>
       </attribute>
      </widget>
     </item>
     <item row="1" column="3">
      <widget class="QPushButton" name="btn_minus">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>-</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_binary</string>
       </attribute>
      </widget>
     </item>
     <item row="2" column="3">
      <widget class="QPushButton" name="btn_mult">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>*</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_binary</string>
       </attribute>
      </widget>
     </item>
     <item row="4" column="0">
      <widget class="QPushButton" name="btn_pow">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>^</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_binary</string>
       </attribute>
      </widget>
     </item>
     <item row="4" column="1">
      <widget class="QPushButton" name="btn_sqrt">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>√</string>
       </property>
      </widget>
     </item>
     <item row="4" column="2">
      <widget class="QPushButton" name="btn_fact">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="text">
        <string>!</string>
       </property>
      </widget>
     </item>
     <item row="4" column="3">
      <widget class="QPushButton" name="btn_clear">
       <property name="minimumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>80</width>
         <height>80</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Helvetica</family>
         <pointsize>36</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(254, 166, 43);</string>
       </property>
       <property name="text">
        <string>С</string>
       </property>
      </widget>
     </item>
    </layout>
   </item>
  </layout>
 </widget>
</widget>
<resources/>
<connections/>
<buttongroups>
 <buttongroup name="buttonGroup_binary"/>
 <buttongroup name="buttonGroup_digits"/>
</buttongroups>
</ui>
"""


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)

        # Подключаем цифры
        for i in self.buttonGroup_digits.buttons():
            i.clicked.connect(self.add_char)
            # Подключаем бинарные операции (+,-,*,/)
        for i in self.buttonGroup_binary.buttons():
            i.clicked.connect(self.calc)
        # Подключаем точку
        self.btn_dot.clicked.connect(self.add_char)
        # Подключаем кнопку равно
        self.btn_eq.clicked.connect(self.evaluate_result)
        # Подключаем кнопку очистки
        self.btn_clear.clicked.connect(self.clear)
        # Подключаем унарные операции
        self.btn_sqrt.clicked.connect(self.sqrt)
        self.btn_fact.clicked.connect(self.fact)

        # Переменная, в которой хранится последнее введённое число/результат вычисленного выражения
        self.data = ''
        # Переменная, в которой хранится выражение, которое нужно подсчитать
        self.data_eval = ''

    def eval_fact(self, n):
        if n < 0:
            return -1
        if n == 0:
            return 1
        else:
            return n * self.eval_fact(n - 1)

    def fact(self):
        if self.data_eval:
            self.data_eval = f'self.eval_fact({self.data_eval})'
            self.evaluate_result()

    # Сброс всех данных, очистка экрана
    def clear(self):
        self.data = ''
        self.data_eval = ''
        self.table.display('')

    def add_char(self):
        # Формируется число, с помощью нажатий кнопок и отображается на дисплее
        if self.sender().text() == '.':
            if '.' in self.data:
                return
        if self.data != '0' or (
                self.data == '0' and self.sender().text() == '.'):
            self.data = self.data + self.sender().text()
            self.data_eval = self.data_eval + self.sender().text()
            self.table.display(self.data)
        else:
            self.data = self.sender().text()
            self.data_eval = self.sender().text()
            self.table.display(self.data)

    def sqrt(self):
        if self.data_eval:
            self.data_eval = f'({self.data_eval})**0.5'
            self.evaluate_result()

    def evaluate_result(self):
        # Происходит попытка вычисления выражения, в случае попытки деления на 0, выводится ошибка
        try:
            self.data = eval(self.data_eval)
            self.data_eval = str(self.data)
            self.table.display(self.data)
        except Exception as _:
            self.table.display('Error')
        self.data = ''

    def calc(self):
        # Происходит вычисление текущего выражения и дописывается новый знак.
        # Если последним был уже знак действия, то он менятся.
        if self.data_eval:
            self.evaluate_result()
            if (self.data_eval[-1] not in ['+', '-', '/', '*']):
                self.data_eval += self.sender().text()
            else:
                self.data_eval = self.data_eval[0:len(
                    self.data_eval) - 1] + self.sender().text()
            self.data_eval = self.data_eval.replace('^', '**')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
