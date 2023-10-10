from grid import *
from pac import *


        
if __name__ == "__main__":

    game = Game(10, 10, 0.2, 2, [[3,5], [7, 8]])
    game.initGame()
    game.getPacman().move(Direction.RIGHT)
    game.getPacman().move(Direction.RIGHT)
    game.getPacman().move(Direction.RIGHT)
    game.getPacman().move(Direction.RIGHT)
    game.getPacman().move(Direction.RIGHT)
    for i in range(7):
        game.getPacman().move(Direction.DOWN)
    game.getPhantom()[0].move(Direction.LEFT) 
    print(game.getGrid().grid)
