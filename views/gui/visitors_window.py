from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class VisitorsWindow(QWidget):
    def __init__(self, visitors, genders, books, history):
        super(VisitorsWindow, self).__init__()
        # self.setGeometry(800, 800, 800, 550)
        self.setWindowTitle('Visitors')
        self.setWindowIcon(QIcon('Lb.png'))
        self.initialize_buttons(visitors, genders)
        self.table.setFixedSize(self.table.horizontalHeader().length() + 19, 400)
        self.adjustSize()
        self.move_to_center()

        self.visitors = visitors
        self.books = books
        self.history = history

    def move_to_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initialize_buttons(self, visitors, genders):
        # layout = QHBoxLayout()

        self.search_line = QLineEdit()
        self.search_line.setPlaceholderText('Enter book name')

        self.ok = QPushButton('OK')
        self.ok.clicked.connect(self.search_visitor)
        self.ok.setShortcut(Qt.CTRL + Qt.Key_F)

        # grid = QGridLayout()
        # grid.setSpacing(10)

        self.table = QTableWidget()
        self.table.horizontalHeader().resizeSection(0, 150)
        self.table.setRowCount(len(visitors))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem('Name'))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem('Last name'))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem('Date'))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem('Number'))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem('Gender'))

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        for row in range(len(visitors)):
            visitor = visitors[row]
            # for gender in genders:
            #     if gender.id == visitor.gender_id:
            self.table.setItem(row, 0, QTableWidgetItem(visitor.name))
            self.table.setItem(row, 1, QTableWidgetItem(visitor.last_name))
            self.table.setItem(row, 2, QTableWidgetItem(str(visitor.birth_date)))
            self.table.setItem(row, 3, QTableWidgetItem(str(visitor.number)))
            self.table.setItem(row, 4, QTableWidgetItem(visitor.gender.name))

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
        #
        # self.setLayout(grid)


    def search_visitor(self):

        self.search_line_title = self.search_line.text()
        self.search_line_title = self.search_line_title.title()
        if len(self.search_line_title) == 0:
            self.number_row = 0
            for i in reversed(range(self.table.rowCount())):
                self.table.removeRow(i)
            self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

            for visitor in self.visitors:
                self.table.insertRow(self.number_row)
                self.table.setItem(self.number_row, 0, QTableWidgetItem(visitor.name))
                self.table.setItem(self.number_row, 1, QTableWidgetItem(visitor.last_name))
                self.table.setItem(self.number_row, 2, QTableWidgetItem(str(visitor.birth_date)))
                self.table.setItem(self.number_row, 3, QTableWidgetItem(str(visitor.number)))
                self.table.setItem(self.number_row, 4, QTableWidgetItem(visitor.gender.name))
                self.number_row += 1
            return

        self.number_of_row = 0
        for i in reversed(range(self.table.rowCount())):
            self.table.removeRow(i)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        current_book = None
        for book in self.books:
            if book.name == self.search_line_title:
                current_book = book
                break
        if not current_book:
            return
        not_returned_history = [history for history in current_book.history if not history.returning_date]

        for record in not_returned_history:
            visitor_name = record.visitor.name
            visitor_last_name = record.visitor.last_name
            visitor_birth_date = str(record.visitor.birth_date)
            visitor_number = str(record.visitor.number)
            visitor_gender = record.visitor.gender.name
            self.table.insertRow(self.number_of_row)
            self.table.setItem(self.number_of_row, 0, QTableWidgetItem(visitor_name))
            self.table.setItem(self.number_of_row, 1, QTableWidgetItem(visitor_last_name))
            self.table.setItem(self.number_of_row, 2, QTableWidgetItem(visitor_birth_date))
            self.table.setItem(self.number_of_row, 3, QTableWidgetItem(visitor_number))
            self.table.setItem(self.number_of_row, 4, QTableWidgetItem(visitor_gender))
            self.number_of_row += 1


        # self.search_line_title = self.search_line.text()
        # self.search_line_title = self.search_line_title.title()
        # if len(self.search_line_title) == 0:
        #     self.number_row = 0
        #     for i in reversed(range(self.table.rowCount())):
        #         self.table.removeRow(i)
        #     self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        #     for row in range(len(self.visitors)):
        #         visitor = self.visitors[row]
        #         self.table.insertRow(self.number_row)
        #         self.table.setItem(self.number_row, 0, QTableWidgetItem(visitor.name))
        #         self.table.setItem(self.number_row, 1, QTableWidgetItem(visitor.last_name))
        #         self.table.setItem(self.number_row, 2, QTableWidgetItem(str(visitor.birth_date)))
        #         self.table.setItem(self.number_row, 3, QTableWidgetItem(str(visitor.number)))
        #         self.table.setItem(self.number_row, 4, QTableWidgetItem(visitor.gender.name))
        #         self.number_row += 1
        #     return
        # self.number_of_row = 0
        # for i in reversed(range(self.table.rowCount())):
        #     self.table.removeRow(i)
        # self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # for row in range(len(self.history)):
        #     record = self.history[row]
        #     if self.search_line_title == record.book.name and record.returning_date == None:
        #         for visitor in self.visitors:
        #             if visitor.id == record.visitor_id:
        #                 self.table.insertRow(self.number_of_row)
        #                 self.table.setItem(self.number_of_row, 0, QTableWidgetItem(visitor.name))
        #                 self.table.setItem(self.number_of_row, 1, QTableWidgetItem(visitor.last_name))
        #                 self.table.setItem(self.number_of_row, 2, QTableWidgetItem(str(visitor.birth_date)))
        #                 self.table.setItem(self.number_of_row, 3, QTableWidgetItem(str(visitor.number)))
        #                 self.table.setItem(self.number_of_row, 4, QTableWidgetItem(visitor.gender.name))
        #                 self.number_of_row += 1


