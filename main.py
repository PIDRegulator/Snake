import pygame
import random


pygame.init()
screen_size = (1000,1000)

screen = pygame.display.set_mode(screen_size)
direction = (0,1)

clock = pygame.time.Clock()
score = 0
cell_y = 4
cell_x = 4
apple = [random.randint(0,cell_y-1),random.randint(0,cell_x-1)]
snake = [1,1]
cell_size = screen_size[0]/cell_x
background = pygame.Surface(screen_size)
background.fill((6, 189, 36))
for y in range(cell_y):
    for x in range(cell_x):
        if (x+y) % 2 == 0:
            pygame.draw.rect(background,[17, 140, 37],[x*cell_size,y*cell_size,cell_size,cell_size])
                 

running = True
movecount = 20
while running:
    clock.tick(60)
    framerate = clock.get_fps()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((6, 189, 36))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        direction = (-1,0)

    if keys[pygame.K_s]:
        direction = (1,0)

    if keys[pygame.K_a]:
        direction = (0,-1)

    if keys[pygame.K_d]:
        direction = (0,1)
        
    # print(framerate)
    print(score)

    if movecount ==0:
        snake[0] += direction[0]
        snake[1] += direction[1]
        if snake[0] >= cell_y or snake[1] >= cell_x:
            running = False
        if snake[0] < 0 or snake[1] < 0:
            running = False
        if snake == apple:
            apple = [random.randint(0,cell_y-1),random.randint(0,cell_x-1)]
            score += 1
        movecount = 20
    else:
        movecount -= 1

    screen.blit(background,(0,0))
    pygame.draw.rect(screen,[227, 7, 14],[apple[1]*cell_size,apple[0]*cell_size,cell_size,cell_size])
    pygame.draw.rect(screen,[0,0,255],[snake[1]*cell_size,snake[0]*cell_size,cell_size,cell_size])


