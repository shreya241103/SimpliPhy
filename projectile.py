import pygame
import pymunk
import math
import random
from projectile_class import *
def running():
    u = 50
    g = 9.8
    pygame.init()
    space = pymunk.Space()
    space.gravity = 0, -1000
    SCREEN = WIDTH, HEIGHT = 600, 600
    display = pygame.display.set_mode(SCREEN)
    clock = pygame.time.Clock()
    FPS = 60
    BLACK = (18, 18, 18)
    WHITE=(255,255,255)
    origin = (150, 350)
    radius = 250
    font = pygame.font.SysFont('arial', 20)
    projectile = Projectile(u, 0)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display.fill(BLACK)


        theta =get_angle(pygame.mouse.get_pos(), origin)
    
        pygame.draw.line(display, WHITE, origin, (origin[0] + 250, origin[1]), 2)
        space.step(1/FPS)

        if pygame.mouse.get_pressed()[0]:
            theta = get_angle(pygame.mouse.get_pos(), origin)
            if -90 < theta <= 0:
                projectile = Projectile(u, theta)


        projectile.update()

        degreetext = font.render(f"{int(abs(theta))}°", True, WHITE)
        display.blit(degreetext, (origin[0] + 38, origin[1] - 20))

        pygame.draw.rect(display, (0, 0, 0), (0, 0, WIDTH, HEIGHT), 5)
        clock.tick(FPS)
        pygame.display.update()
