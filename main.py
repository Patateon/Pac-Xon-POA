from game import *
from agent import *
import pygame

        
if __name__ == "__main__":

    game = Game(10, 10, 0.2, 2, [[3,5], [7, 8]])
    game.initGame()

    BLACK = (0, 0, 0)
    DARK_BLUE = ()
    LIGHT_BLUE = ()
    RED = ()
    WHITE = (200, 200, 200)
    sizeX = game.getGrid().getSize()[0]
    sizeY = game.getGrid().getSize()[1]
    WINDOW_WIDTH = sizeX*25
    WINDOW_HEIGHT = sizeY*25

    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    def drawGrid():
        blockSize = 25
        for x in range(0, WINDOW_WIDTH, blockSize):
            for y in range(0, WINDOW_HEIGHT, blockSize):
                match grid[x, y]:
                    case 0:
                        pass
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(SCREEN, WHITE, rect, 1)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


   
