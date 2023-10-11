from grid import *


        
if __name__ == "__main__":

    grid_instance = Grid(10, 10,0.20)
    grid_instance.initGrid()
    grid_instance.setValue(1,1,2)
    grid_instance.setValue(2,1,2)
    grid_instance.setValue(2,2,2)
    grid_instance.setValue(2,3,2)
    grid_instance.setValue(3,3,2)
    grid_instance.setValue(3,4,2)
    grid_instance.setValue(3,5,2)
    grid_instance.setValue(4,5,2)
    grid_instance.setValue(5,5,2)
    grid_instance.setValue(5,6,2)
    grid_instance.setValue(5,7,2)
    grid_instance.setValue(4,7,2)
    grid_instance.setValue(3,7,2)
    grid_instance.setValue(2,7,2)
    grid_instance.setValue(2,6,2)
    grid_instance.setValue(1,6,2)
    print(grid_instance.grid)
    grid_instance.setEndPath(True)
    grid_instance.update(1,4,5,2)
    print(grid_instance.grid)
    print("Victoire? "+str(grid_instance.endGame))

    grid_instance2 = Grid(10, 10,0.30)
    grid_instance2.initGrid()
    grid_instance2.setValue(1,1,2)
    grid_instance2.setValue(2,1,2)
    grid_instance2.setValue(2,2,2)
    grid_instance2.setValue(2,3,2)
    grid_instance2.setValue(3,3,2)
    grid_instance2.setValue(3,4,2)
    grid_instance2.setValue(3,5,2)
    grid_instance2.setValue(4,5,2)
    grid_instance2.setValue(5,5,2)
    grid_instance2.setValue(5,6,2)
    grid_instance2.setValue(5,7,2)
    grid_instance2.setValue(4,7,2)
    grid_instance2.setValue(3,7,2)
    grid_instance2.setValue(2,7,2)
    grid_instance2.setValue(2,6,2)
    grid_instance2.setValue(1,6,2)
    print(grid_instance2.grid)
    grid_instance2.setEndPath(True)
    grid_instance2.update(4,4,5,2)
    print(grid_instance2.grid)
    print("Victoire? "+str(grid_instance2.endGame))

    game = Game(10, 10, 0.2, 2, [[3,5], [7, 8]])
    game.initGame()
    game.getPacman().move(Direction.RIGHT)
    game.getPacman().move(Direction.RIGHT)
    for i in range(10):
        game.getPacman().move(Direction.DOWN)
    print(game.getGrid().grid)


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
    print(game.getGrid().grid)
