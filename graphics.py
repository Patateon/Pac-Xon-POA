import pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

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
vel=10

nbblock_x=SCREEN_WIDTH//radius
nbblock_y=SCREEN_HEIGHT//radius


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
    if keys[pygame.K_RIGHT]:
        if x<SCREEN_WIDTH-radius-1:
            x+=vel
    if keys[pygame.K_UP]:
        if y>radius:
            y-=vel
    if keys[pygame.K_DOWN]:
        if y<SCREEN_HEIGHT-radius-1:
            y+=vel
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255,255,0), (x,y), radius)
    for i in range(nbblock_y):
        for j in range(nbblock_x):
            if resulting_matrix[i][j]==1:
                pygame.draw.rect(screen, (128, 0, 128), (j*10,i*10, radius, radius))
    pygame.display.update()

pygame.quit()
