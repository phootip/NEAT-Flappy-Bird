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
gameover = False

font = pygame.font.Font('freesansbold.ttf', 32)
green = (0, 255, 0) 
blue = (0, 0, 128) 
text = font.render('Game Over', True, green, blue)
textRect = text.get_rect(center=(300,200))
gen = 0

def move(birds, pipes):
    # if not gameover:
    for inst in birds:
       bird = inst['bird']
       value = inst['net'].activate([bird.rect[1], pipes[0].y])[0]
       if value > 0: 
           bird.jump()
       bird.move() 
       inst['genome'].fitness += 0.1
    for pipe in pipes:
        pipe.move()
        if pipe.x < -100:
            return True
    return False

def think(birds, pipes, addPipe):
    for inst in birds:
        bird = inst['bird']
        if bird.rect[1] < 0:
            birds.remove(inst)
        if base_img.get_rect(topleft=(0,700)).colliderect(bird.rect): 
            birds.remove(inst)
            # gameover = True
        for pipe in pipes:
            if pipe.is_collided_with(bird):
                # gameover = True
                birds.remove(inst)
    if addPipe:
        del pipes[0]
        pipes.append(Pipe())
        addPipe = False
        return 1
    return 0

def draw(birds, pipes, score):
    global gen
    scoreText = font.render(f'Score: {score}', True, green, blue)
    genText = font.render(f'Gen: {gen}', True, green, blue)
    birdText = font.render(f'Bird: {len(birds)}', True, green, blue)
    screen.blit(bg_img, (0,0))
    screen.blit(base_img, (0,700))
    screen.blit(scoreText, (0,0))
    screen.blit(genText, (300,0))
    screen.blit(birdText, (150,0))
    for inst in birds:
        bird = inst['bird']
        bird.draw()
    for pipe in pipes:
        pipe.draw()
    # if gameover:
    #     screen.blit(text, textRect)
    pygame.display.flip()

def eval_genomes(genomes, config):
    global gen
    gen += 1
    
    # nets = []
    birds = []
    # ge = []
    clock = pygame.time.Clock()
    pipes = [Pipe()]
    score = 0
    addPipe = False
    for genome_id, genome in genomes:
        bird = {}
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome,config)
        bird['net'] = net
        bird['bird'] = Bird(200,200) 
        bird['genome'] = genome
        birds.append(bird)
    crashed = False
    while not crashed and len(birds) > 0 and score < 50:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # bird.jump()
                    pass
        addPipe = move(birds,pipes)
        score += think(birds,pipes,addPipe)
        draw(birds,pipes,score)

def main():
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(eval_genomes, 50)
    print('\nBest genome:\n{!s}'.format(winner))

if __name__ == "__main__":
    print("starting the game")
    main()
