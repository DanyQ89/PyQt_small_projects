import io
import sqlite3
import sys
from string import ascii_lowercase

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow, QMessageBox

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
  <widget class="QTabWidget" name="tabWidget">
   <property name="geometry">
    <rect>
     <x>6</x>
     <y>9</y>
     <width>581</width>
     <height>521</height>
    </rect>
   </property>
   <property name="currentIndex">
    <number>0</number>
   </property>
   <widget class="QWidget" name="filmsTab">
    <attribute name="title">
     <string>Tab 1</string>
    </attribute>
    <widget class="QPushButton" name="addFilmButton">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>20</y>
       <width>101</width>
       <height>23</height>
      </rect>
     </property>
     <property name="text">
      <string>Добавить фильм</string>
     </property>
    </widget>
    <widget class="QPushButton" name="editFilmButton">
     <property name="geometry">
      <rect>
       <x>120</x>
       <y>20</y>
       <width>111</width>
       <height>23</height>
      </rect>
     </property>
     <property name="text">
      <string>Изменить фильм</string>
     </property>
    </widget>
    <widget class="QPushButton" name="deleteFilmButton">
     <property name="geometry">
      <rect>
       <x>250</x>
       <y>20</y>
       <width>111</width>
       <height>23</height>
      </rect>
     </property>
     <property name="text">
      <string>Удалить фильм</string>
     </property>
    </widget>
    <widget class="QTableWidget" name="filmsTable">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>60</y>
       <width>561</width>
       <height>431</height>
      </rect>
     </property>
    </widget>
   </widget>
   <widget class="QWidget" name="genresTab">
    <attribute name="title">
     <string>Tab 2</string>
    </attribute>
    <widget class="QTableWidget" name="genresTable">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>60</y>
       <width>561</width>
       <height>431</height>
      </rect>
     </property>
    </widget>
    <widget class="QPushButton" name="addGenreButton">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>20</y>
       <width>101</width>
       <height>23</height>
      </rect>
     </property>
     <property name="text">
      <string>Добавить жанр</string>
     </property>
    </widget>
    <widget class="QPushButton" name="editGenreButton">
     <property name="geometry">
      <rect>
       <x>124</x>
       <y>20</y>
       <width>131</width>
       <height>23</height>
      </rect>
     </property>
     <property name="text">
      <string>Редактировать жанр</string>
     </property>
    </widget>
    <widget class="QPushButton" name="deleteGenreButton">
     <property name="geometry">
      <rect>
       <x>264</x>
       <y>20</y>
       <width>111</width>
       <height>23</height>
      </rect>
     </property>
     <property name="text">
      <string>Удалить жанр</string>
     </property>
    </widget>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
template_1 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>AddFilmWidget</class>
 <widget class="QWidget" name="AddFilmWidget">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>442</width>
    <height>388</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Добавить элемент</string>
  </property>
  <widget class="QWidget" name="formLayoutWidget">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>100</y>
     <width>401</width>
     <height>221</height>
    </rect>
   </property>
   <layout class="QFormLayout" name="formLayout">
    <item row="0" column="0">
     <widget class="QLabel" name="label">
      <property name="text">
       <string>Название</string>
      </property>
     </widget>
    </item>
    <item row="0" column="1">
     <widget class="QPlainTextEdit" name="title"/>
    </item>
    <item row="1" column="0">
     <widget class="QLabel" name="label_2">
      <property name="text">
       <string>Год выпуска</string>
      </property>
     </widget>
    </item>
    <item row="1" column="1">
     <widget class="QPlainTextEdit" name="year"/>
    </item>
    <item row="2" column="0">
     <widget class="QLabel" name="label_4">
      <property name="text">
       <string>Жанр</string>
      </property>
     </widget>
    </item>
    <item row="2" column="1">
     <widget class="QComboBox" name="comboBox"/>
    </item>
    <item row="3" column="0">
     <widget class="QLabel" name="label_5">
      <property name="text">
       <string>Продолжительность</string>
      </property>
     </widget>
    </item>
    <item row="3" column="1">
     <widget class="QPlainTextEdit" name="duration"/>
    </item>
    <item row="4" column="1">
     <widget class="QPushButton" name="pushButton">
      <property name="text">
       <string>Добавить</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
template_2 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>AddGenreWidget</class>
 <widget class="QMainWindow" name="AddGenreWidget">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>469</width>
    <height>205</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPlainTextEdit" name="title">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>10</y>
      <width>341</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>310</x>
      <y>80</y>
      <width>121</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Сохранить</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>10</y>
      <width>71</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Название</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>469</width>
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


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.con = sqlite3.connect('films_db.sqlite')
        self.cur = self.con.cursor()

        self.add_film_widget = AddFilmWidget(self)
        self.edit_film_widget = AddFilmWidget(self)
        self.add_genre_widget = AddGenreWidget(self)
        self.edit_genre_widget = AddGenreWidget(self)
        self.genres_dict = {'комедия': 1, 'драма': 2, 'мелодрама': 3, 'детектив': 4, 'документальный': 5, 'ужасы': 6,
                            'музыка': 7,
                            'фантастика': 8, 'анимация': 9, 'биография': 10, 'боевик': 11, 'приключения': 13,
                            'война': 15,
                            'семейный': 16, 'триллер': 17, 'фэнтези': 18, 'вестерн': 19, 'мистика': 20,
                            'короткометражный': 21,
                            'мюзикл': 22, 'исторический': 23, 'нуар': 24}
        self.initUI()

    def renew_main(self):
        self.update_films()
        self.update_genres()

    def add_film(self):
        self.add_film_widget = AddFilmWidget(self)
        self.add_film_widget.show()

    def edit_film(self):
        row = self.filmsTable.currentRow()
        if row > -1:
            item = self.filmsTable.item(row, 0).text()
            self.edit_film_widget = AddFilmWidget(self, film_id=item)
            self.edit_film_widget.show()

    def delete_film(self):
        valid = QMessageBox.question(self, '', "Действительно удалить фильм?", QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            row = self.filmsTable.currentRow()
            if row > -1:
                item = self.filmsTable.item(row, 0).text()
                self.cur.execute(f"""
                DELETE FROM FILMS 
                WHERE id = {item}
                """)
                self.con.commit()
                self.update_films()

    def add_genre(self):
        self.add_genre_widget = AddGenreWidget(self)
        self.add_genre_widget.show()

    def edit_genre(self):
        row = self.genresTable.currentRow()
        if row > -1:
            item = self.genresTable.item(row, 1).text()
            self.edit_genre_widget = AddGenreWidget(self, item)
            self.edit_genre_widget.show()

    def delete_genre(self):
        valid = QMessageBox.question(self, '', "Действительно удалить жанр?", QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            row = self.genresTable.currentRow()
            if row > -1:
                item = self.genresTable.item(row, 0).text()
                print(0)
                self.cur.execute(f"""
                UPDATE FILMS
                SET GENRE = 0
                WHERE GENRE={item}
                """)
                print(1)
                self.cur.execute(f"""
                DELETE FROM GENRES
                WHERE id = {item}
                """)
                print(2)
                self.con.commit()
                self.update_genres()

    def tab_changed(self, index):
        if index == 0:
            self.update_films()
        else:
            self.update_genres()

    def update_genres(self):
        self.genresTable.setColumnCount(2)
        self.genresTable.setHorizontalHeaderLabels(['ИД', 'Название жанра'])
        res = self.cur.execute("""
        SELECT DISTINCT GENRES.ID, GENRES.TITLE FROM GENRES
        LEFT JOIN FILMS ON FILMS.GENRE = GENRES.ID
        """).fetchall()
        self.genresTable.setRowCount(len(res))
        for i in range(len(res)):
            el = res[i]
            for g in range(len(res[0])):
                self.genresTable.setItem(i, g, QTableWidgetItem(str(el[g])))

    def update_films(self):
        self.filmsTable.setColumnCount(5)
        self.filmsTable.setHorizontalHeaderLabels(
            ['ИД', 'Название фильма', 'Год выпуска', 'Жанр', 'Продолжительность'])
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        res = cur.execute("""
        SELECT Films.id, Films.title, year, genres.title, duration FROM genres
        LEFT JOIN Films ON Films.genre = genres.id
        ORDER BY Films.id DESC
        """).fetchall()
        self.filmsTable.setRowCount(len(res))
        for i in range(len(res)):
            el = res[i]
            for g in range(len(res[0])):
                self.filmsTable.setItem(i, g, QTableWidgetItem(str(el[g])))

    def initUI(self):
        self.tabWidget.setTabText(0, 'Фильмы')
        self.tabWidget.setTabText(1, 'Жанры')
        self.tabWidget.currentChanged.connect(self.tab_changed)
        self.renew_main()
        self.addFilmButton.clicked.connect(self.add_film)
        self.editFilmButton.clicked.connect(self.edit_film)
        self.deleteFilmButton.clicked.connect(self.delete_film)
        self.addGenreButton.clicked.connect(self.add_genre)
        self.editGenreButton.clicked.connect(self.edit_genre)
        self.deleteGenreButton.clicked.connect(self.delete_genre)


class AddFilmWidget(QMainWindow):
    def __init__(self, parent=None, film_id=None):
        super().__init__(parent)
        f = io.StringIO(template_1)
        uic.loadUi(f, self)
        self.f = film_id
        self.duration_el = None
        self.genre_el = None
        self.year_el = None
        self.title_el = None
        self.value = None
        self.params = {'комедия': 1, 'драма': 2, 'мелодрама': 3, 'детектив': 4, 'документальный': 5, 'ужасы': 6,
                       'музыка': 7,
                       'фантастика': 8, 'анимация': 9, 'биография': 10, 'боевик': 11, 'приключения': 13, 'война': 15,
                       'семейный': 16, 'триллер': 17, 'фэнтези': 18, 'вестерн': 19, 'мистика': 20,
                       'короткометражный': 21,
                       'мюзикл': 22, 'исторический': 23, 'нуар': 24}
        self.con = sqlite3.connect('films_db.sqlite')
        self.cur = self.con.cursor()
        self.initUI()

    def renew(self):
        res = self.cur.execute("""
        SELECT DISTINCT genres.title from genres
        LEFT JOIN Films ON FILMS.GENRE = GENRES.ID
        """).fetchall()
        for i in res:
            self.comboBox.addItem(i[0])
        self.pushButton.clicked.connect(self.run)

    def get_adding_verdict(self):
        if type(self.year_el) is int and 0 < self.year_el < 2024 and type(
                self.duration_el) is int and self.duration_el > 0 and self.genre_el and self.title_el:
            return True
        return False

    def get_editing_verdict(self):
        if type(self.year_el) is int and 0 < self.year_el < 2024 and type(
                self.duration_el) is int and self.duration_el > 0 and self.genre_el and self.title_el:
            return True
        return False

    def run(self):
        def check(word):
            letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
            if not word:
                return True
            for i in word.lower():
                if i in ascii_lowercase + letters:
                    return True
            return False

        res_len = self.cur.execute("""
        SELECT * FROM Films
        ORDER BY id DESC
        """).fetchall()
        self.title_el = self.title.toPlainText()
        self.year_el = self.year.toPlainText() if check(self.year.toPlainText()) else int(self.year.toPlainText())
        self.genre_el = self.comboBox.currentText()
        self.duration_el = self.duration.toPlainText() if check(self.duration.toPlainText()) else int(
            self.duration.toPlainText())
        statusbar = self.statusBar()

        if self.f:
            self.value = self.f
        else:
            self.value = len(res_len) + 1
        if self.get_adding_verdict():
            self.cur.execute(f"""
            INSERT OR REPLACE INTO Films 
            VAlUES{(self.value, self.title_el, self.year_el, self.params[self.genre_el], self.duration_el)}
            """)
            statusbar.showMessage('')
            self.con.commit()
            self.parent().renew_main()
            self.close()
        else:
            statusbar.showMessage('Неверно заполнена форма')

    def initUI(self):
        self.renew()
        if self.f:
            res = self.cur.execute(f"""
            SELECT films.title, films.year, genres.title, films.duration from genres
            LEFT JOIN films ON films.genre = genres.id
            WHERE FILMS.ID = {self.f}
            """).fetchone()
            self.title.insertPlainText(str(res[0]))
            self.year.insertPlainText(str(res[1]))
            self.comboBox.setCurrentText(str(res[2]))
            self.duration.insertPlainText(str(res[-1]))


class AddGenreWidget(QMainWindow):
    def __init__(self, parent=None, genre_id=None):
        super().__init__(parent)
        f = io.StringIO(template_2)
        uic.loadUi(f, self)
        self.value = None
        self.genre_id = genre_id
        self.con = sqlite3.connect('films_db.sqlite')
        self.cur = self.con.cursor()
        self.params = {'комедия': 1, 'драма': 2, 'мелодрама': 3, 'детектив': 4, 'документальный': 5, 'ужасы': 6,
                       'музыка': 7,
                       'фантастика': 8, 'анимация': 9, 'биография': 10, 'боевик': 11, 'приключения': 13, 'война': 15,
                       'семейный': 16, 'триллер': 17, 'фэнтези': 18, 'вестерн': 19, 'мистика': 20,
                       'короткометражный': 21,
                       'мюзикл': 22, 'исторический': 23, 'нуар': 24}
        self.initUI()

    def get_adding_verdict(self, text):
        if text and type(text) is str and not text.isnumeric() and text[0] not in '0123456789':
            return True
        return False

    def get_editing_verdict(self, text):
        if text and type(text) is str and not text.isnumeric() and text[0] not in '0123456789':
            return True
        return False

    def run(self):
        def save():
            self.con.commit()
            self.parent().renew_main()
            self.close()

        text = self.title.toPlainText()
        if self.genre_id:
            if self.get_editing_verdict(text):
                print(text)
                self.cur.execute(f"""
                UPDATE genres
                SET title='{text}'
                WHERE title='{self.genre_id}'
                """)
                save()
        else:
            if self.get_adding_verdict(text):
                self.cur.execute(f"""
                INSERT INTO genres(title) VALUES('{text}')
                """)
                save()

    def initUI(self):
        if self.genre_id:
            self.title.insertPlainText(self.genre_id)
        self.pushButton.clicked.connect(self.run)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
