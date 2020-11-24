import sys
from PyQt5 import QtWidgets
from tictactoe import TicTacToe
from mainwindow import Ui_MainWindow


def openGameWindow():
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    mainform = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(mainform, TicTacToe())
    mainform.show()
    app.exec_()


if __name__ == "__main__":
    openGameWindow()
