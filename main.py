import pygame
import neat
import time
import random
import os

WIN_WIDTH = 600
WIN_HEIGHT = 700
pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

from classes.flappy_bird import Bird

pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")).convert_alpha())
bg_img = pygame.transform.scale(pygame.image.load(os.path.join("imgs","bg.png")).convert_alpha(), (600, 900))
bird_images = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird" + str(x) + ".png"))) for x in range(1,4)]
base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")).convert_alpha())

def run():
    pygame.display.set_caption('Flappy Happy')
    clock = pygame.time.Clock()
    crashed = False
    bird = Bird(200,200)
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            print(event)
        screen.blit(bg_img, (0,0))
        bird.move()
        bird.draw()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    print("starting the game")
    run()
