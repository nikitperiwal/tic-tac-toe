from math import inf
import numpy as np


class TicTacToe:
    def __init__(self):
        """
        Initialises the game.
        """
        self.board_state = None
        self.board_left = 9
        self.player = 'X'
        self.resetBoardState()

    def resetBoardState(self):
        """
        Resets the game board.
        """
        self.board_state = [['.', '.', '.'],
                            ['.', '.', '.'],
                            ['.', '.', '.']]

    def updateBoardState(self, turn_index):
        """
        Updates the state of the board with the turn_index.
        Also, decreases the board_left counter.
        Parameters:
            turn_index: (i-th, j-th) index of the turn to be played.
        """
        if self.player == 'X':
            self.board_state[turn_index[0]][turn_index[1]] = 'X'
        else:
            self.board_state[turn_index[0]][turn_index[1]] = 'O'
        self.board_left -= 1

    def checkWin(self):
        """
        Checks whether the game has been won or not.
        Returns:
            True: If the game has been won.
            False: If the game hasn't been won.
        """
        if self.board_state[0][0] == self.board_state[1][1] == self.board_state[2][2] == self.player:
            return True
        elif self.board_state[0][2] == self.board_state[1][1] == self.board_state[2][0] == self.player:
            return True
        for i in range(3):
            if self.board_state[0][i] == self.board_state[1][i] == self.board_state[2][i] == self.player:
                return True
            elif self.board_state[i][0] == self.board_state[i][1] == self.board_state[i][2] == self.player:
                return True
        return False

    def checkDraw(self):
        """
        Checks whether the game is a draw or not.
        Returns:
            True: If the game is a draw.
            False: If the game isn't a draw.
        """
        if self.board_left == 0:
            return True
        return False

    def resetGame(self):
        """
        Resets the game and the game variables.
        """
        self.resetBoardState()
        self.board_left = 9
        self.player = 'X'

    def swapPlayer(self):
        """
        Swaps the current player.
        """
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def turnPlayed(self, turn_index):
        """
        Plays the Game turn according to the parameter passed and returns the result.
        Also, resets the game if it's a draw or won.
        Parameters:
            turn_index: (i-th, j-th) index of the turn to be played.
        Returns:
            True : If the game has been won.
            False: If the game is a draw.
            None : If there is no result.
        """
        self.updateBoardState(turn_index)
        result = self.checkWin()
        if result:
            self.resetGame()
            return True
        else:
            result = self.checkDraw()
            if result:
                self.resetGame()
                return False
            else:
                self.swapPlayer()
                return None

    def getScore(self):
        """
        Check who is going to win and send an appropriate score according to the result.
        Returns:
             10: If, the player-1 wins.
            -10: If, the player-2 wins.
              0: If, it is a draw.
        """
        temp = self.player
        self.player = 'X'
        if self.checkWin():
            self.player = temp
            return 10
        self.player = 'O'
        if self.checkWin():
            self.player = temp
            return -10
        self.player = temp
        return 0

    def validPos(self, turn_index):
        """
        Checks whether the position is a valid turn or not.
        Parameters:
            turn_index: (i-th, j-th) position of the turn to be played.
        Returns:
            True : If the position is valid.
            False: If the position is invalid.
        """
        if self.board_state[turn_index[0]][turn_index[1]] == '.':
            return True
        return False

    def alpha_beta(self, depth, alpha, beta, player):
        row = -1
        col = -1
        if depth == 0 or self.checkWin():
            return [(row, col), self.getScore()]

        else:
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.board_state[i][j] == '.':
                        self.board_state[i][j] = player

                        if player == 'X':
                            score = self.alpha_beta(depth - 1, alpha, beta, 'O')
                            if score[1] > alpha:
                                alpha = score[1]
                                row = i
                                col = j

                        else:
                            score = self.alpha_beta(depth - 1, alpha, beta, 'X')
                            if score[1] < beta:
                                beta = score[1]
                                row = i
                                col = j
                        self.board_state[i][j] = '.'

                        if alpha >= beta:
                            break

            if player == 'X':
                return [(row, col), alpha]
            else:
                return [(row, col), beta]
    
    def bestMovePlayer1(self, btnNumber=-1):
        """
        Function that uses alpha-beta pruning to evaluate the best move for the player-1.
        Returns:
            turn_index: The best possible move - (ith, jth) position - for the player
        """
        if btnNumber == -1:
            while True:
                turn_index, m = self.alpha_beta(self.board_left, -inf, inf, 'X')
                if self.validPos(turn_index):
                    break
        else:
            num = np.arange(0, 9).reshape(3, 3)
            pos = np.argwhere(num == int(btnNumber)-1)
            turn_index = [int(pos[0, 0]), int(pos[0, 1])]
        return turn_index

    def bestMovePlayer2(self):
        """
        Function that uses alpha-beta pruning to evaluate the best move for the player-2.
        Returns:
            turn_index: The best possible move - (ith, jth) position - for the player
        """
        while True:
            turn_index, m = self.alpha_beta(self.board_left, -inf, inf, 'O')
            if self.validPos(turn_index):
                break
        return turn_index
