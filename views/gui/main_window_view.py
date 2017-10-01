from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from model.library import Library
from views.gui.books_window import BooksWindow
from views.gui.visitors_window import VisitorsWindow
from views.gui.show_history_window import ShowHistory
from views.gui.add_book_window import AddBookWindow
from views.gui.add_visitor_window import AddVisitorWindow
from views.gui.authors_window import ShowAuthorWindow
from views.gui.edit_visitor_window import ChangeVisitorWindow
from views.gui.write_book_on_visitor import WriteBookOnVisitor
from views.gui.add_remove_date_window import AddRemoveDate
from views.gui.search_book_by_name_window import SearchBookByName
from views.gui.ui.main_window import Ui_MainWindow

class MainWindowView(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowView, self).__init__()
        self.setupUi(self)

        # move to center
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.setWindowTitle('LiB')
        self.setWindowIcon(QIcon('Lb.png'))

        self.bind_elements()

        self.library = Library()

    def bind_elements(self):
        self.show_books.clicked.connect(self.create_books_window)
        self.show_visitors.clicked.connect(self.create_visitors_window)
        self.add_visitor.clicked.connect(self.add_visitor_window)
        self.add_book.clicked.connect(self.add_book_window)
        self.show_author.clicked.connect(self.show_author_window)
        self.change_visitor.clicked.connect(self.chenge_visitor_window)
        self.write_book_on_visitor.clicked.connect(self.write_book_on_visitor_window)
        self.add_remove_date.clicked.connect(self.add_remove_date_window)
        self.show_history.clicked.connect(self.show_history_window)
        self.search_book_by_name.clicked.connect(self.search_book_by_name_window)


    def create_books_window(self):
        self.books_window = BooksWindow(self.library.books, self.library.book_has_author_list,
                                                     self.library.authors,
                                                     self.library.history, self.library.visitors)
        self.books_window.show()

    def create_visitors_window(self):
        self.visitors_window = VisitorsWindow(self.library.visitors, self.library.genders, self.library.books,
                                              self.library.history)
        self.visitors_window.show()

    def add_visitor_window(self):
        self.add_visitor = AddVisitorWindow(self.library)
        self.add_visitor.show()

    def add_book_window(self):
        self.add_book = AddBookWindow(self.library)
        self.add_book.show()

    def show_author_window(self):
        self.show_author = ShowAuthorWindow(self.library.authors)
        self.show_author.show()

    def chenge_visitor_window(self):
        self.chenge_visitor = ChangeVisitorWindow(self.library)
        self.chenge_visitor.show()

    def write_book_on_visitor_window(self):
        self.write_book_on_visitor = WriteBookOnVisitor(self.library)
        self.write_book_on_visitor.show()

    def add_remove_date_window(self):
        self.add_remove_date = AddRemoveDate(self.library)
        self.add_remove_date.show()

    def show_history_window(self):
        self.show_history = ShowHistory(self.library.history, self.library.visitors, self.library.books,
                                        self.library.book_has_author_list, self.library.authors)
        self.show_history.show()

    def search_book_by_name_window(self):
        self.search_book_by_name = SearchBookByName(self.library.books, self.library.book_has_author_list,
                                                    self.library.authors, self.library.visitors, self.library.history)
        self.search_book_by_name.show()

