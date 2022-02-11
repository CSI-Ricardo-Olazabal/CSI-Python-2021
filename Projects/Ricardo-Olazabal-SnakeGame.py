import pygame
pygame.init()

yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis = pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption("Snake game by JD")
game_over = False
x1 = 150
y1 = 150

x1_change = 0
y1_change = 0


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_chsnge = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    x1+=x1_change
    y1+=y1_change
    dis.fill(black)
    pygame.draw.rect(dis, yellow, [x1, y1, 10, 10])
    pygame.display.update
pygame.quit()
quit()

