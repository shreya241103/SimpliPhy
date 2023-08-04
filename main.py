import pygame
import pymunk
from ball import Ball
from segment import StaticSegment
from textinput import Input
scr_wd, scr_ht = 800, 800

# Frames per second - frequency
FPS = 50

def trans_coord(coord):
    return int(coord[0]), int(scr_ht - coord[1])

def create(ht, vel):
    global space, ball, floor, wall_right, wall_left
    # Pymunk space
    space = pymunk.Space()
    space.gravity = 0, -981

    ball = Ball(space, 20, (200, ht), (0, 255, 0), vel, elasticity= 2/3)

    floor = StaticSegment( space, (0, 0), (800, 0), 10, 2)
    wall_right = StaticSegment( space, (scr_wd, 0), (scr_wd, scr_ht + 1000), 0)
    wall_left = StaticSegment(space, (0, 0), (0, scr_ht + 1000), 0)

collisions = 0
dist = 0
def collide(arbiter, space, data):
    global dist, text, textRect
    font = pygame.font.Font( None,
                            50)
    text = font.render(f'{dist}',
                       True,
                       (0, 0, 255))
    textRect = text.get_rect()
    textRect.center = trans_coord((700, 600))
    global collisions
    collisions += 1
    return True

def calcDist(arbiter, space, data):
    global dist
    max_d = ( (ball.body.velocity[1]) * (ball.body.velocity[1]) )/ (2 * abs(space.gravity[1]))
    if  max_d*2/100 > 0.1:
        print(int(ball.body.velocity[1]))
        print(max_d)
        dist += int(max_d*2/100)
    return True

def updateText(display, data, coord):
    font = pygame.font.Font( None,
                            50)
    text = font.render(f'{data}',
                       True,
                       (0, 0, 255))
    textRect = text.get_rect()
    textRect.center = trans_coord((coord))
    display.blit(text, textRect)

pygame.init()
font = pygame.font.Font( None,
                            50)
text = font.render(f'{0}',
                       True,
                       (0, 0, 255))
textRect = text.get_rect()
def simulate_bounce(ht, vel):
    display = pygame.display.set_mode((scr_wd, scr_ht))
    clock = pygame.time.Clock()
    create(ht, vel)
    global dist
    dist = int(ht/100)
    global collisions
    collisions = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill((255, 255, 255))
        col = space.add_collision_handler( 1, 2)
        col.begin = collide
        col.separate = calcDist
        floor.drawSegment(display)
        updateText(display, collisions, (700, 700))
        # updateText(display, dist, (700, 600))
        display.blit(text, textRect)
        updateText(display, "1", (6, 100))
        updateText(display, "2", (6, 200))
        updateText(display, "3", (6, 300))
        updateText(display, "4", (6, 400))
        updateText(display, "5", (6, 500))
        updateText(display, "6", (6, 600))
        updateText(display, "7", (6, 700))
        ball.drawBall(display)
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

def userInput():
    pygame.init()
    display = pygame.display.set_mode((scr_wd, scr_ht))
    num = 3
    inputs = [ Input("Height = "), Input("Velocity (x) = "),
               Input("Velocity (y) = ")]
    initial = 100, 300
    for box in inputs:
        box.setRect( initial[0], initial[1])
        initial = initial[0], initial[1] + 100

    clock = pygame.time.Clock()

    active = True
    inp = []
    i = 0
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    inputs[i].text = inputs[i].text[:-1]
                elif event.key == 13:
                    inp = [ box.text for box in inputs ]
                    active = False
                    break
                elif event.key == pygame.K_TAB:
                    i = (i + 1) % num
                elif event.key == pygame.K_UP:
                    if i > 0:
                        i -= 1
                elif event.key == pygame.K_DOWN:
                    if i < num - 1:
                        i += 1
                else:
                    inputs[i].text +=  event.unicode
        if active:
            display.fill((255, 255, 255))
            for rect in inputs:
                rect.draw(display)
            pygame.display.flip()
            clock.tick(FPS)

    # print(inp)
    inp = [ int(i) for i in inp]
    return inp[0], inp[1], inp[2]

if __name__ == "__main__":
    ht, vel_x, vel_y = userInput()
    # print( ht, vel_x, vel_y)
    simulate_bounce(ht, (vel_x, vel_y))

