from grid import *
from pac import *


        
if __name__ == "__main__":

    game = Game(10, 10, 0.2, 2, [[3,5], [7, 8]])
    game.initGame()
    game.getPacman().move(Direction.RIGHT)
    game.getPacman().move(Direction.RIGHT)
    for i in range(10):
        game.getPacman().move(Direction.DOWN)
    print(game.getGrid().grid)
