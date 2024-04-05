import io

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton

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
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>69</x>
      <y>49</y>
      <width>411</width>
      <height>311</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="widgetArt"/>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class WidgetArt(QMainWindow):
    def __init__(self, matrix=None):
        super().__init__()
        self.matrix = matrix
        f = io.StringIO(template)
        uic.loadUi(f, self)
        # print(self.matrix)
        positions = [(i, j) for i in range(len(self.matrix)) for j in range(len(self.matrix[0]))]
        self.matrix = (' '.join(' '.join(i) for i in map(lambda x: [str(g) for g in x], self.matrix))).split()
        for position, name in zip(positions, self.matrix):
            if name == '1':
                name = '*'
            else:
                name = ''
            btn = QPushButton(name)
            self.widgetArt.addWidget(btn, *position)
            
