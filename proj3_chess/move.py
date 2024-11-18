# TODO: rename file
from pydantic import BaseModel


class MoveVector(BaseModel):
    x: int
    y: int


class Spot(BaseModel):  # TODO: constraint this to non-negative nums
    x: int
    y: int

    def __str__(self) -> str:
        convert_num_to_char = lambda num: chr(
            num + 97
        )  # TODO: what about boards larger than 26?
        return convert_num_to_char(self.x) + str(self.y)

    def __add__(self, vector: MoveVector) -> "Spot":
        if not isinstance(vector, MoveVector):
            raise TypeError("Can only add a Spot and a MoveVector.")
        return Spot(x=self.x + vector.x, y=self.y + vector.y)


class Move(BaseModel):
    destination: Spot
    does_capture_piece: bool
    piece_symbol: str  # TODO: does it make more sence to save a reference to the piece?

    CAPTURE_SYMBOL: str = "x"

    def __str__(self) -> str:
        capture_indicator = self.CAPTURE_SYMBOL if self.does_capture_piece else ""

        return self.piece_symbol + capture_indicator + str(self.destination)
