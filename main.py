# YUITyper Developed by Mack Alex
# Start date: 19.10.222

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys
import string


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_main_window()

        # Close button
        exit_button = QPushButton("Exit", self)
        exit_button.setGeometry(150, 150, 400, 400)
        exit_button.show()
        exit_button.clicked.connect(self.destroy_app)

        # Main active part
        app = QLabel(self)
        app.move(810, 410)
        app.setText("app in maintenance")

        # List of basic datasets

    def setup_main_window(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setStyleSheet("border-radius: 40px;") сюда цвет
        self.setWindowTitle("YUITyper")
        self.resize(1620, 820)
        app_window = self.frameGeometry()
        window = QDesktopWidget().availableGeometry().center()
        app_window.moveCenter(window)
        self.move(app_window.topLeft())

    # Поменять на Slot
    @staticmethod
    def destroy_app():
        sys.exit(app.exec_())


# Прототип загрузки пользовательских датасетов
def load_data(filename):
    data = []
    file = open(filename, "r")

    for raw_string in file:
        for mark in string.punctuation:
            if mark in raw_string:
                raw_string = raw_string.replace(mark, '')

        data.append(raw_string.lower().split())
    file.close()

    print(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())
