class Board:
    EMPTY_TILE_STRING = "  "
    SEPARATOR_STRING = " | "

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.board_state = [[None] * self.height for i in range(self.width)]

    def __str__(self) -> str:
        string = ""
        for line in self.board_state:
            string += self.SEPARATOR_STRING
            for spot in line:
                string += (
                    spot.name if spot else self.EMPTY_TILE_STRING
                ) + self.SEPARATOR_STRING
            string += "\n"
        return string

    def is_spot_within_range(self, spot: tuple) -> bool:
        return 0 <= spot[0] < self.width and 0 <= spot[1] < self.height
