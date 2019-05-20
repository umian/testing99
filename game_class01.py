import pygame
import sys

class Ball:
    def __init__(self,x,y):
        self.ball_x=x
        self.ball_y=y
        self.ball_x_speed=7
        self.ball_y_speed=7
        self.ball_pic=pygame.image.load("small.bmp")
    def update(self):
        self.ball_x+=self.ball_x_speed
        self.ball_y+=self.ball_y_speed

        if self.ball_x>610: self.ball_x_speed = -7
        if self.ball_y>450: self.ball_y_speed = -7
        if self.ball_x<0: self.ball_x_speed = 7
        if self.ball_y<0: self.ball_y_speed = 7
    def render(self):
        screen.blit(self.ball_pic,(self.ball_x,self.ball_y))

pygame.init()

screen = pygame.display.set_mode((640,480))

ball1=Ball(30,30)
ball2=Ball(80,80)
ball3=Ball(100,10)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((90,230,90))
    ball1.update()
    ball1.render()
    ball2.update()
    ball2.render()
    ball3.update()
    ball3.render()

    pygame.display.flip()
    pygame.time.wait(10)