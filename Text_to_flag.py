import io
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>405</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>FlagMaker</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>90</y>
      <width>101</width>
      <height>84</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QLabel" name="label">
       <property name="text">
        <string>Цвет №1</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton1">
       <property name="minimumSize">
        <size>
         <width>158</width>
         <height>17</height>
        </size>
       </property>
       <property name="text">
        <string>Синий</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_2">
       <property name="text">
        <string>Красный</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_3">
       <property name="text">
        <string>Зелёный</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>90</y>
      <width>111</width>
      <height>84</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_2">
     <item>
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>Цвет №2</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_4">
       <property name="text">
        <string>Синий</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_5">
       <property name="text">
        <string>Красный</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_6">
       <property name="text">
        <string>Зелёный</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_3">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>90</y>
      <width>160</width>
      <height>84</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_3">
     <item>
      <widget class="QLabel" name="label_3">
       <property name="text">
        <string>Цвет №3</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_7">
       <property name="text">
        <string>Синий</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_8">
       <property name="text">
        <string>Красный</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_9">
       <property name="text">
        <string>Зелёный</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="make_flag">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>220</y>
      <width>101</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Сделать флаг</string>
    </property>
   </widget>
   <widget class="QLabel" name="result">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>295</y>
      <width>191</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>405</width>
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


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        ff = io.StringIO(template)
        uic.loadUi(ff, self)
        QMainWindow.setFixedSize(self, 400, 400)
        self.color_group_1 = QButtonGroup()
        self.color_group_2 = QButtonGroup()
        self.color_group_3 = QButtonGroup()
        self.color_group_1.addButton(self.radioButton1, id=1)
        self.color_group_1.addButton(self.radioButton_2, id=2)
        self.color_group_1.addButton(self.radioButton_3, id=3)
        self.color_group_2.addButton(self.radioButton_4, id=4)
        self.color_group_2.addButton(self.radioButton_5, id=5)
        self.color_group_2.addButton(self.radioButton_6, id=6)
        self.color_group_3.addButton(self.radioButton_7, id=7)
        self.color_group_3.addButton(self.radioButton_8, id=8)
        self.color_group_3.addButton(self.radioButton_9, id=9)
        self.make_flag.clicked.connect(self.run)

    def run(self):
        f = self.color_group_1.checkedButton().text()
        s = self.color_group_2.checkedButton().text()
        t = self.color_group_3.checkedButton().text()
        self.result.setText(f'Цвета: {f}, {s} и {t}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec_())
