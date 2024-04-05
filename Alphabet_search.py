import io
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MyWidget</class>
 <widget class="QWidget" name="MyWidget">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>764</width>
    <height>758</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Алфавитный указатель</string>
  </property>
  <widget class="QTableWidget" name="tableWidget">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>70</y>
     <width>741</width>
     <height>421</height>
    </rect>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()
        self.size = 15
        self.x, self.y = 50, 50
        self.buttons = []
        for char in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
            button = QPushButton(char, self)
            button.clicked.connect(self.on_click)
            button.resize(self.size, self.size)
            button.move(self.x, self.y)
            self.x += self.size
            self.buttons.append(button)
        self.hbox = QHBoxLayout()
        for button in self.buttons:
            self.hbox.addWidget(button)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Название', 'Год', 'Жанр', 'Продолжительность'])

    def on_click(self):
        sender = self.sender().text()
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        result = cur.execute(f"""SELECT id, title, year, genre, duration FROM films
         WHERE title like '{sender}%'""").fetchall()
        self.tableWidget.setRowCount(0)
        for i in result:
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for g in range(5):
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, g, QTableWidgetItem(str(i[g])))
        if len(result):
            QMainWindow.statusBar(self).showMessage(f'Нашлось {len(result)} записей')
        else:
            QMainWindow.statusBar(self).showMessage('К сожалению, ничего не нашлось')

    def initUI(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
