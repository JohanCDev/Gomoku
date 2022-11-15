#!/usr/bin/env python3
from src.ParseInput import ParseInput


class Game:
    def __init__(self):
        self.parser = ParseInput()

    def run(self) -> int:
        while 1:
            self.parser.askInput()
            self.parser.parseInput()
            print(self.parser.getParsedInput())
            break
        return 0
