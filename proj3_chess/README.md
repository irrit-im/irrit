# Chess Implementation

This is a Python implementation of a chess game. It includes the ability to generate random game boards with pieces placed in random spots, and to calculate and display available moves for each piece.

## Features

- **Chess Pieces**: Supports chess pieces like Rooks, Bishops, Knights, Queens, Kings, and Pawns.
- **Board Generation**: Automatically generates random chess boards with dimensions specified by the user (the board dosn't have to be the traditional 8x8 board!).
- **Available Moves**: For each piece, the program calculates and displays available legal moves based on the piece's (simplified) rules and its current position. 
- **Piece Movement**: Each piece can move according to its unique set of rules (e.g., Rooks move in straight lines, Knights in an "L" shape).

## Structure

### `board.py`

Defines the `Board` class, which represents the chessboard. It handles the board's size, the pieces on it, and some basic board operations such as checking if a spot is within the board's range.

### `piece_properties.py`

Contains definitions related to players, such as their direction of movement on the board and how their symbols are represented.

### `chess_pieces.py`

Defines the abstract `ChessPiece` class and the specific chess pieces that inherit from it (e.g., `Rook`, `Knight`, `Bishop`, `Queen`, `King`, `Pawn`). Each piece class includes the logic for calculating its available moves based on its unique movement rules. The movement for each piece is implemented using vectors, and the logic accounts for the board's constraints and the legality of each move.

### `move.py`

Defines helper classes such as `MoveVector` and `Spot` to represent positions and movement vectors on the board. This file also includes the `Move` class that captures information about a move, including whether it involves capturing an opponent's piece.


### `setup_utils.py`

Contains utility functions that simplify game setup, including `generate_random_board()` for creating a random board in a random size with pieces placed in random spots, and `create_default_players()` to initialize the default players with their respective properties.


### `getting_player_moves.py`

Contains the main execution logic. This file generates a random board, populates it with pieces, and prints the board along with available moves for each piece. 
















~~Slight chance Chat GPT wrote this - don't compliment me~~