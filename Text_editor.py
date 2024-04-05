import io
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Notebook</class>
 <widget class="QMainWindow" name="Notebook">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>486</width>
    <height>416</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Текстовый редактор</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="formLayoutWidget">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>30</y>
      <width>321</width>
      <height>311</height>
     </rect>
    </property>
    <layout class="QFormLayout" name="formLayout">
     <item row="0" column="0">
      <widget class="QLineEdit" name="filename_edit"/>
     </item>
     <item row="0" column="1">
      <widget class="QPlainTextEdit" name="text_edit">
       <property name="plainText">
        <string/>
       </property>
      </widget>
     </item>
     <item row="3" column="0">
      <widget class="QPushButton" name="open_button">
       <property name="text">
        <string>Открыть файл</string>
       </property>
      </widget>
     </item>
     <item row="2" column="0">
      <widget class="QPushButton" name="save_button">
       <property name="text">
        <string>Сохранить файл</string>
       </property>
      </widget>
     </item>
     <item row="1" column="0">
      <widget class="QPushButton" name="new_button">
       <property name="text">
        <string>Создать новый</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>486</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Notebook(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.new_button.clicked.connect(self.new)
        self.save_button.clicked.connect(self.save)
        self.open_button.clicked.connect(self.open)

    def new(self):
        self.filename_edit.setText('')
        self.text_edit.clear()

    def save(self):
        with open(self.filename_edit.text(), 'w', encoding='utf8') as out_file:
            for i in self.text_edit.toPlainText():
                out_file.write(i)

    def open(self):
        self.text_edit.clear()
        try:
            text = self.filename_edit.text()
            if 'txt' not in text:
                text += '.txt'
            with open(text, encoding='utf8') as file:
                data = [i.strip() for i in file.readlines()]
                for i in data:
                    self.text_edit.appendPlainText(i)
        except Exception:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Notebook()
    ex.show()
    sys.exit(app.exec_())
