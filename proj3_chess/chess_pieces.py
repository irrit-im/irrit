from board import Board
from player import Player


class ChessPiece:

    def __init__(self, player: Player, board: Board, spot: list) -> None:
        # TODO: raise error if spot is already taken or is outside of range
        self.player = player
        self.board = board
        self.spot = spot
        self.board.board_state[spot[0]][spot[1]] = self

    def available_moves(self) -> list:
        pass

    def legal_move(self, spot: tuple) -> bool:
        spot_state = self.board.board_state[spot[0]][spot[1]]
        return True if spot_state == None else spot_state.player != self.player

    def captures_piece(self, spot: tuple) -> bool:  # TODO: rename
        spot_state = self.board.board_state[spot[0]][spot[1]]  # TODO: rename
        return (
            False
            if (spot_state == None) or (spot_state.player == self.player)
            else True
        )


class Rook(ChessPiece):
    def available_moves(self) -> list:  # check if legal, if a piece is taken
        moves = []  # TODO: think - represent moves as tuples or objs?
        for x in range(self.board.width):
            s = (x, self.spot[1])
            if x != self.spot[0] and self.legal_move(s):
                moves.append((s[0], s[1], self.captures_piece(s)))
        for y in range(self.board.height):
            s = (self.spot[0], y)
            if y != self.spot[1] and self.legal_move(s):
                moves.append((s[0], s[1], self.captures_piece(s)))
        return moves
