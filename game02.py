import pygame

pygame.init()

screen = pygame.display.set_mode((640,480))
ball = pygame.image.load("small.bmp")
ball_x = 10
ball_y = 10

ball_x_speed = 3
ball_y_speed = 3

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ball_x+=ball_x_speed
    ball_y+=ball_y_speed

    if ball_x>610:
        ball_x_speed=-3
    if ball_y > 450:
        ball_y_speed=-3

    if ball_x<0:
        ball_x_speed=2
    if ball_y <0:
        ball_y_speed=2

    screen.fill((90,230,90))

    screen.blit(ball,(ball_x,ball_y))

    pygame.display.flip()
    pygame.time.wait(10)