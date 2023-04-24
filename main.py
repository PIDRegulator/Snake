import pygame

pygame.init()
screen_size = (1000,1000)
screen = pygame.display.set_mode(screen_size)
direction = "Right"

clock = pygame.time.Clock()
cell_y = 40
cell_x = 40
board = []
for _ in range (cell_y):
    board.append([0]*cell_x)
cell_size = screen_size[0]/cell_x

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((6, 189, 36))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        direction = "Up"

    if keys[pygame.K_s]:
        direction = "Down"

    if keys[pygame.K_a]:
        direction = "Left"

    if keys[pygame.K_d]:
        direction = "Right"

    print (direction)

    for y,row in enumerate(board):
        for x,cell in enumerate(row):
            if cell == 0:
                if (x+y) % 2 == 0:
                    pygame.draw.rect(screen,[17, 140, 37],[x*cell_size,y*cell_size,cell_size,cell_size])
            if cell == 1:
                pygame.draw.rect(screen,[0, 63, 212],[x*cell_size,y*cell_size,cell_size,cell_size])
            if cell == 2:
                pygame.draw.rect(screen,[61, 14, 156],[x*cell_size,y*cell_size,cell_size,cell_size])
            if cell == 3:
                 pygame.draw.rect(screen,[227, 7, 14],[x*cell_size,y*cell_size,cell_size,cell_size])

    pygame.display.flip()


