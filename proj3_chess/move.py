class Move:
    CAPTURE_SYMBOL = "x"

    def __init__(self, piece_symbol: str, spot: tuple, does_capture_piece: bool):
        self.spot = spot
        self.does_capture_piece = does_capture_piece
        self.piece_symbol = piece_symbol  # TODO: does it make more sence to save a reference to the piece?

    def _convert_num_to_char(self, num: int):
        # TODO: figure how to represent board larger that 26
        return chr(num + 97)

    def __str__(self) -> str:
        piece = self.piece_symbol
        capture_indicator = self.CAPTURE_SYMBOL if self.does_capture_piece else ""
        column = self._convert_num_to_char(self.spot[0])
        row = self.spot[1]

        return f"{piece}{capture_indicator}{column}{row}"
