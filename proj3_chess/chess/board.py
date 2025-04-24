from coordinates import Spot
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from chess_pieces import ChessPiece


class Board:
    EMPTY_TILE_STRING = "  "
    SEPARATOR_STRING = " | "

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.state: list[list[("ChessPiece" | None)]] = [
            [None] * self.height for _ in range(self.width)
        ]

    def __str__(self) -> str:
        string = ""
        for line in self.state:
            string += self.SEPARATOR_STRING
            for piece in line:
                string += (
                    piece.symbol if piece else self.EMPTY_TILE_STRING
                ) + self.SEPARATOR_STRING
            string += "\n"
        return string

    def is_spot_within_range(self, spot: Spot) -> bool:
        return 0 <= spot.x < self.width and 0 <= spot.y < self.height
