import pygame

pygame.init()
screen_size = (1000,1000)
screen = pygame.display.set_mode(screen_size)
direction = "Right"

clock = pygame.time.Clock()
cell_y = 40
cell_x = 40
board = [[0]*cell_x]*cell_y
cell_size = screen_size[0]/cell_x

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((6, 189, 36))
    pygame.display.flip()
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
            ...


