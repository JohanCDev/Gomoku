#!/usr/bin/env python3
from src.GomokuBoard import *
from src.ParseInput import ParseInput
from src.Globals import *
from src.utils.PrintGomoku import print_gomoku


class Game:
    def __init__(self):
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
        self.__boardSize = 0
        self.__started: bool = False

    def __check_win(self, pawnTypeToCheck: pawnType) -> bool:
        def check_on_line(lineToCheck: list[pawnType]) -> bool:
            nb: int = 0
            for char in lineToCheck:
                if char == pawnTypeToCheck:
                    nb += 1
                else:
                    nb = 0
                if nb == 5:
                    return True
            return False

        def check_on_column(y: int) -> bool:
            nb: int = 0
            for x in range(0, self.__boardSize - 1):
                if self.__boardManager.getPawn(x, y) == pawnTypeToCheck:
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
                        if self.__boardManager.boardMap[i][j] == self.__boardManager.boardMap[i+1][j+1] == self.__boardManager.boardMap[i+2][j+2] == self.__boardManager.boardMap[i+3][j+3] == self.__boardManager.boardMap[i+4][j+4] == pawnTypeToCheck:
                            return True
                    if i + 4 < self.__boardSize and j - 4 >= 0:
                        if self.__boardManager.boardMap[i][j] == self.__boardManager.boardMap[i+1][j-1] == self.__boardManager.boardMap[i+2][j-2] == self.__boardManager.boardMap[i+3][j-3] == self.__boardManager.boardMap[i+4][j-4] == pawnTypeToCheck:
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
            try:
                self.parser.askInput()
            except EOFError:
                print_gomoku('EOFError')
                break
            except KeyboardInterrupt:
                print_gomoku('KeyboardInterrupt')
                break
            try:
                if self.parser.getParsedInput()[0] != "START" and not self.__started:
                    print_gomoku(
                        "DEBUG message - Please start the game with START command")
                    continue
                self.command_map[self.parser.getParsedInput()[0]]()
            except KeyError:
                print_gomoku("UNKNOWN message - command ",
                             self.parser.getParsedInput()[0], "not existing.")

        return 0

    def start_command(self) -> bool:
        boardSize: int = -1
        try:
            if len(self.parser.getParsedInput()) != 2:
                raise ValueError
            boardSize = int(self.parser.getParsedInput()[1])
            if boardSize < 5:
                raise ValueError
        except ValueError:
            print_gomoku("ERROR message - unsupported size or other error")
            return False
        # Create board
        self.__boardSize = boardSize
        print_gomoku("OK - everything is good")
        self.__started = True
        return True

    def turn_command(self) -> bool:
        try:
            parsed_args = self.parser.getParsedInput()[1].split(",")
            if len(parsed_args) != 2:
                print_gomoku("ERROR message - Unauthorized move")
                return False
            for arg in parsed_args:
                if int(arg) >= self.__boardSize or int(arg) < 0:
                    print_gomoku(
                        "ERROR message - Unauthorized move (invalid position)")
                    return False
            print_gomoku("DEBUG message - Valid TURN command")
            # Add movement to board
            # Launch AI reflexion
            # Place AI decision on board
            # Answer as pos_x,pos_y
        except IndexError:
            print_gomoku("ERROR message - No movement was given")
            return False
        except ValueError:
            print_gomoku("ERROR message - Position is not a number")
            return False
        print_gomoku(f'{self.__boardSize - 3},{self.__boardSize - 2}')
        return True

    def begin_command(self) -> bool:
        # Launch AI reflexion
        # Place AI decision on board
        # Answer as pos_x,pos_y
        print_gomoku(f'{self.__boardSize - 3},{self.__boardSize - 2}')
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
            print_gomoku("DEBUG Message - Succes on Board Input")
            return True

        while True:
            self.parser.askInput()
            inpt = self.parser.getParsedInput()
            if inpt[0] == "DONE":
                print_gomoku("DEBUG Message - Exit BOARD")
                break
            if not check_board_input(inpt):
                return False
        return True

    def info_command(self) -> bool:
        def handleTimeoutTurn(value: str or int):
            print_gomoku("DEBUG message - TODO Change timeout turn to", value)

        def handleTimeoutMatch(value: str or int):
            print_gomoku("DEBUG message - TODO Change timeout match to", value)

        def handleMaxMemory(value: str or int):
            print_gomoku("DEBUG message - TODO Change max memory to", value)

        def handleTimeLeft(value: str or int):
            print_gomoku(
                "DEBUG message - TODO Change time left of the game to", value)

        def handlegameType(value: str or int):
            print_gomoku("DEBUG message - TODO Change game type to", value)

        def handleRule(value: str or int):
            print_gomoku("DEBUG message - TODO Change game rule to", value)

        def handleEvaluate(value: str or int):
            print_gomoku("DEBUG message - TODO Evaluate ", value)

        def handleFolder(value: str or int):
            print_gomoku(
                "DEBUG message - TODO Change persistent files folder to", value)

        key_dict = {
            "timeout_turn": handleTimeoutTurn,
            "timeout_match": handleTimeoutMatch,
            "max_memory": handleMaxMemory,
            "time_left": handleTimeLeft,
            "game_type": handlegameType,
            "rule": handleRule,
            "evaluate": handleEvaluate,
            "folder": handleFolder
        }

        try:
            key_dict[self.parser.getParsedInput()[1]](
                self.parser.getParsedInput()[2])
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
