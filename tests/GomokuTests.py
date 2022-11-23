from tests.GomokuBoardTests import run_gomoku_board_tests
from tests.ParserTests import run_parser_tests
from tests.CheckWinTests import run_check_win_tests
from tests.CheckAlign import run_check_align_tests


def test_run():
    run_gomoku_board_tests()
    run_parser_tests()
    run_check_win_tests()
    run_check_align_tests()