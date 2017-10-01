from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class SearchBookByName(QWidget):
    def __init__(self, books, book_has_author_list, authors, visitors, history):
        super(SearchBookByName, self).__init__()
        self.setGeometry(800, 800, 1300, 350)
        self.setWindowTitle('Search information')
        self.setWindowIcon(QIcon('Lb.png'))
        self.move_to_center()
        self.initialize_buttons()

        self.books = books
        self.book_has_author_list = book_has_author_list
        self.authors = authors
        self.visitors = visitors
        self.history = history

    def move_to_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initialize_buttons(self):
        self.find_by = QLabel('Choose by')
        self.name = QLabel('Name')
        self.last_name = QLabel('Last name')
        self.result = QLabel('Result')

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText('Input name')

        self.last_name_edit = QLineEdit()
        self.last_name_edit.setPlaceholderText('Input last name')

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.name, 1, 0)
        grid.addWidget(self.name_edit, 1, 1)

        grid.addWidget(self.last_name, 2, 0)
        grid.addWidget(self.last_name_edit, 2, 1)

        grid.addWidget(self.find_by, 3, 0)
        self.combobox = QComboBox()
        self.combobox.addItems(['', 'Book', 'Author', 'Visitor'])
        grid.addWidget(self.combobox, 3, 1)

        grid.addWidget(self.result, 4, 0)
        self.list_widget = QListWidget()
        grid.addWidget(self.list_widget, 4, 1)

        self.ok = QPushButton('OK', self)
        self.ok.clicked.connect(self.ok_button)
        self.ok.setShortcut(Qt.CTRL + Qt.Key_F)
        grid.addWidget(self.ok, 5, 1)

        self.setLayout(grid)

    def ok_button(self):
        name = self.name_edit.text()
        last_name = self.last_name_edit.text()
        found = True
        if self.combobox.currentText() == 'Book':

            for book in self.books:
                if book.name == name:
                    for book_author in self.book_has_author_list:
                        if book.id == book_author.book_id:
                            break
                    for author in self.authors:
                        if author.id == book_author.author_id:
                            break
                    self.list_widget.addItem(str(book.id) + ' ' + 'Book: ' + book.name + ', Available count: ' + str(
                        book.available_count) + ', Author name: ' + author.name + ', Author last name: ' + author.last_name)
                    self.list_widget.setMaximumWidth(self.list_widget.sizeHintForColumn(0))
                    found = False
            if found:
                self.list_widget.addItem('-' * 45 + 'Not found' + '-' * 47)
        elif self.combobox.currentText() == 'Author':
            for author in self.authors:
                if author.name == name and author.last_name == last_name:
                    for book_author in self.book_has_author_list:
                        if book_author.author_id == author.id:
                            for book in self.books:
                                if book_author.book_id == book.id:
                                    break
                            self.list_widget.addItem('Book: ' + book.name + ', Available count: ' + str(
                                book.available_count) + ', Author name: ' + author.name + ', Author last name: ' + author.last_name)
                            self.list_widget.setMaximumWidth(self.list_widget.sizeHintForColumn(0))
                            found = False
            if found:
                self.list_widget.addItem('-' * 45 + 'Not found' + '-' * 47)
        elif self.combobox.currentText() == 'Visitor':
            for visitor in self.visitors:
                if visitor.name == name and visitor.last_name == last_name:
                    for i in self.history:
                        if visitor.id == i.visitor_id:
                            for book in self.books:
                                if i.book_id == book.id:
                                    break
                            for author_per_book in self.book_has_author_list:
                                if book.id == author_per_book.book_id:
                                    break
                            for author in self.authors:
                                if author_per_book.author_id == author.id:
                                    break
                            self.list_widget.addItem(str(
                                visitor.id) + ', ' + 'Name: ' + visitor.name + ', Last name: ' + visitor.last_name + ', Take book: ' + book.name + ', Author name: ' + author.name + ', Author last name: ' + author.last_name + ', Taking date: ' + str(
                                i.taking_date) + ', Returning date: ' + str(i.returning_date))
                            self.list_widget.setMaximumWidth(self.list_widget.sizeHintForColumn(0))
                            found = False
            if found == True:
                self.list_widget.addItem('-' * 70 + 'Not found' + '-' * 70)