from math import inf
import numpy as np


class TicTacToe:
    def __init__(self):
        self.board_state = None
        self.board_left = 9
        self.player = 'X'
        self.initialBoardState()

    def initialBoardState(self):
        self.board_state = [['.', '.', '.'],
                            ['.', '.', '.'],
                            ['.', '.', '.']]

    def updateBoardState(self, turn_index):
        if self.player == 'X':
            self.board_state[turn_index[0]][turn_index[1]] = 'X'
        else:
            self.board_state[turn_index[0]][turn_index[1]] = 'O'
        self.board_left -= 1

    def checkWin(self):
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
        if self.board_left == 0:
            return True
        return False

    def resetGame(self):
        self.initialBoardState()
        self.board_left = 9
        self.player = 'X'

    def swapPlayer(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def turnPlayed(self, turn_index):
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
        # Checks whos going to win
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
        if self.board_state[turn_index[0]][turn_index[1]] == '.':
            return True
        return False

    def ai(self, depth, alpha, beta, player):
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
                            score = self.ai(depth - 1, alpha, beta, 'O')
                            if score[1] > alpha:
                                alpha = score[1]
                                row = i
                                col = j

                        else:
                            score = self.ai(depth - 1, alpha, beta, 'X')
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
        """Function that uses alpha-beta pruning to evaluate the best move for the player."""
        if btnNumber == -1:
            while True:
                turn_index, m = self.ai(self.board_left, -inf, inf, 'X')
                if self.validPos(turn_index):
                    break
        else:
            num = np.arange(0, 9).reshape(3, 3)
            pos = np.argwhere(num == int(btnNumber)-1)
            turn_index = [int(pos[0, 0]), int(pos[0, 1])]
        self.turnPlayed(turn_index)

    def bestMovePlayer2(self):
        """Function that uses alpha-beta pruning to evaluate the best move for the computer."""
        while True:
            turn_index, m = self.ai(self.board_left, -inf, inf, 'O')
            if self.validPos(turn_index):
                break
        return turn_index
        self.turnPlayed(turn_index)


if __name__ == "__main__":
    ttt = TicTacToe()
    while True:
        ttt.bestMovePlayer1(-1)
        print(ttt.board_state)
        ttt.bestMovePlayer2()
        print(ttt.board_state)
