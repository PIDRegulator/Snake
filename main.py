import pygame

pygame.init()
screen = pygame.display.set_mode((1000,1000))
direction = "Right"

clock = pygame.time.Clock()


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

