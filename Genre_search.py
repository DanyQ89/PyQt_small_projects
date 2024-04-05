import io
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MyWidget</class>
 <widget class="QWidget" name="MyWidget">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>526</width>
    <height>470</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Фильтрация по жанрам</string>
  </property>
  <widget class="QPushButton" name="queryButton">
   <property name="geometry">
    <rect>
     <x>50</x>
     <y>90</y>
     <width>75</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Пуск</string>
   </property>
  </widget>
  <widget class="QComboBox" name="parameterSelection">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>30</y>
     <width>121</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QTableWidget" name="tableWidget">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>30</y>
     <width>341</width>
     <height>251</height>
    </rect>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.cur = None
        self.con = None
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()
        self.queryButton.clicked.connect(self.run)

    def new(self):
        pass

    def add(self, arr):
        self.tableWidget.setRowCount(0)
        for i in arr:
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for g in range(3):
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, g, QTableWidgetItem(str(i[g])))

    def run(self):
        g = self.parameterSelection.currentText()
        filt = self.cur.execute(f"""SELECT title, genre, year FROM Films 
        WHERE genre IN (SELECT id FROM genres WHERE title = '{g}')""").fetchall()
        self.tableWidget.setColumnCount(3)
        self.add(list(filt))

    def initUI(self):
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Название', 'Жанр', 'Год'])

        self.con = sqlite3.connect('films_db.sqlite')
        self.cur = self.con.cursor()
        result = self.cur.execute(
            """SELECT DISTINCT genres.title FROM genres JOIN Films ON Films.genre = genres.id""").fetchall()
        for i in result:
            self.parameterSelection.addItem(i[0])
        g = self.cur.execute("""SELECT title, genre, year FROM Films""").fetchall()
        self.add(list(g))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
