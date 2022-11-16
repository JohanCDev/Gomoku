# CELL TYPE
EMPTY = 0
BRAIN = 1
OPPONENT = 2

# DIRECTIONS
NORTH = 0
NORTHEAST = 1
EAST = 2
SOUTHEAST = 3
SOUTH = 4
SOUTHWEST = 5
WEST = 6
NORTHWEST = 7

# BOARD
BOARD: list[list[int]] = []


def INITBOARD(size: int) -> None:
    for i in range(0, size):
        for j in range(0, size):
            BOARD[i][j] = EMPTY
