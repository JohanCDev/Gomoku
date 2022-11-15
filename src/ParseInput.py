#!/usr/bin/env python3

class ParseInput:
    def __init__(self):
        self.input = ""
        self.parsedInput = []

    def askInput(self):
        self.input = input()

    def parseInput(self):
        self.parsedInput = self.input.rstrip().split(" ")

    def getInput(self):
        return self.input

    def getParsedInput(self) -> list:
        return self.parsedInput
