from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ShowAuthorWindow(QWidget):
    def __init__(self, authors):
        super(ShowAuthorWindow, self).__init__()
        # self.setGeometry(800, 800, 800, 550)
        self.setWindowTitle('Authors')
        self.setWindowIcon(QIcon('Lb.png'))
        self.initialize_buttons(authors)
        self.table.setFixedSize(self.table.horizontalHeader().length() + 19, 350)
        self.adjustSize()
        self.move_to_center()

        self.authors = authors

    def move_to_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initialize_buttons(self, authors):
        grid = QGridLayout()

        self.search_line = QLineEdit()
        self.search_line.setPlaceholderText('Enter author')

        self.ok = QPushButton('OK')
        self.ok.clicked.connect(self.search_author)
        self.ok.setShortcut(Qt.CTRL + Qt.Key_F)

        self.table = QTableWidget()
        self.table.setRowCount(len(authors))
        self.table.setColumnCount(2)

        self.table.setHorizontalHeaderItem(0, QTableWidgetItem('Name'))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem('Last name'))

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        for row in range(len(authors)):
            author = authors[row]
            self.table.setItem(row, 0, QTableWidgetItem(author.name))
            self.table.setItem(row, 1, QTableWidgetItem(author.last_name))



        grid.addWidget(self.search_line, 1, 0)
        grid.addWidget(self.ok, 2, 0)
        grid.addWidget(self.table, 3, 0)

        self.setLayout(grid)

    def search_author(self):
        self.search_line_title = self.search_line.text()
        self.search_line_title = self.search_line_title.title()
        if len(self.search_line_title) == 0:
            self.number_row = 0
            for i in reversed(range(self.table.rowCount())):
                self.table.removeRow(i)
            self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            for row in range(len(self.authors)):
                author = self.authors[row]
                self.table.insertRow(self.number_row)
                self.table.setItem(self.number_row, 0, QTableWidgetItem(author.name))
                self.table.setItem(self.number_row, 1, QTableWidgetItem(author.last_name))
                self.number_row += 1
            return
        self.number_of_row = 0
        for i in reversed(range(self.table.rowCount())):
            self.table.removeRow(i)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        for row in range(len(self.authors)):
            record = self.authors[row]
            if self.search_line_title == record.name or self.search_line_title == record.last_name:
                self.table.insertRow(self.number_of_row)
                self.table.setItem(self.number_of_row, 0, QTableWidgetItem(record.name))
                self.table.setItem(self.number_of_row, 1, QTableWidgetItem(record.last_name))
                self.number_of_row += 1