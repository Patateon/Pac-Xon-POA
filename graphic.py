import pygame
from game import *

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

vel=20      #size of the block or speed pac bc he travels by block

nbblock_x=SCREEN_WIDTH//vel     
nbblock_y=SCREEN_HEIGHT//vel

game=Game(nbblock_y,nbblock_x,0.5,2,[[3,6],[7,4]])
game.initGame()

def crete_level(game, nbblock_x, nbblock_y, speed_pac):
    for j in range(nbblock_x):
        for i in range(nbblock_y):
            if game.grid.getValue(i,j)==1:
                
                pygame.draw.rect(screen,(0,71,171), (j*speed_pac,i*speed_pac, speed_pac, speed_pac))
                pygame.draw.polygon(screen, (155,221,255), [(j*speed_pac,i*speed_pac),((j+1)*speed_pac,i*speed_pac),(((j+1)*speed_pac)-3,(i*speed_pac)+3),((j*speed_pac)+3,(i*speed_pac)+3)])
                pygame.draw.polygon(screen, (0,191,255), [(j*speed_pac,i*speed_pac),(j*speed_pac,(i+1)*speed_pac),((j*speed_pac)+3,((i+1)*speed_pac)-3),((j*speed_pac)+3,(i*speed_pac)+3)])
                pygame.draw.polygon(screen, (0,0,128), [(j*speed_pac,(i+1)*speed_pac),((j+1)*speed_pac,(i+1)*speed_pac),(((j+1)*speed_pac)-3,((i+1)*speed_pac)-3),((j*speed_pac)+3,((i+1)*speed_pac)-3)])
                pygame.draw.polygon(screen, (0,0,128), [((j+1)*speed_pac,i*speed_pac),((j+1)*speed_pac,(i+1)*speed_pac),(((j+1)*speed_pac)-3,((i+1)*speed_pac)-3),(((j+1)*speed_pac)-3,(i*speed_pac)+3)])
                
            elif game.grid.getValue(i,j)==2:          
                pygame.draw.rect(screen,(0,71,171), (j*speed_pac,i*speed_pac, speed_pac, speed_pac))

            elif game.grid.getValue(i,j)==3: 
                pygame.draw.rect(screen,(255,0,0), (j*speed_pac,i*speed_pac,speed_pac, speed_pac))


def draw_ghosts(coord_x,coord_y,speed_pac):
    pygame.draw.rect(screen,(171,0,171), (coord_x*speed_pac,coord_y*speed_pac, speed_pac, speed_pac))

def draw_pac(coord_x,coord_y,speed_pac):
    radius = 10
    pygame.draw.circle(screen, (255,255,0), (radius+(coord_y*speed_pac),radius+(coord_x*speed_pac)), radius)





running = True

while running:
    
    pygame.time.delay(16)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.getGrid().propagation()
    
    screen.fill((0,0,0))
   
   
    crete_level(game, nbblock_x, nbblock_y, vel)
   
   
    draw_pac(game.pacman.x,game.pacman.y,vel)

    game.getPacman().move(Direction.DOWN)
    game.getPacman().move(Direction.RIGHT)
    game.getPhantom()[0].move()
    game.getPhantom()[1].move()
    game.getGrid().propagation()
    
    
    draw_ghosts(game.phantom[0].getCoord()[0],game.phantom[0].getCoord()[1],vel)
    draw_ghosts(game.phantom[1].getCoord()[0],game.phantom[1].getCoord()[1],vel)


    pygame.display.update()

pygame.quit()
