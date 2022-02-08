import os

import pygame


class pipe:
    screen = pygame.display
    x = 1000
    y = 500
    img = None
    birdSpeed = 3
    collision_happened = False
    width = 50
    passed = False
    def __init__(self,screen,x,y,img):
        self.x = x
        self.y = y
        self.screen = screen
        self.img = img
        self.screen.blit(self.img,(self.x,self.y))


    def move(self,birdspeed = 3):
        self.birdSpeed = birdspeed
        self.x = self.x - self.birdSpeed
        self.screen.blit(self.img, (self.x, self.y))
    def show(self):

        self.screen.blit(self.img, (self.x, self.y))


class pipe_up(pipe):

    def __init__(self,screen,x,y):
        p = pygame.transform.scale(pygame.image.load(os.path.join('Files/Photos','pipe_green.png')), (self.width, 300))
        self.mask = pygame.mask.from_surface(p)
        super().__init__(screen,x,y, p)


class pipe_down(pipe):

    def __init__(self, screen, x, y):
        p = pygame.transform.scale(pygame.image.load(os.path.join( 'Files/Photos','pipe_green.png')), (self.width, 300))
        pd = pygame.transform.rotate(p, 180)
        self.mask = pygame.mask.from_surface(pd)
        super().__init__(screen, x, y,pd)

class ground:
    x=0
    y=590
    land = pygame.transform.scale(pygame.image.load(os.path.join('Files/Photos','land.png')),(1050,40))
    def __init__(self,screen,x=0,y=570):
        self.screen = screen
        self.x = x
        self.y = y
        self.screen.blit(self.land,(self.x,self.y))

    def move(self,speed = 3):
        self.x -= speed
        self.screen.blit(self.land, (self.x, self.y))