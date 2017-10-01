import sys
from PyQt5.QtWidgets import QApplication

from views.gui.main_window_view import MainWindowView


def main():
    app = QApplication([])
    window = MainWindowView()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
