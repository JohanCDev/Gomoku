#!/usr/bin/env python3
from src.Game import Game
from src.GomokuBoard import pawnType


def run_check_win_tests():
    test_basic_diagonal_win()
    test_basic_line_win()
    test_basic_col_win()
    test_huge_diagonal_win()
    test_huge_line_win()
    test_huge_col_win()


def test_basic_diagonal_win():
    game = Game()
    game.get_board_manager().reset_board(20)
    game.get_board_manager().boardMap[0][0] = pawnType.BRAIN
    game.get_board_manager().boardMap[1][1] = pawnType.BRAIN
    game.get_board_manager().boardMap[2][2] = pawnType.BRAIN
    game.get_board_manager().boardMap[3][3] = pawnType.BRAIN
    game.get_board_manager().boardMap[4][4] = pawnType.BRAIN
    game.get_brain().boardSize = 20
    assert game.get_brain().check_win(pawnType.BRAIN) == True, game.get_brain().check_win(
        pawnType.MANAGER) == False


def test_basic_line_win():
    game = Game()
    game.get_board_manager().reset_board(5)
    game.get_board_manager().boardMap = [
        [pawnType.BRAIN, pawnType.BRAIN, pawnType.BRAIN,
            pawnType.BRAIN, pawnType.BRAIN],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.BRAIN,
            pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.BRAIN, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.BRAIN],
    ]
    game.get_brain().boardSize = 5
    game.get_board_manager().__boardSize = 5
    assert game.get_brain().check_win(pawnType.BRAIN) == True, game.get_brain().check_win(
        pawnType.MANAGER) == False

def test_basic_col_win():
    game = Game()
    game.get_board_manager().reset_board(5)
    game.get_board_manager().boardMap = [
        [pawnType.BRAIN, pawnType.EMPTY, pawnType.BRAIN,
            pawnType.BRAIN, pawnType.BRAIN],
        [pawnType.BRAIN, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.BRAIN, pawnType.EMPTY, pawnType.BRAIN,
            pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.BRAIN, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.BRAIN, pawnType.EMPTY],
        [pawnType.BRAIN, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.BRAIN],
    ]
    game.get_brain().boardSize = 5
    game.get_board_manager().__boardSize = 5
    assert game.get_brain().check_win(pawnType.BRAIN) == True, game.get_brain().check_win(
        pawnType.MANAGER) == False


def test_huge_col_win():
    game = Game()
    game.get_board_manager().reset_board(10)
    game.get_board_manager().boardMap = [
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.BRAIN,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.BRAIN,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.BRAIN,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.BRAIN,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.BRAIN,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
    ]
    game.get_brain().boardSize = 10
    game.get_board_manager().__boardSize = 10
    assert game.get_brain().check_win(pawnType.BRAIN) == True, game.get_brain().check_win(
        pawnType.MANAGER) == False


def test_huge_line_win():
    game = Game()
    game.get_board_manager().reset_board(10)
    game.get_board_manager().boardMap = [
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.BRAIN, pawnType.BRAIN,
            pawnType.BRAIN, pawnType.BRAIN, pawnType.BRAIN, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
    ]
    game.get_brain().boardSize = 10
    game.get_board_manager().__boardSize = 10
    assert game.get_brain().check_win(pawnType.BRAIN) == True, game.get_brain().check_win(
        pawnType.MANAGER) == False


def test_huge_diagonal_win():
    game = Game()
    game.get_board_manager().reset_board(10)
    game.get_board_manager().boardMap = [
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.BRAIN, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.BRAIN,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.BRAIN, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.BRAIN, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.BRAIN, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
        [pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY,
            pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY, pawnType.EMPTY],
    ]
    game.get_brain().boardSize = 10
    game.get_board_manager().__boardSize = 10
    assert game.get_brain().check_win(pawnType.BRAIN) == True, game.get_brain().check_win(
        pawnType.MANAGER) == False
