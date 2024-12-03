from board import Board
from piece_properties import Player
from abc import ABC, abstractmethod
from coordinates import Move, Spot, MoveVector
from typing import Iterable, Optional

RIGHT = MoveVector(x=1, y=0)
LEFT = MoveVector(x=-1, y=0)
UP = MoveVector(x=0, y=1)
DOWN = MoveVector(x=0, y=-1)
UP_RIGHT = MoveVector(x=1, y=1)
UP_LEFT = MoveVector(x=-1, y=1)
DOWN_RIGHT = MoveVector(x=1, y=-1)
DOWN_LEFT = MoveVector(x=-1, y=-1)


class ChessPiece(ABC):
    PIECE_NAME = ""

    def __init__(self, player: Player) -> None:
        self.player = player
        self.direction = player.direction.value
        self.symbol = player.symbol_transformation(self.PIECE_NAME)

    def add_to_board(self, board: Board, spot: Spot) -> None:
        self.board = board
        if board.state[spot.x][spot.y]:
            raise ValueError("spot is already taken")
        board.state[spot.x][spot.y] = self

    def is_legal_move(self, spot: Spot) -> bool:
        if not self.board.is_spot_within_range(spot):
            return False
        spot_state = self.board.state[spot.x][spot.y]
        return spot_state == None or spot_state.player != self.player

    def does_capture_piece(self, spot: Spot) -> bool:
        if not self.is_legal_move(spot):
            raise ValueError("Spot is out of board range")
        spot_state = self.board.state[spot.x][spot.y]
        return spot_state is not None and spot_state.player != self.player

    def get_spot(self) -> Spot:
        for x in range(self.board.width):
            for y in range(self.board.height):
                if self.board.state[x][y] == self:
                    return Spot(x=x, y=y)

    @abstractmethod
    def get_available_moves(self) -> list[Move]:
        pass

    def get_moves_in_directions(
        self,
        move_directions: Iterable[MoveVector],
        depth: Optional[int] = -1,
        from_spot: Optional[Spot] = None,
    ) -> list[Move]:

        depth -= 1
        moves = []
        spot = from_spot or self.get_spot()
        for step in move_directions:
            move_target = spot + step
            if self.is_legal_move(move_target):
                moves.append(
                    Move(
                        destination=move_target,
                        does_capture_piece=self.does_capture_piece(move_target),
                        piece_symbol=self.PIECE_NAME,
                    )
                )

                if depth != 0 and not self.does_capture_piece(move_target):
                    moves += self.get_moves_in_directions(
                        [step], depth - 1, move_target
                    )
        return moves


class Rook(ChessPiece):
    PIECE_NAME = "R"
    MOVE_DIRECTIONS = (UP, DOWN, RIGHT, LEFT)

    def get_available_moves(self) -> list[Move]:
        return self.get_moves_in_directions(self.MOVE_DIRECTIONS)


class Bishop(ChessPiece):
    PIECE_NAME = "B"
    MOVE_DIRECTIONS = (UP_RIGHT, DOWN_LEFT, DOWN_RIGHT, UP_LEFT)

    def get_available_moves(self) -> list[Move]:
        return self.get_moves_in_directions(self.MOVE_DIRECTIONS)


class Queen(Bishop, Rook):
    PIECE_NAME = "Q"
    MOVE_DIRECTIONS = Rook.MOVE_DIRECTIONS + Bishop.MOVE_DIRECTIONS

    def get_available_moves(self) -> list[Move]:
        return self.get_moves_in_directions(self.MOVE_DIRECTIONS)


class King(ChessPiece):
    PIECE_NAME = "K"
    MOVES = (UP, DOWN, RIGHT, LEFT, UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

    def get_available_moves(self) -> list[Move]:
        return self.get_moves_in_directions(self.MOVES, depth=1)


class Knight(ChessPiece):
    PIECE_NAME = "N"
    MV = MoveVector
    MOVES = [
        MV(x=1, y=2),
        MV(x=1, y=-2),
        MV(x=2, y=1),
        MV(x=2, y=-1),
        MV(x=-1, y=2),
        MV(x=-1, y=-2),
        MV(x=-2, y=1),
        MV(x=-2, y=-1),
    ]

    def get_available_moves(self) -> list[Move]:
        return self.get_moves_in_directions(self.MOVES, depth=1)


class Pawn(ChessPiece):
    PIECE_NAME = "P"
    MOVES = (UP_LEFT, UP, UP_RIGHT)

    def get_available_moves(self) -> list[Move]:
        moves = []
        for step in self.MOVES:
            move_target = self.get_spot() + step * self.direction
            should_capture = bool(step.x)
            if (
                self.is_legal_move(move_target)
                and self.does_capture_piece(move_target) == should_capture
            ):
                moves.append(
                    Move(
                        destination=move_target,
                        does_capture_piece=should_capture,
                        piece_symbol=self.PIECE_NAME,
                    )
                )
        return moves
