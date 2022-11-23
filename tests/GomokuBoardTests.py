from src.GomokuBoard import *


def run_gomoku_board_tests():
    test_board_init()
    test_add_pawn()
    test_reset_board()


def test_board_init():
    firstBoard = GomokuBoard(10)
    try:
        secondBoard = GomokuBoard(4)
    except RuntimeError:
        pass
    assert firstBoard.get_board_size() == 10


def test_add_pawn():
    board = GomokuBoard(5)
    board.add_brain_pawn(1, 1)
    try:
        board.add_manager_pawn(5, 5)
    except RuntimeError:
        pass
    assert board.get_pawn(1, 1) is pawnType.BRAIN

def test_reset_board():
    board = GomokuBoard(5)
    board.add_brain_pawn(1, 1)
    board.reset_board()
    for line in board.boardMap:
        for cell in line:
            assert cell is pawnType.EMPTY