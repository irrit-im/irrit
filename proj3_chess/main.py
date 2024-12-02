from tests import generate_random_board, create_default_players

MIN_BOARD_SIZE = 2
MAX_BOARD_SIZE = 5

white, black = create_default_players()
board = generate_random_board(MIN_BOARD_SIZE, MAX_BOARD_SIZE, white, black)


def main():
    print(board)
    for row in board.state:
        for spot in row:
            if spot:
                print(f"\n{spot.symbol} at {spot.get_spot()}:  ", end="")
                for i in spot.get_available_moves():
                    print(i, end=" , ")


if __name__ == "__main__":
    main()
