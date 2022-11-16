#!/usr/bin/env python3
from enum import Enum

""" Enumeration of all the differents types of possible pawn on the board"""
class pawnType(Enum):
    EMPTY = 0
    BRAIN = 1
    MANAGER = 2

class GomokuBoard:
    """ Class Constructor, taking a board Size for the Game"""
    def __init__(self, boardSize):
        if boardSize < 5:
            raise RuntimeError("The given value can't be a Gomoku board size")
        self.__boardSize = boardSize
        self.boardMap = [[pawnType]]
        self.resetBoard()

    def __checkPos(self, x : int, y : int) -> bool:
        """ Private Method, useful to check if the given coordinates are allowed """
        if x >= self.__boardSize or x < 0:
            return False
        if y >= self.__boardSize or y < 0:
            return False
        return True

    def __isEmpty(self, x : int, y : int) -> bool:
        """ Private Method, check if the pawn on the given coordinates is empty """
        if not self.__checkPos(x, y):
            return False
        if self.boardMap[x][y] != pawnType.EMPTY:
            return False
        return True

    def __addPawn(self, x : int, y : int, type : pawnType):
        """ Add a pawn at the given coordinates """
        if not self.__checkPos(x, y):
            return
        if not self.__isEmpty(x, y):
            return
        self.boardMap[x][y] = type

    def addBrainPawn(self, x : int, y : int):
        """ Add a Brain Pawn at the given coordinates """
        self.__addPawn(x, y, pawnType.BRAIN)

    def addManagerPawn(self, x : int, y : int):
        """ Add a Manager Pawn at the given coordinates"""
        self.__addPawn(x, y, pawnType.MANAGER)

    def resetBoard(self, boardSize : int = -1):
        if boardSize == -1:
            boardSize = self.__boardSize
        boardRow = [pawnType.EMPTY] * boardSize
        self.boardMap = boardRow * boardSize

    def getPawn(self, x : int, y :int) -> pawnType:
        if not self.__checkPos(x, y):
            #RAISE QQ CHOSE#
            return RuntimeError("The pawn can't be get with the given coordinates")
        return self.boardMap[x][y]