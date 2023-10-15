import numpy as np
from grid import *


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3 # cw

class Game:

    def __init__ (self, x, y, tr, nPhantom, phantomCoord):
        self.grid = Grid(x, y, tr)
        self.phantom = [None]*nPhantom
        self.nPhantom = nPhantom
        self.phantomCoord = phantomCoord
        self.pacman = PacMan(0, 0, self)

    def initGame(self):
        self.grid.initGrid()
        for i in range(self.nPhantom):
            self.phantom[i] = Phantom(self.phantomCoord[i][0], self.phantomCoord[i][1], self)

    def getGrid(self):
        return self.grid

    def getPhantom(self):
        return self.phantom

    def getPacman(self):
        return self.pacman


class Phantom:

    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.direction = Direction.LEFT
        self.game = game #De classe Grid

    def getCoord(self):
        return [self.x, self.y]

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def getDirection(self):
        return self.direction
    
    def move(self, rec=False):
        currentX, currentY = self.x, self.y
        currentValue = self.game.getGrid().getValue(currentX, currentY)
        direction = self.direction

        # C'est dégueu je sais, skill issue
        match direction:
            case Direction.LEFT: #up-right
                if (currentY != 0 and currentX != self.game.getGrid().getSize()[1]-1): # On vérifie si on ne va pas au dessus de la grille
                    nextX, nextY = currentX+1, currentY-1
                    nextValue = self.game.getGrid().getValue(nextX, nextY)
                    topValue, botValue = self.game.getGrid().getValue(currentX, currentY-1), self.game.getGrid().getValue(currentX+1, currentY)
                    if (nextValue == 2 and topValue !=2 and botValue !=2) :
                        self.game.getGrid().setValue(nextX, nextY, 3)
                    if (topValue == 2):
                        self.game.getGrid().setValue(currentX, currentY-1, 3)
                    if (botValue == 2):
                        self.game.getGrid().setValue(currentX+1, currentY, 3)
                    if nextValue == 0:
                        self.y = nextY
                        self.x = nextX
                    else:
                        self.direction = self.changeMove(direction, topValue, botValue)
                        if (not rec):
                            self.move(True)
                
            case Direction.DOWN: #down-right
                if (currentX != self.game.getGrid().getSize()[0]-1 and currentX != self.game.getGrid().getSize()[1]-1): # On vérifie si on ne va pas à droite de la grille
                    nextX, nextY = currentX+1, currentY+1
                    nextValue = self.game.getGrid().getValue(nextX, nextY)
                    topValue, botValue = self.game.getGrid().getValue(currentX, currentY+1), self.game.getGrid().getValue(currentX+1, currentY)
                    if (nextValue == 2 and topValue !=2 and botValue !=2) :
                        self.game.getGrid().setValue(nextX, nextY, 3)
                    if (topValue == 2):
                        self.game.getGrid().setValue(currentX, currentY+1, 3)
                    if (botValue == 2):
                        self.game.getGrid().setValue(currentX+1, currentY, 3)
                    if nextValue == 0:
                        self.y = nextY
                        self.x = nextX
                    else:
                        self.direction = self.changeMove(direction, topValue, botValue)
                        if (not rec):
                            self.move(True)

            case Direction.RIGHT: #down-left
                if (currentY != self.game.getGrid().getSize()[1]-1 and currentX != 0): # On vérifie si on ne va pas en dessous de la grille
                    nextX, nextY = currentX-1, currentY+1
                    nextValue = self.game.getGrid().getValue(nextX, nextY)
                    topValue, botValue = self.game.getGrid().getValue(currentX, currentY+1), self.game.getGrid().getValue(currentX-1, currentY)
                    if (nextValue == 2 and topValue !=2 and botValue !=2) :
                        self.game.getGrid().setValue(nextX, nextY, 3)
                    if (topValue == 2):
                        self.game.getGrid().setValue(currentX, currentY+1, 3)
                    if (botValue == 2):
                        self.game.getGrid().setValue(currentX-1, currentY, 3)
                    if nextValue == 0:
                        self.y = nextY
                        self.x = nextX
                    else:
                        self.direction = self.changeMove(direction, topValue, botValue)
                        if (not rec):
                            self.move(True)

            case Direction.UP: #up-left
                if (currentX != 0 and currentX != 0): # On vérifie si on ne va pas à gauche de la grille
                    nextX, nextY = currentX-1, currentY-1
                    nextValue = self.game.getGrid().getValue(nextX, nextY)
                    topValue, botValue = self.game.getGrid().getValue(currentX, currentY-1), self.game.getGrid().getValue(currentX-1, currentY)
                    if (nextValue == 2 and topValue !=2 and botValue !=2) :
                        self.game.getGrid().setValue(nextX, nextY, 3)
                    if (topValue == 2):
                        self.game.getGrid().setValue(currentX, currentY-1, 3)
                    if (botValue == 2):
                        self.game.getGrid().setValue(currentX-1, currentY, 3)
                    if nextValue == 0:
                        self.y = nextY
                        self.x = nextX
                    else:
                        self.direction = self.changeMove(direction, topValue, botValue)
                        if (not rec):
                            self.move(True)

            case _:
                pass
    
    def changeMove(self, direction, topValue, botValue):
        match direction:
            case Direction.LEFT:
                if (topValue != 0 and botValue != 0):
                    return Direction.RIGHT
                elif (topValue != 0):
                    return Direction.DOWN
                else:
                    return Direction.UP
            case Direction.DOWN:
                if (topValue != 0 and botValue != 0):
                    return Direction.UP
                elif (topValue != 0):
                    return Direction.LEFT
                else:
                    return Direction.RIGHT
            case Direction.RIGHT:
                if (topValue != 0 and botValue != 0):
                    return Direction.LEFT
                elif (topValue != 0):
                    return Direction.UP
                else:
                    return Direction.DOWN
            case Direction.UP:
                if (topValue != 0 and botValue != 0):
                    return Direction.DOWN
                elif (topValue != 0):
                    return Direction.RIGHT
                else:
                    return Direction.LEFT
            case _:
                pass



class PacMan:

    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.game = game

    def getCoord(self):
        return (self.x, self.y)


    def move(self, direction):
        currentX, currentY = self.x, self.y
        currentValue = self.game.getGrid().getValue(currentX, currentY)
        nextValue = 0

        # C'est dégueu je sais, skill issue
        match direction:
            case Direction.LEFT:
                if (currentY != 0): # On vérifie si on ne va pas au dessus de la grille
                    nextX, nextY = currentX, currentY-1
                    self.y = nextY
                    nextValue = self.game.getGrid().getValue(nextX, nextY)
                    if (nextValue == 0):
                        self.game.getGrid().setValue(nextX, nextY, 2)
                    if (nextValue == 1 and currentValue != 1):
                        self.game.getGrid().setEndPath(True)
                        phantoms = self.game.getPhantom()
                        self.game.getGrid().update(phantoms[0].getCoord()[0], phantoms[0].getCoord()[1], phantoms[1].getCoord()[0], phantoms[1].getCoord()[1])
                
            case Direction.DOWN:
                if (currentX != self.game.getGrid().getSize()[0]-1): # On vérifie si on ne va pas à droite de la grille
                    nextX, nextY = currentX+1, currentY
                    self.x = nextX
                    nextValue = self.game.getGrid().getValue(nextX, nextY)
                    if (nextValue == 0):
                        self.game.getGrid().setValue(nextX, nextY, 2)
                    if (nextValue == 1 and currentValue != 1):
                        self.game.getGrid().setEndPath(True)
                        phantoms = self.game.getPhantom()
                        self.game.getGrid().update(phantoms[0].getCoord()[0], phantoms[0].getCoord()[1], phantoms[1].getCoord()[0], phantoms[1].getCoord()[1])

            case Direction.RIGHT:
                if (currentY != self.game.getGrid().getSize()[1]-1): # On vérifie si on ne va pas en dessous de la grille
                    nextX, nextY = currentX, currentY+1
                    self.y = nextY
                    nextValue = self.game.getGrid().getValue(nextX, nextY)
                    if (nextValue == 0):
                        self.game.getGrid().setValue(nextX, nextY, 2)
                    if (nextValue == 1 and currentValue != 1):
                        self.game.getGrid().setEndPath(True)
                        phantoms = self.game.getPhantom()
                        self.game.getGrid().update(phantoms[0].getCoord()[0], phantoms[0].getCoord()[1], phantoms[1].getCoord()[0], phantoms[1].getCoord()[1])

            case Direction.UP:
                if (currentX != 0): # On vérifie si on ne va pas à gauche de la grille
                    nextX, nextY = currentX-1, currentY
                    self.x = nextX
                    nextValue = self.game.getGrid().getValue(nextX, nextY)
                    if (nextValue == 0):
                        self.game.getGrid().setValue(nextX, nextY, 2)
                    if (nextValue == 1 and currentValue != 1):
                        self.game.getGrid().setEndPath(True)
                        phantoms = self.game.getPhantom()
                        self.game.getGrid().update(phantoms[0].getCoord()[0], phantoms[0].getCoord()[1], phantoms[1].getCoord()[0], phantoms[1].getCoord()[1])

            case _:
                pass

            
        if (nextValue == 2):
            self.game.getGrid().setEndGame(True)

    def is_propagated(self):
        if (self.game.getGrid().getValue(self.x, self.y) == 3):
            self.game.getGrid().setEndGame(True)

            