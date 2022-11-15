#!/usr/bin/env python3
from src.ParseInput import ParseInput


class Game:
    def __init__(self):
        self.parser = ParseInput()

    def run(self) -> int:
        self.parser.askInput()
        print(self.parser.getParsedInput())
        return 0
