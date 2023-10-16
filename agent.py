from game import *
import numpy as np

class Node():

    def __init__(self, position):
        self.position = position
        self.parent = None
        self.g_cost = 0
        self.h_cost = 0

    def f_cost(self):
        return self.g_cost + self.h_cost

    def getPosition(self)->np.ndarray:
        return self.position

    def getg_cost(self):
        return self.g_cost

    def geth_cost(self):
        return self.h_cost

    def setParent(self, parent):
        self.parent = parent

    def setg_cost(self, g):
        self.g_cost = g

    def seth_cost(self, h):
        self.h_cost = h

    def __eq__(self, other):
        return np.array_equal(self.position, other.position)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.position[0], self.position[1]))


class Agent():

    def __init__(self, game, alpha):
        self.game = game
        self.alpha = alpha
        self.openSet = []
        self.closeSet = {None}
        self.path = []
        self.pathFound = False
        self.panicHere = False

    def setAlpha(self, alpha):
        self.alpha = alpha

    def getAlpha(self):
        return self.alpha

    def dist(self, n1, n2):
        return np.linalg.norm(n1.getPosition() - n2.getPosition())

    def distManhattan(self, n1, n2):
        return np.linalg.norm(n1.getPosition() - n2.getPosition(), ord=1)
    
    def translateDirection(self, direction):
        match direction:
            case Direction.UP:
                return np.array([-1, -1])

            case Direction.RIGHT:
                return np.array([-1, 1])

            case Direction.DOWN:
                return np.array([1, 1])
            
            case Direction.LEFT:
                return np.array([1, -1])


    def findEndPoints(self, startingPoint, rng):
        emptyPoints = np.where(self.game.getGrid().grid==0)
        indice = rng.integers(emptyPoints[0].shape[0])
        emptyPoints = [emptyPoints[0][indice], emptyPoints[1][indice]]
        direction = emptyPoints-startingPoint
        direction = direction/np.linalg.norm(direction)

        endPoints = emptyPoints
        while self.game.getGrid().getValue(*endPoints) != 1:
            endPoints = (endPoints + direction).round().astype(int)
        return endPoints


    def startSearch(self, start, end):
        self.clearSet()
        self.searching = True
        self.path = self.findPath(Node(start), Node(end))

    def minF_set(self):
        minNode = self.openSet[0]
        for node in self.openSet:
            minNode = node if (node.f_cost()<=minNode.f_cost() and node.geth_cost()<minNode.geth_cost()) else minNode
        return minNode

    def getFrontier(self, n):
        position = n.getPosition()
        x, y = position[0], position[1]
        neighbours = []
        for offset in np.array([[1, 0], [0, 1], [-1, 0], [0, -1]]):
            tmp = offset + position
            if (tmp[0]<0 or tmp[0]>= self.game.getGrid().getSize()[0] or tmp[1]<0 or tmp[1]>= self.game.getGrid().getSize()[1] or self.game.getGrid().getValue(*tmp)>1):
                continue
            neighbours.append(Node(tmp))
        return neighbours

    def clearSet(self):
        self.pathFound = False
        self.openSet = []
        self.closeSet = {None}

    def lenPath(self, current, start):
        size = 0
        currentNode = current
        while (currentNode != start):
            size+=1
            currentNode = currentNode.parent
        return size

    def backTrack(self, end, start):
        path = []
        currentNode = end
        while (currentNode != start):
            path.append(currentNode)
            currentNode = currentNode.parent
        return path[::-1] 

    def phantomNextPos(self, n, indice):
        coordPhantom = self.game.getPhantom()[indice].getCoord()
        direction = self.game.getPhantom()[indice].getDirection()
        coordDirection = self.translateDirection(direction) # C'est Beau

        nextPosition = np.array(coordPhantom)+coordDirection
        nextValue = self.game.getGrid().getValue(nextPosition[0], nextPosition[1])
        if (coordPhantom[1]+coordDirection[1]>coordPhantom[1]):
            topValue = self.game.getGrid().getValue(coordPhantom[0], coordPhantom[1]+coordDirection[1])
            botValue = self.game.getGrid().getValue(coordPhantom[0]+coordDirection[0], coordPhantom[1])
        else:
            topValue = self.game.getGrid().getValue(coordPhantom[0]+coordDirection[0], coordPhantom[1])
            botValue = self.game.getGrid().getValue(coordPhantom[0], coordPhantom[1]+coordDirection[1])
        for i in range(1, n):  
            if (nextValue != 0):
                direction = self.game.getPhantom()[indice].changeMove(direction, topValue, botValue)
                coordDirection = self.translateDirection(direction) # C'est Beau

            nextPosition = np.array(coordPhantom)+coordDirection
            nextValue = self.game.getGrid().getValue(nextPosition[0], nextPosition[1])
            if (coordPhantom[1]+coordDirection[1]>coordPhantom[1]):
                topValue = self.game.getGrid().getValue(coordPhantom[0], coordPhantom[1]+coordDirection[1])
                botValue = self.game.getGrid().getValue(coordPhantom[0]+coordDirection[0], coordPhantom[1])
            else:
                topValue = self.game.getGrid().getValue(coordPhantom[0]+coordDirection[0], coordPhantom[1])
                botValue = self.game.getGrid().getValue(coordPhantom[0], coordPhantom[1]+coordDirection[1])

        return nextPosition


    def findPath(self, start, end):
        self.openSet.append(start)
        while len(self.openSet):
            current = self.minF_set()
            self.openSet.remove(current)
            self.closeSet.add(current)

            if (current == end):
                self.pathFound = True
                return self.backTrack(current, start)

            for neighbour in self.getFrontier(current):
                if neighbour in self.closeSet:
                    continue

                nodeP1 = Node(self.phantomNextPos(self.lenPath(current, start)+1, 0))
                nodeP2 = Node(self.phantomNextPos(self.lenPath(current, start)+1, 1))

                dist1 = self.dist(neighbour, nodeP1)
                dist2 = self.dist(neighbour, nodeP2)
                g_cost = current.getg_cost() + 1 + (self.alpha/(dist1+1) + self.alpha/(dist2+1))

                # g_cost = current.getg_cost() + 1 - (self.dist(neighbour, Node(self.game.getPhantom()[0].getCoord())) + ((self.dist(neighbour, Node(self.game.getPhantom()[1].getCoord())))))

                # g_cost = current.getg_cost() + 1 + self.alpha*np.exp((self.dist(neighbour, Node(self.game.getPhantom()[0].getCoord())) + ((self.dist(neighbour, Node(self.game.getPhantom()[1].getCoord()))))))

                if (g_cost<neighbour.getg_cost() or not neighbour in self.openSet):
                    neighbour.setg_cost(g_cost)
                    neighbour.seth_cost(self.dist(neighbour, end))
                    neighbour.setParent(current)
                    if (not neighbour in self.openSet):
                        self.openSet.append(neighbour)

    def showPath(self):
        for node in self.path:
            self.game.getGrid().setValue(*node.getPosition(), 4)

    def detectRed(self):
        if (self.game.getGrid().grid[self.game.getGrid().grid==3].shape[0] != 0):
            self.panicHere = True

    def findClosestEscape(self):
        candidats = np.where(self.game.getGrid().grid==1)
        minCandidat = [candidats[0][0],candidats[1][0]]
        for i in range(candidats[0].shape[0]):
            candidat = np.array([candidats[0][i],candidats[1][i]])
            minCandidat = candidat if self.dist(Node(candidat), Node(np.array(self.game.getPacman().getCoord())))<self.dist(Node(minCandidat), Node(np.array(self.game.getPacman().getCoord()))) else minCandidat
        return minCandidat

        
    def move(self):
        if not self.path:
            self.pathFound = False
            self.panicHere = False
            return
        nextMove = self.path.pop(0)
        direction = np.array(self.game.getPacman().getCoord())-nextMove.getPosition()

        if (np.array_equal(direction, np.array([0, 1]))):
            self.game.getPacman().move(Direction.LEFT)

        elif (np.array_equal(direction, np.array([0, -1]))):
            self.game.getPacman().move(Direction.RIGHT)
        
        elif (np.array_equal(direction, np.array([1, 0]))):
            self.game.getPacman().move(Direction.UP)

        elif (np.array_equal(direction, np.array([-1, 0]))):
            self.game.getPacman().move(Direction.DOWN)
                
