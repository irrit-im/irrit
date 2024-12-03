from setup_utils import generate_random_board, create_default_players
from board import Board
from piece_properties import Player
from chess_pieces import ChessPiece


MIN_BOARD_SIZE = 2
MAX_BOARD_SIZE = 5

white, black = create_default_players()
board = generate_random_board(MIN_BOARD_SIZE, MAX_BOARD_SIZE, white, black)


def get_player_pieces(board: Board, player: Player) -> list[ChessPiece]:
    pieces = []
    for row in board.state:
        for spot_state in row:
            if spot_state and spot_state.player == player:
                pieces.append(spot_state)
    return pieces


def print_player_moves() -> None:
    print(board)
    for piece in get_player_pieces(board, white):
        print(f"\n{piece.symbol} at {piece.get_spot()}:  ", end="")
        for i in piece.get_available_moves():
            print(i, end=" , ")


print_player_moves()
