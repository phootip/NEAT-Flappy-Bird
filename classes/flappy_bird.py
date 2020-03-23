import pygame
import neat
import time
import random
import os

screen = pygame.display.get_surface()
bird_images = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird" + str(x) + ".png"))) for x in range(1,4)]

class Bird:
    MAX_ROTATION = 25
    IMGS = bird_images
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 0
        self.tick_count = 0
        self.img = self.IMGS[0] 
        self.acc = 5

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0

    def move(self):
        self.tick_count += 1
        
        d = self.vel*self.tick_count + 0.5 * self.acc * (self.tick_count ** 2)
        if d >= 16: d = 16

        print(d)
        self.y = self.y + d

    def draw(self):
        imagerect = self.img.get_rect()
        # screen.blit(self.img, imagerect)
        screen.blit(self.img, (self.x,self.y))

    def get_mask(self):
        return pygame.mask.form_surface(self.img)

