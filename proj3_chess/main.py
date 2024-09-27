from chess_pieces import *
from board import Board
from player import Player


b = Board(3, 1)
plr1 = Player(1, "white")
plr2 = Player(-1, "black")

p1 = Rook(plr1, b, (0, 0))
p2 = Rook(plr2, b, (1, 0))
print(p1.available_moves())
