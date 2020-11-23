
class Alpha_Beta:
    def max_ab(self, current_State, alpha, beta):
        """Function to return the best positions for AI
        Inputs:
            current_State - The current state of the 3x3 board
            alpha - The least value of alpha that's possible
            beta - The Max value of beta that's possible

        Outputs:
            maxv - The highest value choice
            turn_index - The best move for the AI
        """

        maxv = -2
        turn_index = [None, None]
        for i in range(0, 3):
            for j in range(0, 3):
                if current_State[i][j] == '.':
                    current_State[i][j] = 'O'
                    (m, turn_index) = self.min_ab(current_State, alpha, beta)
                    if m > maxv:
                        maxv = m
                        turn_index = [i, j]
                    current_State[i][j] = '.'
                    if maxv >= beta:
                        return maxv, turn_index
                    if maxv > alpha:
                        alpha = maxv
        return maxv, turn_index

    def min_ab(self, current_State, alpha, beta):
        """Function to return the best positions for AI
        Inputs:
            current_State - The current state of the 3x3 board
            alpha - The least value of alpha that's possible
            beta - The Max value of beta that's possible

        Outputs:
            minv - The lowest value choice
            turn_index - The best move for the AI (Contains the Positions)
        """

        minv = 2
        turn_index = [None, None]
        for i in range(0, 3):
            for j in range(0, 3):
                if current_State[i][j] == '.':
                    current_State[i][j] = 'X'
                    (m, turn_index) = self.max_ab(current_State, alpha, beta)
                    if m < minv:
                        minv = m
                        turn_index = [i, j]
                    current_State[i][j] = '.'
                    if minv <= alpha:
                        return minv, turn_index

                    if minv < beta:
                        beta = minv

        return minv, turn_index
