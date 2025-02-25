from dataclasses import dataclass


@dataclass(frozen=True)
class Tile:
    x: int
    y: int

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, tile: "Tile") -> bool:
        return self.x == tile.x and self.y == tile.y

    def __gt__(self, tile: "Tile") -> bool:
        """x value takes priority"""
        if self.x > tile.x:
            return True
        elif self.x == tile.x:
            if self.y > tile.y:
                return True

        return False

    def __ge__(self, tile: "Tile") -> bool:
        return self == tile or self > tile


Block = Tile  # TODO (but only after everything else is done): represent as ranges instead of single tiles, use sweepline alg (or an extension of it) for determining spot's validity


@dataclass(frozen=True)
class Block(Tile): ...


class Graph:
    def __init__(self, width, height, blocks: list[Block]) -> None:
        self.width = width
        self.height = height
        self.blocks = blocks.sort()

    def is_tile_on_board(self, tile: Tile) -> bool:
        return 0 <= tile.x < self.width and 0 <= tile.y < self.height

    def is_tile_not_blocked(self, tile: Block) -> bool:
        top_thresh = len(self.blocks)
        bottom_tresh = 0
        while top_thresh - bottom_tresh != 0:
            test_index = (bottom_tresh + top_thresh) // 2
            if self.blocks[test_index] == tile:
                bottom_tresh, top_thresh
