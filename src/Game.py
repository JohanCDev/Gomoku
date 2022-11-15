#!/usr/bin/env python3
from src.ParseInput import ParseInput


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

    def run(self) -> int:
        self.parser.askInput()
        try:
            self.command_map[self.parser.getParsedInput()[0]]()
        except KeyError:
            print("UNKNOWN message - command ", self.parser.getParsedInput()[0], "not existing.")
        return 0

    def start_command(self) -> bool:
        if self.parser.getParsedInput()[1] != 20:
            print("ERROR message - unsupported size or other error")
            return False
        # Create board
        print("OK - everything is good")
        return True

    def turn_command(self) -> bool:
        try:
            parsed_args = self.parser.getParsedInput()[1].split(",")
            if len(parsed_args) != 2:
                print("ERROR message - Unauthorized move")
                return False
            for arg in parsed_args:
                if int(arg) >= 20:
                    print("ERROR message - Unauthorized move (invalid position)")
                    return False
            print("DEBUG message - Valid TURN command")
            # Add movement to board
            # Launch AI reflexion
            # Place AI decision on board
            # Answer as pos_x,pos_y
        except IndexError:
            print("ERROR message - No movement was given")
            return False
        except ValueError:
            print("ERROR message - Position is not a number")
            return False
        return True

    def begin_command(self) -> bool:
        # Launch AI reflexion
        # Place AI decision on board
        # Answer as pos_x,pos_y
        print("DEBUG message - Valid BEGIN command")
        return True

    def board_command(self) -> bool:
        # TODO
        print("board")
        print(self.parser.getParsedInput())
        return True

    def info_command(self) -> bool:
        def handleTimeoutTurn(value: str | int):
            print("DEBUG message - TODO Change timeout turn to", value)

        def handleTimeoutMatch(value: str | int):
            print("DEBUG message - TODO Change timeout match to", value)

        def handleMaxMemory(value: str | int):
            print("DEBUG message - TODO Change max memory to", value)

        def handleTimeLeft(value: str | int):
            print("DEBUG message - TODO Change time left of the game to", value)

        def handlegameType(value: str | int):
            print("DEBUG message - TODO Change game type to", value)

        def handleRule(value: str | int):
            print("DEBUG message - TODO Change game rule to", value)

        def handleEvaluate(value: str | int):
            print("DEBUG message - TODO Evaluate ", value)

        def handleFolder(value: str | int):
            print("DEBUG message - TODO Change persistent files folder to", value)

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
            key_dict[self.parser.getParsedInput()[1]](self.parser.getParsedInput()[2])
        except IndexError:
            print("ERROR message - No key or no value was given")
            return False
        return True

    def end_command(self) -> bool:
        # Delete files and quit program
        return True

    def about_command(self) -> bool:
        print('name="Hugomoku", version="0.0.1", author="Nathan Rousseau, Johan Chrillesen, Guillaume Terrière", '
              'country="FR"')
        return True
