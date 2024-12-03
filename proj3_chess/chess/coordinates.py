from pydantic import BaseModel


class MoveVector(BaseModel):
    x: int
    y: int

    def __mul__(self, vector: "MoveVector"):
        return MoveVector(x=self.x * vector.x, y=self.y * vector.y)


MV = MoveVector


def convert_num_to_str(num):
    text = ""
    if num > 25:
        text += convert_num_to_str(num // 26)
        print("hi")
    text += chr(num % 26 + 97)
    return text


class Spot(BaseModel):
    x: int
    y: int

    def __str__(self) -> str:
        return convert_num_to_str(self.x) + str(self.y)

    def __add__(self, vector: MoveVector) -> "Spot":
        if not isinstance(vector, MoveVector):
            raise TypeError("Can only add a Spot and a MoveVector.")
        return Spot(x=self.x + vector.x, y=self.y + vector.y)


class Move(BaseModel):
    destination: Spot
    does_capture_piece: bool
    piece_symbol: str

    CAPTURE_SYMBOL: str = "x"

    def __str__(self) -> str:
        capture_indicator = self.CAPTURE_SYMBOL if self.does_capture_piece else ""

        return self.piece_symbol + capture_indicator + str(self.destination)
