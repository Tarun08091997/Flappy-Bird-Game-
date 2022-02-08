import pygame
import os

class points_img:
    screen = pygame.display
    images = [ pygame.image.load(os.path.join('Files/Photos','0_big_gold.png')),
          pygame.image.load(os.path.join('Files/Photos','1_big_gold.png')),
          pygame.image.load(os.path.join('Files/Photos','2_big_gold.png')),
          pygame.image.load(os.path.join('Files/Photos','3_big_gold.png')),
          pygame.image.load(os.path.join('Files/Photos','4_big_gold.png')),
          pygame.image.load(os.path.join('Files/Photos','5_big_gold.png')),
          pygame.image.load(os.path.join('Files/Photos','6_big_gold.png')),
          pygame.image.load(os.path.join('Files/Photos','7_big_gold.png')),
          pygame.image.load(os.path.join('Files/Photos','8_big_gold.png')),
          pygame.image.load(os.path.join('Files/Photos','9_big_gold.png'))
          ]
    def __init__(self,screen):
        self.screen = screen
        pass

    def show_point(self,point):
        x = 200
        p = str(point)
        for a in p :
           self.screen.blit(self.images[int(a)],(x,0))
           x += 30
        pass



class life:
    life = pygame.image.load('Files/Photos/bird_0.png')
    def __init__(self,screen):
        self.screen = screen
        pass

    def show_life(self,lives):
        x = 10
        y = 540
        for i in range(0,lives):
            self.screen.blit(self.life,(x,y))
            x += 40


class decision:
    def __init__(self,screen):
        self.screen = screen
        pass

    def check_status(self,lives,score):
        if lives <= 0 :
            return False
        else :
            return True
