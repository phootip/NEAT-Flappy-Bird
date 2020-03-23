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
        self.vel = 0
        self.tick_count = 0
        self.img = self.IMGS[0] 
        self.rect = self.img.get_rect(topleft=(x,y))
        self.acc = 2

    def jump(self):
        self.vel = -20
        self.tick_count = 0

    def move(self):
        self.tick_count += 1
        self.vel += self.acc
        self.rect.y += self.vel

    def draw(self):
        screen.blit(self.img, self.rect)

    def get_mask(self):
        return pygame.mask.form_surface(self.img)

