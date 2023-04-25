import pygame
import random


pygame.init()
screen_size = (1000,1000)
y_offset = 100

font = pygame.font.Font('MINECRAFT.otf', 70)

screen = pygame.display.set_mode((screen_size[0],screen_size[1]+y_offset))
direction = (0,1)
old_direction = (0,1)

clock = pygame.time.Clock()
speed = 20
score = 0
cells = 20
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
        if snake[-1][0] < 0 or snake[-1][1] < 0:
            running = False
        if apple == new_body:
            score += 1
            if len(snake)+1>=max_len:
                running = False
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
        snake.append(new_body)
        movecount = speed
    else:
        movecount -= 1
    

    screen.blit(background,(0,0))
    pygame.draw.rect(screen,[227, 7, 14],[apple[1]*cell_size,apple[0]*cell_size,cell_size,cell_size])
    colors = range(0,255,round(255/len(snake)))[::-1]
    for i,body in enumerate(snake[:-1]):
        color = colors[i]
        pygame.draw.rect(screen,[0,0,color],[body[1]*cell_size,body[0]*cell_size,cell_size,cell_size])
    pygame.draw.rect(screen,[0, 0, colors[-1]],[snake[-1][1]*cell_size,snake[-1][0]*cell_size,cell_size,cell_size])

    text = font.render(f'score: {score}; {highscore_str}', True, (255,255,255))
    text_rect = text.get_rect()
    screen.blit(text,((screen_size[0]-text_rect.width)/2,screen_size[1]+(y_offset-text_rect.height)/2))

    pygame.display.flip()

print(f"your score is {score}")

f = open("highscore.txt","r")
highs = int(f.read().splitlines()[0])
if score > highs:
    f = open("highscore.txt","w")
    f.write(str(score))
    f.close()