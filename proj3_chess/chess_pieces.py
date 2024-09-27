from board import Board
from player import Player


class ChessPiece:

    def __init__(self, player: Player, board: Board, spot: tuple) -> None:
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

    def captures_piece(self, spot: tuple) -> bool:
        spot_state = self.board.board_state[spot[0]][spot[1]]
        return (
            False
            if (spot_state == None) or (spot_state.player == self.player)
            else True
        )


class Rook(ChessPiece):
    def available_moves(self) -> list:
        moves = []
        for x in [1, -1]:
            s = [self.spot[0] + x, self.spot[1]]
            while 0 <= s[0] < self.board.width and self.legal_move(s):
                moves.append((s[0], s[1], self.captures_piece(s)))
                if self.captures_piece(s):
                    break
                s[0] += x
        for y in [1, -1]:
            s = [self.spot[0], self.spot[1] + y]
            while 0 <= s[1] < self.board.height and self.legal_move(s):
                moves.append((s[0], s[1], self.captures_piece(s)))
                if self.captures_piece(s):
                    break
                s[1] += y
        return moves


class Bishop(ChessPiece):
    def available_moves(self) -> list:
        moves = []
        for x in [1, -1]:
            for y in [1, -1]:
                s = [self.spot[0] + x, self.spot[1] + y]
                while (
                    0 <= s[0] < self.board.width
                    and 0 <= s[1] < self.board.height
                    and self.legal_move(s)
                ):
                    moves.append((s[0], s[1], self.captures_piece(s)))
                    if self.captures_piece(s):
                        break
                    s[0] += x
                    s[1] += y
        return moves
