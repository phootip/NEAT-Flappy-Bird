import pygame
import neat
import time
import random
import os

WIN_WIDTH = 600
WIN_HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")).convert_alpha())
bg_img = pygame.transform.scale(pygame.image.load(os.path.join("imgs","bg.png")).convert_alpha(), (600, 900))
bird_images = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird" + str(x) + ".png"))) for x in range(1,4)]
base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")).convert_alpha())

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

        self.y = self.y + d

    def draw(self):
        imagerect = self.img.get_rect()
        screen.blit(self.img, imagerect)

    def get_mask(self):
        return pygame.mask.form_surface(self.img)

class GameController:
    def __init__(self):
        None

def run():
    pygame.display.set_caption('Flappy Happy')
    clock = pygame.time.Clock()
    crashed = False
    a = Bird(50,50)
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            print(event)
        # screen.fill(black)
        a.draw()
        pygame.draw.rect(screen, (255,0,0), (50,50,50,50))
        pygame.display.flip()
        clock.tick(60)
        # break

if __name__ == '__main__':
    print('starting the game...')
    run()
