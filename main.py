# YUITyper Developed by Mack Alex
# Start date: 19.10.222

import PyQt5
from PyQt5.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("YUITyper")
        self.resize(1620, 820)
        self.center()

    def center(self):
        app_window = self.frameGeometry()
        window = QDesktopWidget().availableGeometry().center()
        app_window.moveCenter(window)
        self.move(app_window.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
