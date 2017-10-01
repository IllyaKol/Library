from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class BooksWindow(QWidget):
    def __init__(self, books, book_has_author_list, authors, history, visitors):
        super(BooksWindow, self).__init__()
        # self.setGeometry(800, 800, 841, 550)
        self.setWindowTitle('Books')
        self.setWindowIcon(QIcon('Lb.png'))
        self.initialize_buttons(books, book_has_author_list, authors)
        self.table.setFixedSize(self.table.horizontalHeader().length() + 19, 400)
        self.adjustSize()
        self.move_to_center()

        self.history = history
        self.books = books
        self.book_has_author_list = book_has_author_list
        self.authors = authors
        self.visitors = visitors
        # self.library = library

    def move_to_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initialize_buttons(self, books, book_has_author_list, authors):
        # layout = QHBoxLayout()

        self.search_line = QLineEdit()
        self.search_line.setPlaceholderText('Enter visitor name')

        self.ok = QPushButton('OK')
        self.ok.clicked.connect(self.search_book)
        self.ok.setShortcut(Qt.CTRL + Qt.Key_F)

        # grid = QGridLayout()
        # grid.setSpacing(10)


        self.table = QTableWidget()
        self.table.setRowCount(len(books))
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem('Name'))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem('Date'))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem('Author name'))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem('Author last name'))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem('Count'))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem('Available count'))

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        for row in range(len(books)):
            book = books[row]
            for book_has_author in book_has_author_list:
                if book_has_author.book_id == book.id:
                    author_id = book_has_author.author_id
            for author in authors:
                if author_id == author.id:

                    authors_names = ', '.join([x.author.name for x in book.book_has_author])
                    authors_last_names = ', '.join([x.author.last_name for x in book.book_has_author])
                    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                    self.table.setItem(row, 0, QTableWidgetItem(book.name))
                    self.table.setItem(row, 1, QTableWidgetItem(str(book.date)))
                    self.table.setItem(row, 2, QTableWidgetItem(authors_names))
                    self.table.setItem(row, 3, QTableWidgetItem(authors_last_names))
                    self.table.setItem(row, 4, QTableWidgetItem(str(book.count)))
                    self.table.setItem(row, 5, QTableWidgetItem(str(book.available_count)))

        hbox = QHBoxLayout()
        hbox.addWidget(self.search_line)
        hbox.addWidget(self.ok)

        horizontal_box = QHBoxLayout()
        horizontal_box.addWidget(self.table)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(horizontal_box)

        self.setLayout(vbox)

        # grid.addWidget(self.search_line, 1, 0)
        # grid.addWidget(self.ok, 1, 1)
        # grid.addWidget(self.table, 2, 0)

        # self.setLayout(grid)


    def search_book(self):
        self.search_line_title = self.search_line.text()
        self.search_line_title = self.search_line_title.title()
        if len(self.search_line_title) == 0:
            self.number_row = 0
            for i in reversed(range(self.table.rowCount())):
                self.table.removeRow(i)
            self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

            for book in self.books:
                name_book = book.name
                date_book = str(book.date)
                count_book = str(book.count)
                count_available = str(book.available_count)

                authors_names = ', '.join([x.author.name for x in book.book_author])
                authors_last_names = ', '.join([x.author.last_name for x in book.book_author])

                self.table.insertRow(self.number_row)
                self.table.setItem(self.number_row, 0, QTableWidgetItem(name_book))
                self.table.setItem(self.number_row, 1, QTableWidgetItem(date_book))
                self.table.setItem(self.number_row, 2, QTableWidgetItem(authors_names))
                self.table.setItem(self.number_row, 3, QTableWidgetItem(authors_last_names))
                self.table.setItem(self.number_row, 4, QTableWidgetItem(count_book))
                self.table.setItem(self.number_row, 5, QTableWidgetItem(count_available))
                self.number_row += 1
            return

        self.number_of_row = 0
        for i in reversed(range(self.table.rowCount())):
            self.table.removeRow(i)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        current_visitor = None
        for visitor in self.visitors:
            if visitor.name == self.search_line_title or visitor.last_name == self.search_line_title:
                current_visitor = visitor
                break
        if not current_visitor:
            return
        not_returned_history = [history for history in current_visitor.history if not history.returning_date]
        for record in not_returned_history:
            book_name = record.book.name

            authors_names = ', '.join([x.author.name for x in record.book.book_author])
            authors_last_names = ', '.join([x.author.last_name for x in record.book.book_author])

            self.table.insertRow(self.number_of_row)
            self.table.setItem(self.number_of_row, 0, QTableWidgetItem(book_name))
            self.table.setItem(self.number_of_row, 1, QTableWidgetItem(str(record.book.date)))
            self.table.setItem(self.number_of_row, 2, QTableWidgetItem(authors_names))
            self.table.setItem(self.number_of_row, 3, QTableWidgetItem(authors_last_names))
            self.table.setItem(self.number_of_row, 4, QTableWidgetItem(str(record.book.count)))
            self.table.setItem(self.number_of_row, 5, QTableWidgetItem(str(record.book.available_count)))
            self.number_of_row += 1

            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # for row in range(len(self.books)):
            #     book = self.books[row]
            #     for book_has_author in self.book_has_author_list:
            #         if book_has_author.book_id == book.id:
            #             author_id = book_has_author.author_id
            #     for author in self.authors:
            #         if author_id == author.id:
            #             self.table.insertRow(self.number_row)
            #             self.table.setItem(row, 0, QTableWidgetItem(book.name))
            #             self.table.setItem(row, 1, QTableWidgetItem(str(book.date)))
            #             self.table.setItem(row, 2, QTableWidgetItem(author.name))
            #             self.table.setItem(row, 3, QTableWidgetItem(author.last_name))
            #             self.table.setItem(row, 4, QTableWidgetItem(str(book.count)))
            #             self.table.setItem(row, 5, QTableWidgetItem(str(book.available_count)))
            #             self.number_row += 1
            # return
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # self.number_of_row = 0
        # for i in reversed(range(self.table.rowCount())):
        #     self.table.removeRow(i)
        # self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # for row in range(len(self.history)):
        #     record = self.history[row]
        #     if (self.search_line_title == record.visitor.name and record.returning_date == None) or \
        #             (self.search_line_title == record.visitor.last_name and record.returning_date == None):
        #         for book in self.books:
        #             if book.id == record.book_id:
        #                 for book_has_author in self.book_has_author_list:
        #                     if book_has_author.book_id == record.book_id:
        #                         author_id = book_has_author.author_id
        #                 for author in self.authors:
        #                     if author_id == author.id:
        #                         self.table.insertRow(self.number_of_row)
        #                         self.table.setItem(self.number_of_row, 0, QTableWidgetItem(book.name))
        #                         self.table.setItem(self.number_of_row, 1, QTableWidgetItem(str(book.date)))
        #                         self.table.setItem(self.number_of_row, 2, QTableWidgetItem(author.name))
        #                         self.table.setItem(self.number_of_row, 3, QTableWidgetItem(author.last_name))
        #                         self.table.setItem(self.number_of_row, 4, QTableWidgetItem(str(book.count)))
        #                         self.table.setItem(self.number_of_row, 5, QTableWidgetItem(str(book.available_count)))
        #                         self.number_of_row += 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
