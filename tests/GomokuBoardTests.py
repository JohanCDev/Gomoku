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
    assert firstBoard.getBoardSize() is 10


def test_add_pawn():
    board = GomokuBoard(5)
    board.addBrainPawn(1, 1)
    try:
        board.addManagerPawn(5, 5)
    except RuntimeError:
        pass
    assert board.getPawn(1, 1) == pawnType.BRAIN

def test_reset_board():
    board = GomokuBoard(5)
    board.addBrainPawn(1, 1)
    board.resetBoard()
    for line in board.boardMap:
        for cell in line:
            assert cell is pawnType.EMPTY