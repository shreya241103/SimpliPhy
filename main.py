import pygame
import pymunk
from ball import Ball
from segment import StaticSegment
scr_wd, scr_ht = 800, 800

# Frames per second - frequency
FPS = 50

def create():
    global space, ball, floor, wall_right, wall_left
    # Pymunk space
    space = pymunk.Space()
    space.gravity = 0, -980


    ball = Ball(space, 20, (200, 700), (0, 255, 0), (100, 0), elasticity= 0.6)

    floor = StaticSegment( space, (0, 30), (800, 30), 10, 2)
    wall_right = StaticSegment( space, (scr_wd, 0), (scr_wd, scr_ht + 1000), 0)
    wall_left = StaticSegment(space, (0, 0), (0, scr_ht + 1000), 0)

def trans_coord(coord):
    return int(coord[0]), int(scr_ht - coord[1])

collisions = 0

def collide(arbiter, space, data):
    global collisions
    collisions += 1
    return True

def updateText(display, data):
    font = pygame.font.Font( None,
                            50)
    text = font.render(f'{data}',
                       True,
                       (0, 0, 255))
    textRect = text.get_rect()
    textRect.center = trans_coord((700, 700))
    display.blit(text, textRect)

def simulate_bounce():
    pygame.init()
    display = pygame.display.set_mode((scr_wd, scr_ht))
    clock = pygame.time.Clock()
    create()

    global collisions
    collisions = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill((255, 255, 255))
        col = space.add_collision_handler( 1, 2)
        col.begin = collide
        floor.drawSegment(display)
        updateText(display, collisions)
        ball.drawBall(display)
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

if __name__ == "__main__":
    simulate_bounce()

