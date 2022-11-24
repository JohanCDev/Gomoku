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
        nb: int = 0
        coord: int = -1
        for x in range(0, len(line_to_check) - 4):
            aligns = line_to_check[x:x + 5]
            coord = -1
            for i in range(0, len(aligns)):
                if aligns[i] == searched_pawn_type:
                    nb += 1
                elif aligns[i] == pawnType.EMPTY:
                    coord = i + x
                else:
                    nb = 0
            if nb == WIN:
                return True, coord
            elif nb == nb_align and coord != -1:
                return True, coord
            nb = 0
        return False, -1

    def __check_align(self, nb_align: int, pawn_type_to_check: pawnType):
        x = 0
        cols, rows, fdiag, bdiag = self.board.get_cols_rows_diags()
        for col in cols:
            found, y = self.__check_lines(nb_align, col, pawn_type_to_check)
            if found:
                return COLUMN, y, x
            x += 1
        x = 0
        for row in rows:
            found, y = self.__check_lines(nb_align, row, pawn_type_to_check)
            if found:
                return LINE, x, y
            x += 1
        x = 0
        for diag in fdiag:
            found, y = self.__check_lines(nb_align, diag, pawn_type_to_check)
            if found:
                if x < 19:
                    return DIAGONAL_LEFT, 9 - x + y - 1, y
                else:
                    return DIAGONAL_LEFT, y + 7, x - 20 + y + 1
            x += 1
        x = 0
        for diag in bdiag:
            found, y = self.__check_lines(nb_align, diag, pawn_type_to_check)
            if found:
                if x < 19:
                    return DIAGONAL_RIGHT, y + 1, 19 - x + y - 1 # not yet tested
                else:
                    return DIAGONAL_RIGHT, x - 20 + y + 1, y
            x += 1
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

    def call_naive(self):
        """ Only for tests """
        return self.__naive_thinking()
