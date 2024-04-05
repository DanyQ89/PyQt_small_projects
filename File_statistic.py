import io
import sys
from statistics import mean

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>FileStat</class>
 <widget class="QMainWindow" name="FileStat">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>576</width>
    <height>564</height>
   </rect>
  </property>
  <property name="acceptDrops">
   <bool>false</bool>
  </property>
  <property name="windowTitle">
   <string>Файловая статистика</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>50</y>
      <width>491</width>
      <height>73</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QLabel" name="label">
       <property name="text">
        <string>Имя файла</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="filenameEdit"/>
     </item>
     <item>
      <widget class="QPushButton" name="button">
       <property name="text">
        <string>Рассчитать</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="formLayoutWidget">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>120</y>
      <width>491</width>
      <height>91</height>
     </rect>
    </property>
    <layout class="QFormLayout" name="formLayout">
     <item row="0" column="0">
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>Максимальное значение:</string>
       </property>
      </widget>
     </item>
     <item row="1" column="0">
      <widget class="QLabel" name="label_3">
       <property name="text">
        <string>Минимальное значение:</string>
       </property>
      </widget>
     </item>
     <item row="2" column="0">
      <widget class="QLabel" name="label_4">
       <property name="text">
        <string>Среднее значение:</string>
       </property>
      </widget>
     </item>
     <item row="0" column="1">
      <widget class="QLineEdit" name="maxEdit">
       <property name="text">
        <string>0</string>
       </property>
      </widget>
     </item>
     <item row="1" column="1">
      <widget class="QLineEdit" name="minEdit">
       <property name="text">
        <string>0</string>
       </property>
      </widget>
     </item>
     <item row="2" column="1">
      <widget class="QLineEdit" name="avgEdit">
       <property name="text">
        <string>0,00</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.button.clicked.connect(self.run)
        self.flag = True

    def set_zeros(self):
        self.maxEdit.setText('0')
        self.minEdit.setText('0')
        self.avgEdit.setText('0,00')

    def run(self):
        self.flag = True
        try:
            with open(self.filenameEdit.text(), encoding='utf8') as file:
                # with open('lines.txt', encoding='utf8') as file:
                data = file.readlines()
                # print(data)
                numbers = []
                for el in data:
                    if not self.flag:
                        break
                    now_num = ''
                    for i in el:
                        if i.isnumeric() or (i == '-' and not now_num):
                            now_num += i
                        elif i in ' \n\t':
                            if now_num:
                                numbers.append(int(now_num))
                                now_num = ''
                        else:
                            self.set_zeros()
                            QMainWindow.statusBar(self).showMessage("Файл содержит некорректные данные")
                            self.flag = False
                            break

                if not numbers and self.flag:
                    self.set_zeros()
                    QMainWindow.statusBar(self).showMessage("Указанный файл пуст")
                elif self.flag:
                    self.minEdit.setText(str(min(numbers)))
                    self.maxEdit.setText(str(max(numbers)))
                    mn = str(round(mean(numbers), 2)).replace('.', ',')
                    self.avgEdit.setText(f'{mn}{"0" if mn[-2] == "," else ""}')
                    with open('out.txt', 'w', encoding='utf8', newline="") as out_file:
                        print(f'Максимальное значение: {self.maxEdit.text()}', file=out_file)
                        print(f'Минимальное значение: {self.minEdit.text()}', file=out_file)
                        print(f'Среднее значение: {self.avgEdit.text()}', file=out_file)
        except FileNotFoundError:
            self.set_zeros()
            QMainWindow.statusBar(self).showMessage("Указанный файл не существует")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileStat()
    ex.show()
    sys.exit(app.exec_())
