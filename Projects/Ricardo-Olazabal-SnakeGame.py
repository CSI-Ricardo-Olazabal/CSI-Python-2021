import random
import pygame
import time
pygame.init()

yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 400
dis_height = 300
dis = pygame.display.set_mode((dis_width,dis_height))

pygame.display.update()
pygame.display.set_caption("Snake game by ME, RICARDO OLAZABAL MUAHAHAHAHAHAHAHA")
game_over = False

snake_block = 10
snake_speed = 30

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 25)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/7, dis_height/2])

def gameRestart():
    game_over = False
    game_close = False
    
    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0,dis_width-snake_block)/snake_block)*snake_block
    foody = round(random.randrange(0,dis_width-snake_block)/snake_block)*snake_block


    while not game_over:

        while game_close:
            dis.fill(black)
            message("You LOST Press Q-Quit or P-Play Again.", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameRestart()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -1
                    y1_chsnge = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 1
                    y1_change = 0
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 1
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -1
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change*snake_block
        y1 += y1_change*snake_block
        dis.fill(black)
        pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, blue, [x1, y1, snake_block, snake_block])
        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameRestart()