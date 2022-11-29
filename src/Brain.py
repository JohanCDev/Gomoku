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

TWO_PAWN_WIN = 1000000000

def evaluate_board(board : GomokuBoard, team : pawnType, enemy : pawnType) -> int:

    def check_explore():
        def explore_two_pawn_win(line) -> bool:
            if line.count(enemy) == 0 and line.count(team) == 3 and line[-1] == pawnType.EMPTY:
                for z in range(len(line)):
                    if line[z] == pawnType.EMPTY:
                        return True, z
            return False, -1
        
        for y in range(board.get_board_size()):
            for x in range(board.get_board_size()):
                cell = board.get_pawn(x, y)
                if cell == pawnType.EMPTY:
                    try:
                        line = []
                        for i in range(5):
                            line.append(board.get_pawn(x + i + 1, y))
                        can_win, z = explore_two_pawn_win(line)
                        if can_win:
                            return TWO_PAWN_WIN, y, x + z + 1
                    except:
                        pass
                    try:
                        column = []
                        for i in range(5):
                            column.append(board.get_pawn(x, y + i + 1))
                        can_win, z =  explore_two_pawn_win(column)
                        if can_win:
                            return TWO_PAWN_WIN, y + z + 1, x
                    except:
                        pass
                    try:
                        right_diago = []
                        for i in range(5):
                            right_diago.append(board.get_pawn(x + i + 1, y + i + 1))
                        can_win, z =  explore_two_pawn_win(right_diago)
                        if can_win:
                            return TWO_PAWN_WIN, y + z + 1, x + z + 1
                    except:
                        pass
                    try:
                        left_diago = []
                        for i in range(5):
                            left_diago.append(board.get_pawn(x + i + 1, y - i - 1))
                        can_win, z =  explore_two_pawn_win(left_diago)
                        if can_win:
                            return TWO_PAWN_WIN, y - z - 1, x + z + 1
                    except:
                        pass
        return 0, -1, -1

    score, y, x = check_explore()
    if score == TWO_PAWN_WIN:
        return score, y, x
    score = 0
    return score, -1, -1


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
        cols, rows = self.board.get_cols_rows()
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
        def get_rows(grid):
            return [[c for c in r] for r in grid]

        def get_cols(grid):
            return zip(*grid)

        def get_backward_diagonals(grid):
            b = [None] * (len(grid) - 1)
            grid = [b[i:] + r + b[:i] for i, r in enumerate(get_rows(grid))]
            return [[c for c in r if c is not None] for r in get_cols(grid)]

        def get_forward_diagonals(grid):
            b = [None] * (len(grid) - 1)
            grid = [b[:i] + r + b[i:] for i, r in enumerate(get_rows(grid))]
            return [[c for c in r if c is not None] for r in get_cols(grid)]

        pos = []
        for i in range(self.boardSize - 1, -1, -1):
            pos.append((0, i))
        for i in range(1, self.boardSize):
            pos.append((i, 0))
        for diag in get_backward_diagonals(self.board.boardMap):
            found, y = self.__check_lines(nb_align, diag, pawn_type_to_check)
            if found:
                return DIAGONAL_RIGHT, pos[x][0] + y, pos[x][1] + y
            x += 1
        x = 0
        pos.clear()
        for i in range(0, self.boardSize - 1):
            pos.append((i, 0))
        for i in range(0, self.boardSize):
            pos.append((self.boardSize - 1, i))
        for diag in get_forward_diagonals(self.board.boardMap):
            found, y = self.__check_lines(nb_align, diag, pawn_type_to_check)
            if found:
                return DIAGONAL_LEFT, pos[x][0] - y, pos[x][1] + y
            x += 1
        return NONE, -1, -1

    def __get_random_coords(self, max_value: int):
        pawns_list: list[tuple[int, int]] = []
        directions = {
            0: (-1, -1),
            1: (0, -1),
            2: (1, -1),
            3: (1, 0),
            4: (1, 1),
            5: (0, 1),
            6: (-1, 1),
            7: (-1, 0)
        }
        for y in range(self.boardSize - 1):
            for x in range(self.boardSize - 1):
                if self.board.get_pawn(x, y) == pawnType.BRAIN:
                    pawns_list.append((x, y))
        if len(pawns_list) == 0:
            rand_x = random.randrange(self.boardSize - 1)
            rand_y = random.randrange(self.boardSize - 1)
            while self.board.get_pawn(rand_x, rand_y) != pawnType.EMPTY:
                rand_x = random.randrange(self.boardSize - 1)
                rand_y = random.randrange(self.boardSize - 1)
            return rand_x, rand_y
        while True:
            list_rand = random.randrange(len(pawns_list))
            selected_pawn = pawns_list[list_rand]
            dir_rand = random.randrange(8)
            try:
                if self.board.get_pawn(selected_pawn[0] + directions[dir_rand][0],
                                       selected_pawn[1] + directions[dir_rand][1]) == pawnType.EMPTY:
                    return selected_pawn[0] + directions[dir_rand][0], selected_pawn[1] + directions[dir_rand][1]
            except RuntimeError:
                continue

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
            # newBoardTest = self.board.new(self.board.boardMap, x, y, pawnType.MANAGER)
            # print_gomoku("DEBUG TEST BOARD\n", newBoardTest)
            self.board.add_brain_pawn(x, y)
        else:
            action, x, y = self.__naive_thinking()
            if action == PAWN_UP:
                ### EXPLORE ###
                score, y, x = evaluate_board(self.board, pawnType.BRAIN, pawnType.MANAGER)
                if score == TWO_PAWN_WIN:
                    self.board.add_brain_pawn(x, y)
                    return
                score, y, x = evaluate_board(self.board, pawnType.MANAGER, pawnType.BRAIN)
                if score == TWO_PAWN_WIN:
                    self.board.add_brain_pawn(x, y)
                    return
                ### EXPLORE ###
                self.act(True)
            else:
                self.board.add_brain_pawn(x, y)

    def call_naive(self):
        """ Only for tests """
        return self.__naive_thinking()
