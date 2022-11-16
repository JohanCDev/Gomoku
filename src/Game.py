#!/usr/bin/env python3
from src.ParseInput import ParseInput


class Game:
    def __init__(self):
        self.parser = ParseInput()

    def run(self) -> int:
        try:
            self.parser.askInput()
        except EOFError:
            print('EOFError')
        except KeyboardInterrupt:
            print('KeyboardInterrupt')
        print(self.parser.getParsedInput())
        return 0
