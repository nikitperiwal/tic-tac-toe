import sys
from PyQt5 import QtWidgets
from tictactoe import TicTacToe
from mainwindow import Ui_MainWindow

game = TicTacToe()
ui = None


def resetGame():
    game.resetGame()


def userTurn(indexes, player="User"):
    result = game.turnPlayed(indexes)
    if None == result:
        if player == "User":
            AITurn()
    elif result:
        ui.increaseScore(player)
        ui.resetGamePanel()
    elif not result:
        ui.resetGamePanel()


def AITurn():
    i, j = bestAIMove()
    userTurn((i, j), player="AI")


def bestAIMove():
    for i in range(3):
        for j in range(3):
            if game.board_state[i][j] == '.':
                return i, j


def openGameWindow():
    global ui
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    MainForm = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainForm)
    MainForm.show()
    app.exec_()

if __name__ == "__main__":
    openGameWindow()
