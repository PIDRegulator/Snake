import pygame
import random
import time

pygame.init()
pygame.display.set_caption("Snake")
screen_size_pixels = 1000
font_multiplier = screen_size_pixels/1000
screen_size = (screen_size_pixels, screen_size_pixels) #sets screen size for the game without score
y_offset = 100*font_multiplier # sets screen size offset for the text at the bottom
screen = pygame.display.set_mode((screen_size[0],screen_size[1]+y_offset)) #calculates the screen size form the offset and the board sizes

font = pygame.font.Font('MINECRAFT.otf', int(70*font_multiplier)) #sets font sizes for the score and win/lose menu
fontdied = pygame.font.Font('MINECRAFT.otf', int(100*font_multiplier))
fontspace = pygame.font.Font('MINECRAFT.otf', int(40*font_multiplier))

speed = int(input("speed: ")) #takes speed input from console 
cells = int(input("cells: ")) #takes number of cells in one row from console
print("Press 'alt + tab'") #navigates yout o what to
time.sleep(5)

# def draw_rect_alpha(surface, color, rect):
#     shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
#     pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
#     surface.blit(shape_surf, rect)

while True: #Main loop to  reset the game
    win = False
    pygame.display.flip() #resets display 

    direction = (0,1) #sets directions to right
    old_direction = (0,1)

    clock = pygame.time.Clock() #sets clock
    score = 0 #score to 0
    max_len = cells*cells #sets winning lenght of the snake by multiplying board size
    apple = [random.randint(0,cells-1),random.randint(0,cells-1)] #sets where apples can spawn
    snake = [[1,1]] #sets snake spawnpoint
    cell_size = screen_size[0]/cells #divides how many pixels every cell is

    background = pygame.Surface(screen_size) #backround size
    background.fill((6, 189, 36)) #board color
    for y in range(cells): #makes checkerboard pattern on board
        for x in range(cells):
            if (x+y) % 2 == 0:
                pygame.draw.rect(background,[17, 140, 37],[x*cell_size,y*cell_size,cell_size,cell_size])
                    
    f = open("highscore.txt","r") #reads highscore from file
    highs = int(f.read().splitlines()[0])
    if highs > 0:
        highscore_str = f"highscore: {highs}"
    else:
        highscore_str = ""

    running = True #sets game to run
    movecount = speed
    
    while running: #loop for the game to run
        clock.tick(120) #fps 
        framerate = clock.get_fps()
        for event in pygame.event.get(): #enables quitting easily
            if event.type == pygame.QUIT:
                running = False

        screen.fill((46, 92, 43)) #fills score background
        keys = pygame.key.get_pressed() #finds which direction it goes using WASD
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            direction = (-1,0)

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            direction = (1,0)

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            direction = (0,-1)

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            direction = (0,1)

        if old_direction != direction and old_direction[0] + direction[0] == 0: #locks turning 180 degrees at once
            direction = old_direction

        if movecount ==0: #snake movement
            old_direction = direction 
            new_y = snake[-1][0] + direction[0]
            new_x = snake[-1][1] + direction[1]
            new_body = [new_y,new_x] 

            if snake[-1][0] >= cells or snake[-1][1] >= cells: #snake collision 
                running = False
                continue

            if snake[-1][0] < 0 or snake[-1][1] < 0: #snake collision into wall
                running = False
                continue
                
            if apple == new_body: #checks if apple is anywhere in snake
                score += 1 #adds score
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