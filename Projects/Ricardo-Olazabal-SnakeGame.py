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

x1 = dis_width/2
y1 = dis_height/2

x1_change = 0
y1_change = 0

snake_block = 10
snake_speed = 30

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [110, dis_height/2])

while not game_over:
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
        game_over = True

    x1 += x1_change*snake_block
    y1 += y1_change*snake_block
    dis.fill(black)
    pygame.draw.rect(dis, blue, [x1, y1, snake_block, snake_block])
    pygame.display.update()

    clock.tick(snake_speed)

message("You LOST", red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()

