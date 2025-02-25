from chess_pieces import *
from board import Board
from piece_properties import Player, EndLine
from random import randint, choice
from typing import Tuple

PIECE_TYPES = (
    Rook,
    Bishop,
    Knight,
    Pawn,
    King,
    Queen,
)


def generate_random_board(
    min_size: int,
    max_size: int,
    player1: Player,
    player2: Player,
    piece_types: Tuple[ChessPiece] = PIECE_TYPES,
) -> Board:
    width = randint(min_size, max_size)
    height = randint(min_size, max_size)
    board = Board(width, height)

    for x in range(board.width):
        for y in range(board.height):
            if randint(0, 1):
                piece = choice(piece_types)(choice((player1, player2)))
                piece.add_to_board(board, Spot(x=x, y=y))
    return board


def create_default_players() -> Tuple[Player, Player]:
    white = Player("white", EndLine.BOTTOM, lambda x: x.upper() + " ")
    black = Player("black", EndLine.TOP, lambda y: y.lower() + "*")
    return white, black
