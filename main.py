import numpy as np
from enum import Enum

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3 # cw

class Grid:

    # 0 = case vide
    # 1 = case pleine
    # 2 = case en construction
    # 3 = case corrompue

    def __init__(self, nX, nY):
        self.nX = nX
        self.nY = nY
        self.grid = np.arange(nX*nY, dtype=np.int16).reshape(nX, nY)

    def getValue(self, x, y):
        return self.grid[x, y]

    def setValue(self, x, y, v):
        self.grid[x, y] = v

class Pacman:

    def __init__(self, grid):
        self.x = 0
        self.y = 0
        self.alive = True
        self.grid = grid

    def checkAlive(self):
        case = self.grid.getValue(self.x, self.y) 
        if (case == 3 or case == 2):  # 3 case rouge car touche par le fantome, 2 case en contruction
            self.alive = False

    def move(self, direction):
        if (direction == 0 and self.y != 0):
            self.y = self.y - 1
            if(self.grid.setValue(self.x, self.y+1, 2)==0)
                self.grid.setValue(self.x, self.y+1, 2)
        elif (direction == 1 and self.x != grid.nX):
            self.x = self.x + 1
            if(self.grid.setValue(self.x-1, self.y, 2)==0)
                self.grid.setValue(self.x-1, self.y, 2)
        elif (direction == 2 and self.y != grid.nY):
            self.y = self.y + 1
            if(self.grid.setValue(self.x, self.y-1, 2)==0)
                self.grid.setValue(self.x, self.y-1, 2)
        elif (direction == 3 and self.x != 0):
            self.x = self.x -1
            if(self.grid.setValue(self.x+1, self.y, 2)==0)
                self.grid.setValue(self.x+1, self.y, 2)



