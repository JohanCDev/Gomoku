#!/usr/bin/env python3

class ParseInput:
    """ParseInput class

    Class that will ask the user what move he will make. It will automatically parse it to create a list of strings
    """

    def __init__(self):
        """Initialize the class to have an empty string and an empty array"""

        self.__input: str = ""
        self.__parsedInput: list = []

    def askInput(self) -> None:
        """Ask the user its input, it will be parsed in this function"""

        self.__input = input()
        self.__parsedInput = self.__input.rstrip().split(" ")

    def getInput(self) -> str:
        """Get the value of the previous input"""

        return self.__input

    def getParsedInput(self) -> list:
        """Get the input parsed in a list of strings"""

        return self.__parsedInput

    def setInput(self, value: str) -> None:
        """Function made for tests. It will allow us to not use the input() function."""

        self.__input = value
        self.__parsedInput = self.__input.rstrip().split(" ")
