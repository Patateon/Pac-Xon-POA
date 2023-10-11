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
        self.game = game #De classe Grid

    def getCoord(self):
        return [self.x, self.y]
    
    def move(self, direction):
        currentX, currentY = self.x, self.y
        currentValue = self.game.getGrid().getValue(currentX, currentY)

        # C'est dégueu je sais, skill issue
        match direction:
            case Direction.UP:
                if (currentY != 0): # On vérifie si on ne va pas au dessus de la grille
                    nextX, nextY = currentX, currentY-1
                    nextValue = self.game.getGrid().getValue(nextX, nextY)
                    if (nextValue == 2):
                        self.game.getGrid().setValue(nextX, nextY, 3)
                    if nextValue != 1 or nextValue != 2:
                        self.y = nextY
                
            case Direction.RIGHT:
                if (currentX != self.game.getGrid().getSize()[0]): # On vérifie si on ne va pas à droite de la grille
                    nextX, nextY = currentX+1, currentY
                    nextValue = self.game.getGrid().getValue(nextX, nextY)
                    if (nextValue == 2):
                        self.game.getGrid().setValue(nextX, nextY, 3)
                    if nextValue != 1 or nextValue != 2:
                        self.x = nextX

            case Direction.DOWN:
                if (currentY != self.game.getGrid().getSize()[1]): # On vérifie si on ne va pas en dessous de la grille
                    nextX, nextY = currentX, currentY+1
                    nextValue = self.game.getGrid().getValue(nextX, nextY)
                    if (nextValue == 2):
                        self.game.getGrid().setValue(nextX, nextY, 3)
                    if nextValue != 1 or nextValue != 2:
                        self.y = nextY

            case Direction.LEFT:
                if (currentX != 0): # On vérifie si on ne va pas à gauche de la grille
                    nextX, nextY = currentX-1, currentY
                    nextValue = self.game.getGrid().getValue(nextX, nextY)
                    if (nextValue == 2):
                        self.game.getGrid().setValue(nextX, nextY, 3)
                    if nextValue != 1 or nextValue != 2:
                        self.x = nextX

            case _:
                pass


class PacMan:

    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.game = game


    def move(self, direction):
        currentX, currentY = self.x, self.y
        currentValue = self.game.getGrid().getValue(currentX, currentY)

        # C'est dégueu je sais, skill issue
        match direction:
            case Direction.LEFT:
                if (currentY != 0): # On vérifie si on ne va pas au dessus de la grille
                    nextX, nextY = currentX, currentY-1
                    self.y = nextY
                    nextValue = self.game.getGrid().getValue(nextX, nextY)
                    if (nextValue == 0):
                        self.game.getGrid().setValue(nextX, nextY, 2)
                    if (nextValue == 1 and currentValue == 2):
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
                    if (nextValue == 1 and currentValue == 2):
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
                    if (nextValue == 1 and currentValue == 2):
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
                    if (nextValue == 1 and currentValue == 2):
                        self.game.getGrid().setEndPath(True)
                        phantoms = self.game.getPhantom()
                        self.game.getGrid().update(phantoms[0].getCoord()[0], phantoms[0].getCoord()[1], phantoms[1].getCoord()[0], phantoms[1].getCoord()[1])

            case _:
                pass
            
class Ghost:

    def __init__(self, grid, direction):
        self.x
        self.y
        self.grid = grid
        self.direction = direction

    #UP-RIGHT = 0
    #DOWN-RIGHT = 1
    #DOWN-LEFT = 2
    #UP-LEFT = 3

    def move(self, direction):
        if (direction == 0 and self.y-1 == 0 and self.x+1 == 0):
            self.y = self.y - 1
        elif (direction == 1 and self.x+1 ==0 and self.y+1 == 0):
            self.x = self.x + 1
        elif (direction == 2 and self.y+1 == 0 and self.x-1 == 0):
            self.y = self.y + 1
        elif (direction == 3 and self.x-1 == 0 and self.y-1 == 0):
            self.x = self.x - 1
        elif (direction == 3):
            self.direction = 0
        else:
            self.direction = direction + 1