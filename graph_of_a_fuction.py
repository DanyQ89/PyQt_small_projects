import io
import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow
from PyQt5.QtWidgets import QApplication

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MyWidget</class>
 <widget class="QWidget" name="MyWidget">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>601</width>
    <height>540</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Фильмотека 1.0 </string>
  </property>
  <widget class="PlotWidget" name="widget">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>30</y>
     <width>581</width>
     <height>281</height>
    </rect>
   </property>
  </widget>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>450</x>
     <y>340</y>
     <width>141</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Построить График</string>
   </property>
  </widget>
  <widget class="QTextEdit" name="textEdit">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>370</y>
     <width>361</width>
     <height>31</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>330</y>
     <width>311</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>Введите формулу графика в формате y = x*2 или x * 2</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>421</y>
     <width>321</width>
     <height>21</height>
    </rect>
   </property>
   <property name="text">
    <string>Выберите кол-во точек (необязательно)</string>
   </property>
  </widget>
  <widget class="QSpinBox" name="spinBox">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>460</y>
     <width>221</width>
     <height>31</height>
    </rect>
   </property>
  </widget>
 </widget>
 <customwidgets>
  <customwidget>
   <class>PlotWidget</class>
   <extends>QGraphicsView</extends>
   <header>pyqtgraph</header>
  </customwidget>
 </customwidgets>
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
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(10 ** 4)
        self.spinBox.setValue(100)

    def run(self):
        self.widget.clear()
        text = self.textEdit.toPlainText()
        value = self.spinBox.value()
        if '=' in text:
            text = text.split('=')[1]
        if text:
            x = [i for i in range(value)]
            y = []
            for i in x:
                y.append(eval(text.replace('x', str(i))))
            self.widget.plot(x, y, pen='w')

    def initUI(self):
        self.setWindowTitle('График функции')
        self.setFixedSize(500, 500)
        self.pushButton.clicked.connect(self.run)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
