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
        
        neighbour = self.getNeighbour(self.game.getPacman().getCoord()[0], self.game.getPacman().getCoord()[1])
        tmp = neighbour
        for i in range(n):
            print("neighbour : " + str(neighbour))
            for j in range(len(neighbour)):
                print("j : " + str(j))
                tmp.append([self.getNeighbour(neighbour[j][0], neighbour[j][1])])
            print("tmp : " + str(tmp))
            neighbour+=tmp

        return neighbour
