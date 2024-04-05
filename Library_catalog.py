import sqlite3
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, \
    QPushButton, QTableWidget, QTableWidgetItem


class LibraryCatalog(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Каталог")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.setup_ui()

        self.conn = sqlite3.connect("library.db")
        self.create_table()

        self.display_data()

    def setup_ui(self):
        self.layout = QVBoxLayout(self.central_widget)

        self.search_layout = QHBoxLayout()
        self.search_author_edit = QLineEdit(self)
        self.search_author_edit.setPlaceholderText("Поиск по автору")
        self.search_title_edit = QLineEdit(self)
        self.search_title_edit.setPlaceholderText("Поиск по названию")
        self.search_btn = QPushButton("Найти", self)
        self.search_btn.clicked.connect(self.search_books)

        self.search_layout.addWidget(self.search_author_edit)
        self.search_layout.addWidget(self.search_title_edit)
        self.search_layout.addWidget(self.search_btn)

        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Название", "Автор", "Год", "Жанр", "Обложка"])

        self.book_info_layout = QVBoxLayout()
        self.book_info_label = QLabel("Информация о книге", self)
        self.book_info_label.setAlignment(Qt.AlignCenter)
        self.book_info_image = QLabel(self)
        self.book_info_image.setAlignment(Qt.AlignCenter)

        self.book_info_layout.addWidget(self.book_info_label)
        self.book_info_layout.addWidget(self.book_info_image)

        self.layout.addLayout(self.search_layout)
        self.layout.addWidget(self.table)
        self.layout.addLayout(self.book_info_layout)

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                year INTEGER,
                genre TEXT,
                image_path TEXT
            )
        ''')
        self.conn.commit()

    def display_data(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()

        self.table.setRowCount(len(books))

        for row, book in enumerate(books):
            for col, data in enumerate(book[:-1]):
                item = QTableWidgetItem(str(data))
                self.table.setItem(row, col, item)

            image_path = book[-1]
            if image_path:
                pixmap = QPixmap(image_path)
            else:
                pixmap = QPixmap("no_image.png")

            self.table.setRowHeight(row, pixmap.height())
            image_label = QLabel()
            image_label.setPixmap(pixmap)
            image_label.setAlignment(Qt.AlignCenter)
            self.table.setCellWidget(row, 4, image_label)

    def search_books(self):
        author = self.search_author_edit.text()
        title = self.search_title_edit.text()

        cursor = self.conn.cursor()
        query = f'''
            SELECT * FROM books
            WHERE author LIKE '%{author}%' AND title LIKE '%{title}%'
        '''
        cursor.execute(query)
        books = cursor.fetchall()

        self.table.setRowCount(len(books))

        for row, book in enumerate(books):
            for col, data in enumerate(book[:-1]):
                item = QTableWidgetItem(str(data))
                self.table.setItem(row, col, item)

            image_path = book[-1]
            if image_path:
                pixmap = QPixmap(image_path)
            else:
                pixmap = QPixmap("no_image.png")

            self.table.setRowHeight(row, pixmap.height())
            image_label = QLabel()
            image_label.setPixmap(pixmap)
            image_label.setAlignment(Qt.AlignCenter)
            self.table.setCellWidget(row, 4, image_label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryCatalog()
    window.show()
    sys.exit(app.exec_())
