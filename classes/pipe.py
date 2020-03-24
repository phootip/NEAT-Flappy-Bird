import pygame
import random
import os

screen = pygame.display.get_surface()
pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")).convert_alpha())

class Pipe:
    GAP = 200
    VELO = 16
    def __init__(self):
        self.x = 800
        self.y = random.randrange(200,400)
        self.bottomPipe = pipe_img
        self.topPipe = pygame.transform.flip(pipe_img, False, True)
        self.bottom = self.y + self.GAP
        self.top = self.y - self.topPipe.get_height()
        self.topRect = self.topPipe.get_rect(topleft=(self.x, self.top))
        self.bottomRect = self.bottomPipe.get_rect(topleft=(self.x, self.bottom))

    def draw(self):
        screen.blit(self.bottomPipe, self.bottomRect) 
        screen.blit(self.topPipe, self.topRect)

    def move(self):
        self.x -= self.VELO
        self.topRect.x = self.x
        self.bottomRect.x = self.x

    def is_collided_with(self, bird):
        return self.topRect.colliderect(bird.rect) or self.bottomRect.colliderect(bird.rect)
