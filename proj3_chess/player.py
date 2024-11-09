from enum import Enum
from typing import Callable


class Direction(Enum):  # TODO: Maybe rename this? or add RIGHT and LEFT?
    UP = 1
    DOWN = -1


class Player:
    def __init__(
        self, direction: Direction, symbol_transformation: Callable[[str], str]
    ) -> None:
        self.direction = direction
        self.symbolize = symbol_transformation
        self.pieces = []

    def get_available_moves(self) -> dict:  # TODO: proper type hint
        moves = {}
        for piece in self.pieces:
            moves.append[piece] = piece.get_available_moves()
        return moves
