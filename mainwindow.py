from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def __init__(self, MainWindow, game_obj):
        """
        Initialises the GameWindow and sets the some values.
        Also, sets the game object.
        Parameters:
            MainWindow : MainWindow object in which the UI is to be displayed.
            game_obj   : TicTacToe game object in which the game is to be played.
        """
        self.iconX = QtGui.QIcon()
        self.iconX.addPixmap(QtGui.QPixmap("Resources/X.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconO = QtGui.QIcon()
        self.iconO.addPixmap(QtGui.QPixmap("Resources/Y.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconGame = QtGui.QIcon()
        self.iconGame.addPixmap(QtGui.QPixmap("Resources/Logo.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_list = [0] * 9
        self.game = game_obj
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        """
        Sets up the UI in the mainwindow passed.
        Parameters:
            MainWindow : MainWindow object in which the UI is to be displayed.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 571)
        MainWindow.setMinimumSize(QtCore.QSize(391, 571))
        MainWindow.setMaximumSize(QtCore.QSize(391, 571))
        MainWindow.setWindowIcon(self.iconGame)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frm_TicTacToe = QtWidgets.QFrame(self.centralwidget)
        self.frm_TicTacToe.setGeometry(QtCore.QRect(0, 0, 391, 571))
        self.frm_TicTacToe.setStyleSheet("background: rgb(12, 160, 144);")
        self.frm_TicTacToe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_TicTacToe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_TicTacToe.setObjectName("frm_TicTacToe")
        self.btn_Restart = QtWidgets.QPushButton(self.frm_TicTacToe)
        self.btn_Restart.setGeometry(QtCore.QRect(10, 480, 371, 71))
        self.btn_Restart.setStyleSheet("background: rgb(21, 189, 172);\n"
                                       "border-radius: 10px;\n"
                                       "font-size: 30px;\n"
                                       "color: rgb(238, 236, 211);")
        self.btn_Restart.setObjectName("btn_Restart")
        self.frm_PlayArea = QtWidgets.QFrame(self.frm_TicTacToe)
        self.frm_PlayArea.setGeometry(QtCore.QRect(10, 90, 371, 371))
        self.frm_PlayArea.setStyleSheet("background: rgb(12, 160, 144);\n"
                                        "border-radius: 10px;")
        self.frm_PlayArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_PlayArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_PlayArea.setObjectName("frm_PlayArea")
        self.frm_NegOneOne = QtWidgets.QFrame(self.frm_PlayArea)
        self.frm_NegOneOne.setGeometry(QtCore.QRect(0, 0, 110, 110))
        self.frm_NegOneOne.setStyleSheet("background: rgb(21, 189, 172);\n"
                                         "border-radius: 10px;")
        self.frm_NegOneOne.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_NegOneOne.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_NegOneOne.setObjectName("frm_NegOneOne")
        self.btn_TTT1 = QtWidgets.QPushButton(self.frm_NegOneOne)
        self.btn_TTT1.setGeometry(QtCore.QRect(0, 0, 111, 111))
        self.btn_TTT1.setText("")
        self.btn_TTT1.setObjectName("btn_TTT1")
        self.frm_ZeroOne = QtWidgets.QFrame(self.frm_PlayArea)
        self.frm_ZeroOne.setGeometry(QtCore.QRect(130, 0, 110, 110))
        self.frm_ZeroOne.setStyleSheet("background: rgb(21, 189, 172);\n"
                                       "border-radius: 10px;")
        self.frm_ZeroOne.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_ZeroOne.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_ZeroOne.setObjectName("frm_ZeroOne")
        self.btn_TTT2 = QtWidgets.QPushButton(self.frm_ZeroOne)
        self.btn_TTT2.setGeometry(QtCore.QRect(0, 0, 111, 111))
        self.btn_TTT2.setText("")
        self.btn_TTT2.setObjectName("btn_TTT2")
        self.frm_OneOne = QtWidgets.QFrame(self.frm_PlayArea)
        self.frm_OneOne.setGeometry(QtCore.QRect(260, 0, 110, 110))
        self.frm_OneOne.setStyleSheet("background: rgb(21, 189, 172);\n"
                                      "border-radius: 10px;")
        self.frm_OneOne.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_OneOne.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_OneOne.setObjectName("frm_OneOne")
        self.btn_TTT3 = QtWidgets.QPushButton(self.frm_OneOne)
        self.btn_TTT3.setGeometry(QtCore.QRect(0, 0, 111, 111))
        self.btn_TTT3.setText("")
        self.btn_TTT3.setObjectName("btn_TTT3")
        self.frm_OneZero = QtWidgets.QFrame(self.frm_PlayArea)
        self.frm_OneZero.setGeometry(QtCore.QRect(260, 130, 110, 110))
        self.frm_OneZero.setStyleSheet("background: rgb(21, 189, 172);\n"
                                       "border-radius: 10px;")
        self.frm_OneZero.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_OneZero.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_OneZero.setObjectName("frm_OneZero")
        self.btn_TTT6 = QtWidgets.QPushButton(self.frm_OneZero)
        self.btn_TTT6.setGeometry(QtCore.QRect(0, 0, 111, 111))
        self.btn_TTT6.setText("")
        self.btn_TTT6.setObjectName("btn_TTT6")
        self.frm_ZeroZero = QtWidgets.QFrame(self.frm_PlayArea)
        self.frm_ZeroZero.setGeometry(QtCore.QRect(130, 130, 110, 110))
        self.frm_ZeroZero.setStyleSheet("background: rgb(21, 189, 172);\n"
                                        "border-radius: 10px;")
        self.frm_ZeroZero.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_ZeroZero.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_ZeroZero.setObjectName("frm_ZeroZero")
        self.btn_TTT5 = QtWidgets.QPushButton(self.frm_ZeroZero)
        self.btn_TTT5.setGeometry(QtCore.QRect(0, 0, 111, 111))
        self.btn_TTT5.setText("")
        self.btn_TTT5.setObjectName("btn_TTT5")
        self.frm_NegOneZero = QtWidgets.QFrame(self.frm_PlayArea)
        self.frm_NegOneZero.setGeometry(QtCore.QRect(0, 130, 110, 110))
        self.frm_NegOneZero.setStyleSheet("background: rgb(21, 189, 172);\n"
                                          "border-radius: 10px;")
        self.frm_NegOneZero.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_NegOneZero.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_NegOneZero.setObjectName("frm_NegOneZero")
        self.btn_TTT4 = QtWidgets.QPushButton(self.frm_NegOneZero)
        self.btn_TTT4.setGeometry(QtCore.QRect(0, 0, 111, 111))
        self.btn_TTT4.setText("")
        self.btn_TTT4.setObjectName("btn_TTT4")
        self.frm_NegOneNegOne = QtWidgets.QFrame(self.frm_PlayArea)
        self.frm_NegOneNegOne.setGeometry(QtCore.QRect(0, 260, 110, 110))
        self.frm_NegOneNegOne.setStyleSheet("background: rgb(21, 189, 172);\n"
                                            "border-radius: 10px;")
        self.frm_NegOneNegOne.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_NegOneNegOne.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_NegOneNegOne.setObjectName("frm_NegOneNegOne")
        self.btn_TTT7 = QtWidgets.QPushButton(self.frm_NegOneNegOne)
        self.btn_TTT7.setGeometry(QtCore.QRect(0, 0, 111, 111))
        self.btn_TTT7.setText("")
        self.btn_TTT7.setObjectName("btn_TTT7")
        self.frm_ZeroNegOne = QtWidgets.QFrame(self.frm_PlayArea)
        self.frm_ZeroNegOne.setGeometry(QtCore.QRect(130, 260, 110, 110))
        self.frm_ZeroNegOne.setStyleSheet("background: rgb(21, 189, 172);\n"
                                          "border-radius: 10px;")
        self.frm_ZeroNegOne.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_ZeroNegOne.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_ZeroNegOne.setObjectName("frm_ZeroNegOne")
        self.btn_TTT8 = QtWidgets.QPushButton(self.frm_ZeroNegOne)
        self.btn_TTT8.setGeometry(QtCore.QRect(0, 0, 111, 111))
        self.btn_TTT8.setText("")
        self.btn_TTT8.setObjectName("btn_TTT8")
        self.frm_OneNegOne = QtWidgets.QFrame(self.frm_PlayArea)
        self.frm_OneNegOne.setGeometry(QtCore.QRect(260, 260, 110, 110))
        self.frm_OneNegOne.setStyleSheet("background: rgb(21, 189, 172);\n"
                                         "border-radius: 10px;")
        self.frm_OneNegOne.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_OneNegOne.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_OneNegOne.setObjectName("frm_OneNegOne")
        self.btn_TTT9 = QtWidgets.QPushButton(self.frm_OneNegOne)
        self.btn_TTT9.setGeometry(QtCore.QRect(0, 0, 111, 111))
        self.btn_TTT9.setText("")
        self.btn_TTT9.setObjectName("btn_TTT9")

        self.btn_TTT1.setIconSize(QtCore.QSize(90, 90))
        self.btn_TTT2.setIconSize(QtCore.QSize(90, 90))
        self.btn_TTT3.setIconSize(QtCore.QSize(90, 90))
        self.btn_TTT4.setIconSize(QtCore.QSize(90, 90))
        self.btn_TTT5.setIconSize(QtCore.QSize(90, 90))
        self.btn_TTT6.setIconSize(QtCore.QSize(90, 90))
        self.btn_TTT7.setIconSize(QtCore.QSize(90, 90))
        self.btn_TTT8.setIconSize(QtCore.QSize(90, 90))
        self.btn_TTT9.setIconSize(QtCore.QSize(90, 90))

        self.frm_ScoreBoard = QtWidgets.QFrame(self.frm_TicTacToe)
        self.frm_ScoreBoard.setGeometry(QtCore.QRect(10, 10, 371, 71))
        self.frm_ScoreBoard.setStyleSheet("background: rgb(12, 160, 144);\n"
                                          "border-radius: 10px;")
        self.frm_ScoreBoard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_ScoreBoard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_ScoreBoard.setObjectName("frm_ScoreBoard")
        self.frm_PlayerScore = QtWidgets.QFrame(self.frm_ScoreBoard)
        self.frm_PlayerScore.setGeometry(QtCore.QRect(0, 20, 181, 51))
        self.frm_PlayerScore.setStyleSheet("background: rgb(21, 189, 172)")
        self.frm_PlayerScore.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_PlayerScore.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_PlayerScore.setObjectName("frm_PlayerScore")
        self.txt_PlayerScore = QtWidgets.QLabel(self.frm_PlayerScore)
        self.txt_PlayerScore.setGeometry(QtCore.QRect(0, 1, 181, 51))
        self.txt_PlayerScore.setStyleSheet("font-family: MS PGothic;\n"
                                           "font-size: 40px;\n"
                                           "color: rgb(238, 236, 211);")
        self.txt_PlayerScore.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_PlayerScore.setObjectName("txt_PlayerScore")
        self.frm_AIScore = QtWidgets.QFrame(self.frm_ScoreBoard)
        self.frm_AIScore.setGeometry(QtCore.QRect(190, 20, 180, 51))
        self.frm_AIScore.setStyleSheet("background: rgb(21, 189, 172)")
        self.frm_AIScore.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_AIScore.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_AIScore.setObjectName("frm_AIScore")
        self.txt_AIScore = QtWidgets.QLabel(self.frm_AIScore)
        self.txt_AIScore.setGeometry(QtCore.QRect(0, 1, 181, 51))
        self.txt_AIScore.setStyleSheet("font-family: MS PGothic;\n"
                                       "font-size: 40px;\n"
                                       "color: rgb(238, 236, 211);")
        self.txt_AIScore.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_AIScore.setObjectName("txt_AIScore")
        self.lbl_AIDisplay = QtWidgets.QLabel(self.frm_ScoreBoard)
        self.lbl_AIDisplay.setGeometry(QtCore.QRect(190, 0, 181, 21))
        self.lbl_AIDisplay.setStyleSheet("color: rgb(238, 236, 211);\n"
                                         "background: ;\n"
                                         "font-size: 16px;\n"
                                         "font-weight: bold;")
        self.lbl_AIDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_AIDisplay.setObjectName("lbl_AIDisplay")
        self.lbl_PlayerDisplay = QtWidgets.QLabel(self.frm_ScoreBoard)
        self.lbl_PlayerDisplay.setGeometry(QtCore.QRect(0, 0, 181, 21))
        self.lbl_PlayerDisplay.setStyleSheet("font-size: 16px;\n"
                                             "font-weight: bold;\n"
                                             "color: rgb(238, 236, 211);")
        self.lbl_PlayerDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_PlayerDisplay.setObjectName("lbl_PlayerDisplay")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.userFunctions()

    def retranslateUi(self, MainWindow):
        """
        Sets the texts in window objects which can be translated.
        Parameters:
            MainWindow : MainWindow object in which the UI is to be displayed.
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TicTacToe"))
        self.btn_Restart.setText(_translate("MainWindow", "Restart Game"))
        self.txt_PlayerScore.setText(_translate("MainWindow", "0"))
        self.txt_AIScore.setText(_translate("MainWindow", "0"))
        self.lbl_AIDisplay.setText(_translate("MainWindow", "AI"))
        self.lbl_PlayerDisplay.setText(_translate("MainWindow", "Player"))

    def userFunctions(self):
        """
        Connects the button pressed events with their respective functions.
        """
        self.btn_TTT1.clicked.connect(lambda: self.buttonPressed(0))
        self.btn_TTT2.clicked.connect(lambda: self.buttonPressed(1))
        self.btn_TTT3.clicked.connect(lambda: self.buttonPressed(2))
        self.btn_TTT4.clicked.connect(lambda: self.buttonPressed(3))
        self.btn_TTT5.clicked.connect(lambda: self.buttonPressed(4))
        self.btn_TTT6.clicked.connect(lambda: self.buttonPressed(5))
        self.btn_TTT7.clicked.connect(lambda: self.buttonPressed(6))
        self.btn_TTT8.clicked.connect(lambda: self.buttonPressed(7))
        self.btn_TTT9.clicked.connect(lambda: self.buttonPressed(8))
        self.btn_Restart.clicked.connect(lambda: self.resetForm())

    def changeButtonIcon(self, index, icon='X'):
        """
        Changes the button icons of the index passed in the form.
        Parameters:
            index : Contains index of the button to change icon of.
            icon  : Contains the icon to change to.
        """
        button_list = [self.btn_TTT1, self.btn_TTT2, self.btn_TTT3,
                       self.btn_TTT4, self.btn_TTT5, self.btn_TTT6,
                       self.btn_TTT7, self.btn_TTT8, self.btn_TTT9]

        self.btn_list[index] = 1
        if icon == 'X':
            icon = self.iconX
        else:
            icon = self.iconO
        button_list[index].setIcon(icon)

    def buttonPressed(self, index, icon='X'):
        """
        Function to handle what to do if button pressed.
        Parameters:
            index : Contains index of the button to change icon of.
            icon  : Contains the icon to change to.
        """
        if self.btn_list[index] == 0:
            self.changeButtonIcon(index, icon)
            i, j = index // 3, index % 3
            self.userTurn((i, j))

    def resetGamePanel(self):
        """
        Resets the game panel, game object and button icons.
        """
        self.btn_list = [0] * 9
        self.btn_TTT1.setIcon(QtGui.QIcon())
        self.btn_TTT2.setIcon(QtGui.QIcon())
        self.btn_TTT3.setIcon(QtGui.QIcon())
        self.btn_TTT4.setIcon(QtGui.QIcon())
        self.btn_TTT5.setIcon(QtGui.QIcon())
        self.btn_TTT6.setIcon(QtGui.QIcon())
        self.btn_TTT7.setIcon(QtGui.QIcon())
        self.btn_TTT8.setIcon(QtGui.QIcon())
        self.btn_TTT9.setIcon(QtGui.QIcon())
        self.game.resetGame()

    def resetForm(self):
        """
        Resets the whole form, along with the score board.
        """
        self.txt_AIScore.setText("0")
        self.txt_PlayerScore.setText("0")
        self.resetGamePanel()

    def increaseScore(self, player="User"):
        """
        Increases Score of the player passed in the scoreboard.
        Parameters:
            player : Player to increase the score of.
        """
        if player == "User":
            num = int(self.txt_PlayerScore.text()) + 1
            self.txt_PlayerScore.setText(str(num))
        else:
            num = int(self.txt_AIScore.text()) + 1
            self.txt_AIScore.setText(str(num))

    def gameResult(self, result):
        """
        Displays a popup message with the result for the game.
        Parameters:
            result : the result to print in the popup message.
        """
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(self.iconGame)
        msg.setWindowTitle("Result")
        msg.setText(result)
        msg.exec_()

    def userTurn(self, indexes, player="User"):
        """
        Function to handle the user turn.
        Updates the game object with the user-turn and gets the result.
        Prints the appropriate result and resets game when game ends.
        Parameters:
            indexes: indexes of the move to play. (ith, jth)
            player : Player to play the turn of.
        """
        result = self.game.turnPlayed(indexes)
        if None == result:
            if player == "User":
                self.AITurn()
        elif result:
            self.increaseScore(player)
            if player == "User":
                self.gameResult("You Won!")
            else:
                self.gameResult("You Lose!")
            self.resetGamePanel()
        elif not result:
            self.gameResult("It's a Draw!")
            self.resetGamePanel()

    def AITurn(self):
        """
        Function to handle the AI turn.
        Changes the button icon of the move played.
        Also plays the turn in the indexes predicted.
        """
        i, j = self.game.bestMovePlayer2()
        index = i*3+j
        self.changeButtonIcon(index, icon='O')
        self.userTurn((i, j), player="AI")
