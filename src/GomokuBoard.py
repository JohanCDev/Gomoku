""" Enumeration of all the differents types of possible pawn on the board"""
from enum import Enum
from src.utils.PrintGomoku import print_gomoku
from sys import platform

class pawnType(Enum):
    EMPTY = 0
    BRAIN = 1
    MANAGER = 2


class GomokuBoard:
    """ Class Constructor, taking a board Size for the Game"""

    def __init__(self, boardSize):
        if boardSize < 5:
            raise RuntimeError("The given value can't be a Gomoku board size")
        self.__boardSize = boardSize
        self.boardMap = [[]]
        self.reset_board()

    def __check_pos(self, x: int, y: int) -> bool:
        """ Private Method, useful to check if the given coordinates are allowed """
        if x >= self.__boardSize or x < 0:
            return False
        if y >= self.__boardSize or y < 0:
            return False
        return True

    def __is_empty(self, x: int, y: int) -> bool:
        """ Private Method, check if the pawn on the given coordinates is empty """
        if not self.__check_pos(x, y):
            return False
        if self.boardMap[y][x] != pawnType.EMPTY:
            return False
        return True

    def __add_pawn(self, x: int, y: int, type):
        """ Add a pawn at the given coordinates """
        if not self.__check_pos(x, y):
            raise RuntimeError('Invalid Coordinate')
        if not self.__is_empty(x, y):
            raise RuntimeError('Cell is not empty')
        self.boardMap[y][x] = type

    def duplicate_pawn(self, x, y, type):
        """ TO USE ONLY IN ADD AND DUPLICATE """
        self.__add_pawn(x, y, type)

    def add_brain_pawn(self, x: int, y: int, display=True):
        """ Add a Brain Pawn at the given coordinates """
        self.__add_pawn(x, y, pawnType.BRAIN)
        if display:
            print_gomoku(f"{x},{y}")

    def add_manager_pawn(self, x: int, y: int):
        """ Add a Manager Pawn at the given coordinates"""
        self.__add_pawn(x, y, pawnType.MANAGER)

    def reset_board(self, boardSize: int = -1):
        """ Reset completly the board, setting all the cells to empty state """
        if boardSize == -1:
            boardSize = self.__boardSize
        self.__boardSize = boardSize
        self.boardMap = [[pawnType.EMPTY] *
                         boardSize for i in range(boardSize)]

    def get_pawn(self, x: int, y: int):
        """ Get the Pawn at the given coordinates """
        if not self.__check_pos(x, y):
            raise RuntimeError("The pawn can't be get with the given coordinates")
        return self.boardMap[y][x]

    def get_board_size(self) -> int:
        """ Get the Board Size """
        return self.__boardSize


    def get_cols_rows(self):
        """ Get all the diagonals"""
        max_col = len(self.boardMap[0])
        max_row = len(self.boardMap)
        cols = [[] for _ in range(max_col)]
        rows = [[] for _ in range(max_row)]
        for x in range(max_col):
            for y in range(max_row):
                cols[x].append(self.boardMap[x][y])
                rows[y].append(self.boardMap[x][y])
        return cols, rows

    def get_reverse_diagonal(self, x: int, y: int) -> list:
        """ Get the reverse diagonal of the given coordinates """
        if not self.__check_pos(x, y):
            return RuntimeError("The pawn can't be get with the given coordinates")
        diagonal = []
        for i in range(0, self.__boardSize):
            diagonal.append(self.boardMap[i][self.__boardSize - i - 1])
        return diagonal

    def __str__(self):
        BLUE = ''
        RED = ''
        WHITE = ''
        if platform == "linux" or platform == "linux2" or platform == "darwin":
            BLUE = '\033[94m'
            RED = "\033[1;31;40m"
            WHITE = "\033[0;37;40m"
        elif platform == "win32":
            pass

        """ Pass the board as string to be displayed """
        toPrint: str = f"DEBUG - Current board (size {self.__boardSize}):\n"
        toPrint += "DEBUG - 0 is Empty / 1 is Brain / 2 is Manager\n"
        for lines in self.boardMap:
            toPrint += 'DEBUG - '
            for cell in lines:
                value: str = f'[{cell.value}]' + WHITE
                if cell == pawnType.BRAIN:
                    value = RED + value
                if cell == pawnType.MANAGER:
                    value = BLUE + value
                toPrint += f'{value}'
            toPrint += '\n'
        toPrint = toPrint[:-1]
        return toPrint
