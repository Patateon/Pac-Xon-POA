import pygame
from grid import *

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")



def crete_level(level_matrix, nbblock_x, nbblock_y, pac_radius, speed_pac):
    for i in range(nbblock_y):
        for j in range(nbblock_x):
            if level_matrix[i][j]==1:
                
                pygame.draw.rect(screen,(0,71,171), (j*speed_pac,i*speed_pac, pac_radius*2, pac_radius*2))
                pygame.draw.polygon(screen, (155,221,255), [(j*speed_pac,i*speed_pac),((j+1)*speed_pac,i*speed_pac),(((j+1)*speed_pac)-3,(i*speed_pac)+3),((j*speed_pac)+3,(i*speed_pac)+3)])
                pygame.draw.polygon(screen, (0,191,255), [(j*speed_pac,i*speed_pac),(j*speed_pac,(i+1)*speed_pac),((j*speed_pac)+3,((i+1)*speed_pac)-3),((j*speed_pac)+3,(i*speed_pac)+3)])
                pygame.draw.polygon(screen, (0,0,128), [(j*speed_pac,(i+1)*speed_pac),((j+1)*speed_pac,(i+1)*speed_pac),(((j+1)*speed_pac)-3,((i+1)*speed_pac)-3),((j*speed_pac)+3,((i+1)*speed_pac)-3)])
                pygame.draw.polygon(screen, (0,0,128), [((j+1)*speed_pac,i*speed_pac),((j+1)*speed_pac,(i+1)*speed_pac),(((j+1)*speed_pac)-3,((i+1)*speed_pac)-3),(((j+1)*speed_pac)-3,(i*speed_pac)+3)])
                
            elif level_matrix[i][j]==2:          
                pygame.draw.rect(screen,(0,71,171), (j*speed_pac,i*speed_pac, pac_radius*2, pac_radius*2))

            elif level_matrix[i][j]==3: 
                pygame.draw.rect(screen,(255,0,0), (j*speed_pac,i*speed_pac, pac_radius*2, pac_radius*2))





# Game Loop
def create_matrix(width, height):
    matrix = [[0 for _ in range(width)] for _ in range(height)]
    
    # Set '1's in the first and last rows
    for col in range(width):
        matrix[0][col] = 1
        matrix[height - 1][col] = 1
    
    # Set '1's in the first and last columns
    for row in range(height):
        matrix[row][0] = 1
        matrix[row][width - 1] = 1
    
    return matrix




running = True


radius = 10
x=radius
y=radius
vel=20

nbblock_x=SCREEN_WIDTH//vel
nbblock_y=SCREEN_HEIGHT//vel



WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


resulting_matrix = create_matrix(nbblock_x, nbblock_y)
print(len(resulting_matrix[0]))
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x>radius:
            x-=vel
    elif keys[pygame.K_RIGHT]:
        if x<SCREEN_WIDTH-radius-1:
            x+=vel
    elif keys[pygame.K_UP]:
        if y>radius:
            y-=vel
    elif keys[pygame.K_DOWN]:
        if y<SCREEN_HEIGHT-radius-1:
            y+=vel
    screen.fill((0,0,0))
    crete_level(resulting_matrix, nbblock_x, nbblock_y, radius, vel)
    pygame.draw.circle(screen, (255,255,0), (x,y), radius)
    pygame.display.update()

pygame.quit()
