class Player:
    def __init__(self, direction: int, color: str) -> None:
        """This class represents a player in a chess game. \n
        direction (int): the direction in which the pieces move - either 1 or -1 \n
        color (function): a string function that recieves no arguments and returns a string. this will be the graphichal representation for the pieces. example: passig the function upper means the players pieces will be sybmolized by capital letters.
        """
        self.direction = direction
        self.color = color
