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
score = 0
addPipe = False
gameover = False

font = pygame.font.Font('freesansbold.ttf', 32)
green = (0, 255, 0) 
blue = (0, 0, 128) 
text = font.render('Game Over', True, green, blue)
textRect = text.get_rect(center=(300,200))

def move():
    global addPipe
    if not gameover:
        bird.move()
        for pipe in pipes:
            pipe.move()
            if pipe.x < -100:
                addPipe = True

def think():
    global addPipe, score, gameover
    if base_img.get_rect(topleft=(0,700)).colliderect(bird.rect): gameover = True
    for pipe in pipes:
        if pipe.is_collided_with(bird):
            gameover = True
    if addPipe:
        score += 1
        print(score)
        del pipes[0]
        pipes.append(Pipe())
        addPipe = False

def draw():
    scoreText = font.render(f'Score: {score}', True, green, blue)
    screen.blit(bg_img, (0,0))
    screen.blit(base_img, (0,700))
    screen.blit(scoreText, (0,0))
    bird.draw()
    for pipe in pipes:
        pipe.draw()
    if gameover:
        screen.blit(text, textRect)
    pygame.display.flip()

def run():
    crashed = False
    while not crashed:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
        move()
        think()
        draw()


if __name__ == "__main__":
    print("starting the game")
    run()
