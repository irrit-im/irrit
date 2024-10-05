from chess_pieces import *
from board import Board
from player import Player
from random import randint, choice

MAX_SIZE = 5
MIN_SIZE = 2

# players:
plr1 = Player(1, lambda x: x.upper() + " ")
plr2 = Player(-1, lambda y: y.lower() + "*")

# generate a random board:
b = Board(randint(MIN_SIZE, MAX_SIZE), randint(MIN_SIZE, MAX_SIZE))
for x in range(b.width):
    for y in range(b.height):
        if randint(0, 1) == True:
            choice((Rook, Bishop, Knight, Pawn, King, Queen))(
                choice((plr1, plr2)), b, (x, y)
            )

b.print()

for i in plr1.all_available_moves():
    print(i[0], i[1])
