import csv
import io
import sys

from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>TitanicSearch</class>
 <widget class="QWidget" name="TitanicSearch">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>600</width>
    <height>470</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Поиск на Титанике </string>
  </property>
  <widget class="QTableWidget" name="resultTable">
   <property name="geometry">
    <rect>
     <x>15</x>
     <y>91</y>
     <width>561</width>
     <height>341</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>50</x>
     <y>40</y>
     <width>141</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>Подстрока для поиска:</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="searchEdit">
   <property name="geometry">
    <rect>
     <x>180</x>
     <y>40</y>
     <width>381</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class TitanicSearch(QWidget):
    def __init__(self):
        super().__init__()
        self.data = None
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()
        self.searchEdit.textChanged.connect(self.run)

    def run(self):
        name = self.searchEdit.text()
        survived = QColor('#00FF00')
        not_survived = QColor('#FF0000')
        self.resultTable.setRowCount(0)
        color = ''
        for i in range(1, len(self.data)):
            el = self.data[i]
            if len(name) >= 3:
                if name.lower() not in el[1].lower():
                    continue
            if el[-2] == '1':
                color = survived
            else:
                color = not_survived
            self.resultTable.setRowCount(self.resultTable.rowCount() + 1)
            for g in range(len(self.data[0])):
                self.resultTable.setItem(self.resultTable.rowCount() - 1, g, QTableWidgetItem(str(el[g])))
                self.resultTable.item(self.resultTable.rowCount() - 1, g).setBackground(color)

    def initUI(self):
        with open('titanic.csv', encoding='utf8') as file:
            data = list(csv.reader(file))
            self.data = data
            self.resultTable.setColumnCount(len(data[0]))
            self.resultTable.setHorizontalHeaderLabels(data[0])
            survived = QColor('#00FF00')
            not_survived = QColor('#FF0000')
            color = ''
            for i in range(1, len(data)):
                el = data[i]
                if el[-2] == '1':
                    color = survived
                else:
                    color = not_survived
                self.resultTable.setRowCount(self.resultTable.rowCount() + 1)
                for g in range(len(data[0])):
                    self.resultTable.setItem(self.resultTable.rowCount() - 1, g, QTableWidgetItem(str(el[g])))
                    self.resultTable.item(self.resultTable.rowCount() - 1, g).setBackground(color)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TitanicSearch()
    ex.show()
    sys.exit(app.exec())
