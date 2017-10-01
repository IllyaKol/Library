from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import zbar

class ChangeVisitorWindow(QWidget):
    def __init__(self, library):
        super(ChangeVisitorWindow, self).__init__()
        self.setGeometry(800, 800, 600, 250)
        self.setWindowTitle('Change visitor')
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
        self.new_name = QLabel('New name')
        self.new_last_name = QLabel('New last name')
        self.new_number = QLabel('New number')

        self.new_name_edit = QLineEdit()
        self.new_last_name_edit = QLineEdit()
        self.new_number_edit = QLineEdit()
        self.visitor_id_edit = QLineEdit()
        self.visitor_id_edit.setPlaceholderText('Enter visitor id')

        # self.new_number_edit.setValidator(QIntValidator())
        # self.visitor_id_edit.setValidator(QIntValidator())

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.new_name, 1, 0)
        grid.addWidget(self.new_name_edit, 1, 1)

        grid.addWidget(self.new_last_name, 2, 0)
        grid.addWidget(self.new_last_name_edit, 2, 1)

        grid.addWidget(self.new_number, 3, 0)
        grid.addWidget(self.new_number_edit, 3, 1)

        self.camera = QPushButton('Open camera', self)
        self.camera.clicked.connect(self.read_id)
        grid.addWidget(self.camera, 4, 0)
        grid.addWidget(self.visitor_id_edit, 4, 1)

        self.ok = QPushButton('OK', self)
        self.ok.setToolTip('Will close the window')
        self.ok.clicked.connect(self.save)
        self.ok.setShortcut(Qt.CTRL + Qt.Key_F)
        grid.addWidget(self.ok, 5, 1)

        self.setLayout(grid)

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
        if self.check_fields():
            found = True
            for i in self.library.visitors:
                if self.visitor_id_edit.text() == str(i.id):
                    found = False
            if found == True:
                QMessageBox.question(self, 'Message', "User not found", QMessageBox.Ok)
                return

            self.new_name_edit = self.new_name_edit.text()
            self.new_name_edit = self.new_name_edit.title()
            self.new_last_name_edit = self.new_last_name_edit.text()
            self.new_last_name_edit = self.new_last_name_edit.title()

            self.library.change_visitor(self.visitor_id_edit.text(), self.new_name_edit,
                                        self.new_last_name_edit, self.new_number_edit.text())
            self.show_window_ok()

    #Open window with text
    def show_window_ok(self):
        button_reply = QMessageBox.question(self, 'Message', "Visitor was changed", QMessageBox.Ok)
        if button_reply == QMessageBox.Ok:
            self.close()

    def set_default_stylesheets(self):
        if self.new_name_edit.text():
            self.new_name.setStyleSheet('')
        if self.new_last_name_edit.text():
            self.new_last_name.setStyleSheet('')
        if self.new_number_edit.text():
            self.new_number.setStyleSheet('')
        if self.visitor_id_edit.text():
            self.camera.setStyleSheet('')

    def check_fields(self):
        fields_ok = True
        if not self.new_name_edit.text():
            self.new_name.setStyleSheet("color : #DC143C")
            self.new_number_edit.textChanged.connect(self.set_default_stylesheets)
            fields_ok = False
        if not self.new_last_name_edit.text():
            self.new_last_name.setStyleSheet("color : #DC143C")
            self.new_last_name_edit.textChanged.connect(self.set_default_stylesheets)
            fields_ok = False
        if not self.new_number_edit.text():
            self.new_number.setStyleSheet("color : #DC143C")
            self.new_number_edit.textChanged.connect(self.set_default_stylesheets)
            fields_ok = False
        if not self.visitor_id_edit.text():
            self.camera.setStyleSheet("color: #DC143C")
            self.visitor_id_edit.textChanged.connect(self.set_default_stylesheets)
            fields_ok = False
        return fields_ok
