from AI import Alpha_Beta


class TicTacToe:
    def __init__(self):
        self.board_state = None
        self.board_left = 9
        self.player = 'X'
        self.initialBoardState()
        self.ai = Alpha_Beta()

    def initialBoardState(self):
        self.board_state = [['.', '.', '.'],
                            ['.', '.', '.'],
                            ['.', '.', '.']]

    def updateBoardState(self, turn_index):
        if self.board_state[turn_index[0]][turn_index[1]] != '.':
            return False
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

    def bestMoveAi(self):
        """Function that uses alpha-beta pruning to evaluate the best move for the computer."""
        (m, turn_index) = self.ai.max_ab(self.board_state, -2, 2)
        return turn_index

    def bestMoveHelp(self):
        """Function that uses alpha-beta pruning to evaluate the best move for the player."""
        (m, turn_index) = self.ai.min_ab(self.board_state, -2, 2)
        return turn_index

    def printBoardState(self):
        print("Board state: ")
        print(self.board_state[0])
        print(self.board_state[1])
        print(self.board_state[2], '\n')


if __name__ == "__main__":
    obj = TicTacToe()
    print(obj.turnPlayed((0, 2)))
    obj.printBoardState()
    print(obj.turnPlayed((1, 0)))
    obj.printBoardState()
    print(obj.turnPlayed((0, 0)))
    obj.printBoardState()
    print(obj.turnPlayed((0, 1)))
    obj.printBoardState()
