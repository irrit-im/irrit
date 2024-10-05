from player import Player


class Board:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.board_state = [[None] * self.height for i in range(self.width)]

    def within_range(self, spot: tuple) -> bool:
        return 0 <= spot[0] < self.width and 0 <= spot[1] < self.height

    def print(self):
        for line in self.board_state:
            print("|", end="")
            for spot in line:
                print(spot.name if spot else "  ", end=" | ")
            print("")
