from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import zbar

class WriteBookOnVisitor(QWidget):
    def __init__(self, library):
        super(WriteBookOnVisitor, self).__init__()
        self.setGeometry(800, 800, 600, 250)
        self.setWindowTitle('Write book on visitor')
        self.setWindowIcon(QIcon('Lb.png'))
        self.move_to_center()
        self.initialize_buttons()

        self.library = library

    def move_to_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initialize_buttons(self):
        self.date = QLabel('Date')

        self.date_edit = QLineEdit()
        self.visitor_id_edit = QLineEdit()
        self.book_id_edit = QLineEdit()

        self.visitor_id_edit.setValidator(QIntValidator())
        self.book_id_edit.setValidator(QIntValidator())

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.date, 1, 0)
        self.dateEdit = QDateEdit(self)
        self.dateEdit.setDisplayFormat('yyyy-MM-dd')
        self.dateEdit.setDateTime(QDateTime.currentDateTime())
        self.dateEdit.setMaximumDate(QDate(7999, 12, 28))
        self.dateEdit.setMaximumTime(QTime(23, 59, 59))
        self.dateEdit.setCalendarPopup(True)
        grid.addWidget(self.dateEdit, 1, 1)

        self.camera_visitor = QPushButton('Visitor cam', self)
        self.camera_visitor.clicked.connect(self.visitor_id)
        grid.addWidget(self.camera_visitor, 2, 0)
        grid.addWidget(self.visitor_id_edit, 2, 1)

        self.camera_book = QPushButton('Book cam', self)
        self.camera_book.clicked.connect(self.book_id)
        grid.addWidget(self.camera_book, 3, 0)
        grid.addWidget(self.book_id_edit, 3, 1)

        self.ok = QPushButton('OK', self)
        self.ok.clicked.connect(self.save)
        self.ok.setShortcut(Qt.CTRL + Qt.Key_F)
        grid.addWidget(self.ok, 4, 1)

        self.setLayout(grid)

    def visitor_id(self):
        self.visitor_id_edit.setText(self.scan())

    def book_id(self):
        self.book_id_edit.setText(self.scan())

    def scan(self):
        proc = zbar.Processor()
        proc.parse_config('enable')
        device = '/dev/video0'
        proc.init(device)
        proc.visible = True
        proc.process_one()
        proc.visible = False
        for symbol in proc.results:
            return symbol.data

    def save(self):
        if self.check_fields():
            found = True
            for i in self.library.visitors:
                if self.visitor_id_edit.text() == str(i.id):
                    found = False
            if found == True:
                QMessageBox.question(self, 'Message', "User not found", QMessageBox.Ok)
                return

            found = True
            for i in self.library.books:
                if self.book_id_edit.text() == str(i.id):
                    found = False
            if found == True:
                QMessageBox.question(self, 'Message', "Book not found", QMessageBox.Ok)
                return

            self.library.write_book_on_visitor_to_bd(self.visitor_id_edit.text(), self.book_id_edit.text(),
                                                     self.dateEdit.text())
            self.show_window_ok()

    def show_window_ok(self):
        button_reply = QMessageBox.question(self, 'Message', "Visitor take book", QMessageBox.Ok)
        if button_reply == QMessageBox.Ok:
            self.close()

    def set_default_stylesheets(self):
        if self.visitor_id_edit.text():
            self.camera_visitor.setStyleSheet('')
        if self.book_id_edit.text():
            self.camera_book.setStyleSheet('')

    def check_fields(self):
        fields_ok = True
        if not self.visitor_id_edit.text():
            self.camera_visitor.setStyleSheet("color : #DC143C")
            self.visitor_id_edit.textChanged.connect(self.set_default_stylesheets)
            fields_ok = False
        if not self.book_id_edit.text():
            self.camera_book.setStyleSheet("color : #DC143C")
            self.book_id_edit.textChanged.connect(self.set_default_stylesheets)
            fields_ok = False
        return fields_ok