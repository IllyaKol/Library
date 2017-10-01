# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 150)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.show_author = QtWidgets.QPushButton(self.centralwidget)
        self.show_author.setObjectName("show_author")
        self.horizontalLayout.addWidget(self.show_author)
        self.show_visitors = QtWidgets.QPushButton(self.centralwidget)
        self.show_visitors.setObjectName("show_visitors")
        self.horizontalLayout.addWidget(self.show_visitors)
        self.show_books = QtWidgets.QPushButton(self.centralwidget)
        self.show_books.setObjectName("show_books")
        self.horizontalLayout.addWidget(self.show_books)
        self.show_history = QtWidgets.QPushButton(self.centralwidget)
        self.show_history.setObjectName("show_history")
        self.horizontalLayout.addWidget(self.show_history)
        self.search_book_by_name = QtWidgets.QPushButton(self.centralwidget)
        self.search_book_by_name.setObjectName("search_book_by_name")
        self.horizontalLayout.addWidget(self.search_book_by_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_visitor = QtWidgets.QPushButton(self.centralwidget)
        self.add_visitor.setObjectName("add_visitor")
        self.horizontalLayout_2.addWidget(self.add_visitor)
        self.add_book = QtWidgets.QPushButton(self.centralwidget)
        self.add_book.setObjectName("add_book")
        self.horizontalLayout_2.addWidget(self.add_book)
        self.change_visitor = QtWidgets.QPushButton(self.centralwidget)
        self.change_visitor.setObjectName("change_visitor")
        self.horizontalLayout_2.addWidget(self.change_visitor)
        self.add_remove_date = QtWidgets.QPushButton(self.centralwidget)
        self.add_remove_date.setObjectName("add_remove_date")
        self.horizontalLayout_2.addWidget(self.add_remove_date)
        self.write_book_on_visitor = QtWidgets.QPushButton(self.centralwidget)
        self.write_book_on_visitor.setObjectName("write_book_on_visitor")
        self.horizontalLayout_2.addWidget(self.write_book_on_visitor)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.show_author.setText(_translate("MainWindow", "Show authors"))
        self.show_visitors.setText(_translate("MainWindow", "Show visitors"))
        self.show_books.setText(_translate("MainWindow", "Show books"))
        self.show_history.setText(_translate("MainWindow", "Show history"))
        self.search_book_by_name.setText(_translate("MainWindow", "Search"))
        self.add_visitor.setText(_translate("MainWindow", "Add visitor"))
        self.add_book.setText(_translate("MainWindow", "Add book"))
        self.change_visitor.setText(_translate("MainWindow", "Change visitor"))
        self.add_remove_date.setText(_translate("MainWindow", "Return book"))
        self.write_book_on_visitor.setText(_translate("MainWindow", "Write book"))

