#!/usr/bin/env python3


def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys    # for linux/unix
        import termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


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

        try:
            self.__input = input()
            self.__parsedInput = self.__input.rstrip().split(" ")
        except (EOFError, KeyboardInterrupt):
            # See what to do in this case
            pass

    def getInput(self) -> str:
        """Get the value of the previous input

        Returns
        ----------
        str
            Previous input
        """

        return self.__input

    def getParsedInput(self) -> list:
        """Get the input parsed in a list of strings.

        Returns
        ----------
        list
            List of strings being the input parsed by spaces
        """

        return self.__parsedInput

    def setInput(self, value: str) -> None:
        """Function made for tests. It will allow us to not use the input() function.

        Parameters
        ----------
        value: str
            The new value of input
        """

        self.__input = value
        self.__parsedInput = self.__input.rstrip().split(" ")
