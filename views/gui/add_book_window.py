from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import zbar

class AddBookWindow(QWidget):
    def __init__(self, library):
        super(AddBookWindow, self).__init__()
        self.setGeometry(800, 800, 500, 250)
        self.setWindowTitle('Add book')
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
        self.name = QLabel('Name')
        self.author_name = QLabel('Author name')
        self.author_last_name = QLabel('Author last name')
        self.date = QLabel('Date')
        self.count = QLabel('Count')

        self.name_edit = QLineEdit()
        self.author_name_edit = QLineEdit()
        self.author_last_name_edit = QLineEdit()
        self.date_edit = QLineEdit()
        self.count_edit = QLineEdit()
        self.book_id_edit = QLineEdit()

        self.book_id_edit.setValidator(QIntValidator())
        self.count_edit.setValidator(QIntValidator())

        self.dateEdit = QDateEdit(self)
        self.dateEdit.setDisplayFormat('yyyy-MM-dd')
        self.dateEdit.setDateTime(QDateTime.currentDateTime())
        self.dateEdit.setMaximumDate(QDate(7999, 12, 28))
        self.dateEdit.setMaximumTime(QTime(23, 59, 59))
        self.dateEdit.setCalendarPopup(True)

        self.camera = QPushButton('Open camera', self)
        self.camera.clicked.connect(self.read_id)

        self.ok = QPushButton('OK', self)
        self.ok.setToolTip('Will close the window')
        self.ok.clicked.connect(self.save)
        self.ok.setShortcut(Qt.CTRL + Qt.Key_F)


        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.name, 1, 0)
        grid.addWidget(self.name_edit, 1, 1)
        grid.addWidget(self.author_name, 2, 0)
        grid.addWidget(self.author_name_edit, 2, 1)
        grid.addWidget(self.author_last_name, 3, 0)
        grid.addWidget(self.author_last_name_edit, 3, 1)
        grid.addWidget(self.date, 4, 0)
        grid.addWidget(self.dateEdit, 4, 1)
        grid.addWidget(self.count, 5, 0)
        grid.addWidget(self.count_edit, 5, 1)
        grid.addWidget(self.camera, 6, 0)
        grid.addWidget(self.book_id_edit, 6, 1)
        grid.addWidget(self.ok, 7, 1)

        self.setLayout(grid)

    def read_id(self):
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
            for i in self.library.books:
                if self.book_id_edit.text() == str(i.id):
                    QMessageBox.question(self, 'Message', "This id use", QMessageBox.Ok)
                    return
                if self.name_edit.text() == i.name:
                    QMessageBox.question(self, 'Message', "This book exist", QMessageBox.Ok)
                    return

            self.name_edit = self.name_edit.text()
            self.name_edit = self.name_edit.title()
            self.author_name_edit = self.author_name_edit.text()
            self.author_name_edit = self.author_name_edit.title()
            self.author_last_name_edit = self.author_last_name_edit.text()
            self.author_last_name_edit = self.author_last_name_edit.title()

            self.library.add_book_to_bd(self.book_id_edit.text(), self.name_edit, self.author_name_edit,
                                        self.author_last_name_edit, self.dateEdit.text(), self.count_edit.text())
            self.show_window_ok()

    def show_window_ok(self):
        QMessageBox.question(self, 'Message', "Book was added", QMessageBox.Ok)
        self.close()

    def set_default_stylesheets(self):
        if self.name_edit.text():
            self.name.setStyleSheet('')
        if self.author_name_edit.text():
            self.author_name.setStyleSheet('')
        if self.author_last_name_edit.text():
            self.author_last_name.setStyleSheet('')
        if self.count_edit.text():
            self.count.setStyleSheet('')
        if self.book_id_edit.text():
            self.camera.setStyleSheet('')

    def check_fields(self):
        fields_ok = True
        if not self.name_edit.text():
            self.name.setStyleSheet("color : #DC143C")
            self.name_edit.textChanged.connect(self.set_default_stylesheets)
            fields_ok = False
        if not self.author_name_edit.text():
            self.author_name.setStyleSheet("color : #DC143C")
            self.author_name_edit.textChanged.connect(self.set_default_stylesheets)
            fields_ok = False
        if not self.author_last_name_edit.text():
            self.author_last_name.setStyleSheet("color : #DC143C")
            self.author_last_name_edit.textChanged.connect(self.set_default_stylesheets)
            fields_ok = False
        if not self.count_edit.text():
            self.count.setStyleSheet("color : #DC143C")
            self.count_edit.textChanged.connect(self.set_default_stylesheets)
            fields_ok = False
        if not self.book_id_edit.text():
            self.camera.setStyleSheet("color: #DC143C")
            self.book_id_edit.textChanged.connect(self.set_default_stylesheets)
            fields_ok = False
        return fields_ok