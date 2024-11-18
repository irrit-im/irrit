from chess_pieces import *
from board import Board
from proj3_chess.piece_properties import Player
from random import randint, choice


def generate_random_board(
    min_size: int,
    max_size: int,
    color1: Color,
    color2: Color,
    piece_types: Tuple[ChessPiece] = (Rook, Bishop, Knight, Pawn, King, Queen),
):
    width = randint(min_size, max_size)
    height = randint(min_size, max_size)
    board = Board(width, height)

    for x in range(board.width):
        for y in range(board.height):
            if randint(0, 1):
                piece = choice(piece_types)(choice((color1, color2)))
                piece.add_to_board(board, Spot(x=x, y=y))
    return board


white = Color(1, lambda x: x.upper() + " ")
black = Color(-1, lambda y: y.lower() + "*")

generate_random_board(2, 5, white, black)


for move in white.get_available_moves():  # TODO: ummmm
    print(move)
