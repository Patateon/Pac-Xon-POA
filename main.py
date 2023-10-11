from game import *
from agent import *
import pygame

        
if __name__ == "__main__":

    game = Game(10, 10, 0.2, 2, [[3,5], [7, 8]])
    game.initGame()
    agent = Agent(game)
    print(agent.nNeighbour(3))