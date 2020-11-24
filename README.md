# Tic-Tac-Toe
A Gui Game made in Python using PyQT5

## Theory
TicTacToe is a two player game, but not always do we have someone to play with. For that reason, we have integrated an Artificial Intelligence(AI) to play against. This AI can also recommend best moves for the player to perform.
 
### Alpha-Beta Pruning
The AI in this game uses the Alpha-Beta pruning algorithm.
Alpha–beta pruning is a search algorithm that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree. It is an adversarial search algorithm used commonly for machine playing of two-player games. It stops evaluating a move when at least one possibility has been found that proves the move to be worse than a previously examined move. Such moves need not be evaluated further. When applied to a standard minimax tree, it returns the same move as minimax would, but prunes away branches that cannot possibly influence the final decision.


## Modules
1.	Built-in
  a.	sys
  b.	PyQt5
  c.	math
2.	User Defined
  a.	mainwindow
  b.	tictactoe
  c.	AI
