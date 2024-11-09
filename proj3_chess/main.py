from chess_pieces import *
from board import Board
from player import Player
from random import randint, choice


def generate_random_board(
    min_size: int, max_size: int, player1: Player, player2: Player
):

    # generate a random board:
    b = Board(randint(min_size, max_size), randint(min_size, max_size))
    for x in range(b.width):
        for y in range(b.height):
            if randint(0, 1) == True:
                choice((Rook, Bishop, Knight, Pawn, King, Queen))(
                    choice((player1, player1)), b, (x, y)
                )
    print(b)


plr1 = Player(1, lambda x: x.upper() + " ")
plr2 = Player(-1, lambda y: y.lower() + "*")

generate_random_board(2, 5, plr1, plr2)


for move in plr1.get_available_moves():
    print(move)
