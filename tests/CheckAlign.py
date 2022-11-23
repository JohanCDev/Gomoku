#!/usr/bin/env python3
from src.Game import Game
from src.GomokuBoard import pawnType


def run_check_align_tests():
    test_basic_diagonal_win_situation()
    test_basic_diagonal_left_win_situation()
    test_basic_line_win_situation()
    test_basic_col_win_situation()


def test_basic_diagonal_win_situation():
    game = Game()
    game.get_board_manager().reset_board(5)
    game.get_board_manager().boardMap = [
        [pawnType.BRAIN, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.BRAIN, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.BRAIN,
            pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.BRAIN, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY],
    ]
    game.get_brain().boardSize = 5
    game.get_board_manager().__boardSize = 5
    move, x, y = game.get_brain().call_naive()
    assert move == True and x == 4 and y == 4


def test_basic_diagonal_left_win_situation():
    game = Game()
    game.get_board_manager().reset_board(5)
    game.get_board_manager().boardMap = [
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.BRAIN],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.BRAIN, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.BRAIN, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.BRAIN, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
    ]
    game.get_brain().boardSize = 5
    game.get_board_manager().__boardSize = 5
    move, x, y = game.get_brain().call_naive()
    assert move == True and x == 3 and y == 1


def test_basic_line_win_situation():
    game = Game()
    game.get_board_manager().reset_board(5)
    game.get_board_manager().boardMap = [
        [pawnType.BRAIN, pawnType.EMPTY, pawnType.BRAIN, pawnType.BRAIN, pawnType.BRAIN],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.BRAIN, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.BRAIN, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
    ]
    game.get_brain().boardSize = 5
    game.get_board_manager().__boardSize = 5
    move, x, y = game.get_brain().call_naive()
    assert move == True and x == 0 and y == 1


def test_basic_col_win_situation():
    game = Game()
    game.get_board_manager().reset_board(5)
    game.get_board_manager().boardMap = [
        [pawnType.BRAIN, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.BRAIN],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.BRAIN, pawnType.EMPTY],
        [pawnType.BRAIN, pawnType.EMPTY, pawnType.BRAIN, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.BRAIN, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.BRAIN, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
    ]
    game.get_brain().boardSize = 5
    game.get_board_manager().__boardSize = 5
    move, x, y = game.get_brain().call_naive()
    assert move == True and x == 1 and y == 0
