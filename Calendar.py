import datetime
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QPushButton, QLineEdit, QTimeEdit, QListWidget


# template =

class SimplePlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calendarWidget = None
        self.UiComponets()
        self.setGeometry(500, 500, 900, 500)
        self.addEventBtn = QPushButton('Добавить событие', self)
        self.addEventBtn.setGeometry(50, 330, 400, 25)
        self.addEventBtn.clicked.connect(self.func)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(50, 305, 400, 25)
        self.timeEdit = QTimeEdit(self)
        self.timeEdit.setGeometry(50, 30, 400, 20)
        self.eventList = QListWidget(self)
        self.eventList.setGeometry(460, 30, 400, 400)
        self.list_of_events = []

    def UiComponets(self):
        self.calendarWidget = QCalendarWidget(self)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setGeometry(50, 50, 400, 250)

    def func(self):
        # help_dt = str(self.calendarWidget.selectedDate()) + str(self.timeEdit.text())
        date = self.calendarWidget.selectedDate().toString('dd-MM-yyyy')
        time = self.timeEdit.time().toString()
        d = datetime.datetime.strptime(date + time, '%d-%m-%Y%H:%M:%S')
        # t = datetime.datetime.strptime(self.timeEdit.time().toString(), '%H:%M:%S')
        self.list_of_events.append([d, self.lineEdit.text()])
        self.list_of_events.sort()
        self.eventList.clear()
        for i in self.list_of_events:
            self.eventList.addItem(f'{datetime.datetime.strftime(i[0], "%Y-%m-%d %H:%M:%S")} - {i[1]}')
        # print(self.list_of_events)
        # dt_to_event = str(datetime.datetime.strptime(help_dt, "PyQt5.QtCore.QDate(%Y, %m, %d)%H:%M"))
        # self.eventList.addItem(f'{date} {time} - {self.lineEdit.text()}')
        # self.eventList.sortItems()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimplePlanner()
    ex.show()
    sys.exit(app.exec_())
