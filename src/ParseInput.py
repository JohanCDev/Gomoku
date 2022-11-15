#!/usr/bin/env python3

class ParseInput:
    def __init__(self):
        self.__input = ""
        self.__parsedInput = []

    def askInput(self):
        self.__input = input()

    def parseInput(self):
        self.__parsedInput = self.__input.rstrip().split(" ")

    def getInput(self):
        return self.__input

    def getParsedInput(self) -> list:
        return self.__parsedInput
