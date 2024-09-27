class Player:
    def __init__(self, direction: int, symbol) -> None:  # TODO: type hint symbol
        """This class represents a player in a chess game. \n
        direction (int): the direction in which the pieces move - either 1 or -1 \n
        symbol (function): a string function that recieves a string and returns a string. this will be the graphichal representation for the pieces. example: passig the function upper means the players pieces will be sybmolized by capital letters.
        """
        self.direction = direction
        self.symbol = symbol
        self.pieces = []

    def all_available_moves(self):
        moves = []
        for i in self.pieces:
            # print(i.name, i.available_moves())
            moves.append((i.name, i.available_moves()))
        return moves
