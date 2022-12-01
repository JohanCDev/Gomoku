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

SCORE_NOT_CALCULATED = "-1"

def evaluate_explore(board : GomokuBoard, team : pawnType, enemy : pawnType) -> int:

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

def get_score(to_evaluate : GomokuBoard, team : pawnType, enemy : pawnType) -> int:
    def near_wall(value):
        if value < 5 or value > 15:
            return True
        return False
    
    def score_line(pawn, x, y):
        nb_max_align = 3
        try:
            line = []
            for i in range(nb_max_align):
                line.append(to_evaluate.get_pawn(x + i, y))
            if line.count(pawn) == nb_max_align:
                if near_wall(x):
                    return 30
                else:
                    return 75
            else:
                raise
        except:
            nb_max_align -= 1
            line.clear()
        try:
            for i in range(nb_max_align):
                line.append(to_evaluate.get_pawn(x + i, y))
            if line.count(pawn) == nb_max_align:
                if near_wall(x):
                    return 7
                else:
                    return 20
            else:
                raise
        except:
            return 1

    def score_column(pawn, x, y):
        nb_max_align = 3
        try:
            line = []
            for i in range(nb_max_align):
                line.append(to_evaluate.get_pawn(x, y + i))
            if line.count(pawn) == nb_max_align:
                if near_wall(y):
                    return 30
                else:
                    return 75
            else:
                raise
        except:
            nb_max_align -= 1
            line.clear()
        try:
            for i in range(nb_max_align):
                line.append(to_evaluate.get_pawn(x, y + i))
            if line.count(pawn) == nb_max_align:
                if near_wall(y):
                    return 7
                else:
                    return 20
            else:
                raise
        except:
            return 1

    def score_r_diago(pawn, x, y):
        nb_max_align = 3
        try:
            line = []
            for i in range(nb_max_align):
                line.append(to_evaluate.get_pawn(x + i, y + i))
            if line.count(pawn) == nb_max_align:
                if near_wall(x) or near_wall(y):
                    return 50
                else:
                    return 125
            else:
                raise
        except:
            nb_max_align -= 1
            line.clear()
        try:
            for i in range(nb_max_align):
                line.append(to_evaluate.get_pawn(x + i, y + i))
            if line.count(pawn) == nb_max_align:
                if near_wall(x) or near_wall(y):
                    return 13
                else:
                    return 40
            else:
                raise
        except:
            return 1

    def score_l_diago(pawn, x, y):
        nb_max_align = 3
        try:
            line = []
            for i in range(nb_max_align):
                line.append(to_evaluate.get_pawn(x - i, y + i))
            if line.count(pawn) == nb_max_align:
                if near_wall(x) or near_wall(y):
                    return 50
                else:
                    return 125
            else:
                raise
        except:
            nb_max_align -= 1
            line.clear()
        try:
            for i in range(nb_max_align):
                line.append(to_evaluate.get_pawn(x - i, y + i))
            if line.count(pawn) == nb_max_align:
                if near_wall(x) or near_wall(y):
                    return 13
                else:
                    return 40
            else:
                raise
        except:
            return 1

    score : int = 0
    size : int = to_evaluate.get_board_size()
    for y in range(size):
        for x in range(size):
            cell = to_evaluate.get_pawn(x, y)
            if cell == team:
                score += score_line(team, x, y)
                score += score_column(team, x, y)
                score += score_r_diago(team, x, y)
                score += score_l_diago(team, x, y)
            elif cell == enemy:
                score -= score_line(enemy, x, y)
                score -= score_column(enemy, x, y)
                score -= score_r_diago(enemy, x, y)
                score -= score_l_diago(enemy, x, y)

    return score

def add_and_duplicate(boardToCopy : GomokuBoard, i : int, j : int, pawn : pawnType, toEvaluate : bool = False):
    score = SCORE_NOT_CALCULATED
    size = boardToCopy.get_board_size()
    newBoard = GomokuBoard(size)

    for y in range(size):
        for x in range(size):
            newBoard.duplicate_pawn(x, y, boardToCopy.get_pawn(x, y))

    newBoard.duplicate_pawn(i, j, pawn)

    if toEvaluate:
        if pawn == pawnType.BRAIN:
            enemy = pawnType.MANAGER
        else:
            enemy = pawnType.BRAIN
        score = get_score(newBoard, pawn, enemy)
    return newBoard, score

def random_pawn_for_board(a_board : GomokuBoard, type_of_pawn : pawnType):
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
    size = a_board.get_board_size()
    for y in range(size):
        for x in range(size):
            if a_board.get_pawn(x, y) == type_of_pawn:
                pawns_list.append((x, y))
    if len(pawns_list) == 0:
        rand_x = random.randrange(size)
        rand_y = random.randrange(size)
        while a_board.get_pawn(rand_x, rand_y) != pawnType.EMPTY:
            rand_x = random.randrange(size)
            rand_y = random.randrange(size)
        return rand_x, rand_y
    while True:
        list_rand = random.randrange(len(pawns_list))
        selected_pawn = pawns_list[list_rand]
        dir_rand = random.randrange(8)
        try:
            if a_board.get_pawn(selected_pawn[0] + directions[dir_rand][0],
                                    selected_pawn[1] + directions[dir_rand][1]) == pawnType.EMPTY:
                return selected_pawn[0] + directions[dir_rand][0], selected_pawn[1] + directions[dir_rand][1]
        except RuntimeError:
            continue

def min_max(originBoard, currdepth : int = 0, board_list = [], type : pawnType = pawnType.BRAIN):
    BRANCHES = 4
    DEPTH = 4
    needEval : bool = False
    new_board_list = []

    if currdepth == DEPTH:
        needEval = True

    if len(board_list) == 0:
        for _ in range(BRANCHES):
            x, y = random_pawn_for_board(originBoard, type)
            newBoard, score = add_and_duplicate(originBoard, x, y, type, needEval)
            new_board_list.append((newBoard, score, x, y))
    else:
        for old in board_list:
            for _ in range(BRANCHES):
                x, y = random_pawn_for_board(old[0], type)
                i, j = old[2], old[3]
                newBoard, score = add_and_duplicate(old[0], x, y, type, needEval)
                new_board_list.append((newBoard, score, i, j))

    if needEval:
        highest_board = None
        for b in new_board_list:
            if highest_board is None:
                highest_board = b
            elif highest_board[1] < b[1]:
                highest_board = b
        return highest_board[2], highest_board[3]
    else:
        if type == pawnType.BRAIN:
            type = pawnType.MANAGER
        else:
            type = pawnType.BRAIN
        return min_max(originBoard, currdepth + 1, new_board_list, type)

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
            x, y = min_max(self.board)
            self.board.add_brain_pawn(x, y)
        else:
            action, x, y = self.__naive_thinking()
            if action == PAWN_UP:
                ### EXPLORE ###
                score, y, x = evaluate_explore(self.board, pawnType.BRAIN, pawnType.MANAGER)
                if score == TWO_PAWN_WIN:
                    self.board.add_brain_pawn(x, y)
                    return
                score, y, x = evaluate_explore(self.board, pawnType.MANAGER, pawnType.BRAIN)
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
