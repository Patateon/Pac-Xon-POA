from grid import *
from game import *
import pygame

        
if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
    game = Game(10, 10, 0.2, 2, [[3,5], [7, 8]])
    game.initGame()
    game.getPacman().move(Direction.RIGHT)
    game.getPacman().move(Direction.RIGHT)

    
    for i in range(7):
        game.getPacman().move(Direction.DOWN)
    
    game.getPhantom()[0].move(Direction.UP)
    game.getGrid().update(game.getPhantom()[0].getX(), game.getPhantom()[0].getY(), game.getPhantom()[1].getX(), game.getPhantom()[1].getY())
    
    print(game.getGrid().grid)
