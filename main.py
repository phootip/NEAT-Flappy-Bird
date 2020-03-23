import pygame
import neat
import time
import random
import os

WIN_WIDTH = 600
WIN_HEIGHT = 800
pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

from classes.bird import Bird
from classes.pipe import Pipe

bg_img = pygame.transform.scale(pygame.image.load(os.path.join("imgs","bg.png")).convert_alpha(), (600, 900))
base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")).convert_alpha())

pygame.display.set_caption('Flappy Happy')
clock = pygame.time.Clock()
bird = Bird(200,200)
pipes = [Pipe()]

def move():
    bird.move()
    for pipe in pipes:
        pipe.move()

def draw():
    bird.draw()
    for pipe in pipes:
        pipe.draw()

def run():
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
        screen.blit(bg_img, (0,0))
        screen.blit(base_img, (0,700))
        move()
        draw()
        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    print("starting the game")
    run()
