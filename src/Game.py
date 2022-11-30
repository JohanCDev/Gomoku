#!/usr/bin/env python3
from src.GomokuBoard import *
from src.ParseInput import ParseInput
from src.Globals import *
from src.utils.PrintGomoku import print_gomoku
from src.Brain import Brain


class Game:
    def __init__(self):
        self.parser = ParseInput()
        self.command_map = {
            "BOARD": self.board_command,
            "START": self.start_command,
            "TURN": self.turn_command,
            "BEGIN": self.begin_command,
            "INFO": self.info_command,
            "END": self.end_command,
            "ABOUT": self.about_command
        }
        self.__brain = Brain(20)

    def run(self) -> int:
        while True:
            self.parser.ask_input()
            try:
                self.command_map[self.parser.get_parsed_input()[0]]()
            except KeyError:
                print_gomoku("UNKNOWN message - command ",
                             self.parser.get_parsed_input()[0], "not existing.")

    def start_command(self) -> bool:
        board_size: int = -1
        try:
            if len(self.parser.get_parsed_input()) != 2:
                raise ValueError
            board_size = int(self.parser.get_parsed_input()[1])
            if board_size < 5:
                raise ValueError
        except ValueError:
            print_gomoku("ERROR message - unsupported size or other error")
            return False
        self.__brain.boardSize = board_size
        print_gomoku("OK")
        self.__brain.board.reset_board(self.__brain.boardSize)
        return True

    def turn_command(self) -> bool:
        try:
            """ Error Handling of Turn Command """
            parsed_args = self.parser.get_parsed_input()[1].split(",")
            if len(parsed_args) != 2:
                print_gomoku("ERROR message - Unauthorized move")
                return False
            for arg in parsed_args:
                if int(arg) >= self.__brain.boardSize or int(arg) < 0:
                    print_gomoku(
                        "ERROR message - Unauthorized move (invalid position)")
                    return False
            if self.__brain.board.get_pawn(int(parsed_args[0]), int(parsed_args[1])) != pawnType.EMPTY:
                print_gomoku("ERROR message - This cell is already taken")
                return False
            else:
                self.__brain.board.add_manager_pawn(
                    int(parsed_args[0]), int(parsed_args[1]))

            if self.__brain.check_win(pawnType.MANAGER):
                print_gomoku("DEBUG - You've win...")

            self.__brain.act()

            if self.__brain.check_win(pawnType.BRAIN):
                print_gomoku("DEBUG - I've win !!")

        except IndexError:
            print_gomoku("ERROR message - No movement was given")
            return False
        except ValueError:
            print_gomoku("ERROR message - Position is not a number")
            return False
        except RuntimeError:
            print_gomoku("ERROR message - Runtime error of getPawn")
            return False
        return True

    def begin_command(self) -> bool:
        self.__brain.board.add_brain_pawn(
            int(self.__brain.boardSize / 2), int(self.__brain.boardSize / 2))
        return True

    def board_command(self) -> bool:

        def check_board_input(inpt):
            pawnPos = inpt[0].split(',')
            try:
                if len(pawnPos) != 3:
                    print_gomoku(pawnPos)
                    raise ValueError
                x = int(pawnPos[0])
                y = int(pawnPos[1])
                player = int(pawnPos[2])
                if x < 0 or x >= self.__brain.boardSize:
                    raise ValueError
                if y < 0 or y >= self.__brain.boardSize:
                    raise ValueError
                if player not in [1, 2]:
                    raise ValueError
            except ValueError:
                print_gomoku("DEBUG Message - Failure on Board Input")
                return False
            if player == 1:
                self.__brain.board.add_brain_pawn(x, y, False)
            else:
                self.__brain.board.add_manager_pawn(x, y)
            return True

        while True:
            self.parser.ask_input()
            inpt = self.parser.get_parsed_input()
            if inpt[0] == "DONE":
                break
            if not check_board_input(inpt):
                return False
        self.__brain.act()
        if self.__brain.check_win(pawnType.BRAIN):
            print_gomoku("DEBUG message - I've win !!")
        return True

    def info_command(self) -> bool:
        def handle_timeout_turn(value: str or int):
            print_gomoku("DEBUG message - TODO Change timeout turn to", value)

        def handle_timeout_match(value: str or int):
            print_gomoku("DEBUG message - TODO Change timeout match to", value)

        def handle_max_memory(value: str or int):
            print_gomoku("DEBUG message - TODO Change max memory to", value)

        def handle_time_left(value: str or int):
            print_gomoku(
                "DEBUG message - TODO Change time left of the game to", value)

        def handle_game_type(value: str or int):
            print_gomoku("DEBUG message - TODO Change game type to", value)

        def handle_rule(value: str or int):
            print_gomoku("DEBUG message - TODO Change game rule to", value)

        def handle_evaluate(value: str or int):
            print_gomoku("DEBUG message - TODO Evaluate ", value)

        def handle_folder(value: str or int):
            print_gomoku(
                "DEBUG message - TODO Change persistent files folder to", value)

        key_dict = {
            "timeout_turn": handle_timeout_turn,
            "timeout_match": handle_timeout_match,
            "max_memory": handle_max_memory,
            "time_left": handle_time_left,
            "game_type": handle_game_type,
            "rule": handle_rule,
            "evaluate": handle_evaluate,
            "folder": handle_folder
        }

        try:
            key_dict[self.parser.get_parsed_input()[1]](
                self.parser.get_parsed_input()[2])
        except IndexError:
            print_gomoku("ERROR message - No key or no value was given")
            return False
        return True

    def end_command(self) -> bool:
        exit(0)

    def about_command(self) -> bool:
        print_gomoku('name="{}", version="{}", author="{}", '
                     'country="{}"'.format(brainName, version, authors, country))
        return True

    def get_board_manager(self):
        return self.__brain.board

    """ ONLY FOR TESTS"""

    def get_brain(self):
        return self.__brain

    def print_board(self):
        print_gomoku(self.__brain.board)
