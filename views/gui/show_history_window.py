from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ShowHistory(QWidget):
    def __init__(self, history, visitors, books, book_has_author_list, authors):
        super(ShowHistory, self).__init__()
        # self.setGeometry(800, 800, 1000, 550)
        self.setWindowTitle('Show history')
        self.setWindowIcon(QIcon('Lb.png'))
        self.initialize_buttons(history, visitors, books, book_has_author_list, authors)
        self.table.setFixedSize(self.table.horizontalHeader().length() + 19, 400)
        self.adjustSize()
        self.move_to_center()

        self.history = history
        self.visitors = visitors
        self.books = books
        self.book_has_author_list = book_has_author_list
        self.authors = authors

    def move_to_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def initialize_buttons(self, history, visitors, books, book_has_author_list, authors):
        # layout = QHBoxLayout()

        self.search_line = QLineEdit()
        self.search_line.setPlaceholderText('Enter name')

        self.ok = QPushButton('OK')
        self.ok.clicked.connect(self.search_information)
        self.ok.setShortcut(Qt.CTRL + Qt.Key_F)


        grid = QGridLayout()
        grid.setSpacing(10)

        self.table = QTableWidget()
        self.table.setRowCount(len(history))
        self.table.setColumnCount(7)

        self.table.setHorizontalHeaderItem(0, QTableWidgetItem('Visitor name'))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem('Visitor last name'))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem('Book name'))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem('Author name'))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem('Author last name'))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem('Date of take'))
        self.table.setHorizontalHeaderItem(6, QTableWidgetItem('Return date'))

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        for row in range(len(history)):
            record = history[row]
            for visitor in visitors:
                if record.visitor_id == int(visitor.id):
                    break
            for book in books:
                if record.book_id == int(book.id):
                    break
            for author_per_book in book_has_author_list:
                if record.book_id == int(author_per_book.book_id):
                    break
            for author in authors:
                if author_per_book.author_id == author.id:
                    break
            self.table.setItem(row, 0, QTableWidgetItem(visitor.name))
            self.table.setItem(row, 1, QTableWidgetItem(visitor.last_name))
            self.table.setItem(row, 2, QTableWidgetItem(book.name))
            self.table.setItem(row, 3, QTableWidgetItem(author.name))
            self.table.setItem(row, 4, QTableWidgetItem(author.last_name))
            self.table.setItem(row, 5, QTableWidgetItem(str(record.taking_date)))
            self.table.setItem(row, 6, QTableWidgetItem(str(record.returning_date)))

            # hbox = QHBoxLayout()
            # hbox.addWidget(self.search_line)
            # hbox.addWidget(self.ok)
            #
            # horizontal_box = QHBoxLayout()
            # horizontal_box.addWidget(self.table)
            #
            # vbox = QVBoxLayout()
            # vbox.addStretch()
            # vbox.addLayout(hbox)
            # vbox.addLayout(horizontal_box)
            #
            # self.setLayout(vbox)


            grid.addWidget(self.search_line, 1, 0)
            grid.addWidget(self.table, 2, 0)
            grid.addWidget(self.ok, 3, 0)

            self.setLayout(grid)


    def search_information(self):
        self.search_line_title = self.search_line.text()
        self.search_line_title = self.search_line_title.title()
        if len(self.search_line_title) == 0:
            for i in reversed(range(self.table.rowCount())):
                self.table.removeRow(i)
            self.number_row = 0
            for row in range(len(self.history)):
                record = self.history[row]
                for visitor in self.visitors:
                    if record.visitor_id == int(visitor.id):
                        break
                for book in self.books:
                    if record.book_id == int(book.id):
                        break
                for author_per_book in self.book_has_author_list:
                    if record.book_id == int(author_per_book.book_id):
                        break
                for author in self.authors:
                    if author_per_book.author_id == author.id:
                        break
                self.table.insertRow(self.number_row)
                self.table.setItem(self.number_row, 0, QTableWidgetItem(visitor.name))
                self.table.setItem(self.number_row, 1, QTableWidgetItem(visitor.last_name))
                self.table.setItem(self.number_row, 2, QTableWidgetItem(book.name))
                self.table.setItem(self.number_row, 3, QTableWidgetItem(author.name))
                self.table.setItem(self.number_row, 4, QTableWidgetItem(author.last_name))
                self.table.setItem(self.number_row, 5, QTableWidgetItem(str(record.taking_date)))
                self.table.setItem(self.number_row, 6, QTableWidgetItem(str(record.returning_date)))
                self.number_row += 1
            return
        self.number_of_row = 0
        for i in reversed(range(self.table.rowCount())):
            self.table.removeRow(i)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        for row in range(len(self.history)):
            record = self.history[row]
            for visitor in self.visitors:
                if record.visitor_id == int(visitor.id):
                    self.visitor = visitor
                    break
            for book in self.books:
                if record.book_id == int(book.id):
                    self.book = book
                    break
            for author_per_book in self.book_has_author_list:
                if record.book_id == int(author_per_book.book_id):
                    self.author_per_book = author_per_book
                    break
            for author in self.authors:
                if author_per_book.author_id == author.id:
                    self.author = author
                    break
            if self.search_line_title == self.visitor.name or self.search_line_title == self.visitor.last_name or self.search_line_title == self.book.name or self.search_line_title == self.author.name or self.search_line_title == self.author.last_name or self.search_line_title == str(
                    record.taking_date) or self.search_line_title == str(record.returning_date):
                self.table.insertRow(self.number_of_row)
                self.table.setItem(self.number_of_row, 0, QTableWidgetItem(self.visitor.name))
                self.table.setItem(self.number_of_row, 1, QTableWidgetItem(self.visitor.last_name))
                self.table.setItem(self.number_of_row, 2, QTableWidgetItem(self.book.name))
                self.table.setItem(self.number_of_row, 3, QTableWidgetItem(self.author.name))
                self.table.setItem(self.number_of_row, 4, QTableWidgetItem(self.author.last_name))
                self.table.setItem(self.number_of_row, 5, QTableWidgetItem(str(record.taking_date)))
                self.table.setItem(self.number_of_row, 6, QTableWidgetItem(str(record.returning_date)))
                self.number_of_row += 1