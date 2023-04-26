import pygame
import random
import time

pygame.init()
screen_size = (800,800)
y_offset = 100
screen = pygame.display.set_mode((screen_size[0],screen_size[1]+y_offset))

font = pygame.font.Font('MINECRAFT.otf', 70)
fontdied = pygame.font.Font('MINECRAFT.otf', 100)
fontspace = pygame.font.Font('MINECRAFT.otf', 40)

speed = int(input("speed: "))
cells = int(input("cells: "))
print("Press 'alt + tab'")
time.sleep(5)

def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)


while True:
    win = False
    pygame.display.flip()

    direction = (0,1)
    old_direction = (0,1)

    clock = pygame.time.Clock()
    score = 0
    max_len = cells*cells
    apple = [random.randint(0,cells-1),random.randint(0,cells-1)]
    snake = [[1,1]]
    cell_size = screen_size[0]/cells
    background = pygame.Surface(screen_size)
    background.fill((6, 189, 36))
    for y in range(cells):
        for x in range(cells):
            if (x+y) % 2 == 0:
                pygame.draw.rect(background,[17, 140, 37],[x*cell_size,y*cell_size,cell_size,cell_size])
                    
    f = open("highscore.txt","r")
    highs = int(f.read().splitlines()[0])
    if highs > 0:
        highscore_str = f"highscore: {highs}"
    else:
        highscore_str = ""


    running = True
    movecount = speed
    while running:
        clock.tick(60)
        framerate = clock.get_fps()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((46, 92, 43))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            direction = (-1,0)

        if keys[pygame.K_s]:
            direction = (1,0)

        if keys[pygame.K_a]:
            direction = (0,-1)

        if keys[pygame.K_d]:
            direction = (0,1)

        if old_direction != direction and old_direction[0] + direction[0] == 0:
            direction = old_direction

        if movecount ==0:
            old_direction = direction
            new_y = snake[-1][0] + direction[0]
            new_x = snake[-1][1] + direction[1]
            new_body = [new_y,new_x]
            if snake[-1][0] >= cells or snake[-1][1] >= cells:
                running = False
                continue
            if snake[-1][0] < 0 or snake[-1][1] < 0:
                running = False
                continue
            if apple == new_body:
                score += 1
                if len(snake)+1>=max_len:
                    running = False
                    win = True
                    print("you won")
                    continue
                else:
                    while apple in snake+[new_body]:
                        apple = [random.randint(0,cells-1),random.randint(0,cells-1)]
                
                print(score)
            else:
                snake.pop(0)
            if new_body in snake:
                running = False
                continue
            snake.append(new_body)
            movecount = speed
        else:
            movecount -= 1
        

        screen.blit(background,(0,0))
        pygame.draw.rect(screen,[227, 7, 14],[apple[1]*cell_size,apple[0]*cell_size,cell_size,cell_size])
        for i,body in enumerate(snake[:-1]):
            color = abs(255-(255/len(snake)*i))
            pygame.draw.rect(screen,[0,0,color],[body[1]*cell_size,body[0]*cell_size,cell_size,cell_size])
        pygame.draw.rect(screen,[0, 0, 0],[snake[-1][1]*cell_size,snake[-1][0]*cell_size,cell_size,cell_size])

        text = font.render(f'score: {score}; {highscore_str}', True, (255,255,255))
        text_rect = text.get_rect()
        screen.blit(text,((screen_size[0]-text_rect.width)/2,screen_size[1]+(y_offset-text_rect.height)/2))
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()

        pygame.display.flip()

    print(f"your score is {score}")

    f = open("highscore.txt","r")
    highs = int(f.read().splitlines()[0])
    if score > highs:
        f = open("highscore.txt","w")
        f.write(str(score))
        f.close()
    
    screen.fill((255, 0, 0))
    if win:
        screen.fill((0, 255, 0))
    text = fontdied.render(f'YOU DIED', True, (255,255,255))
    if win:
        text = fontdied.render(f'YOU WON', True, (255,255,255))
    text_rect = text.get_rect()
    screen.blit(text,((screen_size[0]-text_rect.width)/2,400))
    text = font.render(f'score: {score}; {highscore_str}', True, (255,255,255))
    text_rect = text.get_rect()
    screen.blit(text,((screen_size[0]-text_rect.width)/2,500))
    text = fontspace.render(f'Press Backspace to start new game', True, (255,255,255))
    text_rect = text.get_rect()
    screen.blit(text,((screen_size[0]-text_rect.width)/2,600))
    text = fontspace.render(f'or Press ESC to leave the game', True, (255,255,255))
    text_rect = text.get_rect()
    screen.blit(text,((screen_size[0]-text_rect.width)/2,700))
    pygame.display.flip()
    while True:
        pygame.event.pump()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE]:
            break
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()