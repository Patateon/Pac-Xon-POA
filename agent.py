from game import *

class Agent():

    def __init__(self, game):
        self.game = game

    def getNeighbour(self, x, y):
        grid = self.game.getGrid()
        neighbour = []

        if (x > 0):
            neighbour.append([x-1, y])
        if (x < grid.getSize()[0]-1):
            neighbour.append([x+1, y])
        if (y > 0):
            neighbour.append([x, y-1])
        if (y < grid.getSize()[1]-1):
            neighbour.append([x, y+1])

        return neighbour
    
    def nNeighbour(self, n):
        
        neighbours = [self.getNeighbour(self.game.getPacman().getCoord()[0], self.game.getPacman().getCoord()[1])]
        tmp = neighbours
        for i in range(n):
            for neighbour in neighbours:
                print(neighbours)
                for coord in neighbour:
                    tmp.append(self.getNeighbour(coord[0], coord[1]))
            neighbours+=tmp

        return tmp
