from board import Board
from player import Player
from abc import ABC, abstractmethod
from move import Move
from typing import Tuple


class ChessPiece(ABC):
    """Parent class for all chess pieces."""  # TODO: "But the documentation requires a better description of what the class represents"

    PIECE_NAME = ""

    def __init__(self, player: Player) -> None:
        self.player = player
        self.direction = player.direction
        # player.pieces.append(self)  # add the piece to the player # TODO: figure out if i actually need this
        self.name = player.symbolize(self.PIECE_NAME)

    def add_to_board(
        self, board: Board, spot: tuple[int, int]
    ) -> None:  # TODO: figure out spot type
        self.board = board
        if self.board[spot[0]][spot[1]]:
            raise ValueError("spot is already taken")
        self.board.board_state[spot[0]][spot[1]] = self

    def is_legal_move(self, spot: tuple[int, int]) -> bool:
        if not self.board.is_spot_within_range(spot):
            return False
        spot_state = self.board.board_state[spot[0]][spot[1]]
        return spot_state == None or spot_state.player != self.player

    def does_capture_piece(self, spot: tuple[int, int]) -> bool:
        spot_state = self.board.board_state[spot[0]][spot[1]]
        return spot_state == None or spot_state.player == self.player

    def get_spot(self) -> tuple[int, int]:
        for x in range(self.board.width):
            for y in range(self.board.height):
                if self.board.board_state[x][y] == self:
                    return (x, y)

    @abstractmethod
    def get_available_moves(self) -> list[Move]:
        pass

    def get_available_moves_in_directions(
        self, move_directions: Tuple[Tuple[int, int]]
    ) -> list[Move]:  # TODO: figure out type hinting
        moves = []
        spot_x, spot_y = self.get_spot()
        for x_move, y_move in move_directions:
            next_move = (spot_x + x_move, spot_y + y_move)
            while self.is_legal_move(next_move):
                moves.append(
                    Move(self.PIECE_NAME, next_move, self.does_capture_piece(next_move))
                )
                if self.does_capture_piece(next_move):
                    break
                next_move = (next_move[0] + x_move, next_move[1] + y_move)
        return moves


class Rook(ChessPiece):
    PIECE_NAME = "R"

    def get_available_moves(self) -> list:
        move_directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        return self.get_available_moves_in_directions(move_directions=move_directions)


class Bishop(ChessPiece):
    PIECE_NAME = "B"

    def get_available_moves(self) -> list[Move]:
        move_directions = (
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        )  # TODO: should make this a class constant?
        return self.get_available_moves_in_directions(move_directions=move_directions)


class Queen(Rook, Bishop):
    PIECE_NAME = "Q"

    def get_available_moves(self) -> list[Move]:
        return Bishop.get_available_moves(self) + Rook.get_available_moves(self)


class King(ChessPiece):
    PIECE_NAME = "K"

    def get_available_moves(self) -> list[Move]:
        moves = []
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                next_move = (self.get_spot()[0] + x, self.get_spot()[1] + y)
                if self.is_legal_move(next_move) and next_move != self.get_spot():
                    moves.append(
                        Move(
                            self.PIECE_NAME,
                            next_move,
                            self.does_capture_piecenext_moves(),
                        )
                    )
        return moves


class Knight(ChessPiece):
    PIECE_NAME = "N"
    KNIGHT_MOVES = [
        (1, 2),
        (2, 1),
        (-1, 2),
        (-2, 1),
        (1, -2),
        (2, -1),
        (-1, -2),
        (-2, -1),
    ]

    def get_available_moves(self) -> list[Move]:
        spot_x, spot_y = self.get_spot()
        moves = []
        for x_move, y_move in self.KNIGHT_MOVES:
            next_move = (spot_x + x_move, spot_y + y_move)
            if self.is_legal_move(next_move):
                moves.append(
                    Move(self.PIECE_NAME, next_move, self.does_capture_piece(next_move))
                )
        return moves


class Pawn(ChessPiece):
    PIECE_NAME = "P"

    def get_available_moves(self) -> list[Move]:  # TODO: clean up this mess :)
        spot_x, spot_y = self.get_spot()
        moves = []
        # move 1 forward
        next_move = (spot_x, spot_y + self.player.direction)
        if self.is_legal_move(next_move) and not self.does_capture_piece(next_move):
            moves.append(Move(self.PIECE_NAME, next_move, False))
        # capture piece diagonally
        for x_move in (-1, 1):
            next_move = (spot_x + x_move, spot_y + self.player.direction)
            if self.is_legal_move(next_move) and self.does_capture_piece(next_move):
                moves.append(Move(self.PIECE_NAME, next_move, True))
        # TODO: add case - move 2 forward
        return moves
