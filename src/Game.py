#!/usr/bin/env python3
from src.ParseInput import ParseInput
import src.utils
import src.values


class Game:
    def __init__(self):
        self.parser = ParseInput()
        src.utils.limitMemory(src.values.maxMemory)

    def run(self) -> int:
        self.parser.askInput()
        print(self.parser.getParsedInput())
        return 0
