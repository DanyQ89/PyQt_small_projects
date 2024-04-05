import io
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MyNotes</class>
 <widget class="QMainWindow" name="MyNotes">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>560</width>
    <height>449</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Записная книжка</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>50</y>
      <width>160</width>
      <height>80</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>160</width>
      <height>80</height>
     </size>
    </property>
    <property name="maximumSize">
     <size>
      <width>160</width>
      <height>80</height>
     </size>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QLabel" name="label">
       <property name="minimumSize">
        <size>
         <width>158</width>
         <height>36</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>158</width>
         <height>36</height>
        </size>
       </property>
       <property name="text">
        <string>Имя</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_2">
       <property name="minimumSize">
        <size>
         <width>158</width>
         <height>36</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>158</width>
         <height>36</height>
        </size>
       </property>
       <property name="text">
        <string>Телефон</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>50</y>
      <width>160</width>
      <height>80</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>160</width>
      <height>80</height>
     </size>
    </property>
    <property name="maximumSize">
     <size>
      <width>160</width>
      <height>80</height>
     </size>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_2">
     <item>
      <widget class="QLineEdit" name="contactName">
       <property name="minimumSize">
        <size>
         <width>158</width>
         <height>20</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>158</width>
         <height>20</height>
        </size>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="contactNumber">
       <property name="minimumSize">
        <size>
         <width>158</width>
         <height>20</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>158</width>
         <height>20</height>
        </size>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="addContactBtn">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>80</y>
      <width>101</width>
      <height>31</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>101</width>
      <height>31</height>
     </size>
    </property>
    <property name="maximumSize">
     <size>
      <width>101</width>
      <height>31</height>
     </size>
    </property>
    <property name="text">
     <string>Добавить</string>
    </property>
   </widget>
   <widget class="QListWidget" name="contactList">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>140</y>
      <width>441</width>
      <height>211</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>441</width>
      <height>211</height>
     </size>
    </property>
    <property name="maximumSize">
     <size>
      <width>441</width>
      <height>211</height>
     </size>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.addContactBtn.clicked.connect(self.run)

    def run(self):
        self.contactList.addItem(f'{self.contactName.text()} {self.contactNumber.text()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec_())
