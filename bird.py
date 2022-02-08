import pygame
import os
class Bird:
    screen = pygame.display
    img0 = pygame.transform.scale(pygame.image.load(os.path.join( 'Files/Photos','bird_0.png')), (60,50))
    img1 = pygame.transform.scale(pygame.image.load(os.path.join('Files/Photos','bird_1.png')), (60,50))
    fly = pygame.transform.rotate(img0,45)
    fall = pygame.transform.rotate(img0,315)


    x = 200
    y = 300
    j_speed = 3
    f_speed = 3
    angle = 0
    def __init__(self,screen):
        self.screen = screen
        screen.blit(self.img0,(self.x,self.y))
        self.mask = pygame.mask.from_surface(self.img0)

    def jump(self,j_speed = 3):
        j_speed = self.j_speed
        self.y = self.y - self.j_speed
        self.screen.blit(self.fly, (self.x, self.y))

    def move(self):
        self.y = self.y + self.f_speed
        self.screen.blit(self.fall, (self.x, self.y))

    def show(self):
        self.screen.blit(self.img1, (self.x, self.y))