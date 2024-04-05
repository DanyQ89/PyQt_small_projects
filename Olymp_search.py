import csv
import io
import sys

from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>OlympResultWin</class>
 <widget class="QWidget" name="OlympResultWin">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>501</width>
    <height>470</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Результат олимпиады: фильтрация</string>
  </property>
  <widget class="QTableWidget" name="tableWidget">
   <property name="geometry">
    <rect>
     <x>15</x>
     <y>91</y>
     <width>471</width>
     <height>341</height>
    </rect>
   </property>
  </widget>
  <widget class="QPushButton" name="resultButton">
   <property name="geometry">
    <rect>
     <x>330</x>
     <y>40</y>
     <width>151</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>Узнать результаты</string>
   </property>
  </widget>
  <widget class="QComboBox" name="schools">
   <property name="geometry">
    <rect>
     <x>28</x>
     <y>31</y>
     <width>91</width>
     <height>31</height>
    </rect>
   </property>
  </widget>
  <widget class="QComboBox" name="classes">
   <property name="geometry">
    <rect>
     <x>148</x>
     <y>31</y>
     <width>111</width>
     <height>31</height>
    </rect>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


def find_color(color, best):
    if best == 301:
        color = QColor('#CCCC00')
    else:
        if color == QColor('#CCCC00'):
            color = QColor('#B5B5BD')
        elif color == QColor('#B5B5BD'):
            color = QColor('#9C5221')
        else:
            color = None
    return color


class OlympResultWin(QWidget):
    def __init__(self):
        super().__init__()
        self.data = None
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()
        self.resultButton.clicked.connect(self.results)

    def results(self):
        def painting():
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(el[0]))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(str(el[-1])))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, QTableWidgetItem(el[-2]))
            if color:
                for index_el in range(3):
                    self.tableWidget.item(self.tableWidget.rowCount() - 1, index_el).setBackground(color)

        school_value = self.schools.itemText(self.schools.currentIndex())
        class_value = self.classes.itemText(self.classes.currentIndex())
        if school_value != 'Все':
            school_value = int(school_value)
        if class_value != 'Все':
            class_value = int(class_value)
        self.tableWidget.setRowCount(0)
        best = 301
        color = None
        if 'Все' not in str(school_value) + str(class_value):
            for i in range(len(self.data)):
                el = self.data[i]
                if el[1] == school_value and el[2] == class_value:
                    if el[-1] < best:
                        color = find_color(color, best)
                        best = el[-1]
                    painting()

        elif school_value != 'Все':
            for i in range(len(self.data)):
                el = self.data[i]
                if school_value == el[1]:
                    if el[-1] < best:
                        color = find_color(color, best)
                        best = el[-1]
                    painting()

        elif class_value != "Все":
            for i in range(len(self.data)):
                el = self.data[i]
                if class_value == el[2]:
                    if el[-1] < best:
                        color = find_color(color, best)
                        best = el[-1]
                    painting()

        else:
            for i in range(len(self.data)):
                el = self.data[i]
                if el[-1] < best:
                    color = find_color(color, best)
                    best = el[-1]
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(el[0]))
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(str(el[-1])))
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, QTableWidgetItem(el[-2]))
                if color:
                    for index in range(3):
                        self.tableWidget.item(self.tableWidget.rowCount() - 1, index).setBackground(color)

    def initUI(self):
        with open('rez.csv', encoding='utf8') as file:
            data = list(csv.reader(file, delimiter=','))[1:]
            data = list(
                map(lambda x: [x[1].split()[-2], int(x[2].split('-')[-3]), int(x[2].split('-')[-2]), x[1], int(x[-1])],
                    data))
            self.data = data
            for i in [self.schools, self.classes]:
                i.addItem('Все')
            for i in sorted(set(map(lambda x: x[1], data))):
                i = str(i)
                self.schools.addItem(i if len(i) > 1 else f'0{i}')
            for i in sorted(set(map(lambda x: x[2], data))):
                i = str(i)
                self.classes.addItem(i if len(i) > 1 else f'0{i}')
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Фамилия", "Результат", 'Логин'])
        best = 301
        color = ''
        for i in range(len(data)):
            el = data[i]
            if el[-1] < best:
                color = find_color(color, best)
                best = el[-1]
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(data[i][0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(data[i][-1])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(data[i][-2])))
            if color:
                for index in range(3):
                    self.tableWidget.item(i, index).setBackground(color)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OlympResultWin()
    ex.show()
    sys.exit(app.exec())
