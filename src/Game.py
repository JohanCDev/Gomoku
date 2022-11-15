#!/usr/bin/env python3
from src.ParseInput import ParseInput


class Game:
    def __init__(self):
        self.parser = ParseInput()

    def run(self) -> int:
        try:
            self.parser.askInput()
        except EOFError:
            print('Hello user it is EOF exception, please enter something and run me again')
        except KeyboardInterrupt:
            print('Hello user you have pressed ctrl-c button.')
        print(self.parser.getParsedInput())
        return 0
