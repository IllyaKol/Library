from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import zbar

class AddVisitorWindow(QWidget):
    def __init__(self, library):
        super(AddVisitorWindow, self).__init__()
        self.setGeometry(800, 800, 500, 250)
        self.setWindowTitle('Add visitor')
        self.setWindowIcon(QIcon('Lb.png'))
        self.initialize_buttons()
        self.move_to_center()

        self.library = library

    def initialize_buttons(self):
        self.name = QLabel('Name')
        self.last_name = QLabel('Last name')
        self.birth_date = QLabel('Birth date')
        self.number = QLabel('Number')
        self.gender = QLabel('Gender')

        self.name_edit = QLineEdit()
        self.last_name_edit = QLineEdit()
        self.birth_date_edit = QLineEdit()
        self.number_edit = QLineEdit()
        self.gender_edit = QLineEdit()
        self.visitor_id_edit = QLineEdit()
        self.visitor_id_edit.setValidator(QIntValidator())

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.name, 1, 0)
        grid.addWidget(self.name_edit, 1, 1)

        grid.addWidget(self.last_name, 2, 0)
        grid.addWidget(self.last_name_edit, 2, 1)

        grid.addWidget(self.birth_date, 3, 0)
        self.dateEdit = QDateEdit(self)
        self.dateEdit.setDisplayFormat('yyyy-MM-dd')
        self.dateEdit.setDateTime(QDateTime.currentDateTime())
        self.dateEdit.setMaximumDate(QDate(7999, 12, 28))
        self.dateEdit.setMaximumTime(QTime(23, 59, 59))
        self.dateEdit.setCalendarPopup(True)
        grid.addWidget(self.dateEdit, 3, 1)

        grid.addWidget(self.number, 4, 0)
        grid.addWidget(self.number_edit, 4, 1)

        grid.addWidget(self.gender, 5, 0)
        self.combobox = QComboBox(self)
        self.combobox.addItems(['Male', 'Female'])
        grid.addWidget(self.combobox, 5, 1)

        self.camera = QPushButton('Open camera', self)
        self.camera.clicked.connect(self.read_id)
        grid.addWidget(self.camera, 6, 0)
        grid.addWidget(self.visitor_id_edit, 6, 1)

        self.ok = QPushButton('OK', self)
        self.ok.setToolTip('Will close the window')
        self.ok.clicked.connect(self.save)
        self.ok.setShortcut(Qt.CTRL + Qt.Key_F)
        grid.addWidget(self.ok, 7, 1)

        self.setLayout(grid)
        self.setWindowTitle("Add visitor")

    def move_to_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def read_id(self):
        self.visitor_id_edit.setText(self.scan())

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
        if self.combobox.currentText() == 'Male':
            self.gender_number = 1
        elif self.combobox.currentText() == 'Female':
            self.gender_number = 2

        if self.check_fields():
            for i in self.library.visitors:
                if self.visitor_id_edit.text() == str(i.id):
                    QMessageBox.question(self, 'Message', "This id use", QMessageBox.Ok)
                    return
                if self.name_edit.text() == i.name and self.last_name_edit.text() == i.last_name and self.number_edit.text() == i.number:
                    QMessageBox.question(self, 'Message', "This person exist", QMessageBox.Ok)
                    return

            self.name_edit = self.name_edit.text()
            self.name_edit = self.name_edit.title()
            self.last_name_edit = self.last_name_edit.text()
            self.last_name_edit = self.last_name_edit.title()

            self.library.add_visitor_to_bd(self.visitor_id_edit.text(), self.name_edit,
                                           self.last_name_edit, self.dateEdit.text(), self.number_edit.text(),
                                           self.gender_number)
            self.show_window_ok()

    def show_window_ok(self):
        QMessageBox.question(self, 'Message', "Visitor was added", QMessageBox.Ok)
        self.close()

    def set_default_stylesheets(self):
        if self.name_edit.text():
            self.name.setStyleSheet('')
        if self.last_name_edit.text():
            self.last_name.setStyleSheet('')
        if self.number_edit.text():
            self.number.setStyleSheet('')
        if self.visitor_id_edit.text():
            self.camera.setStyleSheet('')

    def check_fields(self):
        fields_ok = True
        if not self.name_edit.text():
            self.name.setStyleSheet("color : #DC143C")
            self.name_edit.textChanged.connect(self.set_default_stylesheets)
            fields_ok = False
        if not self.last_name_edit.text():
            self.last_name.setStyleSheet("color : #DC143C")
            self.last_name_edit.textChanged.connect(self.set_default_stylesheets)
            fields_ok = False
        if not self.number_edit.text():
            self.number.setStyleSheet("color : #DC143C")
            self.number_edit.textChanged.connect(self.set_default_stylesheets)
            fields_ok = False
        if not self.visitor_id_edit.text():
            self.camera.setStyleSheet("color: #DC143C")
            self.visitor_id_edit.textChanged.connect(self.set_default_stylesheets)
            fields_ok = False
        return fields_ok