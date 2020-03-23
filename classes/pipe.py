import pygame
import random
import os

screen = pygame.display.get_surface()
pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")).convert_alpha())

class Pipe:
    GAP = 200
    VELO = 4
    def __init__(self):
        self.x = 800
        self.y = random.randrange(200,400)
        self.img = pipe_img
        self.img2 = pygame.transform.flip(pipe_img, False, True)
        self.top = self.y - self.img2.get_height()
        self.bottom = self.y + self.GAP

    def draw(self):
        screen.blit(self.img, (self.x,self.bottom)) 
        screen.blit(self.img2, (self.x,self.top))

    def move(self):
        self.x -= self.VELO
