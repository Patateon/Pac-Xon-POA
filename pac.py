import numpy as np
from grid import *
from abc import ABC


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3 # cw


class Fantom:

    def __init__(self, x, y, grid):
        self.x = x
        self.y = y
        self.grid = grid #De classe Grid


class PacMan:

    def __init__(self, x, y, grid):
        self.x = x
        self.y = y
        self.grid = grid #De classe Grid


    def move(self, direction):
    actualCase = (self.x, self.y)

    match direction with:
        case Direction.UP:


        case Direction.RIGHT:
            
        case Direction.DOWN:
            
        case Direction.LEFT:
        
        case _:

