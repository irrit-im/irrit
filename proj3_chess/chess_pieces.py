from board import Board
from player import Player


class ChessPiece:
    """Mother class for all chess pieces."""

    piece_name = ""

    def __init__(self, player: Player, board: Board, spot: tuple) -> None:
        # TODO: raise error if spot is already taken
        self.player = player
        self.player.pieces.append(self)  # add the piece to the player
        self.name = player.symbol(self.piece_name)
        self.board = board
        self.spot = spot
        self.board.board_state[spot[0]][spot[1]] = self  # add the piece to the board

    def legal_move(self, spot: tuple) -> bool:
        """Recieves a spot on the board, and checks if it's not already occupied by a piece of the same color."""
        spot_state = self.board.board_state[spot[0]][spot[1]]
        return True if spot_state == None or spot_state.player != self.player else False

    def captures_piece(self, spot: tuple) -> bool:
        """Recieves a spot on the board, and checks if it is occupied by an opponent's piece."""
        spot_state = self.board.board_state[spot[0]][spot[1]]
        return (
            False
            if (spot_state == None) or (spot_state.player == self.player)
            else True
        )

    def available_moves(self) -> list:
        """Returns a list of all moves available for the piece."""
        print("'available_moves()' should be overritten by child classes")


class Rook(ChessPiece):
    piece_name = "R"

    def available_moves(self) -> list:
        moves = []
        for x in (1, -1):
            s = (self.spot[0] + x, self.spot[1])
            while self.board.within_range(s) and self.legal_move(s):
                moves.append((s, self.captures_piece(s)))
                if self.captures_piece(s):
                    break
                s = (s[0] + x, s[1])
        for y in (1, -1):
            s = (self.spot[0], self.spot[1] + y)
            while self.board.within_range(s) and self.legal_move(s):
                moves.append((s, self.captures_piece(s)))
                if self.captures_piece(s):
                    break
                s = (s[0], s[1] + y)
        return moves


class Bishop(ChessPiece):
    piece_name = "B"

    def available_moves(self) -> list:
        moves = []
        for x in (1, -1):
            for y in (1, -1):
                s = (self.spot[0] + x, self.spot[1] + y)
                while self.board.within_range(s) and self.legal_move(s):
                    moves.append((s, self.captures_piece(s)))
                    if self.captures_piece(s):
                        break
                    s = (s[0] + x, s[1] + y)
        return moves


class Queen(Rook, Bishop):
    piece_name = "Q"

    def available_moves(self) -> list:
        return Bishop.available_moves(self) + Rook.available_moves(self)


class King(ChessPiece):
    piece_name = "K"

    def available_moves(self) -> list:
        moves = []
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                s = (self.spot[0] + x, self.spot[1] + y)
                if self.board.within_range(s) and s != self.spot and self.legal_move(s):
                    moves.append((s, self.captures_piece(s)))
        return moves


class Knight(ChessPiece):
    piece_name = "N"

    def available_moves(self) -> list:
        moves = []
        for x in (-1, 1):
            for y in (-1, 1):
                for m in ((1, 2), (2, 1)):
                    s = (self.spot[0] + m[0] * x, self.spot[1] + m[1] * y)
                    if self.board.within_range(s) and self.legal_move(s):
                        moves.append((s, self.captures_piece(s)))
        return moves


class Pawn(ChessPiece):
    piece_name = "P"

    def available_moves(self) -> list:
        moves = []
        s = (self.spot[0], self.spot[1] + self.player.direction)
        if (
            self.board.within_range(s)
            and self.legal_move(s)
            and not self.captures_piece(s)
        ):
            moves.append((s, False))
        for i in (-1, 1):
            s = (self.spot[0] + i, self.spot[1] + self.player.direction)
            if (
                self.board.within_range(s)
                and self.legal_move(s)
                and self.captures_piece(s)
            ):
                moves.append((s, True))
        return moves
