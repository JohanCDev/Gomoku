from src.GomokuBoard import pawnType
from src.GomokuBoard import *
from src.utils.PrintGomoku import print_gomoku
import random


PAWN_DOWN = True
PAWN_UP = False

WIN = 5
NAIVE = 4
EXPLORE = 3

NONE = -1
COLUMN = 1
LINE = 2
DIAGONAL_LEFT = 3
DIAGONAL_RIGHT = 4


class Brain:

    def __init__(self, boardSize):
        self.board = GomokuBoard(boardSize)
        self.boardSize = boardSize

    def __check_lines(self, nb_align, line_to_check, searched_pawn_type):
        tmp_first: int = -1
        first_nb: int = -1
        second_nb: int = 0
        first: int = 0
        empty_cell: int = -1
        y: int = 0
        for y in range(0, len(line_to_check)):
            if line_to_check[y] == searched_pawn_type:
                if first_nb == 0:
                    first = y
                if first_nb == -1:
                    first_nb += 2
                elif first_nb != 0:
                    first_nb += 1
                else:
                    second_nb += 1
            else:
                tmp_first = first_nb
                first_nb = -1
                empty_cell = y
            if tmp_first + second_nb + 1 == nb_align:
                return True, empty_cell
            if first_nb == nb_align and nb_align == WIN:
                return True, 0
            elif first_nb == nb_align:
                rightFree = True
                leftFree = True
                if y + 1 < len(line_to_check):
                    if line_to_check[y + 1] != searched_pawn_type and line_to_check[y + 1] != pawnType.EMPTY:
                        rightFree = False
                if first - 1 >= 0:
                    if line_to_check[first - 1] != searched_pawn_type and line_to_check[first - 1] != pawnType.EMPTY:
                        leftFree = False
                if rightFree and not (y + 1 == len(line_to_check)):
                    return True, y + 1
                elif leftFree and not (first - 1 < 0):
                    return True, first - 1
                else:
                    first_nb = 0
            y += 1
        return False, -1

    def __check_columns(self, nb_align, colums_to_check, searched_pawn_type):
        nb: int = 0
        first : int = 0
        x : int = 0
        for x in range(0, len(colums_to_check)):
            if colums_to_check[x] == searched_pawn_type:
                if nb == 0:
                    first = x
                nb += 1
            else:
                nb = 0
            if nb == nb_align and nb_align == WIN:
                return True, 0
            elif nb == nb_align:
                rightFree = True
                leftFree = True
                if x + 1 < len(colums_to_check):
                    if colums_to_check[x + 1] != searched_pawn_type and colums_to_check[x + 1] != pawnType.EMPTY:
                        rightFree = False
                if first - 1 >= 0:
                    if colums_to_check[first - 1] != searched_pawn_type and colums_to_check[first - 1] != pawnType.EMPTY:
                        leftFree = False
                if rightFree and not (x + 1 == len(colums_to_check)):
                    return True, x + 1
                elif leftFree and not (first - 1 < 0):
                    return True, first - 1
                else:
                    nb = 0
            x += 1
        return False, -1

    def __check_diagonals(self, nb_align, searched_pawn_type):
        RIGHT = 1
        LEFT = -1

        def check_one_diagonal(i, j, direct: int) -> bool:
            nb = 0
            x = 0
            y = 0
            for k in range(0, nb_align):
                if self.board.boardMap[i + k][j + (k * direct)] == searched_pawn_type:
                    nb += 1
                else:
                    if self.board.boardMap[i + k][j + (k * direct)] == pawnType.EMPTY:
                        x = i + k
                        y = j + (k * direct)
            return nb + 1 == nb_align or nb == nb_align, x, y

        for i in range(self.boardSize):
            for j in range(len(self.board.boardMap[i])):
                if i + (nb_align - 1) < self.boardSize and j + (nb_align - 1) < len(self.board.boardMap[i]):
                    found, x, y = check_one_diagonal(i, j, RIGHT)
                    if found:
                        return DIAGONAL_RIGHT, x, y
                if i + (nb_align - 1) < self.boardSize and j - (nb_align - 1) >= 0:
                    found, x, y = check_one_diagonal(i, j, LEFT)
                    if found:
                        return DIAGONAL_LEFT, x, y
        return NONE, -1, -1

    def __check_align(self, nb_align: int, pawn_type_to_check: pawnType):

        # def check_on_column(y: int):
        #     nb: int = 0
        #     for x in range(0, self.__boardSize - 1):
        #         if self.__boardManager.get_pawn(x, y) == pawn_type_to_check:
        #             nb += 1
        #         else:
        #             nb = 0
        #         if nb == nb_alignn:
        #             return True, x
        #     return False, -1

        x = 0
        for line in self.board.boardMap:
            found, y = self.__check_lines(nb_align, line, pawn_type_to_check)
            if found:
                return LINE, x, y
            column = self.board.get_column(x)
            found, y = self.__check_lines(nb_align, column, pawn_type_to_check)
            if found:
                return COLUMN, y, x
            x += 1
        found, x, y = self.__check_diagonals(nb_align, pawn_type_to_check)
        if found != NONE:
            return found, x, y
        return NONE, -1, -1


    def __get_random_coords(self, max_value: int):
        rand_x = random.randrange(max_value)
        rand_y = random.randrange(max_value)
        while self.board.get_pawn(rand_x, rand_y) != pawnType.EMPTY:
            rand_x = random.randrange(max_value)
            rand_y = random.randrange(max_value)
        return rand_x, rand_y

    def __naive_thinking(self):
        aligned, x, y = self.__check_align(NAIVE, pawnType.BRAIN)
        if aligned != NONE:
            return PAWN_DOWN, x, y

        aligned, x, y = self.__check_align(NAIVE, pawnType.MANAGER)
        if aligned != NONE:
            return PAWN_DOWN, x, y
        return PAWN_UP, -1, -1

    def check_win(self, pawn_type_to_check: pawnType) -> bool:
        res, _, _ = self.__check_align(WIN, pawn_type_to_check)
        return res != NONE

    def act(self, force_random: bool = False):
        x = 0
        y = 0
        if force_random:
            x, y = self.__get_random_coords(self.boardSize - 1)
            while self.board.get_pawn(x, y) != pawnType.EMPTY:
                x, y = self.__get_random_coords(self.boardSize - 1)
            self.board.add_brain_pawn(x, y)
            return x, y
        else:
            action, x, y = self.__naive_thinking()
            if action == PAWN_UP:
                self.act(True)
            else:
                self.board.add_brain_pawn(x, y)
                return x, y
