import io
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>AntiPlagiarism</class>
 <widget class="QMainWindow" name="AntiPlagiarism">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>576</width>
    <height>587</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Антиплагиат v0.0001 </string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>9</x>
      <y>19</y>
      <width>541</width>
      <height>91</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QLabel" name="label">
       <property name="text">
        <string>Порог срабатывания (%)</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QDoubleSpinBox" name="alert_value"/>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>110</y>
      <width>541</width>
      <height>80</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_2">
     <item>
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>Текст 1</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_3">
       <property name="text">
        <string>Текст 2</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget_3">
    <property name="geometry">
     <rect>
      <x>9</x>
      <y>189</y>
      <width>541</width>
      <height>311</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_3">
     <item>
      <widget class="QPlainTextEdit" name="text1"/>
     </item>
     <item>
      <widget class="QPlainTextEdit" name="text2"/>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="checkBtn">
    <property name="geometry">
     <rect>
      <x>14</x>
      <y>502</y>
      <width>541</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Сравнить</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class AntiPlagiarism(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        # self.status_Bar = QMainWindow.statusBar(self)
        # self.status_Bar.resize(400, 20)
        # self.status_Bar.move(10, 525)
        self.checkBtn.clicked.connect(self.run)

    def run(self):
        set_1 = set()
        set_2 = set()
        for i in self.text1.toPlainText().split('\n'):
            set_1.add(i)
        for i in self.text2.toPlainText().split('\n'):
            set_2.add(i)
        need = 0
        a = len(set_1 - set_2) + len(set_2 - set_1)
        b = len(set_1.union(set_2))
        percent = 100.00 - round((a / b * 100.00), 2)
        if str(percent)[-2] == '.':
            dop = '0'
        else:
            dop = ''
        if percent >= self.alert_value.value():
            pl = 'плагиат'
        else:
            pl = 'не плагиат'
        QMainWindow.statusBar(self).showMessage(f'Тексты похожи на {percent}{dop}%, {pl}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AntiPlagiarism()
    ex.show()
    sys.exit(app.exec_())
