#!/usr/bin/env python3
import random
from src.GomokuBoard import *
from src.ParseInput import ParseInput
from src.Globals import *
from src.utils.PrintGomoku import print_gomoku


class Game:
    def __init__(self):
        self.__started = True
        self.parser = ParseInput()
        self.__boardManager = GomokuBoard(20)
        self.command_map = {
            "BOARD": self.board_command,
            "START": self.start_command,
            "TURN": self.turn_command,
            "BEGIN": self.begin_command,
            "INFO": self.info_command,
            "END": self.end_command,
            "ABOUT": self.about_command
        }
        self.__boardSize = 20

    def __get_random_coords(self, max_value: int):
        rand_x = random.randrange(max_value)
        rand_y = random.randrange(max_value)
        while self.__boardManager.get_pawn(rand_x, rand_y) != pawnType.EMPTY:
            rand_x = random.randrange(max_value)
            rand_y = random.randrange(max_value)
        return rand_x, rand_y

    def check_win(self, pawn_type_to_check: pawnType) -> bool:
        def check_on_line(line_to_check: list[pawnType]) -> bool:
            nb: int = 0
            for char in line_to_check:
                if char == pawn_type_to_check:
                    nb += 1
                else:
                    nb = 0
                if nb == 5:
                    return True
            return False

        def check_on_column(y: int) -> bool:
            nb: int = 0
            for x in range(0, self.__boardSize - 1):
                if self.__boardManager.get_pawn(x, y) == pawn_type_to_check:
                    nb += 1
                else:
                    nb = 0
                if nb == 5:
                    return True
            return False

        def check_diagonal() -> bool:
            for i in range(self.__boardSize):
                for j in range(len(self.__boardManager.boardMap[i])):
                    if i + 4 < self.__boardSize and j + 4 < len(self.__boardManager.boardMap[i]):
                        if self.__boardManager.boardMap[i][j] == self.__boardManager.boardMap[i+1][j+1] == self.__boardManager.boardMap[i+2][j+2] == self.__boardManager.boardMap[i+3][j+3] == self.__boardManager.boardMap[i+4][j+4] == pawn_type_to_check:
                            return True
                    if i + 4 < self.__boardSize and j - 4 >= 0:
                        if self.__boardManager.boardMap[i][j] == self.__boardManager.boardMap[i+1][j-1] == self.__boardManager.boardMap[i+2][j-2] == self.__boardManager.boardMap[i+3][j-3] == self.__boardManager.boardMap[i+4][j-4] == pawn_type_to_check:
                            return True
            return False

        for line in self.__boardManager.boardMap:
            if check_on_line(line):
                return True
        for i in range(0, self.__boardSize - 1):
            if check_on_column(i):
                return True
        if check_diagonal():
            return True
        return False

    def run(self) -> int:
        while True:
            print_gomoku(self.__boardManager)
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
        self.__boardSize = board_size
        print_gomoku("OK - everything is good")
        self.__boardManager.reset_board(self.__boardSize)
        return True

    def turn_command(self) -> bool:
        try:
            parsed_args = self.parser.get_parsed_input()[1].split(",")
            if len(parsed_args) != 2:
                print_gomoku("ERROR message - Unauthorized move")
                return False
            for arg in parsed_args:
                if int(arg) >= self.__boardSize or int(arg) < 0:
                    print_gomoku(
                        "ERROR message - Unauthorized move (invalid position)")
                    return False
            print_gomoku("DEBUG message - Valid TURN command")
            if self.__boardManager.get_pawn(int(parsed_args[0]), int(parsed_args[1])) != pawnType.EMPTY:
                print_gomoku("ERROR message - This cell is already taken")
                return False
            else:
                self.__boardManager.add_manager_pawn(
                    int(parsed_args[0]), int(parsed_args[1]))
            if self.check_win(pawnType.MANAGER) == True:
                print_gomoku("Message message - You've win...")
                self.end_command()
            rand_x, rand_y = self.__get_random_coords(self.__boardSize - 1)
            print_gomoku(f'{rand_x},{rand_y}')
            self.__boardManager.add_brain_pawn(rand_x, rand_y)
            if self.check_win(pawnType.BRAIN) == True:
                print_gomoku("Message message - I've win !")
                self.end_command()
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
        rand_x, rand_y = self.__get_random_coords(self.__boardSize - 1)
        print_gomoku(f'{rand_x},{rand_y}')
        self.__boardManager.add_brain_pawn(rand_x, rand_y)
        print_gomoku("DEBUG message - Valid BEGIN command")
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
                if x < 0 or x >= self.__boardSize:
                    raise ValueError
                if y < 0 or y >= self.__boardSize:
                    raise ValueError
                if player not in [1, 2]:
                    raise ValueError
            except ValueError:
                print_gomoku("DEBUG Message - Failure on Board Input")
                return False
            if player == 1:
                self.__boardManager.add_brain_pawn(x, y)
            else:
                self.__boardManager.add_manager_pawn(x, y)
            print_gomoku("DEBUG Message - Succes on Board Input")
            return True

        while True:
            self.parser.ask_input()
            inpt = self.parser.get_parsed_input()
            if inpt[0] == "DONE":
                print_gomoku("DEBUG Message - Exit BOARD")
                break
            if not check_board_input(inpt):
                return False
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
        return self.__boardManager
