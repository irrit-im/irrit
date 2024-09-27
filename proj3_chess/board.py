class Board:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.board_state = [[None] * self.height for i in range(self.width)]
